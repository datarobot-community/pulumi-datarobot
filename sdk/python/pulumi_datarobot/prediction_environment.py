# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['PredictionEnvironmentArgs', 'PredictionEnvironment']

@pulumi.input_type
class PredictionEnvironmentArgs:
    def __init__(__self__, *,
                 description: pulumi.Input[str],
                 platform: pulumi.Input[str],
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a PredictionEnvironment resource.
        :param pulumi.Input[str] description: The description of the Prediction Environment.
        :param pulumi.Input[str] platform: The platform for the Prediction Environment.
        :param pulumi.Input[str] name: The name of the Prediction Environment.
        """
        pulumi.set(__self__, "description", description)
        pulumi.set(__self__, "platform", platform)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Input[str]:
        """
        The description of the Prediction Environment.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: pulumi.Input[str]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def platform(self) -> pulumi.Input[str]:
        """
        The platform for the Prediction Environment.
        """
        return pulumi.get(self, "platform")

    @platform.setter
    def platform(self, value: pulumi.Input[str]):
        pulumi.set(self, "platform", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Prediction Environment.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _PredictionEnvironmentState:
    def __init__(__self__, *,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 platform: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering PredictionEnvironment resources.
        :param pulumi.Input[str] description: The description of the Prediction Environment.
        :param pulumi.Input[str] name: The name of the Prediction Environment.
        :param pulumi.Input[str] platform: The platform for the Prediction Environment.
        """
        if description is not None:
            pulumi.set(__self__, "description", description)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if platform is not None:
            pulumi.set(__self__, "platform", platform)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the Prediction Environment.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Prediction Environment.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def platform(self) -> Optional[pulumi.Input[str]]:
        """
        The platform for the Prediction Environment.
        """
        return pulumi.get(self, "platform")

    @platform.setter
    def platform(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "platform", value)


class PredictionEnvironment(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 platform: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        prediction environment

        ## Example Usage

        ```python
        import pulumi
        import pulumi_datarobot as datarobot

        toxicity_prediction_environment = datarobot.PredictionEnvironment("toxicityPredictionEnvironment",
            description="Description for the example prediction environment",
            platform="aws")
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The description of the Prediction Environment.
        :param pulumi.Input[str] name: The name of the Prediction Environment.
        :param pulumi.Input[str] platform: The platform for the Prediction Environment.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: PredictionEnvironmentArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        prediction environment

        ## Example Usage

        ```python
        import pulumi
        import pulumi_datarobot as datarobot

        toxicity_prediction_environment = datarobot.PredictionEnvironment("toxicityPredictionEnvironment",
            description="Description for the example prediction environment",
            platform="aws")
        ```

        :param str resource_name: The name of the resource.
        :param PredictionEnvironmentArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(PredictionEnvironmentArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 platform: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = PredictionEnvironmentArgs.__new__(PredictionEnvironmentArgs)

            if description is None and not opts.urn:
                raise TypeError("Missing required property 'description'")
            __props__.__dict__["description"] = description
            __props__.__dict__["name"] = name
            if platform is None and not opts.urn:
                raise TypeError("Missing required property 'platform'")
            __props__.__dict__["platform"] = platform
        super(PredictionEnvironment, __self__).__init__(
            'datarobot:index/predictionEnvironment:PredictionEnvironment',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            description: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            platform: Optional[pulumi.Input[str]] = None) -> 'PredictionEnvironment':
        """
        Get an existing PredictionEnvironment resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The description of the Prediction Environment.
        :param pulumi.Input[str] name: The name of the Prediction Environment.
        :param pulumi.Input[str] platform: The platform for the Prediction Environment.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _PredictionEnvironmentState.__new__(_PredictionEnvironmentState)

        __props__.__dict__["description"] = description
        __props__.__dict__["name"] = name
        __props__.__dict__["platform"] = platform
        return PredictionEnvironment(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        The description of the Prediction Environment.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the Prediction Environment.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def platform(self) -> pulumi.Output[str]:
        """
        The platform for the Prediction Environment.
        """
        return pulumi.get(self, "platform")

