# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['ChatApplicationArgs', 'ChatApplication']

@pulumi.input_type
class ChatApplicationArgs:
    def __init__(__self__, *,
                 deployment_id: pulumi.Input[str],
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ChatApplication resource.
        :param pulumi.Input[str] deployment_id: The deployment ID of the Chat Application.
        :param pulumi.Input[str] name: The name of the Chat Application.
        """
        pulumi.set(__self__, "deployment_id", deployment_id)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="deploymentId")
    def deployment_id(self) -> pulumi.Input[str]:
        """
        The deployment ID of the Chat Application.
        """
        return pulumi.get(self, "deployment_id")

    @deployment_id.setter
    def deployment_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "deployment_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Chat Application.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _ChatApplicationState:
    def __init__(__self__, *,
                 application_url: Optional[pulumi.Input[str]] = None,
                 deployment_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 version_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering ChatApplication resources.
        :param pulumi.Input[str] application_url: The URL of the Chat Application.
        :param pulumi.Input[str] deployment_id: The deployment ID of the Chat Application.
        :param pulumi.Input[str] name: The name of the Chat Application.
        :param pulumi.Input[str] version_id: The version ID of the Chat Application.
        """
        if application_url is not None:
            pulumi.set(__self__, "application_url", application_url)
        if deployment_id is not None:
            pulumi.set(__self__, "deployment_id", deployment_id)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if version_id is not None:
            pulumi.set(__self__, "version_id", version_id)

    @property
    @pulumi.getter(name="applicationUrl")
    def application_url(self) -> Optional[pulumi.Input[str]]:
        """
        The URL of the Chat Application.
        """
        return pulumi.get(self, "application_url")

    @application_url.setter
    def application_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "application_url", value)

    @property
    @pulumi.getter(name="deploymentId")
    def deployment_id(self) -> Optional[pulumi.Input[str]]:
        """
        The deployment ID of the Chat Application.
        """
        return pulumi.get(self, "deployment_id")

    @deployment_id.setter
    def deployment_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "deployment_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Chat Application.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="versionId")
    def version_id(self) -> Optional[pulumi.Input[str]]:
        """
        The version ID of the Chat Application.
        """
        return pulumi.get(self, "version_id")

    @version_id.setter
    def version_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "version_id", value)


class ChatApplication(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 deployment_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Chat Application

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] deployment_id: The deployment ID of the Chat Application.
        :param pulumi.Input[str] name: The name of the Chat Application.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ChatApplicationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Chat Application

        :param str resource_name: The name of the resource.
        :param ChatApplicationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ChatApplicationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 deployment_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ChatApplicationArgs.__new__(ChatApplicationArgs)

            if deployment_id is None and not opts.urn:
                raise TypeError("Missing required property 'deployment_id'")
            __props__.__dict__["deployment_id"] = deployment_id
            __props__.__dict__["name"] = name
            __props__.__dict__["application_url"] = None
            __props__.__dict__["version_id"] = None
        super(ChatApplication, __self__).__init__(
            'datarobot:index/chatApplication:ChatApplication',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            application_url: Optional[pulumi.Input[str]] = None,
            deployment_id: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            version_id: Optional[pulumi.Input[str]] = None) -> 'ChatApplication':
        """
        Get an existing ChatApplication resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] application_url: The URL of the Chat Application.
        :param pulumi.Input[str] deployment_id: The deployment ID of the Chat Application.
        :param pulumi.Input[str] name: The name of the Chat Application.
        :param pulumi.Input[str] version_id: The version ID of the Chat Application.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ChatApplicationState.__new__(_ChatApplicationState)

        __props__.__dict__["application_url"] = application_url
        __props__.__dict__["deployment_id"] = deployment_id
        __props__.__dict__["name"] = name
        __props__.__dict__["version_id"] = version_id
        return ChatApplication(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="applicationUrl")
    def application_url(self) -> pulumi.Output[str]:
        """
        The URL of the Chat Application.
        """
        return pulumi.get(self, "application_url")

    @property
    @pulumi.getter(name="deploymentId")
    def deployment_id(self) -> pulumi.Output[str]:
        """
        The deployment ID of the Chat Application.
        """
        return pulumi.get(self, "deployment_id")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the Chat Application.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="versionId")
    def version_id(self) -> pulumi.Output[str]:
        """
        The version ID of the Chat Application.
        """
        return pulumi.get(self, "version_id")

