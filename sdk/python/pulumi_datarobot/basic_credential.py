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

__all__ = ['BasicCredentialArgs', 'BasicCredential']

@pulumi.input_type
class BasicCredentialArgs:
    def __init__(__self__, *,
                 password: pulumi.Input[builtins.str],
                 user: pulumi.Input[builtins.str],
                 description: Optional[pulumi.Input[builtins.str]] = None,
                 name: Optional[pulumi.Input[builtins.str]] = None):
        """
        The set of arguments for constructing a BasicCredential resource.
        :param pulumi.Input[builtins.str] password: The password of the Basic Credential.
        :param pulumi.Input[builtins.str] user: The user of the Basic Credential.
        :param pulumi.Input[builtins.str] description: The description of the Basic Credential.
        :param pulumi.Input[builtins.str] name: The name of the Basic Credential.
        """
        pulumi.set(__self__, "password", password)
        pulumi.set(__self__, "user", user)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def password(self) -> pulumi.Input[builtins.str]:
        """
        The password of the Basic Credential.
        """
        return pulumi.get(self, "password")

    @password.setter
    def password(self, value: pulumi.Input[builtins.str]):
        pulumi.set(self, "password", value)

    @property
    @pulumi.getter
    def user(self) -> pulumi.Input[builtins.str]:
        """
        The user of the Basic Credential.
        """
        return pulumi.get(self, "user")

    @user.setter
    def user(self, value: pulumi.Input[builtins.str]):
        pulumi.set(self, "user", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The description of the Basic Credential.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The name of the Basic Credential.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _BasicCredentialState:
    def __init__(__self__, *,
                 description: Optional[pulumi.Input[builtins.str]] = None,
                 name: Optional[pulumi.Input[builtins.str]] = None,
                 password: Optional[pulumi.Input[builtins.str]] = None,
                 user: Optional[pulumi.Input[builtins.str]] = None):
        """
        Input properties used for looking up and filtering BasicCredential resources.
        :param pulumi.Input[builtins.str] description: The description of the Basic Credential.
        :param pulumi.Input[builtins.str] name: The name of the Basic Credential.
        :param pulumi.Input[builtins.str] password: The password of the Basic Credential.
        :param pulumi.Input[builtins.str] user: The user of the Basic Credential.
        """
        if description is not None:
            pulumi.set(__self__, "description", description)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if password is not None:
            pulumi.set(__self__, "password", password)
        if user is not None:
            pulumi.set(__self__, "user", user)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The description of the Basic Credential.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The name of the Basic Credential.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The password of the Basic Credential.
        """
        return pulumi.get(self, "password")

    @password.setter
    def password(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "password", value)

    @property
    @pulumi.getter
    def user(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The user of the Basic Credential.
        """
        return pulumi.get(self, "user")

    @user.setter
    def user(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "user", value)


class BasicCredential(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[builtins.str]] = None,
                 name: Optional[pulumi.Input[builtins.str]] = None,
                 password: Optional[pulumi.Input[builtins.str]] = None,
                 user: Optional[pulumi.Input[builtins.str]] = None,
                 __props__=None):
        """
        Basic Credential

        ## Example Usage

        ```python
        import pulumi
        import pulumi_datarobot as datarobot

        example = datarobot.BasicCredential("example",
            description="Description for the example basic credential",
            password="example_password",
            user="example_user")
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[builtins.str] description: The description of the Basic Credential.
        :param pulumi.Input[builtins.str] name: The name of the Basic Credential.
        :param pulumi.Input[builtins.str] password: The password of the Basic Credential.
        :param pulumi.Input[builtins.str] user: The user of the Basic Credential.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: BasicCredentialArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Basic Credential

        ## Example Usage

        ```python
        import pulumi
        import pulumi_datarobot as datarobot

        example = datarobot.BasicCredential("example",
            description="Description for the example basic credential",
            password="example_password",
            user="example_user")
        ```

        :param str resource_name: The name of the resource.
        :param BasicCredentialArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(BasicCredentialArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[builtins.str]] = None,
                 name: Optional[pulumi.Input[builtins.str]] = None,
                 password: Optional[pulumi.Input[builtins.str]] = None,
                 user: Optional[pulumi.Input[builtins.str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = BasicCredentialArgs.__new__(BasicCredentialArgs)

            __props__.__dict__["description"] = description
            __props__.__dict__["name"] = name
            if password is None and not opts.urn:
                raise TypeError("Missing required property 'password'")
            __props__.__dict__["password"] = None if password is None else pulumi.Output.secret(password)
            if user is None and not opts.urn:
                raise TypeError("Missing required property 'user'")
            __props__.__dict__["user"] = None if user is None else pulumi.Output.secret(user)
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["password", "user"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(BasicCredential, __self__).__init__(
            'datarobot:index/basicCredential:BasicCredential',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            description: Optional[pulumi.Input[builtins.str]] = None,
            name: Optional[pulumi.Input[builtins.str]] = None,
            password: Optional[pulumi.Input[builtins.str]] = None,
            user: Optional[pulumi.Input[builtins.str]] = None) -> 'BasicCredential':
        """
        Get an existing BasicCredential resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[builtins.str] description: The description of the Basic Credential.
        :param pulumi.Input[builtins.str] name: The name of the Basic Credential.
        :param pulumi.Input[builtins.str] password: The password of the Basic Credential.
        :param pulumi.Input[builtins.str] user: The user of the Basic Credential.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _BasicCredentialState.__new__(_BasicCredentialState)

        __props__.__dict__["description"] = description
        __props__.__dict__["name"] = name
        __props__.__dict__["password"] = password
        __props__.__dict__["user"] = user
        return BasicCredential(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[builtins.str]]:
        """
        The description of the Basic Credential.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[builtins.str]:
        """
        The name of the Basic Credential.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def password(self) -> pulumi.Output[builtins.str]:
        """
        The password of the Basic Credential.
        """
        return pulumi.get(self, "password")

    @property
    @pulumi.getter
    def user(self) -> pulumi.Output[builtins.str]:
        """
        The user of the Basic Credential.
        """
        return pulumi.get(self, "user")

