# Copyright 2024 DataRobot, Inc. and its affiliates.
# All rights reserved.
# DataRobot, Inc.
# This is proprietary source code of DataRobot, Inc. and its
# affiliates.
# Released under the terms of DataRobot Tool and Utility Agreement.

from __future__ import annotations

import base64
import datetime as dt
import json
import uuid
from typing import TYPE_CHECKING

import datarobot as dr
import streamlit as st  # type: ignore
import yaml  # type: ignore
from dr_helpers import get_rag_predictions, predict_grade, submit_grade
from langchain_core.messages import AIMessage, HumanMessage

if TYPE_CHECKING:
    from kedro.io import DataCatalog


def get_kedro_catalog(kedro_project_root: str) -> DataCatalog:
    """Initialize a kedro data catalog (as a singleton)."""
    if "KEDRO_CATALOG" not in st.session_state:
        try:
            import pathlib

            from kedro.framework.session import KedroSession
            from kedro.framework.startup import bootstrap_project
        except ImportError as e:
            raise ImportError(
                "Please ensure you've installed `kedro` and `kedro_datasets` to run this app locally"
            ) from e

        project_path = pathlib.Path(kedro_project_root).resolve()
        bootstrap_project(project_path)
        session = KedroSession.create(project_path)
        context = session.load_context()
        catalog = context.catalog

        # initializing a context & catalog is slow enough to be perceived; persist in session state
        st.session_state["KEDRO_CATALOG"] = catalog
    return st.session_state["KEDRO_CATALOG"]


try:
    # in production, parameters are available in the working directory
    with open("app_parameters.yaml") as f:
        params = yaml.safe_load(f)
    DATAROBOT_API_KEY = st.secrets["DATAROBOT_API_TOKEN"]
except (FileNotFoundError, KeyError):
    # during local dev, parameters can be retrieved from the kedro catalog
    project_root = "../../../"
    catalog = get_kedro_catalog(project_root)
    from_catalog = [
        ("params", "deploy_custom_streamlit_app.app_parameters"),
        ("DATAROBOT_API_KEY", "params:credentials.datarobot.api_token"),
    ]
    for var, catalog_name in from_catalog:
        try:
            globals()[var] = catalog.load(catalog_name)
        except Exception as e2:
            raise RuntimeError(
                f"Could not load the kedro dataset '{catalog_name}'; "
                "have you run the pipeline at least once using `kedro run`?"
            ) from e2


DATAROBOT_ENDPOINT = params["datarobot_endpoint"]

TITLE = params["page_title"]

RAG_DEPLOYMENT_ID = params["rag_deployment_id"]
RAG_PROMPT_FEATURE_NAME = params["rag_prompt_feature_name"]

GRADING_DEPLOYMENT_ID = params["grading_deployment_id"]
RENDER_GRADING_MODEL_SCORES = params["render_grading_model_scores"]

st.set_page_config(page_title=TITLE)

with open("./style.css") as f:
    css = f.read()

with open("./DataRobot.svg") as f:
    svg = f.read()

st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

new_c = dr.Client(endpoint=DATAROBOT_ENDPOINT, token=DATAROBOT_API_KEY)
dr.client.set_client(new_c)

pred_server = new_c.get(f"deployments/{RAG_DEPLOYMENT_ID}").json()[
    "defaultPredictionServer"
]
pred_server_url = pred_server["url"]
datarobot_key = pred_server["datarobot-key"]

if "messages" not in st.session_state:
    st.session_state.messages = []


class DataRobotPredictionError(Exception):
    """Raised if there are issues getting predictions from DataRobot"""


def render_svg(svg):
    """Renders the given svg string."""
    b64 = base64.b64encode(svg.encode("utf-8")).decode("utf-8")
    html = r'<img src="data:image/svg+xml;base64,%s"/>' % b64
    st.write(html, unsafe_allow_html=True)


def render_cite_area(think_area, state_key, grade_key, answer_lang="python"):
    try:
        resp = st.session_state[state_key]
    except KeyError:
        raise ValueError("No response generated to your query. Please try again.")
    grade = st.session_state[grade_key]

    with think_area:
        ct = st.container()
        ct.header("**Answer:**")

        ct.markdown(resp["answer"])
        if RENDER_GRADING_MODEL_SCORES:
            ct.header("**Response Grade**: {}".format(grade["grade"]))
            ct.markdown("**Confidence Scores:**")
            ct.markdown(
                "Correct {:.2%}, Incomplete {:.2%}, Digress {:.2%}, Incorrect {:.2%}, No Answer {:.2%}".format(
                    grade["class_correct"],
                    grade["class_incomplete"],
                    grade["class_digress"],
                    grade["class_incorrect"],
                    grade["class_no_answer"],
                )
            )

        ct.header("**Citations:**")
        for i, doc in enumerate(resp["references"]):
            with ct.expander(f"Reference: {i+1}"):
                st.markdown("**Source:** {}".format(doc["metadata"]["source"]))
                st.markdown("**Content:**")
                for text in [s for s in doc["page_content"].split("\\n") if s.strip()]:
                    st.markdown(text)
                    st.markdown("  \n  ")

    return 0


