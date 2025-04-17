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

__all__ = ['AwsCredentialArgs', 'AwsCredential']

@pulumi.input_type
class AwsCredentialArgs:
    def __init__(__self__, *,
                 aws_access_key_id: Optional[pulumi.Input[builtins.str]] = None,
                 aws_secret_access_key: Optional[pulumi.Input[builtins.str]] = None,
                 aws_session_token: Optional[pulumi.Input[builtins.str]] = None,
                 config_id: Optional[pulumi.Input[builtins.str]] = None,
                 description: Optional[pulumi.Input[builtins.str]] = None,
                 name: Optional[pulumi.Input[builtins.str]] = None):
        """
        The set of arguments for constructing a AwsCredential resource.
        :param pulumi.Input[builtins.str] aws_access_key_id: The AWS Access Key ID.
        :param pulumi.Input[builtins.str] aws_secret_access_key: The AWS Secret Access Key.
        :param pulumi.Input[builtins.str] aws_session_token: The AWS Session Token.
        :param pulumi.Input[builtins.str] config_id: The ID of the saved shared secure configuration. If specified, cannot include awsAccessKeyId, awsSecretAccessKey or awsSessionToken.
        :param pulumi.Input[builtins.str] description: The description of the AWS Credential.
        :param pulumi.Input[builtins.str] name: The name of the AWS Credential.
        """
        if aws_access_key_id is not None:
            pulumi.set(__self__, "aws_access_key_id", aws_access_key_id)
        if aws_secret_access_key is not None:
            pulumi.set(__self__, "aws_secret_access_key", aws_secret_access_key)
        if aws_session_token is not None:
            pulumi.set(__self__, "aws_session_token", aws_session_token)
        if config_id is not None:
            pulumi.set(__self__, "config_id", config_id)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="awsAccessKeyId")
    def aws_access_key_id(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The AWS Access Key ID.
        """
        return pulumi.get(self, "aws_access_key_id")

    @aws_access_key_id.setter
    def aws_access_key_id(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "aws_access_key_id", value)

    @property
    @pulumi.getter(name="awsSecretAccessKey")
    def aws_secret_access_key(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The AWS Secret Access Key.
        """
        return pulumi.get(self, "aws_secret_access_key")

    @aws_secret_access_key.setter
    def aws_secret_access_key(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "aws_secret_access_key", value)

    @property
    @pulumi.getter(name="awsSessionToken")
    def aws_session_token(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The AWS Session Token.
        """
        return pulumi.get(self, "aws_session_token")

    @aws_session_token.setter
    def aws_session_token(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "aws_session_token", value)

    @property
    @pulumi.getter(name="configId")
    def config_id(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The ID of the saved shared secure configuration. If specified, cannot include awsAccessKeyId, awsSecretAccessKey or awsSessionToken.
        """
        return pulumi.get(self, "config_id")

    @config_id.setter
    def config_id(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "config_id", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The description of the AWS Credential.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The name of the AWS Credential.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _AwsCredentialState:
    def __init__(__self__, *,
                 aws_access_key_id: Optional[pulumi.Input[builtins.str]] = None,
                 aws_secret_access_key: Optional[pulumi.Input[builtins.str]] = None,
                 aws_session_token: Optional[pulumi.Input[builtins.str]] = None,
                 config_id: Optional[pulumi.Input[builtins.str]] = None,
                 description: Optional[pulumi.Input[builtins.str]] = None,
                 name: Optional[pulumi.Input[builtins.str]] = None):
        """
        Input properties used for looking up and filtering AwsCredential resources.
        :param pulumi.Input[builtins.str] aws_access_key_id: The AWS Access Key ID.
        :param pulumi.Input[builtins.str] aws_secret_access_key: The AWS Secret Access Key.
        :param pulumi.Input[builtins.str] aws_session_token: The AWS Session Token.
        :param pulumi.Input[builtins.str] config_id: The ID of the saved shared secure configuration. If specified, cannot include awsAccessKeyId, awsSecretAccessKey or awsSessionToken.
        :param pulumi.Input[builtins.str] description: The description of the AWS Credential.
        :param pulumi.Input[builtins.str] name: The name of the AWS Credential.
        """
        if aws_access_key_id is not None:
            pulumi.set(__self__, "aws_access_key_id", aws_access_key_id)
        if aws_secret_access_key is not None:
            pulumi.set(__self__, "aws_secret_access_key", aws_secret_access_key)
        if aws_session_token is not None:
            pulumi.set(__self__, "aws_session_token", aws_session_token)
        if config_id is not None:
            pulumi.set(__self__, "config_id", config_id)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="awsAccessKeyId")
    def aws_access_key_id(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The AWS Access Key ID.
        """
        return pulumi.get(self, "aws_access_key_id")

    @aws_access_key_id.setter
    def aws_access_key_id(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "aws_access_key_id", value)

    @property
    @pulumi.getter(name="awsSecretAccessKey")
    def aws_secret_access_key(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The AWS Secret Access Key.
        """
        return pulumi.get(self, "aws_secret_access_key")

    @aws_secret_access_key.setter
    def aws_secret_access_key(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "aws_secret_access_key", value)

    @property
    @pulumi.getter(name="awsSessionToken")
    def aws_session_token(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The AWS Session Token.
        """
        return pulumi.get(self, "aws_session_token")

    @aws_session_token.setter
    def aws_session_token(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "aws_session_token", value)

    @property
    @pulumi.getter(name="configId")
    def config_id(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The ID of the saved shared secure configuration. If specified, cannot include awsAccessKeyId, awsSecretAccessKey or awsSessionToken.
        """
        return pulumi.get(self, "config_id")

    @config_id.setter
    def config_id(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "config_id", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The description of the AWS Credential.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The name of the AWS Credential.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "name", value)


class AwsCredential(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 aws_access_key_id: Optional[pulumi.Input[builtins.str]] = None,
                 aws_secret_access_key: Optional[pulumi.Input[builtins.str]] = None,
                 aws_session_token: Optional[pulumi.Input[builtins.str]] = None,
                 config_id: Optional[pulumi.Input[builtins.str]] = None,
                 description: Optional[pulumi.Input[builtins.str]] = None,
                 name: Optional[pulumi.Input[builtins.str]] = None,
                 __props__=None):
        """
        AWS Credential

        ## Example Usage

        ```python
        import pulumi
        import pulumi_datarobot as datarobot

        example = datarobot.AwsCredential("example",
            aws_access_key_id="example_access_key_id",
            aws_secret_access_key="example_secret_access_key",
            aws_session_token="example_session_token",
            description="Description for the example AWS credential")
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[builtins.str] aws_access_key_id: The AWS Access Key ID.
        :param pulumi.Input[builtins.str] aws_secret_access_key: The AWS Secret Access Key.
        :param pulumi.Input[builtins.str] aws_session_token: The AWS Session Token.
        :param pulumi.Input[builtins.str] config_id: The ID of the saved shared secure configuration. If specified, cannot include awsAccessKeyId, awsSecretAccessKey or awsSessionToken.
        :param pulumi.Input[builtins.str] description: The description of the AWS Credential.
        :param pulumi.Input[builtins.str] name: The name of the AWS Credential.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[AwsCredentialArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        AWS Credential

        ## Example Usage

        ```python
        import pulumi
        import pulumi_datarobot as datarobot

        example = datarobot.AwsCredential("example",
            aws_access_key_id="example_access_key_id",
            aws_secret_access_key="example_secret_access_key",
            aws_session_token="example_session_token",
            description="Description for the example AWS credential")
        ```

        :param str resource_name: The name of the resource.
        :param AwsCredentialArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AwsCredentialArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 aws_access_key_id: Optional[pulumi.Input[builtins.str]] = None,
                 aws_secret_access_key: Optional[pulumi.Input[builtins.str]] = None,
                 aws_session_token: Optional[pulumi.Input[builtins.str]] = None,
                 config_id: Optional[pulumi.Input[builtins.str]] = None,
                 description: Optional[pulumi.Input[builtins.str]] = None,
                 name: Optional[pulumi.Input[builtins.str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AwsCredentialArgs.__new__(AwsCredentialArgs)

            __props__.__dict__["aws_access_key_id"] = aws_access_key_id
            __props__.__dict__["aws_secret_access_key"] = None if aws_secret_access_key is None else pulumi.Output.secret(aws_secret_access_key)
            __props__.__dict__["aws_session_token"] = None if aws_session_token is None else pulumi.Output.secret(aws_session_token)
            __props__.__dict__["config_id"] = config_id
            __props__.__dict__["description"] = description
            __props__.__dict__["name"] = name
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["awsSecretAccessKey", "awsSessionToken"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(AwsCredential, __self__).__init__(
            'datarobot:index/awsCredential:AwsCredential',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            aws_access_key_id: Optional[pulumi.Input[builtins.str]] = None,
            aws_secret_access_key: Optional[pulumi.Input[builtins.str]] = None,
            aws_session_token: Optional[pulumi.Input[builtins.str]] = None,
            config_id: Optional[pulumi.Input[builtins.str]] = None,
            description: Optional[pulumi.Input[builtins.str]] = None,
            name: Optional[pulumi.Input[builtins.str]] = None) -> 'AwsCredential':
        """
        Get an existing AwsCredential resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[builtins.str] aws_access_key_id: The AWS Access Key ID.
        :param pulumi.Input[builtins.str] aws_secret_access_key: The AWS Secret Access Key.
        :param pulumi.Input[builtins.str] aws_session_token: The AWS Session Token.
        :param pulumi.Input[builtins.str] config_id: The ID of the saved shared secure configuration. If specified, cannot include awsAccessKeyId, awsSecretAccessKey or awsSessionToken.
        :param pulumi.Input[builtins.str] description: The description of the AWS Credential.
        :param pulumi.Input[builtins.str] name: The name of the AWS Credential.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _AwsCredentialState.__new__(_AwsCredentialState)

        __props__.__dict__["aws_access_key_id"] = aws_access_key_id
        __props__.__dict__["aws_secret_access_key"] = aws_secret_access_key
        __props__.__dict__["aws_session_token"] = aws_session_token
        __props__.__dict__["config_id"] = config_id
        __props__.__dict__["description"] = description
        __props__.__dict__["name"] = name
        return AwsCredential(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="awsAccessKeyId")
    def aws_access_key_id(self) -> pulumi.Output[Optional[builtins.str]]:
        """
        The AWS Access Key ID.
        """
        return pulumi.get(self, "aws_access_key_id")

    @property
    @pulumi.getter(name="awsSecretAccessKey")
    def aws_secret_access_key(self) -> pulumi.Output[Optional[builtins.str]]:
        """
        The AWS Secret Access Key.
        """
        return pulumi.get(self, "aws_secret_access_key")

    @property
    @pulumi.getter(name="awsSessionToken")
    def aws_session_token(self) -> pulumi.Output[Optional[builtins.str]]:
        """
        The AWS Session Token.
        """
        return pulumi.get(self, "aws_session_token")

    @property
    @pulumi.getter(name="configId")
    def config_id(self) -> pulumi.Output[Optional[builtins.str]]:
        """
        The ID of the saved shared secure configuration. If specified, cannot include awsAccessKeyId, awsSecretAccessKey or awsSessionToken.
        """
        return pulumi.get(self, "config_id")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[builtins.str]]:
        """
        The description of the AWS Credential.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[builtins.str]:
        """
        The name of the AWS Credential.
        """
        return pulumi.get(self, "name")

