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

__all__ = ['AppOauthArgs', 'AppOauth']

@pulumi.input_type
class AppOauthArgs:
    def __init__(__self__, *,
                 client_id: pulumi.Input[builtins.str],
                 client_secret: pulumi.Input[builtins.str],
                 type: pulumi.Input[builtins.str],
                 name: Optional[pulumi.Input[builtins.str]] = None):
        """
        The set of arguments for constructing a AppOauth resource.
        :param pulumi.Input[builtins.str] client_id: OAuth client ID.
        :param pulumi.Input[builtins.str] client_secret: OAuth client secret.
        :param pulumi.Input[builtins.str] type: Type of the OAuth provider, e.g., 'google', 'box', etc.
        :param pulumi.Input[builtins.str] name: Name of the OAuth provider.
        """
        pulumi.set(__self__, "client_id", client_id)
        pulumi.set(__self__, "client_secret", client_secret)
        pulumi.set(__self__, "type", type)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="clientId")
    def client_id(self) -> pulumi.Input[builtins.str]:
        """
        OAuth client ID.
        """
        return pulumi.get(self, "client_id")

    @client_id.setter
    def client_id(self, value: pulumi.Input[builtins.str]):
        pulumi.set(self, "client_id", value)

    @property
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> pulumi.Input[builtins.str]:
        """
        OAuth client secret.
        """
        return pulumi.get(self, "client_secret")

    @client_secret.setter
    def client_secret(self, value: pulumi.Input[builtins.str]):
        pulumi.set(self, "client_secret", value)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[builtins.str]:
        """
        Type of the OAuth provider, e.g., 'google', 'box', etc.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[builtins.str]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        Name of the OAuth provider.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _AppOauthState:
    def __init__(__self__, *,
                 client_id: Optional[pulumi.Input[builtins.str]] = None,
                 client_secret: Optional[pulumi.Input[builtins.str]] = None,
                 name: Optional[pulumi.Input[builtins.str]] = None,
                 org_id: Optional[pulumi.Input[builtins.str]] = None,
                 secure_config_id: Optional[pulumi.Input[builtins.str]] = None,
                 status: Optional[pulumi.Input[builtins.str]] = None,
                 type: Optional[pulumi.Input[builtins.str]] = None):
        """
        Input properties used for looking up and filtering AppOauth resources.
        :param pulumi.Input[builtins.str] client_id: OAuth client ID.
        :param pulumi.Input[builtins.str] client_secret: OAuth client secret.
        :param pulumi.Input[builtins.str] name: Name of the OAuth provider.
        :param pulumi.Input[builtins.str] org_id: Organization ID associated with the OAuth provider.
        :param pulumi.Input[builtins.str] secure_config_id: Secure config ID for the OAuth provider.
        :param pulumi.Input[builtins.str] status: Status of the OAuth provider.
        :param pulumi.Input[builtins.str] type: Type of the OAuth provider, e.g., 'google', 'box', etc.
        """
        if client_id is not None:
            pulumi.set(__self__, "client_id", client_id)
        if client_secret is not None:
            pulumi.set(__self__, "client_secret", client_secret)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if org_id is not None:
            pulumi.set(__self__, "org_id", org_id)
        if secure_config_id is not None:
            pulumi.set(__self__, "secure_config_id", secure_config_id)
        if status is not None:
            pulumi.set(__self__, "status", status)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        OAuth client ID.
        """
        return pulumi.get(self, "client_id")

    @client_id.setter
    def client_id(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "client_id", value)

    @property
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        OAuth client secret.
        """
        return pulumi.get(self, "client_secret")

    @client_secret.setter
    def client_secret(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "client_secret", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        Name of the OAuth provider.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="orgId")
    def org_id(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        Organization ID associated with the OAuth provider.
        """
        return pulumi.get(self, "org_id")

    @org_id.setter
    def org_id(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "org_id", value)

    @property
    @pulumi.getter(name="secureConfigId")
    def secure_config_id(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        Secure config ID for the OAuth provider.
        """
        return pulumi.get(self, "secure_config_id")

    @secure_config_id.setter
    def secure_config_id(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "secure_config_id", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        Status of the OAuth provider.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "status", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        Type of the OAuth provider, e.g., 'google', 'box', etc.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "type", value)


class AppOauth(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 client_id: Optional[pulumi.Input[builtins.str]] = None,
                 client_secret: Optional[pulumi.Input[builtins.str]] = None,
                 name: Optional[pulumi.Input[builtins.str]] = None,
                 type: Optional[pulumi.Input[builtins.str]] = None,
                 __props__=None):
        """
        Resource for managing OAuth providers in DataRobot. This resource allows you to create, read, update, and delete OAuth provider configurations.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[builtins.str] client_id: OAuth client ID.
        :param pulumi.Input[builtins.str] client_secret: OAuth client secret.
        :param pulumi.Input[builtins.str] name: Name of the OAuth provider.
        :param pulumi.Input[builtins.str] type: Type of the OAuth provider, e.g., 'google', 'box', etc.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AppOauthArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource for managing OAuth providers in DataRobot. This resource allows you to create, read, update, and delete OAuth provider configurations.

        :param str resource_name: The name of the resource.
        :param AppOauthArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AppOauthArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 client_id: Optional[pulumi.Input[builtins.str]] = None,
                 client_secret: Optional[pulumi.Input[builtins.str]] = None,
                 name: Optional[pulumi.Input[builtins.str]] = None,
                 type: Optional[pulumi.Input[builtins.str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AppOauthArgs.__new__(AppOauthArgs)

            if client_id is None and not opts.urn:
                raise TypeError("Missing required property 'client_id'")
            __props__.__dict__["client_id"] = None if client_id is None else pulumi.Output.secret(client_id)
            if client_secret is None and not opts.urn:
                raise TypeError("Missing required property 'client_secret'")
            __props__.__dict__["client_secret"] = None if client_secret is None else pulumi.Output.secret(client_secret)
            __props__.__dict__["name"] = name
            if type is None and not opts.urn:
                raise TypeError("Missing required property 'type'")
            __props__.__dict__["type"] = type
            __props__.__dict__["org_id"] = None
            __props__.__dict__["secure_config_id"] = None
            __props__.__dict__["status"] = None
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["clientId", "clientSecret"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(AppOauth, __self__).__init__(
            'datarobot:index/appOauth:AppOauth',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            client_id: Optional[pulumi.Input[builtins.str]] = None,
            client_secret: Optional[pulumi.Input[builtins.str]] = None,
            name: Optional[pulumi.Input[builtins.str]] = None,
            org_id: Optional[pulumi.Input[builtins.str]] = None,
            secure_config_id: Optional[pulumi.Input[builtins.str]] = None,
            status: Optional[pulumi.Input[builtins.str]] = None,
            type: Optional[pulumi.Input[builtins.str]] = None) -> 'AppOauth':
        """
        Get an existing AppOauth resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[builtins.str] client_id: OAuth client ID.
        :param pulumi.Input[builtins.str] client_secret: OAuth client secret.
        :param pulumi.Input[builtins.str] name: Name of the OAuth provider.
        :param pulumi.Input[builtins.str] org_id: Organization ID associated with the OAuth provider.
        :param pulumi.Input[builtins.str] secure_config_id: Secure config ID for the OAuth provider.
        :param pulumi.Input[builtins.str] status: Status of the OAuth provider.
        :param pulumi.Input[builtins.str] type: Type of the OAuth provider, e.g., 'google', 'box', etc.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _AppOauthState.__new__(_AppOauthState)

        __props__.__dict__["client_id"] = client_id
        __props__.__dict__["client_secret"] = client_secret
        __props__.__dict__["name"] = name
        __props__.__dict__["org_id"] = org_id
        __props__.__dict__["secure_config_id"] = secure_config_id
        __props__.__dict__["status"] = status
        __props__.__dict__["type"] = type
        return AppOauth(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="clientId")
    def client_id(self) -> pulumi.Output[builtins.str]:
        """
        OAuth client ID.
        """
        return pulumi.get(self, "client_id")

    @property
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> pulumi.Output[builtins.str]:
        """
        OAuth client secret.
        """
        return pulumi.get(self, "client_secret")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[builtins.str]:
        """
        Name of the OAuth provider.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="orgId")
    def org_id(self) -> pulumi.Output[builtins.str]:
        """
        Organization ID associated with the OAuth provider.
        """
        return pulumi.get(self, "org_id")

    @property
    @pulumi.getter(name="secureConfigId")
    def secure_config_id(self) -> pulumi.Output[builtins.str]:
        """
        Secure config ID for the OAuth provider.
        """
        return pulumi.get(self, "secure_config_id")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[builtins.str]:
        """
        Status of the OAuth provider.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[builtins.str]:
        """
        Type of the OAuth provider, e.g., 'google', 'box', etc.
        """
        return pulumi.get(self, "type")

