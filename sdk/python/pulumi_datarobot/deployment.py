# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs
from ._inputs import *

__all__ = ['DeploymentArgs', 'Deployment']

@pulumi.input_type
class DeploymentArgs:
    def __init__(__self__, *,
                 label: pulumi.Input[str],
                 prediction_environment_id: pulumi.Input[str],
                 registered_model_version_id: pulumi.Input[str],
                 settings: Optional[pulumi.Input['DeploymentSettingsArgs']] = None):
        """
        The set of arguments for constructing a Deployment resource.
        :param pulumi.Input[str] label: The label of the Deployment.
        :param pulumi.Input[str] prediction_environment_id: The ID of the predication environment for this Deployment.
        :param pulumi.Input[str] registered_model_version_id: The ID of the registered model version for this Deployment.
        :param pulumi.Input['DeploymentSettingsArgs'] settings: The settings for the Deployment.
        """
        pulumi.set(__self__, "label", label)
        pulumi.set(__self__, "prediction_environment_id", prediction_environment_id)
        pulumi.set(__self__, "registered_model_version_id", registered_model_version_id)
        if settings is not None:
            pulumi.set(__self__, "settings", settings)

    @property
    @pulumi.getter
    def label(self) -> pulumi.Input[str]:
        """
        The label of the Deployment.
        """
        return pulumi.get(self, "label")

    @label.setter
    def label(self, value: pulumi.Input[str]):
        pulumi.set(self, "label", value)

    @property
    @pulumi.getter(name="predictionEnvironmentId")
    def prediction_environment_id(self) -> pulumi.Input[str]:
        """
        The ID of the predication environment for this Deployment.
        """
        return pulumi.get(self, "prediction_environment_id")

    @prediction_environment_id.setter
    def prediction_environment_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "prediction_environment_id", value)

    @property
    @pulumi.getter(name="registeredModelVersionId")
    def registered_model_version_id(self) -> pulumi.Input[str]:
        """
        The ID of the registered model version for this Deployment.
        """
        return pulumi.get(self, "registered_model_version_id")

    @registered_model_version_id.setter
    def registered_model_version_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "registered_model_version_id", value)

    @property
    @pulumi.getter
    def settings(self) -> Optional[pulumi.Input['DeploymentSettingsArgs']]:
        """
        The settings for the Deployment.
        """
        return pulumi.get(self, "settings")

    @settings.setter
    def settings(self, value: Optional[pulumi.Input['DeploymentSettingsArgs']]):
        pulumi.set(self, "settings", value)


@pulumi.input_type
class _DeploymentState:
    def __init__(__self__, *,
                 label: Optional[pulumi.Input[str]] = None,
                 prediction_environment_id: Optional[pulumi.Input[str]] = None,
                 registered_model_version_id: Optional[pulumi.Input[str]] = None,
                 settings: Optional[pulumi.Input['DeploymentSettingsArgs']] = None):
        """
        Input properties used for looking up and filtering Deployment resources.
        :param pulumi.Input[str] label: The label of the Deployment.
        :param pulumi.Input[str] prediction_environment_id: The ID of the predication environment for this Deployment.
        :param pulumi.Input[str] registered_model_version_id: The ID of the registered model version for this Deployment.
        :param pulumi.Input['DeploymentSettingsArgs'] settings: The settings for the Deployment.
        """
        if label is not None:
            pulumi.set(__self__, "label", label)
        if prediction_environment_id is not None:
            pulumi.set(__self__, "prediction_environment_id", prediction_environment_id)
        if registered_model_version_id is not None:
            pulumi.set(__self__, "registered_model_version_id", registered_model_version_id)
        if settings is not None:
            pulumi.set(__self__, "settings", settings)

    @property
    @pulumi.getter
    def label(self) -> Optional[pulumi.Input[str]]:
        """
        The label of the Deployment.
        """
        return pulumi.get(self, "label")

    @label.setter
    def label(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "label", value)

    @property
    @pulumi.getter(name="predictionEnvironmentId")
    def prediction_environment_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the predication environment for this Deployment.
        """
        return pulumi.get(self, "prediction_environment_id")

    @prediction_environment_id.setter
    def prediction_environment_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "prediction_environment_id", value)

    @property
    @pulumi.getter(name="registeredModelVersionId")
    def registered_model_version_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the registered model version for this Deployment.
        """
        return pulumi.get(self, "registered_model_version_id")

    @registered_model_version_id.setter
    def registered_model_version_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "registered_model_version_id", value)

    @property
    @pulumi.getter
    def settings(self) -> Optional[pulumi.Input['DeploymentSettingsArgs']]:
        """
        The settings for the Deployment.
        """
        return pulumi.get(self, "settings")

    @settings.setter
    def settings(self, value: Optional[pulumi.Input['DeploymentSettingsArgs']]):
        pulumi.set(self, "settings", value)


