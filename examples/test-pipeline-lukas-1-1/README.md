# DocsAssist Recipe
DocsAssist is an easily customizable recipe for building a RAG-powered chatbot. 

In addition to creating a hosted, shareable user interface, DocsAssist provides:
* Regex and prompt-injection guardrails
* A predictive sidecar model that evaluates response quality
* GenAI-focused custom metrics that automatically refresh on a schedule
* DataRobot ML Ops hosting, monitoring, and governing the individual backend deployments


![Using DocsAssist](https://s3.amazonaws.com/datarobot_public/drx/drx_gifs/docs_assist_ui.gif)


## Getting started
1. Ensure you have the following DataRobot feature flags turned on:
   - Enable MLOps
   - Enable Custom Inference Models
   - Enable the Injection of Runtime Parameters for Custom Models
   - Enable Public Network Access for all Custom Models
   - Enable Monitoring Support for Generative Models
   - Enable Global Models in the Model Registry
   - Enable Custom Jobs
   - Enable Additional Custom Model Output in Prediction Responses
   - Enable Moderation Guardrails
   - Enable Custom Applications Workshop
   - Enable Runtime Parameters and Resource Limits
   - Enable LLM Assessment
   - Enable Data Quality Table for Text Generation Target Types
   - Enable Enables launching the Q&A Chat Generation App from the Registry

2. Create a [new][virtualenv-docs] python virtual environment with python >= 3.9.

3. Install `kedro`, create a new kedro project from this template and `cd` to the newly created directory.
   Choose a project name that is likely to be unique - DataRobot requires registered model names to be unique
   for an organization. You can change it later if necessary by editing `parameters.yml`. For authenticating with GitHub please check [here](#gh-auth).
   ```bash
   pip install kedro
   ```
   ```bash
   kedro new --name=your_project_name --starter=https://github.com/datarobot/recipe-docsassist.git --checkout main
   ```
   ```bash
   cd your_project_name
   ```
      
4. Install requirements for this template: `pip install -r requirements.txt`

5. Populate the following credentials in `conf/local/credentials.yml`:
   ```yaml
   datarobot:
     endpoint: <your endpoint>  # e.g. https://your_subdomain.datarobot.com/api/v2
     api_token: <your api token>
     default_prediction_server_id: <your default prediction server id>  # get the id (not the URL) from the details tab on https://app.datarobot.com/console/prediction-environments

   azure_openai_llm_credentials:
     azure_endpoint: <your api endpoint>  # e.g. https://your_subdomain.openai.azure.com/
     api_key: <your api key>
     api_type: <your api type>
     api_version: <your api version>  # please refer to https://learn.microsoft.com/en-US/azure/ai-services/openai/reference 
     deployment_name: <your deployment name>
   ```

6. Run the pipeline: `kedro run`. Start exploring the pipeline using the kedro GUI: `kedro viz --include-hooks`


![Kedro Viz](https://s3.amazonaws.com/datarobot_public/drx/drx_gifs/kedro-viz.gif)


[virtualenv-docs]: https://docs.python.org/3/library/venv.html#creating-virtual-environments

## Making changes to the pipeline
The following files govern pipeline execution. In general, you will not need to modify
any other boilerplate files as you customize the pipeline.:

- `conf/base/parameters.yml`: pipeline configuration options and hyperparameters
- `conf/local/credentials.yml`: API tokens and other secrets
- `conf/base/catalog.yml`: file storage locations that can be used as node inputs or outputs,
  including locations of supporting assets to build DR custom models, execution environments
- `src/your_project_name/pipelines/*/nodes.py`: function definitions for the pipeline nodes
- `src/your_project_name/pipelines/*/pipeline.py`: node names, inputs and outputs
- `src/datarobotx/idp`: directory contains function definitions for for reusable idempotent DR nodes
- `include/your_project_name`: directory contains raw assets and templates used by the pipeline

For a deeper orientation to kedro principles and project structure visit the [Kedro][kedro-docs]
documentation.

[kedro-docs]: https://docs.kedro.org/en/stable/

### Example changes
In many cases it can useful to use `kedro viz --include-hooks` to help explore and understand
a pipeline before making changes. Some examples of changes:

1. Many simple pipeline configuration options can be changed by editing 
   `conf/base/parameters.yml` or `conf/base/catalog.yml` and then rerunning 
   the pipeline using `kedro run`, e.g.
   * `parameters.yml`:
     - Names for each created DataRobot asset (e.g. deployments, custom app, etc.)
     - Document splitting hyperparameters
     - Vector DB embedding model
   * `catalog.yml`:
     - Source documents used by the RAG app; try swapping to this archive of medical research 
       [papers][research-papers] as an example

2. Assets and templates needed to build DR custom models, execution environments, and
   custom apps can generally be found in the respective `include/your_project_name` subdirectories
   and can be edited to e.g. tailor the look and feel of the streamlit app; as with any
   other change just call `kedro run` to rerun the pipeline and incorporate changes

   When editing the streamlit frontend, make sure you have run the pipeline locally at least once.
   You should then be able to run the streamlit app locally while developing in this directory directly.

3. Update function definitions in a pipeline's `nodes.py` to change the actual logic for
   a step in the pipeline or to define a new node, e.g.:
   - `make_chunks()`: contains logic for translating raw documents into chunks prior
     to building the vector database
   - `make_rag_deployment_assets()`: builds the vector DB from the chunks and collects
     all other assets needed to deploy a DR custom model

4. Add newly defined nodes to the pipeline, change execution order, or reconfigure
   node input/output connections by editing `pipeline.py` in a pipeline's folder.

[research-papers]: https://s3.amazonaws.com/datarobot_public_datasets/ai_accelerators/medical_agent/files.zip

## <a name="gh-auth"></a> Authenticating with GitHub
How to install `gh` [GitHub CLI][GitHub CLI-link] 

[GitHub CLI-link]: https://github.com/cli/cli

Run `gh auth login` in the terminal and answer the following questions with:
- `? What account do you want to log into?` **GitHub.com**
- `? What is your preferred protocol for Git operations on this host?` **HTTPS**
- `? Authenticate Git with your GitHub credentials?` **Yes**
- `? How would you like to authenticate GitHub CLI?` **Login with a web browser**

Copy the code in: `! First copy your one-time code:` **XXXX-XXXX**

Open a web browser at https://github.com/login/device and enter the above code manually.

You should see in the terminal:
- `✓ Authentication complete.`
- `✓ Logged in as YOUR_USERNAME`

More details on GitHub authentication [here][gh-docs].

[gh-docs]: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/about-authentication-to-github#https
