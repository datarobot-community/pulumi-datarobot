# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['LlmBlueprintArgs', 'LlmBlueprint']

@pulumi.input_type
class LlmBlueprintArgs:
    def __init__(__self__, *,
                 description: pulumi.Input[str],
                 llm_id: pulumi.Input[str],
                 playground_id: pulumi.Input[str],
                 name: Optional[pulumi.Input[str]] = None,
                 vector_database_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a LlmBlueprint resource.
        :param pulumi.Input[str] description: The description of the LLM Blueprint.
        :param pulumi.Input[str] llm_id: The id of the LLM for the LLM Blueprint.
        :param pulumi.Input[str] playground_id: The id of the Playground for the LLM Blueprint.
        :param pulumi.Input[str] name: The name of the LLM Blueprint.
        :param pulumi.Input[str] vector_database_id: The id of the Vector Database for the LLM Blueprint.
        """
        pulumi.set(__self__, "description", description)
        pulumi.set(__self__, "llm_id", llm_id)
        pulumi.set(__self__, "playground_id", playground_id)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if vector_database_id is not None:
            pulumi.set(__self__, "vector_database_id", vector_database_id)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Input[str]:
        """
        The description of the LLM Blueprint.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: pulumi.Input[str]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="llmId")
    def llm_id(self) -> pulumi.Input[str]:
        """
        The id of the LLM for the LLM Blueprint.
        """
        return pulumi.get(self, "llm_id")

    @llm_id.setter
    def llm_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "llm_id", value)

    @property
    @pulumi.getter(name="playgroundId")
    def playground_id(self) -> pulumi.Input[str]:
        """
        The id of the Playground for the LLM Blueprint.
        """
        return pulumi.get(self, "playground_id")

    @playground_id.setter
    def playground_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "playground_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the LLM Blueprint.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="vectorDatabaseId")
    def vector_database_id(self) -> Optional[pulumi.Input[str]]:
        """
        The id of the Vector Database for the LLM Blueprint.
        """
        return pulumi.get(self, "vector_database_id")

    @vector_database_id.setter
    def vector_database_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "vector_database_id", value)


