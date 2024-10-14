# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

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

__all__ = ['GoogleCloudCredentialArgs', 'GoogleCloudCredential']

@pulumi.input_type
class GoogleCloudCredentialArgs:
    def __init__(__self__, *,
                 gcp_key: Optional[pulumi.Input[str]] = None,
                 gcp_key_file: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a GoogleCloudCredential resource.
        :param pulumi.Input[str] gcp_key: The GCP key in JSON format.
        :param pulumi.Input[str] gcp_key_file: The file that has the GCP key. Cannot be used with `gcp_key`.
        :param pulumi.Input[str] name: The name of the Google Cloud Credential.
        """
        if gcp_key is not None:
            pulumi.set(__self__, "gcp_key", gcp_key)
        if gcp_key_file is not None:
            pulumi.set(__self__, "gcp_key_file", gcp_key_file)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="gcpKey")
    def gcp_key(self) -> Optional[pulumi.Input[str]]:
        """
        The GCP key in JSON format.
        """
        return pulumi.get(self, "gcp_key")

    @gcp_key.setter
    def gcp_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "gcp_key", value)

    @property
    @pulumi.getter(name="gcpKeyFile")
    def gcp_key_file(self) -> Optional[pulumi.Input[str]]:
        """
        The file that has the GCP key. Cannot be used with `gcp_key`.
        """
        return pulumi.get(self, "gcp_key_file")

    @gcp_key_file.setter
    def gcp_key_file(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "gcp_key_file", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Google Cloud Credential.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _GoogleCloudCredentialState:
    def __init__(__self__, *,
                 gcp_key: Optional[pulumi.Input[str]] = None,
                 gcp_key_file: Optional[pulumi.Input[str]] = None,
                 gcp_key_file_hash: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering GoogleCloudCredential resources.
        :param pulumi.Input[str] gcp_key: The GCP key in JSON format.
        :param pulumi.Input[str] gcp_key_file: The file that has the GCP key. Cannot be used with `gcp_key`.
        :param pulumi.Input[str] gcp_key_file_hash: The hash of the GCP key file contents.
        :param pulumi.Input[str] name: The name of the Google Cloud Credential.
        """
        if gcp_key is not None:
            pulumi.set(__self__, "gcp_key", gcp_key)
        if gcp_key_file is not None:
            pulumi.set(__self__, "gcp_key_file", gcp_key_file)
        if gcp_key_file_hash is not None:
            pulumi.set(__self__, "gcp_key_file_hash", gcp_key_file_hash)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="gcpKey")
    def gcp_key(self) -> Optional[pulumi.Input[str]]:
        """
        The GCP key in JSON format.
        """
        return pulumi.get(self, "gcp_key")

    @gcp_key.setter
    def gcp_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "gcp_key", value)

    @property
    @pulumi.getter(name="gcpKeyFile")
    def gcp_key_file(self) -> Optional[pulumi.Input[str]]:
        """
        The file that has the GCP key. Cannot be used with `gcp_key`.
        """
        return pulumi.get(self, "gcp_key_file")

    @gcp_key_file.setter
    def gcp_key_file(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "gcp_key_file", value)

    @property
    @pulumi.getter(name="gcpKeyFileHash")
    def gcp_key_file_hash(self) -> Optional[pulumi.Input[str]]:
        """
        The hash of the GCP key file contents.
        """
        return pulumi.get(self, "gcp_key_file_hash")

    @gcp_key_file_hash.setter
    def gcp_key_file_hash(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "gcp_key_file_hash", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Google Cloud Credential.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


class GoogleCloudCredential(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 gcp_key: Optional[pulumi.Input[str]] = None,
                 gcp_key_file: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Api Token Credential

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] gcp_key: The GCP key in JSON format.
        :param pulumi.Input[str] gcp_key_file: The file that has the GCP key. Cannot be used with `gcp_key`.
        :param pulumi.Input[str] name: The name of the Google Cloud Credential.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[GoogleCloudCredentialArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Api Token Credential

        :param str resource_name: The name of the resource.
        :param GoogleCloudCredentialArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(GoogleCloudCredentialArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 gcp_key: Optional[pulumi.Input[str]] = None,
                 gcp_key_file: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = GoogleCloudCredentialArgs.__new__(GoogleCloudCredentialArgs)

            __props__.__dict__["gcp_key"] = None if gcp_key is None else pulumi.Output.secret(gcp_key)
            __props__.__dict__["gcp_key_file"] = gcp_key_file
            __props__.__dict__["name"] = name
            __props__.__dict__["gcp_key_file_hash"] = None
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["gcpKey"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(GoogleCloudCredential, __self__).__init__(
            'datarobot:index/googleCloudCredential:GoogleCloudCredential',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            gcp_key: Optional[pulumi.Input[str]] = None,
            gcp_key_file: Optional[pulumi.Input[str]] = None,
            gcp_key_file_hash: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None) -> 'GoogleCloudCredential':
        """
        Get an existing GoogleCloudCredential resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] gcp_key: The GCP key in JSON format.
        :param pulumi.Input[str] gcp_key_file: The file that has the GCP key. Cannot be used with `gcp_key`.
        :param pulumi.Input[str] gcp_key_file_hash: The hash of the GCP key file contents.
        :param pulumi.Input[str] name: The name of the Google Cloud Credential.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _GoogleCloudCredentialState.__new__(_GoogleCloudCredentialState)

        __props__.__dict__["gcp_key"] = gcp_key
        __props__.__dict__["gcp_key_file"] = gcp_key_file
        __props__.__dict__["gcp_key_file_hash"] = gcp_key_file_hash
        __props__.__dict__["name"] = name
        return GoogleCloudCredential(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="gcpKey")
    def gcp_key(self) -> pulumi.Output[Optional[str]]:
        """
        The GCP key in JSON format.
        """
        return pulumi.get(self, "gcp_key")

    @property
    @pulumi.getter(name="gcpKeyFile")
    def gcp_key_file(self) -> pulumi.Output[Optional[str]]:
        """
        The file that has the GCP key. Cannot be used with `gcp_key`.
        """
        return pulumi.get(self, "gcp_key_file")

    @property
    @pulumi.getter(name="gcpKeyFileHash")
    def gcp_key_file_hash(self) -> pulumi.Output[str]:
        """
        The hash of the GCP key file contents.
        """
        return pulumi.get(self, "gcp_key_file_hash")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the Google Cloud Credential.
        """
        return pulumi.get(self, "name")

