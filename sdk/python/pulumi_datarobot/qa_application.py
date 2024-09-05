# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['QaApplicationArgs', 'QaApplication']

@pulumi.input_type
class QaApplicationArgs:
    def __init__(__self__, *,
                 deployment_id: pulumi.Input[str],
                 external_access_enabled: Optional[pulumi.Input[bool]] = None,
                 external_access_recipients: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a QaApplication resource.
        :param pulumi.Input[str] deployment_id: The deployment ID of the Q&A Application.
        :param pulumi.Input[bool] external_access_enabled: Whether external access is enabled for the Q&A Application.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] external_access_recipients: The list of external email addresses that have access to the Q&A Application.
        :param pulumi.Input[str] name: The name of the Q&A Application.
        """
        pulumi.set(__self__, "deployment_id", deployment_id)
        if external_access_enabled is not None:
            pulumi.set(__self__, "external_access_enabled", external_access_enabled)
        if external_access_recipients is not None:
            pulumi.set(__self__, "external_access_recipients", external_access_recipients)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="deploymentId")
    def deployment_id(self) -> pulumi.Input[str]:
        """
        The deployment ID of the Q&A Application.
        """
        return pulumi.get(self, "deployment_id")

    @deployment_id.setter
    def deployment_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "deployment_id", value)

    @property
    @pulumi.getter(name="externalAccessEnabled")
    def external_access_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether external access is enabled for the Q&A Application.
        """
        return pulumi.get(self, "external_access_enabled")

    @external_access_enabled.setter
    def external_access_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "external_access_enabled", value)

    @property
    @pulumi.getter(name="externalAccessRecipients")
    def external_access_recipients(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The list of external email addresses that have access to the Q&A Application.
        """
        return pulumi.get(self, "external_access_recipients")

    @external_access_recipients.setter
    def external_access_recipients(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "external_access_recipients", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Q&A Application.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _QaApplicationState:
    def __init__(__self__, *,
                 application_url: Optional[pulumi.Input[str]] = None,
                 deployment_id: Optional[pulumi.Input[str]] = None,
                 external_access_enabled: Optional[pulumi.Input[bool]] = None,
                 external_access_recipients: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 source_id: Optional[pulumi.Input[str]] = None,
                 source_version_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering QaApplication resources.
        :param pulumi.Input[str] application_url: The URL of the Q&A Application.
        :param pulumi.Input[str] deployment_id: The deployment ID of the Q&A Application.
        :param pulumi.Input[bool] external_access_enabled: Whether external access is enabled for the Q&A Application.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] external_access_recipients: The list of external email addresses that have access to the Q&A Application.
        :param pulumi.Input[str] name: The name of the Q&A Application.
        :param pulumi.Input[str] source_id: The ID of the Q&A Application Source.
        :param pulumi.Input[str] source_version_id: The version ID of the Q&A Application Source.
        """
        if application_url is not None:
            pulumi.set(__self__, "application_url", application_url)
        if deployment_id is not None:
            pulumi.set(__self__, "deployment_id", deployment_id)
        if external_access_enabled is not None:
            pulumi.set(__self__, "external_access_enabled", external_access_enabled)
        if external_access_recipients is not None:
            pulumi.set(__self__, "external_access_recipients", external_access_recipients)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if source_id is not None:
            pulumi.set(__self__, "source_id", source_id)
        if source_version_id is not None:
            pulumi.set(__self__, "source_version_id", source_version_id)

    @property
    @pulumi.getter(name="applicationUrl")
    def application_url(self) -> Optional[pulumi.Input[str]]:
        """
        The URL of the Q&A Application.
        """
        return pulumi.get(self, "application_url")

    @application_url.setter
    def application_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "application_url", value)

    @property
    @pulumi.getter(name="deploymentId")
    def deployment_id(self) -> Optional[pulumi.Input[str]]:
        """
        The deployment ID of the Q&A Application.
        """
        return pulumi.get(self, "deployment_id")

    @deployment_id.setter
    def deployment_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "deployment_id", value)

    @property
    @pulumi.getter(name="externalAccessEnabled")
    def external_access_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether external access is enabled for the Q&A Application.
        """
        return pulumi.get(self, "external_access_enabled")

    @external_access_enabled.setter
    def external_access_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "external_access_enabled", value)

    @property
    @pulumi.getter(name="externalAccessRecipients")
    def external_access_recipients(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The list of external email addresses that have access to the Q&A Application.
        """
        return pulumi.get(self, "external_access_recipients")

    @external_access_recipients.setter
    def external_access_recipients(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "external_access_recipients", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Q&A Application.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="sourceId")
    def source_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the Q&A Application Source.
        """
        return pulumi.get(self, "source_id")

    @source_id.setter
    def source_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source_id", value)

    @property
    @pulumi.getter(name="sourceVersionId")
    def source_version_id(self) -> Optional[pulumi.Input[str]]:
        """
        The version ID of the Q&A Application Source.
        """
        return pulumi.get(self, "source_version_id")

    @source_version_id.setter
    def source_version_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source_version_id", value)


class QaApplication(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 deployment_id: Optional[pulumi.Input[str]] = None,
                 external_access_enabled: Optional[pulumi.Input[bool]] = None,
                 external_access_recipients: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Q&A Application

        ## Example Usage

        ```python
        import pulumi
        import pulumi_datarobot as datarobot

        example_custom_model = datarobot.CustomModel("exampleCustomModel",
            description="Description for the example custom model",
            target_type="Binary",
            target_name="my_label",
            base_environment_name="[GenAI] Python 3.11 with Moderations",
            local_files=["example.py"])
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
        example_qa_application = datarobot.QaApplication("exampleQaApplication",
            deployment_id=example_deployment.id,
            external_access_enabled=True,
            external_access_recipients=["recipient@example.com"])
        pulumi.export("datarobotQaApplicationId", example_qa_application.id)
        pulumi.export("datarobotQaApplicationSourceId", example_qa_application.source_id)
        pulumi.export("datarobotQaApplicationSourceVersionId", example_qa_application.source_version_id)
        pulumi.export("datarobotQaApplicationUrl", example_qa_application.application_url)
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] deployment_id: The deployment ID of the Q&A Application.
        :param pulumi.Input[bool] external_access_enabled: Whether external access is enabled for the Q&A Application.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] external_access_recipients: The list of external email addresses that have access to the Q&A Application.
        :param pulumi.Input[str] name: The name of the Q&A Application.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: QaApplicationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Q&A Application

        ## Example Usage

        ```python
        import pulumi
        import pulumi_datarobot as datarobot

        example_custom_model = datarobot.CustomModel("exampleCustomModel",
            description="Description for the example custom model",
            target_type="Binary",
            target_name="my_label",
            base_environment_name="[GenAI] Python 3.11 with Moderations",
            local_files=["example.py"])
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
        example_qa_application = datarobot.QaApplication("exampleQaApplication",
            deployment_id=example_deployment.id,
            external_access_enabled=True,
            external_access_recipients=["recipient@example.com"])
        pulumi.export("datarobotQaApplicationId", example_qa_application.id)
        pulumi.export("datarobotQaApplicationSourceId", example_qa_application.source_id)
        pulumi.export("datarobotQaApplicationSourceVersionId", example_qa_application.source_version_id)
        pulumi.export("datarobotQaApplicationUrl", example_qa_application.application_url)
        ```

        :param str resource_name: The name of the resource.
        :param QaApplicationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(QaApplicationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 deployment_id: Optional[pulumi.Input[str]] = None,
                 external_access_enabled: Optional[pulumi.Input[bool]] = None,
                 external_access_recipients: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = QaApplicationArgs.__new__(QaApplicationArgs)

            if deployment_id is None and not opts.urn:
                raise TypeError("Missing required property 'deployment_id'")
            __props__.__dict__["deployment_id"] = deployment_id
            __props__.__dict__["external_access_enabled"] = external_access_enabled
            __props__.__dict__["external_access_recipients"] = external_access_recipients
            __props__.__dict__["name"] = name
            __props__.__dict__["application_url"] = None
            __props__.__dict__["source_id"] = None
            __props__.__dict__["source_version_id"] = None
        super(QaApplication, __self__).__init__(
            'datarobot:index/qaApplication:QaApplication',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            application_url: Optional[pulumi.Input[str]] = None,
            deployment_id: Optional[pulumi.Input[str]] = None,
            external_access_enabled: Optional[pulumi.Input[bool]] = None,
            external_access_recipients: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            name: Optional[pulumi.Input[str]] = None,
            source_id: Optional[pulumi.Input[str]] = None,
            source_version_id: Optional[pulumi.Input[str]] = None) -> 'QaApplication':
        """
        Get an existing QaApplication resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] application_url: The URL of the Q&A Application.
        :param pulumi.Input[str] deployment_id: The deployment ID of the Q&A Application.
        :param pulumi.Input[bool] external_access_enabled: Whether external access is enabled for the Q&A Application.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] external_access_recipients: The list of external email addresses that have access to the Q&A Application.
        :param pulumi.Input[str] name: The name of the Q&A Application.
        :param pulumi.Input[str] source_id: The ID of the Q&A Application Source.
        :param pulumi.Input[str] source_version_id: The version ID of the Q&A Application Source.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _QaApplicationState.__new__(_QaApplicationState)

        __props__.__dict__["application_url"] = application_url
        __props__.__dict__["deployment_id"] = deployment_id
        __props__.__dict__["external_access_enabled"] = external_access_enabled
        __props__.__dict__["external_access_recipients"] = external_access_recipients
        __props__.__dict__["name"] = name
        __props__.__dict__["source_id"] = source_id
        __props__.__dict__["source_version_id"] = source_version_id
        return QaApplication(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="applicationUrl")
    def application_url(self) -> pulumi.Output[str]:
        """
        The URL of the Q&A Application.
        """
        return pulumi.get(self, "application_url")

    @property
    @pulumi.getter(name="deploymentId")
    def deployment_id(self) -> pulumi.Output[str]:
        """
        The deployment ID of the Q&A Application.
        """
        return pulumi.get(self, "deployment_id")

    @property
    @pulumi.getter(name="externalAccessEnabled")
    def external_access_enabled(self) -> pulumi.Output[bool]:
        """
        Whether external access is enabled for the Q&A Application.
        """
        return pulumi.get(self, "external_access_enabled")

    @property
    @pulumi.getter(name="externalAccessRecipients")
    def external_access_recipients(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        The list of external email addresses that have access to the Q&A Application.
        """
        return pulumi.get(self, "external_access_recipients")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the Q&A Application.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="sourceId")
    def source_id(self) -> pulumi.Output[str]:
        """
        The ID of the Q&A Application Source.
        """
        return pulumi.get(self, "source_id")

    @property
    @pulumi.getter(name="sourceVersionId")
    def source_version_id(self) -> pulumi.Output[str]:
        """
        The version ID of the Q&A Application Source.
        """
        return pulumi.get(self, "source_version_id")