def render_message(container, message, is_user=False):
    message_type = "user" if is_user else "ai"
    container.markdown(
        f"""
    <div class="chat-message {message_type}-message">
        <div class="message-content">
            <span class="message-label"><b>{'Human' if is_user else 'AI'}:</b></span>
            <span class="message-text">{message}</span>
        </div>
    </div>
    """,
        unsafe_allow_html=True,
    )


def render_conversation_history(container):
    container.subheader("Conversation History")
    for message in st.session_state.messages[:-1]:  # Exclude the latest message
        render_message(container, message.content, isinstance(message, HumanMessage))
    st.markdown("---")


def render_answer_and_citations(container, response: dict, grade: dict):
    render_message(container, response["answer"], is_user=False)

    if RENDER_GRADING_MODEL_SCORES:
        st.header(f"**Response Grade**: {grade['grade']}")
        st.markdown("**Confidence Scores:**")
        scores = ", ".join(
            f"{k.split('_')[1]} {v:.2%}"
            for k, v in grade.items()
            if k.startswith("class_")
        )
        st.markdown(scores)

    with st.expander("Show Citations"):
        for i, doc in enumerate(response["references"]):
            st.markdown(f"**Reference {i+1}:**")
            st.markdown(f"**Source:** {doc['metadata']['source']}")
            st.markdown("**Content:**")
            for text in doc["page_content"].split("\\n"):
                if text.strip():
                    st.markdown(text)
            st.markdown("---")


def main():
    render_svg(svg)
    st.title(TITLE)

    chat_container = st.container()

    if st.session_state.messages:
        render_conversation_history(chat_container)
    answer_and_citations_placeholder = chat_container.container()
    if "prompt_sent" not in st.session_state:
        st.session_state.prompt_sent = False
    prompt = chat_container.chat_input(
        placeholder="Your message",
        key=None,
        max_chars=None,
        disabled=False,
        on_submit=None,
        args=None,
        kwargs=None,
    )

    if prompt and prompt.strip():
        association_id = f"{uuid.uuid4().hex}_{dt.datetime.now()}"
        st.session_state.prompt_sent = True
        st.session_state.association_id = association_id

        data = {
            "question": prompt,
            "association_id": association_id,
            "messages": json.dumps([m.dict() for m in st.session_state.messages]),
        }
        with st.spinner("Getting AI response..."):
            response = get_rag_predictions(
                data,
                RAG_DEPLOYMENT_ID,
                DATAROBOT_API_KEY,
                datarobot_key,
                pred_server_url,
                RAG_PROMPT_FEATURE_NAME,
            )
        response["question"] = prompt
        st.session_state.response = response
        st.session_state.messages.extend(
            [HumanMessage(content=prompt), AIMessage(content=response["answer"])]
        )
        with st.spinner("Predicting grade..."):
            grade = predict_grade(response, association_id, GRADING_DEPLOYMENT_ID)
        st.session_state.confidence = grade
        # display the grade
        st.write(f"Grade: {grade}")

        st.rerun()

    if st.session_state.prompt_sent:
        render_answer_and_citations(
            answer_and_citations_placeholder,
            st.session_state.response,
            st.session_state.confidence,
        )

        st.subheader("**How would you rate this response?**")
        cols = st.columns(5)
        grades = ["Correct", "Incorrect", "Incomplete", "Digress", "No Answer"]

        for col, grade in zip(cols, grades):
            if col.button(label=grade):
                submit_grade(
                    GRADING_DEPLOYMENT_ID,
                    grade.lower(),
                    st.session_state.association_id,
                )
                st.success("Thank you for your rating!")

        st.write("""
        **Correct**: the response sufficiently answers the question.
        **Incorrect**: the response "hallucinates" or is the wrong answer to the question.
        **Incomplete**: the response does not fully answer the question.
        **Digress**: the response includes irrelevant information or is not concise.
        **No Answer**: the response claims it cannot or will not answer the question.
        """)


if __name__ == "__main__":
    main()
