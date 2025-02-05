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
from . import outputs
from ._inputs import *

__all__ = ['CustomMetricArgs', 'CustomMetric']

@pulumi.input_type
class CustomMetricArgs:
    def __init__(__self__, *,
                 deployment_id: pulumi.Input[str],
                 directionality: pulumi.Input[str],
                 is_geospatial: pulumi.Input[bool],
                 is_model_specific: pulumi.Input[bool],
                 type: pulumi.Input[str],
                 units: pulumi.Input[str],
                 baseline_value: Optional[pulumi.Input[float]] = None,
                 batch: Optional[pulumi.Input['CustomMetricBatchArgs']] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 sample_count: Optional[pulumi.Input['CustomMetricSampleCountArgs']] = None,
                 timestamp: Optional[pulumi.Input['CustomMetricTimestampArgs']] = None,
                 value: Optional[pulumi.Input['CustomMetricValueArgs']] = None):
        """
        The set of arguments for constructing a CustomMetric resource.
        :param pulumi.Input[str] deployment_id: ID of the Deployment for the Custom Metric.
        :param pulumi.Input[str] directionality: Directionality of the Custom Metric
        :param pulumi.Input[bool] is_geospatial: Determines whether the metric is geospatial.
        :param pulumi.Input[bool] is_model_specific: Determines whether the metric is related to the model or deployment.
        :param pulumi.Input[str] type: Aggregation type of the Custom Metric.
        :param pulumi.Input[str] units: The units, or the y-axis label, of the given Custom Metric.
        :param pulumi.Input[float] baseline_value: The baseline value used to add “reference dots” to the values over time chart.
        :param pulumi.Input['CustomMetricBatchArgs'] batch: A Custom Metric batch ID source when reading values from columnar dataset.
        :param pulumi.Input[str] description: Description of the Custom Metric.
        :param pulumi.Input[str] name: Name of the Custom Metric.
        :param pulumi.Input['CustomMetricSampleCountArgs'] sample_count: A Custom Metric sample source when reading values from columnar dataset.
        :param pulumi.Input['CustomMetricTimestampArgs'] timestamp: A Custom Metric timestamp column source when reading values from columnar dataset.
        :param pulumi.Input['CustomMetricValueArgs'] value: A Custom Metric value source when reading values from columnar dataset.
        """
        pulumi.set(__self__, "deployment_id", deployment_id)
        pulumi.set(__self__, "directionality", directionality)
        pulumi.set(__self__, "is_geospatial", is_geospatial)
        pulumi.set(__self__, "is_model_specific", is_model_specific)
        pulumi.set(__self__, "type", type)
        pulumi.set(__self__, "units", units)
        if baseline_value is not None:
            pulumi.set(__self__, "baseline_value", baseline_value)
        if batch is not None:
            pulumi.set(__self__, "batch", batch)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if sample_count is not None:
            pulumi.set(__self__, "sample_count", sample_count)
        if timestamp is not None:
            pulumi.set(__self__, "timestamp", timestamp)
        if value is not None:
            pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter(name="deploymentId")
    def deployment_id(self) -> pulumi.Input[str]:
        """
        ID of the Deployment for the Custom Metric.
        """
        return pulumi.get(self, "deployment_id")

    @deployment_id.setter
    def deployment_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "deployment_id", value)

    @property
    @pulumi.getter
    def directionality(self) -> pulumi.Input[str]:
        """
        Directionality of the Custom Metric
        """
        return pulumi.get(self, "directionality")

    @directionality.setter
    def directionality(self, value: pulumi.Input[str]):
        pulumi.set(self, "directionality", value)

    @property
    @pulumi.getter(name="isGeospatial")
    def is_geospatial(self) -> pulumi.Input[bool]:
        """
        Determines whether the metric is geospatial.
        """
        return pulumi.get(self, "is_geospatial")

    @is_geospatial.setter
    def is_geospatial(self, value: pulumi.Input[bool]):
        pulumi.set(self, "is_geospatial", value)

    @property
    @pulumi.getter(name="isModelSpecific")
    def is_model_specific(self) -> pulumi.Input[bool]:
        """
        Determines whether the metric is related to the model or deployment.
        """
        return pulumi.get(self, "is_model_specific")

    @is_model_specific.setter
    def is_model_specific(self, value: pulumi.Input[bool]):
        pulumi.set(self, "is_model_specific", value)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        Aggregation type of the Custom Metric.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def units(self) -> pulumi.Input[str]:
        """
        The units, or the y-axis label, of the given Custom Metric.
        """
        return pulumi.get(self, "units")

    @units.setter
    def units(self, value: pulumi.Input[str]):
        pulumi.set(self, "units", value)

    @property
    @pulumi.getter(name="baselineValue")
    def baseline_value(self) -> Optional[pulumi.Input[float]]:
        """
        The baseline value used to add “reference dots” to the values over time chart.
        """
        return pulumi.get(self, "baseline_value")

    @baseline_value.setter
    def baseline_value(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "baseline_value", value)

    @property
    @pulumi.getter
    def batch(self) -> Optional[pulumi.Input['CustomMetricBatchArgs']]:
        """
        A Custom Metric batch ID source when reading values from columnar dataset.
        """
        return pulumi.get(self, "batch")

    @batch.setter
    def batch(self, value: Optional[pulumi.Input['CustomMetricBatchArgs']]):
        pulumi.set(self, "batch", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Description of the Custom Metric.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the Custom Metric.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="sampleCount")
    def sample_count(self) -> Optional[pulumi.Input['CustomMetricSampleCountArgs']]:
        """
        A Custom Metric sample source when reading values from columnar dataset.
        """
        return pulumi.get(self, "sample_count")

    @sample_count.setter
    def sample_count(self, value: Optional[pulumi.Input['CustomMetricSampleCountArgs']]):
        pulumi.set(self, "sample_count", value)

    @property
    @pulumi.getter
    def timestamp(self) -> Optional[pulumi.Input['CustomMetricTimestampArgs']]:
        """
        A Custom Metric timestamp column source when reading values from columnar dataset.
        """
        return pulumi.get(self, "timestamp")

    @timestamp.setter
    def timestamp(self, value: Optional[pulumi.Input['CustomMetricTimestampArgs']]):
        pulumi.set(self, "timestamp", value)

    @property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input['CustomMetricValueArgs']]:
        """
        A Custom Metric value source when reading values from columnar dataset.
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: Optional[pulumi.Input['CustomMetricValueArgs']]):
        pulumi.set(self, "value", value)


@pulumi.input_type
class _CustomMetricState:
    def __init__(__self__, *,
                 baseline_value: Optional[pulumi.Input[float]] = None,
                 batch: Optional[pulumi.Input['CustomMetricBatchArgs']] = None,
                 deployment_id: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 directionality: Optional[pulumi.Input[str]] = None,
                 is_geospatial: Optional[pulumi.Input[bool]] = None,
                 is_model_specific: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 sample_count: Optional[pulumi.Input['CustomMetricSampleCountArgs']] = None,
                 timestamp: Optional[pulumi.Input['CustomMetricTimestampArgs']] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 units: Optional[pulumi.Input[str]] = None,
                 value: Optional[pulumi.Input['CustomMetricValueArgs']] = None):
        """
        Input properties used for looking up and filtering CustomMetric resources.
        :param pulumi.Input[float] baseline_value: The baseline value used to add “reference dots” to the values over time chart.
        :param pulumi.Input['CustomMetricBatchArgs'] batch: A Custom Metric batch ID source when reading values from columnar dataset.
        :param pulumi.Input[str] deployment_id: ID of the Deployment for the Custom Metric.
        :param pulumi.Input[str] description: Description of the Custom Metric.
        :param pulumi.Input[str] directionality: Directionality of the Custom Metric
        :param pulumi.Input[bool] is_geospatial: Determines whether the metric is geospatial.
        :param pulumi.Input[bool] is_model_specific: Determines whether the metric is related to the model or deployment.
        :param pulumi.Input[str] name: Name of the Custom Metric.
        :param pulumi.Input['CustomMetricSampleCountArgs'] sample_count: A Custom Metric sample source when reading values from columnar dataset.
        :param pulumi.Input['CustomMetricTimestampArgs'] timestamp: A Custom Metric timestamp column source when reading values from columnar dataset.
        :param pulumi.Input[str] type: Aggregation type of the Custom Metric.
        :param pulumi.Input[str] units: The units, or the y-axis label, of the given Custom Metric.
        :param pulumi.Input['CustomMetricValueArgs'] value: A Custom Metric value source when reading values from columnar dataset.
        """
        if baseline_value is not None:
            pulumi.set(__self__, "baseline_value", baseline_value)
        if batch is not None:
            pulumi.set(__self__, "batch", batch)
        if deployment_id is not None:
            pulumi.set(__self__, "deployment_id", deployment_id)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if directionality is not None:
            pulumi.set(__self__, "directionality", directionality)
        if is_geospatial is not None:
            pulumi.set(__self__, "is_geospatial", is_geospatial)
        if is_model_specific is not None:
            pulumi.set(__self__, "is_model_specific", is_model_specific)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if sample_count is not None:
            pulumi.set(__self__, "sample_count", sample_count)
        if timestamp is not None:
            pulumi.set(__self__, "timestamp", timestamp)
        if type is not None:
            pulumi.set(__self__, "type", type)
        if units is not None:
            pulumi.set(__self__, "units", units)
        if value is not None:
            pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter(name="baselineValue")
    def baseline_value(self) -> Optional[pulumi.Input[float]]:
        """
        The baseline value used to add “reference dots” to the values over time chart.
        """
        return pulumi.get(self, "baseline_value")

    @baseline_value.setter
    def baseline_value(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "baseline_value", value)

    @property
    @pulumi.getter
    def batch(self) -> Optional[pulumi.Input['CustomMetricBatchArgs']]:
        """
        A Custom Metric batch ID source when reading values from columnar dataset.
        """
        return pulumi.get(self, "batch")

    @batch.setter
    def batch(self, value: Optional[pulumi.Input['CustomMetricBatchArgs']]):
        pulumi.set(self, "batch", value)

    @property
    @pulumi.getter(name="deploymentId")
    def deployment_id(self) -> Optional[pulumi.Input[str]]:
        """
        ID of the Deployment for the Custom Metric.
        """
        return pulumi.get(self, "deployment_id")

    @deployment_id.setter
    def deployment_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "deployment_id", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Description of the Custom Metric.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def directionality(self) -> Optional[pulumi.Input[str]]:
        """
        Directionality of the Custom Metric
        """
        return pulumi.get(self, "directionality")

    @directionality.setter
    def directionality(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "directionality", value)

    @property
    @pulumi.getter(name="isGeospatial")
    def is_geospatial(self) -> Optional[pulumi.Input[bool]]:
        """
        Determines whether the metric is geospatial.
        """
        return pulumi.get(self, "is_geospatial")

    @is_geospatial.setter
    def is_geospatial(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_geospatial", value)

    @property
    @pulumi.getter(name="isModelSpecific")
    def is_model_specific(self) -> Optional[pulumi.Input[bool]]:
        """
        Determines whether the metric is related to the model or deployment.
        """
        return pulumi.get(self, "is_model_specific")

    @is_model_specific.setter
    def is_model_specific(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_model_specific", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the Custom Metric.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="sampleCount")
    def sample_count(self) -> Optional[pulumi.Input['CustomMetricSampleCountArgs']]:
        """
        A Custom Metric sample source when reading values from columnar dataset.
        """
        return pulumi.get(self, "sample_count")

    @sample_count.setter
    def sample_count(self, value: Optional[pulumi.Input['CustomMetricSampleCountArgs']]):
        pulumi.set(self, "sample_count", value)

    @property
    @pulumi.getter
    def timestamp(self) -> Optional[pulumi.Input['CustomMetricTimestampArgs']]:
        """
        A Custom Metric timestamp column source when reading values from columnar dataset.
        """
        return pulumi.get(self, "timestamp")

    @timestamp.setter
    def timestamp(self, value: Optional[pulumi.Input['CustomMetricTimestampArgs']]):
        pulumi.set(self, "timestamp", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        Aggregation type of the Custom Metric.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def units(self) -> Optional[pulumi.Input[str]]:
        """
        The units, or the y-axis label, of the given Custom Metric.
        """
        return pulumi.get(self, "units")

    @units.setter
    def units(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "units", value)

    @property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input['CustomMetricValueArgs']]:
        """
        A Custom Metric value source when reading values from columnar dataset.
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: Optional[pulumi.Input['CustomMetricValueArgs']]):
        pulumi.set(self, "value", value)


