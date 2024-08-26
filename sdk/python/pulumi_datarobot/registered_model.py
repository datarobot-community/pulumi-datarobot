# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['RegisteredModelArgs', 'RegisteredModel']

@pulumi.input_type
class RegisteredModelArgs:
    def __init__(__self__, *,
                 custom_model_version_id: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a RegisteredModel resource.
        :param pulumi.Input[str] custom_model_version_id: The ID of the custom model version for this Registered Model.
        :param pulumi.Input[str] description: The description of the Registered Model.
        :param pulumi.Input[str] name: The name of the Registered Model.
        """
        pulumi.set(__self__, "custom_model_version_id", custom_model_version_id)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="customModelVersionId")
    def custom_model_version_id(self) -> pulumi.Input[str]:
        """
        The ID of the custom model version for this Registered Model.
        """
        return pulumi.get(self, "custom_model_version_id")

    @custom_model_version_id.setter
    def custom_model_version_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "custom_model_version_id", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the Registered Model.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Registered Model.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _RegisteredModelState:
    def __init__(__self__, *,
                 custom_model_version_id: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 version_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering RegisteredModel resources.
        :param pulumi.Input[str] custom_model_version_id: The ID of the custom model version for this Registered Model.
        :param pulumi.Input[str] description: The description of the Registered Model.
        :param pulumi.Input[str] name: The name of the Registered Model.
        :param pulumi.Input[str] version_id: The ID of the Registered Model Version.
        """
        if custom_model_version_id is not None:
            pulumi.set(__self__, "custom_model_version_id", custom_model_version_id)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if version_id is not None:
            pulumi.set(__self__, "version_id", version_id)

    @property
    @pulumi.getter(name="customModelVersionId")
    def custom_model_version_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the custom model version for this Registered Model.
        """
        return pulumi.get(self, "custom_model_version_id")

    @custom_model_version_id.setter
    def custom_model_version_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "custom_model_version_id", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the Registered Model.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Registered Model.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="versionId")
    def version_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the Registered Model Version.
        """
        return pulumi.get(self, "version_id")

    @version_id.setter
    def version_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "version_id", value)


class RegisteredModel(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 custom_model_version_id: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        registered model

        ## Example Usage

        ```python
        import pulumi
        import pulumi_datarobot as datarobot

        example = datarobot.RegisteredModel("example",
            description="Description for the example registered model",
            custom_model_version_id=datarobot_custom_model["example"]["version_id"])
        pulumi.export("datarobotRegisteredModelId", example.id)
        pulumi.export("datarobotRegisteredModelVersionId", example.version_id)
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] custom_model_version_id: The ID of the custom model version for this Registered Model.
        :param pulumi.Input[str] description: The description of the Registered Model.
        :param pulumi.Input[str] name: The name of the Registered Model.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: RegisteredModelArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        registered model

        ## Example Usage

        ```python
        import pulumi
        import pulumi_datarobot as datarobot

        example = datarobot.RegisteredModel("example",
            description="Description for the example registered model",
            custom_model_version_id=datarobot_custom_model["example"]["version_id"])
        pulumi.export("datarobotRegisteredModelId", example.id)
        pulumi.export("datarobotRegisteredModelVersionId", example.version_id)
        ```

        :param str resource_name: The name of the resource.
        :param RegisteredModelArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(RegisteredModelArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 custom_model_version_id: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = RegisteredModelArgs.__new__(RegisteredModelArgs)

            if custom_model_version_id is None and not opts.urn:
                raise TypeError("Missing required property 'custom_model_version_id'")
            __props__.__dict__["custom_model_version_id"] = custom_model_version_id
            __props__.__dict__["description"] = description
            __props__.__dict__["name"] = name
            __props__.__dict__["version_id"] = None
        super(RegisteredModel, __self__).__init__(
            'datarobot:index/registeredModel:RegisteredModel',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            custom_model_version_id: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            version_id: Optional[pulumi.Input[str]] = None) -> 'RegisteredModel':
        """
        Get an existing RegisteredModel resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] custom_model_version_id: The ID of the custom model version for this Registered Model.
        :param pulumi.Input[str] description: The description of the Registered Model.
        :param pulumi.Input[str] name: The name of the Registered Model.
        :param pulumi.Input[str] version_id: The ID of the Registered Model Version.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _RegisteredModelState.__new__(_RegisteredModelState)

        __props__.__dict__["custom_model_version_id"] = custom_model_version_id
        __props__.__dict__["description"] = description
        __props__.__dict__["name"] = name
        __props__.__dict__["version_id"] = version_id
        return RegisteredModel(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="customModelVersionId")
    def custom_model_version_id(self) -> pulumi.Output[str]:
        """
        The ID of the custom model version for this Registered Model.
        """
        return pulumi.get(self, "custom_model_version_id")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The description of the Registered Model.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the Registered Model.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="versionId")
    def version_id(self) -> pulumi.Output[str]:
        """
        The ID of the Registered Model Version.
        """
        return pulumi.get(self, "version_id")

