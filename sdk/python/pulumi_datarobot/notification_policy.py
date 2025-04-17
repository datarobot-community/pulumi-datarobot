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

__all__ = ['NotificationPolicyArgs', 'NotificationPolicy']

@pulumi.input_type
class NotificationPolicyArgs:
    def __init__(__self__, *,
                 channel_id: pulumi.Input[builtins.str],
                 channel_scope: pulumi.Input[builtins.str],
                 related_entity_id: pulumi.Input[builtins.str],
                 related_entity_type: pulumi.Input[builtins.str],
                 active: Optional[pulumi.Input[builtins.bool]] = None,
                 event_group: Optional[pulumi.Input[builtins.str]] = None,
                 event_type: Optional[pulumi.Input[builtins.str]] = None,
                 maximal_frequency: Optional[pulumi.Input[builtins.str]] = None,
                 name: Optional[pulumi.Input[builtins.str]] = None):
        """
        The set of arguments for constructing a NotificationPolicy resource.
        :param pulumi.Input[builtins.str] channel_id: The Channel ID of the Notification Policy.
        :param pulumi.Input[builtins.str] channel_scope: The Channel scope of the Notification Policy.
        :param pulumi.Input[builtins.str] related_entity_id: The ID of the related entity for the Notification Policy.
        :param pulumi.Input[builtins.str] related_entity_type: The Type of the related entity for the Notification Policy.
        :param pulumi.Input[builtins.bool] active: Whether or not the Notification Policy is active.
        :param pulumi.Input[builtins.str] event_group: The group of the events that trigger the Notification.
        :param pulumi.Input[builtins.str] event_type: The group of the event that triggers the Notification.
        :param pulumi.Input[builtins.str] maximal_frequency: The maximal frequency between policy runs in ISO 8601 duration string.
        :param pulumi.Input[builtins.str] name: The name of the Notification Policy.
        """
        pulumi.set(__self__, "channel_id", channel_id)
        pulumi.set(__self__, "channel_scope", channel_scope)
        pulumi.set(__self__, "related_entity_id", related_entity_id)
        pulumi.set(__self__, "related_entity_type", related_entity_type)
        if active is not None:
            pulumi.set(__self__, "active", active)
        if event_group is not None:
            pulumi.set(__self__, "event_group", event_group)
        if event_type is not None:
            pulumi.set(__self__, "event_type", event_type)
        if maximal_frequency is not None:
            pulumi.set(__self__, "maximal_frequency", maximal_frequency)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="channelId")
    def channel_id(self) -> pulumi.Input[builtins.str]:
        """
        The Channel ID of the Notification Policy.
        """
        return pulumi.get(self, "channel_id")

    @channel_id.setter
    def channel_id(self, value: pulumi.Input[builtins.str]):
        pulumi.set(self, "channel_id", value)

    @property
    @pulumi.getter(name="channelScope")
    def channel_scope(self) -> pulumi.Input[builtins.str]:
        """
        The Channel scope of the Notification Policy.
        """
        return pulumi.get(self, "channel_scope")

    @channel_scope.setter
    def channel_scope(self, value: pulumi.Input[builtins.str]):
        pulumi.set(self, "channel_scope", value)

    @property
    @pulumi.getter(name="relatedEntityId")
    def related_entity_id(self) -> pulumi.Input[builtins.str]:
        """
        The ID of the related entity for the Notification Policy.
        """
        return pulumi.get(self, "related_entity_id")

    @related_entity_id.setter
    def related_entity_id(self, value: pulumi.Input[builtins.str]):
        pulumi.set(self, "related_entity_id", value)

    @property
    @pulumi.getter(name="relatedEntityType")
    def related_entity_type(self) -> pulumi.Input[builtins.str]:
        """
        The Type of the related entity for the Notification Policy.
        """
        return pulumi.get(self, "related_entity_type")

    @related_entity_type.setter
    def related_entity_type(self, value: pulumi.Input[builtins.str]):
        pulumi.set(self, "related_entity_type", value)

    @property
    @pulumi.getter
    def active(self) -> Optional[pulumi.Input[builtins.bool]]:
        """
        Whether or not the Notification Policy is active.
        """
        return pulumi.get(self, "active")

    @active.setter
    def active(self, value: Optional[pulumi.Input[builtins.bool]]):
        pulumi.set(self, "active", value)

    @property
    @pulumi.getter(name="eventGroup")
    def event_group(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The group of the events that trigger the Notification.
        """
        return pulumi.get(self, "event_group")

    @event_group.setter
    def event_group(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "event_group", value)

    @property
    @pulumi.getter(name="eventType")
    def event_type(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The group of the event that triggers the Notification.
        """
        return pulumi.get(self, "event_type")

    @event_type.setter
    def event_type(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "event_type", value)

    @property
    @pulumi.getter(name="maximalFrequency")
    def maximal_frequency(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The maximal frequency between policy runs in ISO 8601 duration string.
        """
        return pulumi.get(self, "maximal_frequency")

    @maximal_frequency.setter
    def maximal_frequency(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "maximal_frequency", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The name of the Notification Policy.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _NotificationPolicyState:
    def __init__(__self__, *,
                 active: Optional[pulumi.Input[builtins.bool]] = None,
                 channel_id: Optional[pulumi.Input[builtins.str]] = None,
                 channel_scope: Optional[pulumi.Input[builtins.str]] = None,
                 event_group: Optional[pulumi.Input[builtins.str]] = None,
                 event_type: Optional[pulumi.Input[builtins.str]] = None,
                 maximal_frequency: Optional[pulumi.Input[builtins.str]] = None,
                 name: Optional[pulumi.Input[builtins.str]] = None,
                 related_entity_id: Optional[pulumi.Input[builtins.str]] = None,
                 related_entity_type: Optional[pulumi.Input[builtins.str]] = None):
        """
        Input properties used for looking up and filtering NotificationPolicy resources.
        :param pulumi.Input[builtins.bool] active: Whether or not the Notification Policy is active.
        :param pulumi.Input[builtins.str] channel_id: The Channel ID of the Notification Policy.
        :param pulumi.Input[builtins.str] channel_scope: The Channel scope of the Notification Policy.
        :param pulumi.Input[builtins.str] event_group: The group of the events that trigger the Notification.
        :param pulumi.Input[builtins.str] event_type: The group of the event that triggers the Notification.
        :param pulumi.Input[builtins.str] maximal_frequency: The maximal frequency between policy runs in ISO 8601 duration string.
        :param pulumi.Input[builtins.str] name: The name of the Notification Policy.
        :param pulumi.Input[builtins.str] related_entity_id: The ID of the related entity for the Notification Policy.
        :param pulumi.Input[builtins.str] related_entity_type: The Type of the related entity for the Notification Policy.
        """
        if active is not None:
            pulumi.set(__self__, "active", active)
        if channel_id is not None:
            pulumi.set(__self__, "channel_id", channel_id)
        if channel_scope is not None:
            pulumi.set(__self__, "channel_scope", channel_scope)
        if event_group is not None:
            pulumi.set(__self__, "event_group", event_group)
        if event_type is not None:
            pulumi.set(__self__, "event_type", event_type)
        if maximal_frequency is not None:
            pulumi.set(__self__, "maximal_frequency", maximal_frequency)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if related_entity_id is not None:
            pulumi.set(__self__, "related_entity_id", related_entity_id)
        if related_entity_type is not None:
            pulumi.set(__self__, "related_entity_type", related_entity_type)

    @property
    @pulumi.getter
    def active(self) -> Optional[pulumi.Input[builtins.bool]]:
        """
        Whether or not the Notification Policy is active.
        """
        return pulumi.get(self, "active")

    @active.setter
    def active(self, value: Optional[pulumi.Input[builtins.bool]]):
        pulumi.set(self, "active", value)

    @property
    @pulumi.getter(name="channelId")
    def channel_id(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The Channel ID of the Notification Policy.
        """
        return pulumi.get(self, "channel_id")

    @channel_id.setter
    def channel_id(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "channel_id", value)

    @property
    @pulumi.getter(name="channelScope")
    def channel_scope(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The Channel scope of the Notification Policy.
        """
        return pulumi.get(self, "channel_scope")

    @channel_scope.setter
    def channel_scope(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "channel_scope", value)

    @property
    @pulumi.getter(name="eventGroup")
    def event_group(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The group of the events that trigger the Notification.
        """
        return pulumi.get(self, "event_group")

    @event_group.setter
    def event_group(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "event_group", value)

    @property
    @pulumi.getter(name="eventType")
    def event_type(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The group of the event that triggers the Notification.
        """
        return pulumi.get(self, "event_type")

    @event_type.setter
    def event_type(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "event_type", value)

    @property
    @pulumi.getter(name="maximalFrequency")
    def maximal_frequency(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The maximal frequency between policy runs in ISO 8601 duration string.
        """
        return pulumi.get(self, "maximal_frequency")

    @maximal_frequency.setter
    def maximal_frequency(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "maximal_frequency", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The name of the Notification Policy.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="relatedEntityId")
    def related_entity_id(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The ID of the related entity for the Notification Policy.
        """
        return pulumi.get(self, "related_entity_id")

    @related_entity_id.setter
    def related_entity_id(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "related_entity_id", value)

    @property
    @pulumi.getter(name="relatedEntityType")
    def related_entity_type(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The Type of the related entity for the Notification Policy.
        """
        return pulumi.get(self, "related_entity_type")

    @related_entity_type.setter
    def related_entity_type(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "related_entity_type", value)


class NotificationPolicy(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 active: Optional[pulumi.Input[builtins.bool]] = None,
                 channel_id: Optional[pulumi.Input[builtins.str]] = None,
                 channel_scope: Optional[pulumi.Input[builtins.str]] = None,
                 event_group: Optional[pulumi.Input[builtins.str]] = None,
                 event_type: Optional[pulumi.Input[builtins.str]] = None,
                 maximal_frequency: Optional[pulumi.Input[builtins.str]] = None,
                 name: Optional[pulumi.Input[builtins.str]] = None,
                 related_entity_id: Optional[pulumi.Input[builtins.str]] = None,
                 related_entity_type: Optional[pulumi.Input[builtins.str]] = None,
                 __props__=None):
        """
        Notification Policy

        ## Example Usage

        ```python
        import pulumi
        import pulumi_datarobot as datarobot

        example = datarobot.NotificationPolicy("example",
            channel_id="11111111111111",
            channel_scope="template",
            event_group="model_deployments.all",
            related_entity_id=datarobot_deployment["example"]["id"],
            related_entity_type="deployment",
            event_type="model_deployments.accuracy_green",
            maximal_frequency="PT1H")
        pulumi.export("datarobotNotificationPolicyId", example.id)
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[builtins.bool] active: Whether or not the Notification Policy is active.
        :param pulumi.Input[builtins.str] channel_id: The Channel ID of the Notification Policy.
        :param pulumi.Input[builtins.str] channel_scope: The Channel scope of the Notification Policy.
        :param pulumi.Input[builtins.str] event_group: The group of the events that trigger the Notification.
        :param pulumi.Input[builtins.str] event_type: The group of the event that triggers the Notification.
        :param pulumi.Input[builtins.str] maximal_frequency: The maximal frequency between policy runs in ISO 8601 duration string.
        :param pulumi.Input[builtins.str] name: The name of the Notification Policy.
        :param pulumi.Input[builtins.str] related_entity_id: The ID of the related entity for the Notification Policy.
        :param pulumi.Input[builtins.str] related_entity_type: The Type of the related entity for the Notification Policy.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: NotificationPolicyArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Notification Policy

        ## Example Usage

        ```python
        import pulumi
        import pulumi_datarobot as datarobot

        example = datarobot.NotificationPolicy("example",
            channel_id="11111111111111",
            channel_scope="template",
            event_group="model_deployments.all",
            related_entity_id=datarobot_deployment["example"]["id"],
            related_entity_type="deployment",
            event_type="model_deployments.accuracy_green",
            maximal_frequency="PT1H")
        pulumi.export("datarobotNotificationPolicyId", example.id)
        ```

        :param str resource_name: The name of the resource.
        :param NotificationPolicyArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(NotificationPolicyArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 active: Optional[pulumi.Input[builtins.bool]] = None,
                 channel_id: Optional[pulumi.Input[builtins.str]] = None,
                 channel_scope: Optional[pulumi.Input[builtins.str]] = None,
                 event_group: Optional[pulumi.Input[builtins.str]] = None,
                 event_type: Optional[pulumi.Input[builtins.str]] = None,
                 maximal_frequency: Optional[pulumi.Input[builtins.str]] = None,
                 name: Optional[pulumi.Input[builtins.str]] = None,
                 related_entity_id: Optional[pulumi.Input[builtins.str]] = None,
                 related_entity_type: Optional[pulumi.Input[builtins.str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = NotificationPolicyArgs.__new__(NotificationPolicyArgs)

            __props__.__dict__["active"] = active
            if channel_id is None and not opts.urn:
                raise TypeError("Missing required property 'channel_id'")
            __props__.__dict__["channel_id"] = channel_id
            if channel_scope is None and not opts.urn:
                raise TypeError("Missing required property 'channel_scope'")
            __props__.__dict__["channel_scope"] = channel_scope
            __props__.__dict__["event_group"] = event_group
            __props__.__dict__["event_type"] = event_type
            __props__.__dict__["maximal_frequency"] = maximal_frequency
            __props__.__dict__["name"] = name
            if related_entity_id is None and not opts.urn:
                raise TypeError("Missing required property 'related_entity_id'")
            __props__.__dict__["related_entity_id"] = related_entity_id
            if related_entity_type is None and not opts.urn:
                raise TypeError("Missing required property 'related_entity_type'")
            __props__.__dict__["related_entity_type"] = related_entity_type
        super(NotificationPolicy, __self__).__init__(
            'datarobot:index/notificationPolicy:NotificationPolicy',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            active: Optional[pulumi.Input[builtins.bool]] = None,
            channel_id: Optional[pulumi.Input[builtins.str]] = None,
            channel_scope: Optional[pulumi.Input[builtins.str]] = None,
            event_group: Optional[pulumi.Input[builtins.str]] = None,
            event_type: Optional[pulumi.Input[builtins.str]] = None,
            maximal_frequency: Optional[pulumi.Input[builtins.str]] = None,
            name: Optional[pulumi.Input[builtins.str]] = None,
            related_entity_id: Optional[pulumi.Input[builtins.str]] = None,
            related_entity_type: Optional[pulumi.Input[builtins.str]] = None) -> 'NotificationPolicy':
        """
        Get an existing NotificationPolicy resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[builtins.bool] active: Whether or not the Notification Policy is active.
        :param pulumi.Input[builtins.str] channel_id: The Channel ID of the Notification Policy.
        :param pulumi.Input[builtins.str] channel_scope: The Channel scope of the Notification Policy.
        :param pulumi.Input[builtins.str] event_group: The group of the events that trigger the Notification.
        :param pulumi.Input[builtins.str] event_type: The group of the event that triggers the Notification.
        :param pulumi.Input[builtins.str] maximal_frequency: The maximal frequency between policy runs in ISO 8601 duration string.
        :param pulumi.Input[builtins.str] name: The name of the Notification Policy.
        :param pulumi.Input[builtins.str] related_entity_id: The ID of the related entity for the Notification Policy.
        :param pulumi.Input[builtins.str] related_entity_type: The Type of the related entity for the Notification Policy.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _NotificationPolicyState.__new__(_NotificationPolicyState)

        __props__.__dict__["active"] = active
        __props__.__dict__["channel_id"] = channel_id
        __props__.__dict__["channel_scope"] = channel_scope
        __props__.__dict__["event_group"] = event_group
        __props__.__dict__["event_type"] = event_type
        __props__.__dict__["maximal_frequency"] = maximal_frequency
        __props__.__dict__["name"] = name
        __props__.__dict__["related_entity_id"] = related_entity_id
        __props__.__dict__["related_entity_type"] = related_entity_type
        return NotificationPolicy(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def active(self) -> pulumi.Output[builtins.bool]:
        """
        Whether or not the Notification Policy is active.
        """
        return pulumi.get(self, "active")

    @property
    @pulumi.getter(name="channelId")
    def channel_id(self) -> pulumi.Output[builtins.str]:
        """
        The Channel ID of the Notification Policy.
        """
        return pulumi.get(self, "channel_id")

    @property
    @pulumi.getter(name="channelScope")
    def channel_scope(self) -> pulumi.Output[builtins.str]:
        """
        The Channel scope of the Notification Policy.
        """
        return pulumi.get(self, "channel_scope")

    @property
    @pulumi.getter(name="eventGroup")
    def event_group(self) -> pulumi.Output[Optional[builtins.str]]:
        """
        The group of the events that trigger the Notification.
        """
        return pulumi.get(self, "event_group")

    @property
    @pulumi.getter(name="eventType")
    def event_type(self) -> pulumi.Output[Optional[builtins.str]]:
        """
        The group of the event that triggers the Notification.
        """
        return pulumi.get(self, "event_type")

    @property
    @pulumi.getter(name="maximalFrequency")
    def maximal_frequency(self) -> pulumi.Output[Optional[builtins.str]]:
        """
        The maximal frequency between policy runs in ISO 8601 duration string.
        """
        return pulumi.get(self, "maximal_frequency")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[builtins.str]:
        """
        The name of the Notification Policy.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="relatedEntityId")
    def related_entity_id(self) -> pulumi.Output[builtins.str]:
        """
        The ID of the related entity for the Notification Policy.
        """
        return pulumi.get(self, "related_entity_id")

    @property
    @pulumi.getter(name="relatedEntityType")
    def related_entity_type(self) -> pulumi.Output[builtins.str]:
        """
        The Type of the related entity for the Notification Policy.
        """
        return pulumi.get(self, "related_entity_type")