class CustomMetric(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 baseline_value: Optional[pulumi.Input[float]] = None,
                 batch: Optional[pulumi.Input[Union['CustomMetricBatchArgs', 'CustomMetricBatchArgsDict']]] = None,
                 deployment_id: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 directionality: Optional[pulumi.Input[str]] = None,
                 is_geospatial: Optional[pulumi.Input[bool]] = None,
                 is_model_specific: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 sample_count: Optional[pulumi.Input[Union['CustomMetricSampleCountArgs', 'CustomMetricSampleCountArgsDict']]] = None,
                 timestamp: Optional[pulumi.Input[Union['CustomMetricTimestampArgs', 'CustomMetricTimestampArgsDict']]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 units: Optional[pulumi.Input[str]] = None,
                 value: Optional[pulumi.Input[Union['CustomMetricValueArgs', 'CustomMetricValueArgsDict']]] = None,
                 __props__=None):
        """
        Custom Metric

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[float] baseline_value: The baseline value used to add “reference dots” to the values over time chart.
        :param pulumi.Input[Union['CustomMetricBatchArgs', 'CustomMetricBatchArgsDict']] batch: A Custom Metric batch ID source when reading values from columnar dataset.
        :param pulumi.Input[str] deployment_id: ID of the Deployment for the Custom Metric.
        :param pulumi.Input[str] description: Description of the Custom Metric.
        :param pulumi.Input[str] directionality: Directionality of the Custom Metric
        :param pulumi.Input[bool] is_geospatial: Determines whether the metric is geospatial.
        :param pulumi.Input[bool] is_model_specific: Determines whether the metric is related to the model or deployment.
        :param pulumi.Input[str] name: Name of the Custom Metric.
        :param pulumi.Input[Union['CustomMetricSampleCountArgs', 'CustomMetricSampleCountArgsDict']] sample_count: A Custom Metric sample source when reading values from columnar dataset.
        :param pulumi.Input[Union['CustomMetricTimestampArgs', 'CustomMetricTimestampArgsDict']] timestamp: A Custom Metric timestamp column source when reading values from columnar dataset.
        :param pulumi.Input[str] type: Aggregation type of the Custom Metric.
        :param pulumi.Input[str] units: The units, or the y-axis label, of the given Custom Metric.
        :param pulumi.Input[Union['CustomMetricValueArgs', 'CustomMetricValueArgsDict']] value: A Custom Metric value source when reading values from columnar dataset.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: CustomMetricArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Custom Metric

        :param str resource_name: The name of the resource.
        :param CustomMetricArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CustomMetricArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 baseline_value: Optional[pulumi.Input[float]] = None,
                 batch: Optional[pulumi.Input[Union['CustomMetricBatchArgs', 'CustomMetricBatchArgsDict']]] = None,
                 deployment_id: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 directionality: Optional[pulumi.Input[str]] = None,
                 is_geospatial: Optional[pulumi.Input[bool]] = None,
                 is_model_specific: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 sample_count: Optional[pulumi.Input[Union['CustomMetricSampleCountArgs', 'CustomMetricSampleCountArgsDict']]] = None,
                 timestamp: Optional[pulumi.Input[Union['CustomMetricTimestampArgs', 'CustomMetricTimestampArgsDict']]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 units: Optional[pulumi.Input[str]] = None,
                 value: Optional[pulumi.Input[Union['CustomMetricValueArgs', 'CustomMetricValueArgsDict']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = CustomMetricArgs.__new__(CustomMetricArgs)

            __props__.__dict__["baseline_value"] = baseline_value
            __props__.__dict__["batch"] = batch
            if deployment_id is None and not opts.urn:
                raise TypeError("Missing required property 'deployment_id'")
            __props__.__dict__["deployment_id"] = deployment_id
            __props__.__dict__["description"] = description
            if directionality is None and not opts.urn:
                raise TypeError("Missing required property 'directionality'")
            __props__.__dict__["directionality"] = directionality
            if is_geospatial is None and not opts.urn:
                raise TypeError("Missing required property 'is_geospatial'")
            __props__.__dict__["is_geospatial"] = is_geospatial
            if is_model_specific is None and not opts.urn:
                raise TypeError("Missing required property 'is_model_specific'")
            __props__.__dict__["is_model_specific"] = is_model_specific
            __props__.__dict__["name"] = name
            __props__.__dict__["sample_count"] = sample_count
            __props__.__dict__["timestamp"] = timestamp
            if type is None and not opts.urn:
                raise TypeError("Missing required property 'type'")
            __props__.__dict__["type"] = type
            if units is None and not opts.urn:
                raise TypeError("Missing required property 'units'")
            __props__.__dict__["units"] = units
            __props__.__dict__["value"] = value
        super(CustomMetric, __self__).__init__(
            'datarobot:index/customMetric:CustomMetric',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            baseline_value: Optional[pulumi.Input[float]] = None,
            batch: Optional[pulumi.Input[Union['CustomMetricBatchArgs', 'CustomMetricBatchArgsDict']]] = None,
            deployment_id: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            directionality: Optional[pulumi.Input[str]] = None,
            is_geospatial: Optional[pulumi.Input[bool]] = None,
            is_model_specific: Optional[pulumi.Input[bool]] = None,
            name: Optional[pulumi.Input[str]] = None,
            sample_count: Optional[pulumi.Input[Union['CustomMetricSampleCountArgs', 'CustomMetricSampleCountArgsDict']]] = None,
            timestamp: Optional[pulumi.Input[Union['CustomMetricTimestampArgs', 'CustomMetricTimestampArgsDict']]] = None,
            type: Optional[pulumi.Input[str]] = None,
            units: Optional[pulumi.Input[str]] = None,
            value: Optional[pulumi.Input[Union['CustomMetricValueArgs', 'CustomMetricValueArgsDict']]] = None) -> 'CustomMetric':
        """
        Get an existing CustomMetric resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[float] baseline_value: The baseline value used to add “reference dots” to the values over time chart.
        :param pulumi.Input[Union['CustomMetricBatchArgs', 'CustomMetricBatchArgsDict']] batch: A Custom Metric batch ID source when reading values from columnar dataset.
        :param pulumi.Input[str] deployment_id: ID of the Deployment for the Custom Metric.
        :param pulumi.Input[str] description: Description of the Custom Metric.
        :param pulumi.Input[str] directionality: Directionality of the Custom Metric
        :param pulumi.Input[bool] is_geospatial: Determines whether the metric is geospatial.
        :param pulumi.Input[bool] is_model_specific: Determines whether the metric is related to the model or deployment.
        :param pulumi.Input[str] name: Name of the Custom Metric.
        :param pulumi.Input[Union['CustomMetricSampleCountArgs', 'CustomMetricSampleCountArgsDict']] sample_count: A Custom Metric sample source when reading values from columnar dataset.
        :param pulumi.Input[Union['CustomMetricTimestampArgs', 'CustomMetricTimestampArgsDict']] timestamp: A Custom Metric timestamp column source when reading values from columnar dataset.
        :param pulumi.Input[str] type: Aggregation type of the Custom Metric.
        :param pulumi.Input[str] units: The units, or the y-axis label, of the given Custom Metric.
        :param pulumi.Input[Union['CustomMetricValueArgs', 'CustomMetricValueArgsDict']] value: A Custom Metric value source when reading values from columnar dataset.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _CustomMetricState.__new__(_CustomMetricState)

        __props__.__dict__["baseline_value"] = baseline_value
        __props__.__dict__["batch"] = batch
        __props__.__dict__["deployment_id"] = deployment_id
        __props__.__dict__["description"] = description
        __props__.__dict__["directionality"] = directionality
        __props__.__dict__["is_geospatial"] = is_geospatial
        __props__.__dict__["is_model_specific"] = is_model_specific
        __props__.__dict__["name"] = name
        __props__.__dict__["sample_count"] = sample_count
        __props__.__dict__["timestamp"] = timestamp
        __props__.__dict__["type"] = type
        __props__.__dict__["units"] = units
        __props__.__dict__["value"] = value
        return CustomMetric(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="baselineValue")
    def baseline_value(self) -> pulumi.Output[Optional[float]]:
        """
        The baseline value used to add “reference dots” to the values over time chart.
        """
        return pulumi.get(self, "baseline_value")

    @property
    @pulumi.getter
    def batch(self) -> pulumi.Output[Optional['outputs.CustomMetricBatch']]:
        """
        A Custom Metric batch ID source when reading values from columnar dataset.
        """
        return pulumi.get(self, "batch")

    @property
    @pulumi.getter(name="deploymentId")
    def deployment_id(self) -> pulumi.Output[str]:
        """
        ID of the Deployment for the Custom Metric.
        """
        return pulumi.get(self, "deployment_id")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Description of the Custom Metric.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def directionality(self) -> pulumi.Output[str]:
        """
        Directionality of the Custom Metric
        """
        return pulumi.get(self, "directionality")

    @property
    @pulumi.getter(name="isGeospatial")
    def is_geospatial(self) -> pulumi.Output[bool]:
        """
        Determines whether the metric is geospatial.
        """
        return pulumi.get(self, "is_geospatial")

    @property
    @pulumi.getter(name="isModelSpecific")
    def is_model_specific(self) -> pulumi.Output[bool]:
        """
        Determines whether the metric is related to the model or deployment.
        """
        return pulumi.get(self, "is_model_specific")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the Custom Metric.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="sampleCount")
    def sample_count(self) -> pulumi.Output[Optional['outputs.CustomMetricSampleCount']]:
        """
        A Custom Metric sample source when reading values from columnar dataset.
        """
        return pulumi.get(self, "sample_count")

    @property
    @pulumi.getter
    def timestamp(self) -> pulumi.Output[Optional['outputs.CustomMetricTimestamp']]:
        """
        A Custom Metric timestamp column source when reading values from columnar dataset.
        """
        return pulumi.get(self, "timestamp")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Aggregation type of the Custom Metric.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def units(self) -> pulumi.Output[str]:
        """
        The units, or the y-axis label, of the given Custom Metric.
        """
        return pulumi.get(self, "units")

    @property
    @pulumi.getter
    def value(self) -> pulumi.Output[Optional['outputs.CustomMetricValue']]:
        """
        A Custom Metric value source when reading values from columnar dataset.
        """
        return pulumi.get(self, "value")

