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

__all__ = ['ProviderArgs', 'Provider']

@pulumi.input_type
class ProviderArgs:
    def __init__(__self__, *,
                 apikey: Optional[pulumi.Input[builtins.str]] = None,
                 endpoint: Optional[pulumi.Input[builtins.str]] = None,
                 tracecontext: Optional[pulumi.Input[builtins.str]] = None):
        """
        The set of arguments for constructing a Provider resource.
        :param pulumi.Input[builtins.str] apikey: Key to access DataRobot API
        :param pulumi.Input[builtins.str] endpoint: Endpoint for the DataRobot API
        :param pulumi.Input[builtins.str] tracecontext: DataRobot trace context
        """
        if apikey is not None:
            pulumi.set(__self__, "apikey", apikey)
        if endpoint is not None:
            pulumi.set(__self__, "endpoint", endpoint)
        if tracecontext is not None:
            pulumi.set(__self__, "tracecontext", tracecontext)

    @property
    @pulumi.getter
    def apikey(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        Key to access DataRobot API
        """
        return pulumi.get(self, "apikey")

    @apikey.setter
    def apikey(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "apikey", value)

    @property
    @pulumi.getter
    def endpoint(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        Endpoint for the DataRobot API
        """
        return pulumi.get(self, "endpoint")

    @endpoint.setter
    def endpoint(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "endpoint", value)

    @property
    @pulumi.getter
    def tracecontext(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        DataRobot trace context
        """
        return pulumi.get(self, "tracecontext")

    @tracecontext.setter
    def tracecontext(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "tracecontext", value)


@pulumi.type_token("pulumi:providers:datarobot")
class Provider(pulumi.ProviderResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 apikey: Optional[pulumi.Input[builtins.str]] = None,
                 endpoint: Optional[pulumi.Input[builtins.str]] = None,
                 tracecontext: Optional[pulumi.Input[builtins.str]] = None,
                 __props__=None):
        """
        The provider type for the datarobot package. By default, resources use package-wide configuration
        settings, however an explicit `Provider` instance may be created and passed during resource
        construction to achieve fine-grained programmatic control over provider settings. See the
        [documentation](https://www.pulumi.com/docs/reference/programming-model/#providers) for more information.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[builtins.str] apikey: Key to access DataRobot API
        :param pulumi.Input[builtins.str] endpoint: Endpoint for the DataRobot API
        :param pulumi.Input[builtins.str] tracecontext: DataRobot trace context
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[ProviderArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The provider type for the datarobot package. By default, resources use package-wide configuration
        settings, however an explicit `Provider` instance may be created and passed during resource
        construction to achieve fine-grained programmatic control over provider settings. See the
        [documentation](https://www.pulumi.com/docs/reference/programming-model/#providers) for more information.

        :param str resource_name: The name of the resource.
        :param ProviderArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ProviderArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 apikey: Optional[pulumi.Input[builtins.str]] = None,
                 endpoint: Optional[pulumi.Input[builtins.str]] = None,
                 tracecontext: Optional[pulumi.Input[builtins.str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ProviderArgs.__new__(ProviderArgs)

            __props__.__dict__["apikey"] = None if apikey is None else pulumi.Output.secret(apikey)
            __props__.__dict__["endpoint"] = None if endpoint is None else pulumi.Output.secret(endpoint)
            __props__.__dict__["tracecontext"] = None if tracecontext is None else pulumi.Output.secret(tracecontext)
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["apikey", "endpoint", "tracecontext"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(Provider, __self__).__init__(
            'datarobot',
            resource_name,
            __props__,
            opts)

    @property
    @pulumi.getter
    def apikey(self) -> pulumi.Output[Optional[builtins.str]]:
        """
        Key to access DataRobot API
        """
        return pulumi.get(self, "apikey")

    @property
    @pulumi.getter
    def endpoint(self) -> pulumi.Output[Optional[builtins.str]]:
        """
        Endpoint for the DataRobot API
        """
        return pulumi.get(self, "endpoint")

    @property
    @pulumi.getter
    def tracecontext(self) -> pulumi.Output[Optional[builtins.str]]:
        """
        DataRobot trace context
        """
        return pulumi.get(self, "tracecontext")

    @pulumi.output_type
    class TerraformConfigResult:
        def __init__(__self__, result=None):
            if result and not isinstance(result, dict):
                raise TypeError("Expected argument 'result' to be a dict")
            pulumi.set(__self__, "result", result)

        @property
        @pulumi.getter
        def result(self) -> Mapping[str, Any]:
            return pulumi.get(self, "result")

    def terraform_config(__self__) -> pulumi.Output['Provider.TerraformConfigResult']:
        """
        This function returns a Terraform config object with terraform-namecased keys,to be used with the Terraform Module Provider.
        """
        __args__ = dict()
        __args__['__self__'] = __self__
        return pulumi.runtime.call('pulumi:providers:datarobot/terraformConfig', __args__, res=__self__, typ=Provider.TerraformConfigResult)