class Deployment(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 label: Optional[pulumi.Input[str]] = None,
                 prediction_environment_id: Optional[pulumi.Input[str]] = None,
                 registered_model_version_id: Optional[pulumi.Input[str]] = None,
                 settings: Optional[pulumi.Input[Union['DeploymentSettingsArgs', 'DeploymentSettingsArgsDict']]] = None,
                 __props__=None):
        """
        Deployment

        ## Example Usage

        ```python
        import pulumi
        import pulumi_datarobot as datarobot

        example_custom_model = datarobot.CustomModel("exampleCustomModel",
            description="Description for the example custom model",
            target_type="Binary",
            target_name="my_label",
            base_environment_name="[GenAI] Python 3.11 with Moderations",
            files=["example.py"])
        example_registered_model = datarobot.RegisteredModel("exampleRegisteredModel",
            custom_model_version_id=example_custom_model.version_id,
            description="Description for the example registered model")
        example_prediction_environment = datarobot.PredictionEnvironment("examplePredictionEnvironment",
            description="Description for the example prediction environment",
            platform="datarobotServerless")
        example_deployment = datarobot.Deployment("exampleDeployment",
            label="An example deployment",
            prediction_environment_id=example_prediction_environment.id,
            registered_model_version_id=example_registered_model.version_id)
        # Optional settings
        # settings = {
        #   prediction_row_storage = true
        # }
        pulumi.export("datarobotDeploymentId", example_deployment.id)
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] label: The label of the Deployment.
        :param pulumi.Input[str] prediction_environment_id: The ID of the predication environment for this Deployment.
        :param pulumi.Input[str] registered_model_version_id: The ID of the registered model version for this Deployment.
        :param pulumi.Input[Union['DeploymentSettingsArgs', 'DeploymentSettingsArgsDict']] settings: The settings for the Deployment.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DeploymentArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Deployment

        ## Example Usage

        ```python
        import pulumi
        import pulumi_datarobot as datarobot

        example_custom_model = datarobot.CustomModel("exampleCustomModel",
            description="Description for the example custom model",
            target_type="Binary",
            target_name="my_label",
            base_environment_name="[GenAI] Python 3.11 with Moderations",
            files=["example.py"])
        example_registered_model = datarobot.RegisteredModel("exampleRegisteredModel",
            custom_model_version_id=example_custom_model.version_id,
            description="Description for the example registered model")
        example_prediction_environment = datarobot.PredictionEnvironment("examplePredictionEnvironment",
            description="Description for the example prediction environment",
            platform="datarobotServerless")
        example_deployment = datarobot.Deployment("exampleDeployment",
            label="An example deployment",
            prediction_environment_id=example_prediction_environment.id,
            registered_model_version_id=example_registered_model.version_id)
        # Optional settings
        # settings = {
        #   prediction_row_storage = true
        # }
        pulumi.export("datarobotDeploymentId", example_deployment.id)
        ```

        :param str resource_name: The name of the resource.
        :param DeploymentArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DeploymentArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 label: Optional[pulumi.Input[str]] = None,
                 prediction_environment_id: Optional[pulumi.Input[str]] = None,
                 registered_model_version_id: Optional[pulumi.Input[str]] = None,
                 settings: Optional[pulumi.Input[Union['DeploymentSettingsArgs', 'DeploymentSettingsArgsDict']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DeploymentArgs.__new__(DeploymentArgs)

            if label is None and not opts.urn:
                raise TypeError("Missing required property 'label'")
            __props__.__dict__["label"] = label
            if prediction_environment_id is None and not opts.urn:
                raise TypeError("Missing required property 'prediction_environment_id'")
            __props__.__dict__["prediction_environment_id"] = prediction_environment_id
            if registered_model_version_id is None and not opts.urn:
                raise TypeError("Missing required property 'registered_model_version_id'")
            __props__.__dict__["registered_model_version_id"] = registered_model_version_id
            __props__.__dict__["settings"] = settings
        super(Deployment, __self__).__init__(
            'datarobot:index/deployment:Deployment',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            label: Optional[pulumi.Input[str]] = None,
            prediction_environment_id: Optional[pulumi.Input[str]] = None,
            registered_model_version_id: Optional[pulumi.Input[str]] = None,
            settings: Optional[pulumi.Input[Union['DeploymentSettingsArgs', 'DeploymentSettingsArgsDict']]] = None) -> 'Deployment':
        """
        Get an existing Deployment resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] label: The label of the Deployment.
        :param pulumi.Input[str] prediction_environment_id: The ID of the predication environment for this Deployment.
        :param pulumi.Input[str] registered_model_version_id: The ID of the registered model version for this Deployment.
        :param pulumi.Input[Union['DeploymentSettingsArgs', 'DeploymentSettingsArgsDict']] settings: The settings for the Deployment.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _DeploymentState.__new__(_DeploymentState)

        __props__.__dict__["label"] = label
        __props__.__dict__["prediction_environment_id"] = prediction_environment_id
        __props__.__dict__["registered_model_version_id"] = registered_model_version_id
        __props__.__dict__["settings"] = settings
        return Deployment(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def label(self) -> pulumi.Output[str]:
        """
        The label of the Deployment.
        """
        return pulumi.get(self, "label")

    @property
    @pulumi.getter(name="predictionEnvironmentId")
    def prediction_environment_id(self) -> pulumi.Output[str]:
        """
        The ID of the predication environment for this Deployment.
        """
        return pulumi.get(self, "prediction_environment_id")

    @property
    @pulumi.getter(name="registeredModelVersionId")
    def registered_model_version_id(self) -> pulumi.Output[str]:
        """
        The ID of the registered model version for this Deployment.
        """
        return pulumi.get(self, "registered_model_version_id")

    @property
    @pulumi.getter
    def settings(self) -> pulumi.Output[Optional['outputs.DeploymentSettings']]:
        """
        The settings for the Deployment.
        """
        return pulumi.get(self, "settings")

