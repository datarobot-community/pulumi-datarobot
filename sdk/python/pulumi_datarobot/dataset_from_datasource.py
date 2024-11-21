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

__all__ = ['DatasetFromDatasourceArgs', 'DatasetFromDatasource']

@pulumi.input_type
class DatasetFromDatasourceArgs:
    def __init__(__self__, *,
                 credential_id: pulumi.Input[str],
                 data_source_id: pulumi.Input[str],
                 categories: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 do_snapshot: Optional[pulumi.Input[bool]] = None,
                 persist_data_after_ingestion: Optional[pulumi.Input[bool]] = None,
                 sample_size_rows: Optional[pulumi.Input[int]] = None,
                 use_case_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 use_kerberos: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a DatasetFromDatasource resource.
        :param pulumi.Input[str] credential_id: The ID of the set of credentials to use.
        :param pulumi.Input[str] data_source_id: The ID for the DataSource to use as the source of data.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] categories: An array of strings describing the intended use of the dataset.
        :param pulumi.Input[bool] do_snapshot: If unset, uses the server default: True. If true, creates a snapshot dataset; if false, creates a remote dataset.
        :param pulumi.Input[bool] persist_data_after_ingestion: If unset, uses the server default: True. If true, will enforce saving all data (for download and sampling) and will allow a user to view extended data profile (which includes data statistics like min/max/median/mean, histogram, etc.). If false, will not enforce saving data. The data schema (feature names and types) still will be available.
        :param pulumi.Input[int] sample_size_rows: The number of rows fetched during dataset registration.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] use_case_ids: The list of Use Case IDs to add the Dataset to.
        :param pulumi.Input[bool] use_kerberos: If unset, uses the server default: False. If true, use kerberos authentication for database authentication.
        """
        pulumi.set(__self__, "credential_id", credential_id)
        pulumi.set(__self__, "data_source_id", data_source_id)
        if categories is not None:
            pulumi.set(__self__, "categories", categories)
        if do_snapshot is not None:
            pulumi.set(__self__, "do_snapshot", do_snapshot)
        if persist_data_after_ingestion is not None:
            pulumi.set(__self__, "persist_data_after_ingestion", persist_data_after_ingestion)
        if sample_size_rows is not None:
            pulumi.set(__self__, "sample_size_rows", sample_size_rows)
        if use_case_ids is not None:
            pulumi.set(__self__, "use_case_ids", use_case_ids)
        if use_kerberos is not None:
            pulumi.set(__self__, "use_kerberos", use_kerberos)

    @property
    @pulumi.getter(name="credentialId")
    def credential_id(self) -> pulumi.Input[str]:
        """
        The ID of the set of credentials to use.
        """
        return pulumi.get(self, "credential_id")

    @credential_id.setter
    def credential_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "credential_id", value)

    @property
    @pulumi.getter(name="dataSourceId")
    def data_source_id(self) -> pulumi.Input[str]:
        """
        The ID for the DataSource to use as the source of data.
        """
        return pulumi.get(self, "data_source_id")

    @data_source_id.setter
    def data_source_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "data_source_id", value)

    @property
    @pulumi.getter
    def categories(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        An array of strings describing the intended use of the dataset.
        """
        return pulumi.get(self, "categories")

    @categories.setter
    def categories(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "categories", value)

    @property
    @pulumi.getter(name="doSnapshot")
    def do_snapshot(self) -> Optional[pulumi.Input[bool]]:
        """
        If unset, uses the server default: True. If true, creates a snapshot dataset; if false, creates a remote dataset.
        """
        return pulumi.get(self, "do_snapshot")

    @do_snapshot.setter
    def do_snapshot(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "do_snapshot", value)

    @property
    @pulumi.getter(name="persistDataAfterIngestion")
    def persist_data_after_ingestion(self) -> Optional[pulumi.Input[bool]]:
        """
        If unset, uses the server default: True. If true, will enforce saving all data (for download and sampling) and will allow a user to view extended data profile (which includes data statistics like min/max/median/mean, histogram, etc.). If false, will not enforce saving data. The data schema (feature names and types) still will be available.
        """
        return pulumi.get(self, "persist_data_after_ingestion")

    @persist_data_after_ingestion.setter
    def persist_data_after_ingestion(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "persist_data_after_ingestion", value)

    @property
    @pulumi.getter(name="sampleSizeRows")
    def sample_size_rows(self) -> Optional[pulumi.Input[int]]:
        """
        The number of rows fetched during dataset registration.
        """
        return pulumi.get(self, "sample_size_rows")

    @sample_size_rows.setter
    def sample_size_rows(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "sample_size_rows", value)

    @property
    @pulumi.getter(name="useCaseIds")
    def use_case_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The list of Use Case IDs to add the Dataset to.
        """
        return pulumi.get(self, "use_case_ids")

    @use_case_ids.setter
    def use_case_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "use_case_ids", value)

    @property
    @pulumi.getter(name="useKerberos")
    def use_kerberos(self) -> Optional[pulumi.Input[bool]]:
        """
        If unset, uses the server default: False. If true, use kerberos authentication for database authentication.
        """
        return pulumi.get(self, "use_kerberos")

    @use_kerberos.setter
    def use_kerberos(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "use_kerberos", value)


@pulumi.input_type
class _DatasetFromDatasourceState:
    def __init__(__self__, *,
                 categories: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 credential_id: Optional[pulumi.Input[str]] = None,
                 data_source_id: Optional[pulumi.Input[str]] = None,
                 do_snapshot: Optional[pulumi.Input[bool]] = None,
                 persist_data_after_ingestion: Optional[pulumi.Input[bool]] = None,
                 sample_size_rows: Optional[pulumi.Input[int]] = None,
                 use_case_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 use_kerberos: Optional[pulumi.Input[bool]] = None):
        """
        Input properties used for looking up and filtering DatasetFromDatasource resources.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] categories: An array of strings describing the intended use of the dataset.
        :param pulumi.Input[str] credential_id: The ID of the set of credentials to use.
        :param pulumi.Input[str] data_source_id: The ID for the DataSource to use as the source of data.
        :param pulumi.Input[bool] do_snapshot: If unset, uses the server default: True. If true, creates a snapshot dataset; if false, creates a remote dataset.
        :param pulumi.Input[bool] persist_data_after_ingestion: If unset, uses the server default: True. If true, will enforce saving all data (for download and sampling) and will allow a user to view extended data profile (which includes data statistics like min/max/median/mean, histogram, etc.). If false, will not enforce saving data. The data schema (feature names and types) still will be available.
        :param pulumi.Input[int] sample_size_rows: The number of rows fetched during dataset registration.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] use_case_ids: The list of Use Case IDs to add the Dataset to.
        :param pulumi.Input[bool] use_kerberos: If unset, uses the server default: False. If true, use kerberos authentication for database authentication.
        """
        if categories is not None:
            pulumi.set(__self__, "categories", categories)
        if credential_id is not None:
            pulumi.set(__self__, "credential_id", credential_id)
        if data_source_id is not None:
            pulumi.set(__self__, "data_source_id", data_source_id)
        if do_snapshot is not None:
            pulumi.set(__self__, "do_snapshot", do_snapshot)
        if persist_data_after_ingestion is not None:
            pulumi.set(__self__, "persist_data_after_ingestion", persist_data_after_ingestion)
        if sample_size_rows is not None:
            pulumi.set(__self__, "sample_size_rows", sample_size_rows)
        if use_case_ids is not None:
            pulumi.set(__self__, "use_case_ids", use_case_ids)
        if use_kerberos is not None:
            pulumi.set(__self__, "use_kerberos", use_kerberos)

    @property
    @pulumi.getter
    def categories(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        An array of strings describing the intended use of the dataset.
        """
        return pulumi.get(self, "categories")

    @categories.setter
    def categories(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "categories", value)

    @property
    @pulumi.getter(name="credentialId")
    def credential_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the set of credentials to use.
        """
        return pulumi.get(self, "credential_id")

    @credential_id.setter
    def credential_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "credential_id", value)

    @property
    @pulumi.getter(name="dataSourceId")
    def data_source_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID for the DataSource to use as the source of data.
        """
        return pulumi.get(self, "data_source_id")

    @data_source_id.setter
    def data_source_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "data_source_id", value)

    @property
    @pulumi.getter(name="doSnapshot")
    def do_snapshot(self) -> Optional[pulumi.Input[bool]]:
        """
        If unset, uses the server default: True. If true, creates a snapshot dataset; if false, creates a remote dataset.
        """
        return pulumi.get(self, "do_snapshot")

    @do_snapshot.setter
    def do_snapshot(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "do_snapshot", value)

    @property
    @pulumi.getter(name="persistDataAfterIngestion")
    def persist_data_after_ingestion(self) -> Optional[pulumi.Input[bool]]:
        """
        If unset, uses the server default: True. If true, will enforce saving all data (for download and sampling) and will allow a user to view extended data profile (which includes data statistics like min/max/median/mean, histogram, etc.). If false, will not enforce saving data. The data schema (feature names and types) still will be available.
        """
        return pulumi.get(self, "persist_data_after_ingestion")

    @persist_data_after_ingestion.setter
    def persist_data_after_ingestion(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "persist_data_after_ingestion", value)

    @property
    @pulumi.getter(name="sampleSizeRows")
    def sample_size_rows(self) -> Optional[pulumi.Input[int]]:
        """
        The number of rows fetched during dataset registration.
        """
        return pulumi.get(self, "sample_size_rows")

    @sample_size_rows.setter
    def sample_size_rows(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "sample_size_rows", value)

    @property
    @pulumi.getter(name="useCaseIds")
    def use_case_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The list of Use Case IDs to add the Dataset to.
        """
        return pulumi.get(self, "use_case_ids")

    @use_case_ids.setter
    def use_case_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "use_case_ids", value)

    @property
    @pulumi.getter(name="useKerberos")
    def use_kerberos(self) -> Optional[pulumi.Input[bool]]:
        """
        If unset, uses the server default: False. If true, use kerberos authentication for database authentication.
        """
        return pulumi.get(self, "use_kerberos")

    @use_kerberos.setter
    def use_kerberos(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "use_kerberos", value)


class DatasetFromDatasource(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 categories: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 credential_id: Optional[pulumi.Input[str]] = None,
                 data_source_id: Optional[pulumi.Input[str]] = None,
                 do_snapshot: Optional[pulumi.Input[bool]] = None,
                 persist_data_after_ingestion: Optional[pulumi.Input[bool]] = None,
                 sample_size_rows: Optional[pulumi.Input[int]] = None,
                 use_case_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 use_kerberos: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        """
        Data Set from Data Source.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_datarobot as datarobot

        example = datarobot.DatasetFromDatasource("example",
            datasource_id=datarobot_datasource["example"]["id"],
            credential_id=datarobot_credential["example"]["id"],
            do_snapshot=False,
            persist_data_after_ingestion=False,
            use_kerberos=True,
            categories=["TRAINING"],
            use_case_ids=[datarobot_use_case["example"]["id"]])
        pulumi.export("exampleId", example.id)
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] categories: An array of strings describing the intended use of the dataset.
        :param pulumi.Input[str] credential_id: The ID of the set of credentials to use.
        :param pulumi.Input[str] data_source_id: The ID for the DataSource to use as the source of data.
        :param pulumi.Input[bool] do_snapshot: If unset, uses the server default: True. If true, creates a snapshot dataset; if false, creates a remote dataset.
        :param pulumi.Input[bool] persist_data_after_ingestion: If unset, uses the server default: True. If true, will enforce saving all data (for download and sampling) and will allow a user to view extended data profile (which includes data statistics like min/max/median/mean, histogram, etc.). If false, will not enforce saving data. The data schema (feature names and types) still will be available.
        :param pulumi.Input[int] sample_size_rows: The number of rows fetched during dataset registration.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] use_case_ids: The list of Use Case IDs to add the Dataset to.
        :param pulumi.Input[bool] use_kerberos: If unset, uses the server default: False. If true, use kerberos authentication for database authentication.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DatasetFromDatasourceArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Data Set from Data Source.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_datarobot as datarobot

        example = datarobot.DatasetFromDatasource("example",
            datasource_id=datarobot_datasource["example"]["id"],
            credential_id=datarobot_credential["example"]["id"],
            do_snapshot=False,
            persist_data_after_ingestion=False,
            use_kerberos=True,
            categories=["TRAINING"],
            use_case_ids=[datarobot_use_case["example"]["id"]])
        pulumi.export("exampleId", example.id)
        ```

        :param str resource_name: The name of the resource.
        :param DatasetFromDatasourceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DatasetFromDatasourceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 categories: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 credential_id: Optional[pulumi.Input[str]] = None,
                 data_source_id: Optional[pulumi.Input[str]] = None,
                 do_snapshot: Optional[pulumi.Input[bool]] = None,
                 persist_data_after_ingestion: Optional[pulumi.Input[bool]] = None,
                 sample_size_rows: Optional[pulumi.Input[int]] = None,
                 use_case_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 use_kerberos: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DatasetFromDatasourceArgs.__new__(DatasetFromDatasourceArgs)

            __props__.__dict__["categories"] = categories
            if credential_id is None and not opts.urn:
                raise TypeError("Missing required property 'credential_id'")
            __props__.__dict__["credential_id"] = credential_id
            if data_source_id is None and not opts.urn:
                raise TypeError("Missing required property 'data_source_id'")
            __props__.__dict__["data_source_id"] = data_source_id
            __props__.__dict__["do_snapshot"] = do_snapshot
            __props__.__dict__["persist_data_after_ingestion"] = persist_data_after_ingestion
            __props__.__dict__["sample_size_rows"] = sample_size_rows
            __props__.__dict__["use_case_ids"] = use_case_ids
            __props__.__dict__["use_kerberos"] = use_kerberos
        super(DatasetFromDatasource, __self__).__init__(
            'datarobot:index/datasetFromDatasource:DatasetFromDatasource',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            categories: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            credential_id: Optional[pulumi.Input[str]] = None,
            data_source_id: Optional[pulumi.Input[str]] = None,
            do_snapshot: Optional[pulumi.Input[bool]] = None,
            persist_data_after_ingestion: Optional[pulumi.Input[bool]] = None,
            sample_size_rows: Optional[pulumi.Input[int]] = None,
            use_case_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            use_kerberos: Optional[pulumi.Input[bool]] = None) -> 'DatasetFromDatasource':
        """
        Get an existing DatasetFromDatasource resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] categories: An array of strings describing the intended use of the dataset.
        :param pulumi.Input[str] credential_id: The ID of the set of credentials to use.
        :param pulumi.Input[str] data_source_id: The ID for the DataSource to use as the source of data.
        :param pulumi.Input[bool] do_snapshot: If unset, uses the server default: True. If true, creates a snapshot dataset; if false, creates a remote dataset.
        :param pulumi.Input[bool] persist_data_after_ingestion: If unset, uses the server default: True. If true, will enforce saving all data (for download and sampling) and will allow a user to view extended data profile (which includes data statistics like min/max/median/mean, histogram, etc.). If false, will not enforce saving data. The data schema (feature names and types) still will be available.
        :param pulumi.Input[int] sample_size_rows: The number of rows fetched during dataset registration.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] use_case_ids: The list of Use Case IDs to add the Dataset to.
        :param pulumi.Input[bool] use_kerberos: If unset, uses the server default: False. If true, use kerberos authentication for database authentication.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _DatasetFromDatasourceState.__new__(_DatasetFromDatasourceState)

        __props__.__dict__["categories"] = categories
        __props__.__dict__["credential_id"] = credential_id
        __props__.__dict__["data_source_id"] = data_source_id
        __props__.__dict__["do_snapshot"] = do_snapshot
        __props__.__dict__["persist_data_after_ingestion"] = persist_data_after_ingestion
        __props__.__dict__["sample_size_rows"] = sample_size_rows
        __props__.__dict__["use_case_ids"] = use_case_ids
        __props__.__dict__["use_kerberos"] = use_kerberos
        return DatasetFromDatasource(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def categories(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        An array of strings describing the intended use of the dataset.
        """
        return pulumi.get(self, "categories")

    @property
    @pulumi.getter(name="credentialId")
    def credential_id(self) -> pulumi.Output[str]:
        """
        The ID of the set of credentials to use.
        """
        return pulumi.get(self, "credential_id")

    @property
    @pulumi.getter(name="dataSourceId")
    def data_source_id(self) -> pulumi.Output[str]:
        """
        The ID for the DataSource to use as the source of data.
        """
        return pulumi.get(self, "data_source_id")

    @property
    @pulumi.getter(name="doSnapshot")
    def do_snapshot(self) -> pulumi.Output[bool]:
        """
        If unset, uses the server default: True. If true, creates a snapshot dataset; if false, creates a remote dataset.
        """
        return pulumi.get(self, "do_snapshot")

    @property
    @pulumi.getter(name="persistDataAfterIngestion")
    def persist_data_after_ingestion(self) -> pulumi.Output[bool]:
        """
        If unset, uses the server default: True. If true, will enforce saving all data (for download and sampling) and will allow a user to view extended data profile (which includes data statistics like min/max/median/mean, histogram, etc.). If false, will not enforce saving data. The data schema (feature names and types) still will be available.
        """
        return pulumi.get(self, "persist_data_after_ingestion")

    @property
    @pulumi.getter(name="sampleSizeRows")
    def sample_size_rows(self) -> pulumi.Output[Optional[int]]:
        """
        The number of rows fetched during dataset registration.
        """
        return pulumi.get(self, "sample_size_rows")

    @property
    @pulumi.getter(name="useCaseIds")
    def use_case_ids(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        The list of Use Case IDs to add the Dataset to.
        """
        return pulumi.get(self, "use_case_ids")

    @property
    @pulumi.getter(name="useKerberos")
    def use_kerberos(self) -> pulumi.Output[bool]:
        """
        If unset, uses the server default: False. If true, use kerberos authentication for database authentication.
        """
        return pulumi.get(self, "use_kerberos")