@pulumi.input_type
class _LlmBlueprintState:
    def __init__(__self__, *,
                 description: Optional[pulumi.Input[str]] = None,
                 llm_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 playground_id: Optional[pulumi.Input[str]] = None,
                 vector_database_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering LlmBlueprint resources.
        :param pulumi.Input[str] description: The description of the LLM Blueprint.
        :param pulumi.Input[str] llm_id: The id of the LLM for the LLM Blueprint.
        :param pulumi.Input[str] name: The name of the LLM Blueprint.
        :param pulumi.Input[str] playground_id: The id of the Playground for the LLM Blueprint.
        :param pulumi.Input[str] vector_database_id: The id of the Vector Database for the LLM Blueprint.
        """
        if description is not None:
            pulumi.set(__self__, "description", description)
        if llm_id is not None:
            pulumi.set(__self__, "llm_id", llm_id)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if playground_id is not None:
            pulumi.set(__self__, "playground_id", playground_id)
        if vector_database_id is not None:
            pulumi.set(__self__, "vector_database_id", vector_database_id)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the LLM Blueprint.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="llmId")
    def llm_id(self) -> Optional[pulumi.Input[str]]:
        """
        The id of the LLM for the LLM Blueprint.
        """
        return pulumi.get(self, "llm_id")

    @llm_id.setter
    def llm_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "llm_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the LLM Blueprint.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="playgroundId")
    def playground_id(self) -> Optional[pulumi.Input[str]]:
        """
        The id of the Playground for the LLM Blueprint.
        """
        return pulumi.get(self, "playground_id")

    @playground_id.setter
    def playground_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "playground_id", value)

    @property
    @pulumi.getter(name="vectorDatabaseId")
    def vector_database_id(self) -> Optional[pulumi.Input[str]]:
        """
        The id of the Vector Database for the LLM Blueprint.
        """
        return pulumi.get(self, "vector_database_id")

    @vector_database_id.setter
    def vector_database_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "vector_database_id", value)


class LlmBlueprint(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 llm_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 playground_id: Optional[pulumi.Input[str]] = None,
                 vector_database_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        LLMBlueprint

        ## Example Usage

        ```python
        import pulumi
        import pulumi_datarobot as datarobot

        example = datarobot.LlmBlueprint("example",
            description="Description for the example LLM blueprint",
            playground_id=datarobot_playground["example"]["id"],
            vector_database_id=datarobot_vector_database["example"]["id"],
            llm_id="azure-openai-gpt-3.5-turbo")
        pulumi.export("exampleId", example.id)
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The description of the LLM Blueprint.
        :param pulumi.Input[str] llm_id: The id of the LLM for the LLM Blueprint.
        :param pulumi.Input[str] name: The name of the LLM Blueprint.
        :param pulumi.Input[str] playground_id: The id of the Playground for the LLM Blueprint.
        :param pulumi.Input[str] vector_database_id: The id of the Vector Database for the LLM Blueprint.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: LlmBlueprintArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        LLMBlueprint

        ## Example Usage

        ```python
        import pulumi
        import pulumi_datarobot as datarobot

        example = datarobot.LlmBlueprint("example",
            description="Description for the example LLM blueprint",
            playground_id=datarobot_playground["example"]["id"],
            vector_database_id=datarobot_vector_database["example"]["id"],
            llm_id="azure-openai-gpt-3.5-turbo")
        pulumi.export("exampleId", example.id)
        ```

        :param str resource_name: The name of the resource.
        :param LlmBlueprintArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(LlmBlueprintArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 llm_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 playground_id: Optional[pulumi.Input[str]] = None,
                 vector_database_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = LlmBlueprintArgs.__new__(LlmBlueprintArgs)

            if description is None and not opts.urn:
                raise TypeError("Missing required property 'description'")
            __props__.__dict__["description"] = description
            if llm_id is None and not opts.urn:
                raise TypeError("Missing required property 'llm_id'")
            __props__.__dict__["llm_id"] = llm_id
            __props__.__dict__["name"] = name
            if playground_id is None and not opts.urn:
                raise TypeError("Missing required property 'playground_id'")
            __props__.__dict__["playground_id"] = playground_id
            __props__.__dict__["vector_database_id"] = vector_database_id
        super(LlmBlueprint, __self__).__init__(
            'datarobot:index/llmBlueprint:LlmBlueprint',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            description: Optional[pulumi.Input[str]] = None,
            llm_id: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            playground_id: Optional[pulumi.Input[str]] = None,
            vector_database_id: Optional[pulumi.Input[str]] = None) -> 'LlmBlueprint':
        """
        Get an existing LlmBlueprint resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The description of the LLM Blueprint.
        :param pulumi.Input[str] llm_id: The id of the LLM for the LLM Blueprint.
        :param pulumi.Input[str] name: The name of the LLM Blueprint.
        :param pulumi.Input[str] playground_id: The id of the Playground for the LLM Blueprint.
        :param pulumi.Input[str] vector_database_id: The id of the Vector Database for the LLM Blueprint.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _LlmBlueprintState.__new__(_LlmBlueprintState)

        __props__.__dict__["description"] = description
        __props__.__dict__["llm_id"] = llm_id
        __props__.__dict__["name"] = name
        __props__.__dict__["playground_id"] = playground_id
        __props__.__dict__["vector_database_id"] = vector_database_id
        return LlmBlueprint(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        The description of the LLM Blueprint.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="llmId")
    def llm_id(self) -> pulumi.Output[str]:
        """
        The id of the LLM for the LLM Blueprint.
        """
        return pulumi.get(self, "llm_id")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the LLM Blueprint.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="playgroundId")
    def playground_id(self) -> pulumi.Output[str]:
        """
        The id of the Playground for the LLM Blueprint.
        """
        return pulumi.get(self, "playground_id")

    @property
    @pulumi.getter(name="vectorDatabaseId")
    def vector_database_id(self) -> pulumi.Output[Optional[str]]:
        """
        The id of the Vector Database for the LLM Blueprint.
        """
        return pulumi.get(self, "vector_database_id")

