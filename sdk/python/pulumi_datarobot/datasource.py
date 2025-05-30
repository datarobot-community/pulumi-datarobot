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

__all__ = ['DatasourceArgs', 'Datasource']

@pulumi.input_type
class DatasourceArgs:
    def __init__(__self__, *,
                 canonical_name: pulumi.Input[builtins.str],
                 data_source_type: pulumi.Input[builtins.str],
                 params: pulumi.Input['DatasourceParamsArgs']):
        """
        The set of arguments for constructing a Datasource resource.
        :param pulumi.Input[builtins.str] canonical_name: The user-friendly name of the data source.
        :param pulumi.Input[builtins.str] data_source_type: The type of data source.
        :param pulumi.Input['DatasourceParamsArgs'] params: The data source parameters.
        """
        pulumi.set(__self__, "canonical_name", canonical_name)
        pulumi.set(__self__, "data_source_type", data_source_type)
        pulumi.set(__self__, "params", params)

    @property
    @pulumi.getter(name="canonicalName")
    def canonical_name(self) -> pulumi.Input[builtins.str]:
        """
        The user-friendly name of the data source.
        """
        return pulumi.get(self, "canonical_name")

    @canonical_name.setter
    def canonical_name(self, value: pulumi.Input[builtins.str]):
        pulumi.set(self, "canonical_name", value)

    @property
    @pulumi.getter(name="dataSourceType")
    def data_source_type(self) -> pulumi.Input[builtins.str]:
        """
        The type of data source.
        """
        return pulumi.get(self, "data_source_type")

    @data_source_type.setter
    def data_source_type(self, value: pulumi.Input[builtins.str]):
        pulumi.set(self, "data_source_type", value)

    @property
    @pulumi.getter
    def params(self) -> pulumi.Input['DatasourceParamsArgs']:
        """
        The data source parameters.
        """
        return pulumi.get(self, "params")

    @params.setter
    def params(self, value: pulumi.Input['DatasourceParamsArgs']):
        pulumi.set(self, "params", value)


@pulumi.input_type
class _DatasourceState:
    def __init__(__self__, *,
                 canonical_name: Optional[pulumi.Input[builtins.str]] = None,
                 data_source_type: Optional[pulumi.Input[builtins.str]] = None,
                 params: Optional[pulumi.Input['DatasourceParamsArgs']] = None):
        """
        Input properties used for looking up and filtering Datasource resources.
        :param pulumi.Input[builtins.str] canonical_name: The user-friendly name of the data source.
        :param pulumi.Input[builtins.str] data_source_type: The type of data source.
        :param pulumi.Input['DatasourceParamsArgs'] params: The data source parameters.
        """
        if canonical_name is not None:
            pulumi.set(__self__, "canonical_name", canonical_name)
        if data_source_type is not None:
            pulumi.set(__self__, "data_source_type", data_source_type)
        if params is not None:
            pulumi.set(__self__, "params", params)

    @property
    @pulumi.getter(name="canonicalName")
    def canonical_name(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The user-friendly name of the data source.
        """
        return pulumi.get(self, "canonical_name")

    @canonical_name.setter
    def canonical_name(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "canonical_name", value)

    @property
    @pulumi.getter(name="dataSourceType")
    def data_source_type(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The type of data source.
        """
        return pulumi.get(self, "data_source_type")

    @data_source_type.setter
    def data_source_type(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "data_source_type", value)

    @property
    @pulumi.getter
    def params(self) -> Optional[pulumi.Input['DatasourceParamsArgs']]:
        """
        The data source parameters.
        """
        return pulumi.get(self, "params")

    @params.setter
    def params(self, value: Optional[pulumi.Input['DatasourceParamsArgs']]):
        pulumi.set(self, "params", value)


@pulumi.type_token("datarobot:index/datasource:Datasource")
class Datasource(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 canonical_name: Optional[pulumi.Input[builtins.str]] = None,
                 data_source_type: Optional[pulumi.Input[builtins.str]] = None,
                 params: Optional[pulumi.Input[Union['DatasourceParamsArgs', 'DatasourceParamsArgsDict']]] = None,
                 __props__=None):
        """
        Data source

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[builtins.str] canonical_name: The user-friendly name of the data source.
        :param pulumi.Input[builtins.str] data_source_type: The type of data source.
        :param pulumi.Input[Union['DatasourceParamsArgs', 'DatasourceParamsArgsDict']] params: The data source parameters.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DatasourceArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Data source

        :param str resource_name: The name of the resource.
        :param DatasourceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DatasourceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 canonical_name: Optional[pulumi.Input[builtins.str]] = None,
                 data_source_type: Optional[pulumi.Input[builtins.str]] = None,
                 params: Optional[pulumi.Input[Union['DatasourceParamsArgs', 'DatasourceParamsArgsDict']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DatasourceArgs.__new__(DatasourceArgs)

            if canonical_name is None and not opts.urn:
                raise TypeError("Missing required property 'canonical_name'")
            __props__.__dict__["canonical_name"] = canonical_name
            if data_source_type is None and not opts.urn:
                raise TypeError("Missing required property 'data_source_type'")
            __props__.__dict__["data_source_type"] = data_source_type
            if params is None and not opts.urn:
                raise TypeError("Missing required property 'params'")
            __props__.__dict__["params"] = params
        super(Datasource, __self__).__init__(
            'datarobot:index/datasource:Datasource',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            canonical_name: Optional[pulumi.Input[builtins.str]] = None,
            data_source_type: Optional[pulumi.Input[builtins.str]] = None,
            params: Optional[pulumi.Input[Union['DatasourceParamsArgs', 'DatasourceParamsArgsDict']]] = None) -> 'Datasource':
        """
        Get an existing Datasource resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[builtins.str] canonical_name: The user-friendly name of the data source.
        :param pulumi.Input[builtins.str] data_source_type: The type of data source.
        :param pulumi.Input[Union['DatasourceParamsArgs', 'DatasourceParamsArgsDict']] params: The data source parameters.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _DatasourceState.__new__(_DatasourceState)

        __props__.__dict__["canonical_name"] = canonical_name
        __props__.__dict__["data_source_type"] = data_source_type
        __props__.__dict__["params"] = params
        return Datasource(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="canonicalName")
    def canonical_name(self) -> pulumi.Output[builtins.str]:
        """
        The user-friendly name of the data source.
        """
        return pulumi.get(self, "canonical_name")

    @property
    @pulumi.getter(name="dataSourceType")
    def data_source_type(self) -> pulumi.Output[builtins.str]:
        """
        The type of data source.
        """
        return pulumi.get(self, "data_source_type")

    @property
    @pulumi.getter
    def params(self) -> pulumi.Output['outputs.DatasourceParams']:
        """
        The data source parameters.
        """
        return pulumi.get(self, "params")

