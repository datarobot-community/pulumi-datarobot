# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import builtins
import copy
import warnings
import sys
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
if sys.version_info >= (3, 11):
    from typing import NotRequired, TypedDict, TypeAlias
else:
    from typing_extensions import NotRequired, TypedDict, TypeAlias
from . import _utilities
from . import outputs
from ._inputs import *

__all__ = ['NotificationChannelArgs', 'NotificationChannel']

@pulumi.input_type
class NotificationChannelArgs:
    def __init__(__self__, *,
                 channel_type: pulumi.Input[builtins.str],
                 related_entity_id: pulumi.Input[builtins.str],
                 related_entity_type: pulumi.Input[builtins.str],
                 content_type: Optional[pulumi.Input[builtins.str]] = None,
                 custom_headers: Optional[pulumi.Input[Sequence[pulumi.Input['NotificationChannelCustomHeaderArgs']]]] = None,
                 dr_entities: Optional[pulumi.Input[Sequence[pulumi.Input['NotificationChannelDrEntityArgs']]]] = None,
                 email_address: Optional[pulumi.Input[builtins.str]] = None,
                 language_code: Optional[pulumi.Input[builtins.str]] = None,
                 name: Optional[pulumi.Input[builtins.str]] = None,
                 payload_url: Optional[pulumi.Input[builtins.str]] = None,
                 secret_token: Optional[pulumi.Input[builtins.str]] = None,
                 validate_ssl: Optional[pulumi.Input[builtins.bool]] = None,
                 verification_code: Optional[pulumi.Input[builtins.str]] = None):
        """
        The set of arguments for constructing a NotificationChannel resource.
        :param pulumi.Input[builtins.str] channel_type: The Type of Notification Channel.
        :param pulumi.Input[builtins.str] related_entity_id: The ID of related entity.
        :param pulumi.Input[builtins.str] related_entity_type: The type of related entity.
        :param pulumi.Input[builtins.str] content_type: The content type of the messages of the Notification Channel.
        :param pulumi.Input[Sequence[pulumi.Input['NotificationChannelCustomHeaderArgs']]] custom_headers: Custom headers and their values to be sent in the Notification Channel.
        :param pulumi.Input[Sequence[pulumi.Input['NotificationChannelDrEntityArgs']]] dr_entities: The IDs of the DataRobot Users, Group or Custom Job associated with the DataRobotUser, DataRobotGroup or DataRobotCustomJob channel types.
        :param pulumi.Input[builtins.str] email_address: The email address to be used in the Notification Channel.
        :param pulumi.Input[builtins.str] language_code: The preferred language code.
        :param pulumi.Input[builtins.str] name: The name of the Notification Channel.
        :param pulumi.Input[builtins.str] payload_url: The payload URL of the Notification Channel.
        :param pulumi.Input[builtins.str] secret_token: The secret token to be used for the Notification Channel.
        :param pulumi.Input[builtins.bool] validate_ssl: Defines if validate ssl or not in the Notification Channel.
        :param pulumi.Input[builtins.str] verification_code: Required if the channel type is email.
        """
        pulumi.set(__self__, "channel_type", channel_type)
        pulumi.set(__self__, "related_entity_id", related_entity_id)
        pulumi.set(__self__, "related_entity_type", related_entity_type)
        if content_type is not None:
            pulumi.set(__self__, "content_type", content_type)
        if custom_headers is not None:
            pulumi.set(__self__, "custom_headers", custom_headers)
        if dr_entities is not None:
            pulumi.set(__self__, "dr_entities", dr_entities)
        if email_address is not None:
            pulumi.set(__self__, "email_address", email_address)
        if language_code is not None:
            pulumi.set(__self__, "language_code", language_code)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if payload_url is not None:
            pulumi.set(__self__, "payload_url", payload_url)
        if secret_token is not None:
            pulumi.set(__self__, "secret_token", secret_token)
        if validate_ssl is not None:
            pulumi.set(__self__, "validate_ssl", validate_ssl)
        if verification_code is not None:
            pulumi.set(__self__, "verification_code", verification_code)

    @property
    @pulumi.getter(name="channelType")
    def channel_type(self) -> pulumi.Input[builtins.str]:
        """
        The Type of Notification Channel.
        """
        return pulumi.get(self, "channel_type")

    @channel_type.setter
    def channel_type(self, value: pulumi.Input[builtins.str]):
        pulumi.set(self, "channel_type", value)

    @property
    @pulumi.getter(name="relatedEntityId")
    def related_entity_id(self) -> pulumi.Input[builtins.str]:
        """
        The ID of related entity.
        """
        return pulumi.get(self, "related_entity_id")

    @related_entity_id.setter
    def related_entity_id(self, value: pulumi.Input[builtins.str]):
        pulumi.set(self, "related_entity_id", value)

    @property
    @pulumi.getter(name="relatedEntityType")
    def related_entity_type(self) -> pulumi.Input[builtins.str]:
        """
        The type of related entity.
        """
        return pulumi.get(self, "related_entity_type")

    @related_entity_type.setter
    def related_entity_type(self, value: pulumi.Input[builtins.str]):
        pulumi.set(self, "related_entity_type", value)

    @property
    @pulumi.getter(name="contentType")
    def content_type(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The content type of the messages of the Notification Channel.
        """
        return pulumi.get(self, "content_type")

    @content_type.setter
    def content_type(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "content_type", value)

    @property
    @pulumi.getter(name="customHeaders")
    def custom_headers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['NotificationChannelCustomHeaderArgs']]]]:
        """
        Custom headers and their values to be sent in the Notification Channel.
        """
        return pulumi.get(self, "custom_headers")

    @custom_headers.setter
    def custom_headers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['NotificationChannelCustomHeaderArgs']]]]):
        pulumi.set(self, "custom_headers", value)

    @property
    @pulumi.getter(name="drEntities")
    def dr_entities(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['NotificationChannelDrEntityArgs']]]]:
        """
        The IDs of the DataRobot Users, Group or Custom Job associated with the DataRobotUser, DataRobotGroup or DataRobotCustomJob channel types.
        """
        return pulumi.get(self, "dr_entities")

    @dr_entities.setter
    def dr_entities(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['NotificationChannelDrEntityArgs']]]]):
        pulumi.set(self, "dr_entities", value)

    @property
    @pulumi.getter(name="emailAddress")
    def email_address(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The email address to be used in the Notification Channel.
        """
        return pulumi.get(self, "email_address")

    @email_address.setter
    def email_address(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "email_address", value)

    @property
    @pulumi.getter(name="languageCode")
    def language_code(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The preferred language code.
        """
        return pulumi.get(self, "language_code")

    @language_code.setter
    def language_code(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "language_code", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The name of the Notification Channel.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="payloadUrl")
    def payload_url(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The payload URL of the Notification Channel.
        """
        return pulumi.get(self, "payload_url")

    @payload_url.setter
    def payload_url(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "payload_url", value)

    @property
    @pulumi.getter(name="secretToken")
    def secret_token(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The secret token to be used for the Notification Channel.
        """
        return pulumi.get(self, "secret_token")

    @secret_token.setter
    def secret_token(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "secret_token", value)

    @property
    @pulumi.getter(name="validateSsl")
    def validate_ssl(self) -> Optional[pulumi.Input[builtins.bool]]:
        """
        Defines if validate ssl or not in the Notification Channel.
        """
        return pulumi.get(self, "validate_ssl")

    @validate_ssl.setter
    def validate_ssl(self, value: Optional[pulumi.Input[builtins.bool]]):
        pulumi.set(self, "validate_ssl", value)

    @property
    @pulumi.getter(name="verificationCode")
    def verification_code(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        Required if the channel type is email.
        """
        return pulumi.get(self, "verification_code")

    @verification_code.setter
    def verification_code(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "verification_code", value)


@pulumi.input_type
class _NotificationChannelState:
    def __init__(__self__, *,
                 channel_type: Optional[pulumi.Input[builtins.str]] = None,
                 content_type: Optional[pulumi.Input[builtins.str]] = None,
                 custom_headers: Optional[pulumi.Input[Sequence[pulumi.Input['NotificationChannelCustomHeaderArgs']]]] = None,
                 dr_entities: Optional[pulumi.Input[Sequence[pulumi.Input['NotificationChannelDrEntityArgs']]]] = None,
                 email_address: Optional[pulumi.Input[builtins.str]] = None,
                 language_code: Optional[pulumi.Input[builtins.str]] = None,
                 name: Optional[pulumi.Input[builtins.str]] = None,
                 payload_url: Optional[pulumi.Input[builtins.str]] = None,
                 related_entity_id: Optional[pulumi.Input[builtins.str]] = None,
                 related_entity_type: Optional[pulumi.Input[builtins.str]] = None,
                 secret_token: Optional[pulumi.Input[builtins.str]] = None,
                 validate_ssl: Optional[pulumi.Input[builtins.bool]] = None,
                 verification_code: Optional[pulumi.Input[builtins.str]] = None):
        """
        Input properties used for looking up and filtering NotificationChannel resources.
        :param pulumi.Input[builtins.str] channel_type: The Type of Notification Channel.
        :param pulumi.Input[builtins.str] content_type: The content type of the messages of the Notification Channel.
        :param pulumi.Input[Sequence[pulumi.Input['NotificationChannelCustomHeaderArgs']]] custom_headers: Custom headers and their values to be sent in the Notification Channel.
        :param pulumi.Input[Sequence[pulumi.Input['NotificationChannelDrEntityArgs']]] dr_entities: The IDs of the DataRobot Users, Group or Custom Job associated with the DataRobotUser, DataRobotGroup or DataRobotCustomJob channel types.
        :param pulumi.Input[builtins.str] email_address: The email address to be used in the Notification Channel.
        :param pulumi.Input[builtins.str] language_code: The preferred language code.
        :param pulumi.Input[builtins.str] name: The name of the Notification Channel.
        :param pulumi.Input[builtins.str] payload_url: The payload URL of the Notification Channel.
        :param pulumi.Input[builtins.str] related_entity_id: The ID of related entity.
        :param pulumi.Input[builtins.str] related_entity_type: The type of related entity.
        :param pulumi.Input[builtins.str] secret_token: The secret token to be used for the Notification Channel.
        :param pulumi.Input[builtins.bool] validate_ssl: Defines if validate ssl or not in the Notification Channel.
        :param pulumi.Input[builtins.str] verification_code: Required if the channel type is email.
        """
        if channel_type is not None:
            pulumi.set(__self__, "channel_type", channel_type)
        if content_type is not None:
            pulumi.set(__self__, "content_type", content_type)
        if custom_headers is not None:
            pulumi.set(__self__, "custom_headers", custom_headers)
        if dr_entities is not None:
            pulumi.set(__self__, "dr_entities", dr_entities)
        if email_address is not None:
            pulumi.set(__self__, "email_address", email_address)
        if language_code is not None:
            pulumi.set(__self__, "language_code", language_code)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if payload_url is not None:
            pulumi.set(__self__, "payload_url", payload_url)
        if related_entity_id is not None:
            pulumi.set(__self__, "related_entity_id", related_entity_id)
        if related_entity_type is not None:
            pulumi.set(__self__, "related_entity_type", related_entity_type)
        if secret_token is not None:
            pulumi.set(__self__, "secret_token", secret_token)
        if validate_ssl is not None:
            pulumi.set(__self__, "validate_ssl", validate_ssl)
        if verification_code is not None:
            pulumi.set(__self__, "verification_code", verification_code)

    @property
    @pulumi.getter(name="channelType")
    def channel_type(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The Type of Notification Channel.
        """
        return pulumi.get(self, "channel_type")

    @channel_type.setter
    def channel_type(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "channel_type", value)

    @property
    @pulumi.getter(name="contentType")
    def content_type(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The content type of the messages of the Notification Channel.
        """
        return pulumi.get(self, "content_type")

    @content_type.setter
    def content_type(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "content_type", value)

    @property
    @pulumi.getter(name="customHeaders")
    def custom_headers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['NotificationChannelCustomHeaderArgs']]]]:
        """
        Custom headers and their values to be sent in the Notification Channel.
        """
        return pulumi.get(self, "custom_headers")

    @custom_headers.setter
    def custom_headers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['NotificationChannelCustomHeaderArgs']]]]):
        pulumi.set(self, "custom_headers", value)

    @property
    @pulumi.getter(name="drEntities")
    def dr_entities(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['NotificationChannelDrEntityArgs']]]]:
        """
        The IDs of the DataRobot Users, Group or Custom Job associated with the DataRobotUser, DataRobotGroup or DataRobotCustomJob channel types.
        """
        return pulumi.get(self, "dr_entities")

    @dr_entities.setter
    def dr_entities(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['NotificationChannelDrEntityArgs']]]]):
        pulumi.set(self, "dr_entities", value)

    @property
    @pulumi.getter(name="emailAddress")
    def email_address(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The email address to be used in the Notification Channel.
        """
        return pulumi.get(self, "email_address")

    @email_address.setter
    def email_address(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "email_address", value)

    @property
    @pulumi.getter(name="languageCode")
    def language_code(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The preferred language code.
        """
        return pulumi.get(self, "language_code")

    @language_code.setter
    def language_code(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "language_code", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The name of the Notification Channel.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="payloadUrl")
    def payload_url(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The payload URL of the Notification Channel.
        """
        return pulumi.get(self, "payload_url")

    @payload_url.setter
    def payload_url(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "payload_url", value)

    @property
    @pulumi.getter(name="relatedEntityId")
    def related_entity_id(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The ID of related entity.
        """
        return pulumi.get(self, "related_entity_id")

    @related_entity_id.setter
    def related_entity_id(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "related_entity_id", value)

    @property
    @pulumi.getter(name="relatedEntityType")
    def related_entity_type(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The type of related entity.
        """
        return pulumi.get(self, "related_entity_type")

    @related_entity_type.setter
    def related_entity_type(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "related_entity_type", value)

    @property
    @pulumi.getter(name="secretToken")
    def secret_token(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The secret token to be used for the Notification Channel.
        """
        return pulumi.get(self, "secret_token")

    @secret_token.setter
    def secret_token(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "secret_token", value)

    @property
    @pulumi.getter(name="validateSsl")
    def validate_ssl(self) -> Optional[pulumi.Input[builtins.bool]]:
        """
        Defines if validate ssl or not in the Notification Channel.
        """
        return pulumi.get(self, "validate_ssl")

    @validate_ssl.setter
    def validate_ssl(self, value: Optional[pulumi.Input[builtins.bool]]):
        pulumi.set(self, "validate_ssl", value)

    @property
    @pulumi.getter(name="verificationCode")
    def verification_code(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        Required if the channel type is email.
        """
        return pulumi.get(self, "verification_code")

    @verification_code.setter
    def verification_code(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "verification_code", value)


class NotificationChannel(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 channel_type: Optional[pulumi.Input[builtins.str]] = None,
                 content_type: Optional[pulumi.Input[builtins.str]] = None,
                 custom_headers: Optional[pulumi.Input[Sequence[pulumi.Input[Union['NotificationChannelCustomHeaderArgs', 'NotificationChannelCustomHeaderArgsDict']]]]] = None,
                 dr_entities: Optional[pulumi.Input[Sequence[pulumi.Input[Union['NotificationChannelDrEntityArgs', 'NotificationChannelDrEntityArgsDict']]]]] = None,
                 email_address: Optional[pulumi.Input[builtins.str]] = None,
                 language_code: Optional[pulumi.Input[builtins.str]] = None,
                 name: Optional[pulumi.Input[builtins.str]] = None,
                 payload_url: Optional[pulumi.Input[builtins.str]] = None,
                 related_entity_id: Optional[pulumi.Input[builtins.str]] = None,
                 related_entity_type: Optional[pulumi.Input[builtins.str]] = None,
                 secret_token: Optional[pulumi.Input[builtins.str]] = None,
                 validate_ssl: Optional[pulumi.Input[builtins.bool]] = None,
                 verification_code: Optional[pulumi.Input[builtins.str]] = None,
                 __props__=None):
        """
        Notification Channel

        ## Example Usage

        ```python
        import pulumi
        import pulumi_datarobot as datarobot

        example = datarobot.NotificationChannel("example",
            channel_type="DataRobotUser",
            related_entity_id=datarobot_deployment["example"]["id"],
            related_entity_type="deployment",
            content_type="application/json",
            custom_headers=[{
                "name": "header1",
                "value": "value1",
            }],
            dr_entities=[{
                "id": "11111111111111",
                "name": "example user",
            }],
            language_code="en",
            email_address="example@datarobot.com",
            payload_url="https://example.com",
            secret_token="example_secret_token",
            validate_ssl=True,
            verification_code="11111")
        pulumi.export("datarobotNotificationPolicyId", datarobot_notification_policy["example"]["id"])
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[builtins.str] channel_type: The Type of Notification Channel.
        :param pulumi.Input[builtins.str] content_type: The content type of the messages of the Notification Channel.
        :param pulumi.Input[Sequence[pulumi.Input[Union['NotificationChannelCustomHeaderArgs', 'NotificationChannelCustomHeaderArgsDict']]]] custom_headers: Custom headers and their values to be sent in the Notification Channel.
        :param pulumi.Input[Sequence[pulumi.Input[Union['NotificationChannelDrEntityArgs', 'NotificationChannelDrEntityArgsDict']]]] dr_entities: The IDs of the DataRobot Users, Group or Custom Job associated with the DataRobotUser, DataRobotGroup or DataRobotCustomJob channel types.
        :param pulumi.Input[builtins.str] email_address: The email address to be used in the Notification Channel.
        :param pulumi.Input[builtins.str] language_code: The preferred language code.
        :param pulumi.Input[builtins.str] name: The name of the Notification Channel.
        :param pulumi.Input[builtins.str] payload_url: The payload URL of the Notification Channel.
        :param pulumi.Input[builtins.str] related_entity_id: The ID of related entity.
        :param pulumi.Input[builtins.str] related_entity_type: The type of related entity.
        :param pulumi.Input[builtins.str] secret_token: The secret token to be used for the Notification Channel.
        :param pulumi.Input[builtins.bool] validate_ssl: Defines if validate ssl or not in the Notification Channel.
        :param pulumi.Input[builtins.str] verification_code: Required if the channel type is email.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: NotificationChannelArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Notification Channel

        ## Example Usage

        ```python
        import pulumi
        import pulumi_datarobot as datarobot

        example = datarobot.NotificationChannel("example",
            channel_type="DataRobotUser",
            related_entity_id=datarobot_deployment["example"]["id"],
            related_entity_type="deployment",
            content_type="application/json",
            custom_headers=[{
                "name": "header1",
                "value": "value1",
            }],
            dr_entities=[{
                "id": "11111111111111",
                "name": "example user",
            }],
            language_code="en",
            email_address="example@datarobot.com",
            payload_url="https://example.com",
            secret_token="example_secret_token",
            validate_ssl=True,
            verification_code="11111")
        pulumi.export("datarobotNotificationPolicyId", datarobot_notification_policy["example"]["id"])
        ```

        :param str resource_name: The name of the resource.
        :param NotificationChannelArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(NotificationChannelArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 channel_type: Optional[pulumi.Input[builtins.str]] = None,
                 content_type: Optional[pulumi.Input[builtins.str]] = None,
                 custom_headers: Optional[pulumi.Input[Sequence[pulumi.Input[Union['NotificationChannelCustomHeaderArgs', 'NotificationChannelCustomHeaderArgsDict']]]]] = None,
                 dr_entities: Optional[pulumi.Input[Sequence[pulumi.Input[Union['NotificationChannelDrEntityArgs', 'NotificationChannelDrEntityArgsDict']]]]] = None,
                 email_address: Optional[pulumi.Input[builtins.str]] = None,
                 language_code: Optional[pulumi.Input[builtins.str]] = None,
                 name: Optional[pulumi.Input[builtins.str]] = None,
                 payload_url: Optional[pulumi.Input[builtins.str]] = None,
                 related_entity_id: Optional[pulumi.Input[builtins.str]] = None,
                 related_entity_type: Optional[pulumi.Input[builtins.str]] = None,
                 secret_token: Optional[pulumi.Input[builtins.str]] = None,
                 validate_ssl: Optional[pulumi.Input[builtins.bool]] = None,
                 verification_code: Optional[pulumi.Input[builtins.str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = NotificationChannelArgs.__new__(NotificationChannelArgs)

            if channel_type is None and not opts.urn:
                raise TypeError("Missing required property 'channel_type'")
            __props__.__dict__["channel_type"] = channel_type
            __props__.__dict__["content_type"] = content_type
            __props__.__dict__["custom_headers"] = custom_headers
            __props__.__dict__["dr_entities"] = dr_entities
            __props__.__dict__["email_address"] = email_address
            __props__.__dict__["language_code"] = language_code
            __props__.__dict__["name"] = name
            __props__.__dict__["payload_url"] = payload_url
            if related_entity_id is None and not opts.urn:
                raise TypeError("Missing required property 'related_entity_id'")
            __props__.__dict__["related_entity_id"] = related_entity_id
            if related_entity_type is None and not opts.urn:
                raise TypeError("Missing required property 'related_entity_type'")
            __props__.__dict__["related_entity_type"] = related_entity_type
            __props__.__dict__["secret_token"] = secret_token
            __props__.__dict__["validate_ssl"] = validate_ssl
            __props__.__dict__["verification_code"] = verification_code
        super(NotificationChannel, __self__).__init__(
            'datarobot:index/notificationChannel:NotificationChannel',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            channel_type: Optional[pulumi.Input[builtins.str]] = None,
            content_type: Optional[pulumi.Input[builtins.str]] = None,
            custom_headers: Optional[pulumi.Input[Sequence[pulumi.Input[Union['NotificationChannelCustomHeaderArgs', 'NotificationChannelCustomHeaderArgsDict']]]]] = None,
            dr_entities: Optional[pulumi.Input[Sequence[pulumi.Input[Union['NotificationChannelDrEntityArgs', 'NotificationChannelDrEntityArgsDict']]]]] = None,
            email_address: Optional[pulumi.Input[builtins.str]] = None,
            language_code: Optional[pulumi.Input[builtins.str]] = None,
            name: Optional[pulumi.Input[builtins.str]] = None,
            payload_url: Optional[pulumi.Input[builtins.str]] = None,
            related_entity_id: Optional[pulumi.Input[builtins.str]] = None,
            related_entity_type: Optional[pulumi.Input[builtins.str]] = None,
            secret_token: Optional[pulumi.Input[builtins.str]] = None,
            validate_ssl: Optional[pulumi.Input[builtins.bool]] = None,
            verification_code: Optional[pulumi.Input[builtins.str]] = None) -> 'NotificationChannel':
        """
        Get an existing NotificationChannel resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[builtins.str] channel_type: The Type of Notification Channel.
        :param pulumi.Input[builtins.str] content_type: The content type of the messages of the Notification Channel.
        :param pulumi.Input[Sequence[pulumi.Input[Union['NotificationChannelCustomHeaderArgs', 'NotificationChannelCustomHeaderArgsDict']]]] custom_headers: Custom headers and their values to be sent in the Notification Channel.
        :param pulumi.Input[Sequence[pulumi.Input[Union['NotificationChannelDrEntityArgs', 'NotificationChannelDrEntityArgsDict']]]] dr_entities: The IDs of the DataRobot Users, Group or Custom Job associated with the DataRobotUser, DataRobotGroup or DataRobotCustomJob channel types.
        :param pulumi.Input[builtins.str] email_address: The email address to be used in the Notification Channel.
        :param pulumi.Input[builtins.str] language_code: The preferred language code.
        :param pulumi.Input[builtins.str] name: The name of the Notification Channel.
        :param pulumi.Input[builtins.str] payload_url: The payload URL of the Notification Channel.
        :param pulumi.Input[builtins.str] related_entity_id: The ID of related entity.
        :param pulumi.Input[builtins.str] related_entity_type: The type of related entity.
        :param pulumi.Input[builtins.str] secret_token: The secret token to be used for the Notification Channel.
        :param pulumi.Input[builtins.bool] validate_ssl: Defines if validate ssl or not in the Notification Channel.
        :param pulumi.Input[builtins.str] verification_code: Required if the channel type is email.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _NotificationChannelState.__new__(_NotificationChannelState)

        __props__.__dict__["channel_type"] = channel_type
        __props__.__dict__["content_type"] = content_type
        __props__.__dict__["custom_headers"] = custom_headers
        __props__.__dict__["dr_entities"] = dr_entities
        __props__.__dict__["email_address"] = email_address
        __props__.__dict__["language_code"] = language_code
        __props__.__dict__["name"] = name
        __props__.__dict__["payload_url"] = payload_url
        __props__.__dict__["related_entity_id"] = related_entity_id
        __props__.__dict__["related_entity_type"] = related_entity_type
        __props__.__dict__["secret_token"] = secret_token
        __props__.__dict__["validate_ssl"] = validate_ssl
        __props__.__dict__["verification_code"] = verification_code
        return NotificationChannel(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="channelType")
    def channel_type(self) -> pulumi.Output[builtins.str]:
        """
        The Type of Notification Channel.
        """
        return pulumi.get(self, "channel_type")

    @property
    @pulumi.getter(name="contentType")
    def content_type(self) -> pulumi.Output[Optional[builtins.str]]:
        """
        The content type of the messages of the Notification Channel.
        """
        return pulumi.get(self, "content_type")

    @property
    @pulumi.getter(name="customHeaders")
    def custom_headers(self) -> pulumi.Output[Optional[Sequence['outputs.NotificationChannelCustomHeader']]]:
        """
        Custom headers and their values to be sent in the Notification Channel.
        """
        return pulumi.get(self, "custom_headers")

    @property
    @pulumi.getter(name="drEntities")
    def dr_entities(self) -> pulumi.Output[Optional[Sequence['outputs.NotificationChannelDrEntity']]]:
        """
        The IDs of the DataRobot Users, Group or Custom Job associated with the DataRobotUser, DataRobotGroup or DataRobotCustomJob channel types.
        """
        return pulumi.get(self, "dr_entities")

    @property
    @pulumi.getter(name="emailAddress")
    def email_address(self) -> pulumi.Output[Optional[builtins.str]]:
        """
        The email address to be used in the Notification Channel.
        """
        return pulumi.get(self, "email_address")

    @property
    @pulumi.getter(name="languageCode")
    def language_code(self) -> pulumi.Output[builtins.str]:
        """
        The preferred language code.
        """
        return pulumi.get(self, "language_code")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[builtins.str]:
        """
        The name of the Notification Channel.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="payloadUrl")
    def payload_url(self) -> pulumi.Output[Optional[builtins.str]]:
        """
        The payload URL of the Notification Channel.
        """
        return pulumi.get(self, "payload_url")

    @property
    @pulumi.getter(name="relatedEntityId")
    def related_entity_id(self) -> pulumi.Output[builtins.str]:
        """
        The ID of related entity.
        """
        return pulumi.get(self, "related_entity_id")

    @property
    @pulumi.getter(name="relatedEntityType")
    def related_entity_type(self) -> pulumi.Output[builtins.str]:
        """
        The type of related entity.
        """
        return pulumi.get(self, "related_entity_type")

    @property
    @pulumi.getter(name="secretToken")
    def secret_token(self) -> pulumi.Output[Optional[builtins.str]]:
        """
        The secret token to be used for the Notification Channel.
        """
        return pulumi.get(self, "secret_token")

    @property
    @pulumi.getter(name="validateSsl")
    def validate_ssl(self) -> pulumi.Output[Optional[builtins.bool]]:
        """
        Defines if validate ssl or not in the Notification Channel.
        """
        return pulumi.get(self, "validate_ssl")

    @property
    @pulumi.getter(name="verificationCode")
    def verification_code(self) -> pulumi.Output[Optional[builtins.str]]:
        """
        Required if the channel type is email.
        """
        return pulumi.get(self, "verification_code")

