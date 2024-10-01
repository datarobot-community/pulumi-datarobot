# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['DatasetFromFileArgs', 'DatasetFromFile']

@pulumi.input_type
class DatasetFromFileArgs:
    def __init__(__self__, *,
                 file_path: pulumi.Input[str],
                 name: Optional[pulumi.Input[str]] = None,
                 use_case_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a DatasetFromFile resource.
        :param pulumi.Input[str] file_path: The path to the file to upload.
        :param pulumi.Input[str] name: The name of the Dataset. Defaults to the file name.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] use_case_ids: The list of Use Case IDs to add the Dataset to.
        """
        pulumi.set(__self__, "file_path", file_path)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if use_case_ids is not None:
            pulumi.set(__self__, "use_case_ids", use_case_ids)

    @property
    @pulumi.getter(name="filePath")
    def file_path(self) -> pulumi.Input[str]:
        """
        The path to the file to upload.
        """
        return pulumi.get(self, "file_path")

    @file_path.setter
    def file_path(self, value: pulumi.Input[str]):
        pulumi.set(self, "file_path", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Dataset. Defaults to the file name.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

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


@pulumi.input_type
class _DatasetFromFileState:
    def __init__(__self__, *,
                 file_hash: Optional[pulumi.Input[str]] = None,
                 file_path: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 use_case_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        Input properties used for looking up and filtering DatasetFromFile resources.
        :param pulumi.Input[str] file_hash: The hash of the file contents.
        :param pulumi.Input[str] file_path: The path to the file to upload.
        :param pulumi.Input[str] name: The name of the Dataset. Defaults to the file name.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] use_case_ids: The list of Use Case IDs to add the Dataset to.
        """
        if file_hash is not None:
            pulumi.set(__self__, "file_hash", file_hash)
        if file_path is not None:
            pulumi.set(__self__, "file_path", file_path)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if use_case_ids is not None:
            pulumi.set(__self__, "use_case_ids", use_case_ids)

    @property
    @pulumi.getter(name="fileHash")
    def file_hash(self) -> Optional[pulumi.Input[str]]:
        """
        The hash of the file contents.
        """
        return pulumi.get(self, "file_hash")

    @file_hash.setter
    def file_hash(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "file_hash", value)

    @property
    @pulumi.getter(name="filePath")
    def file_path(self) -> Optional[pulumi.Input[str]]:
        """
        The path to the file to upload.
        """
        return pulumi.get(self, "file_path")

    @file_path.setter
    def file_path(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "file_path", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Dataset. Defaults to the file name.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

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


class DatasetFromFile(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 file_path: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 use_case_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Data set from file

        ## Example Usage

        ```python
        import pulumi
        import pulumi_datarobot as datarobot

        example = datarobot.DatasetFromFile("example",
            file_path="[Path to file to upload]",
            use_case_ids=[datarobot_use_case["example"]["id"]])
        pulumi.export("exampleId", example.id)
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] file_path: The path to the file to upload.
        :param pulumi.Input[str] name: The name of the Dataset. Defaults to the file name.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] use_case_ids: The list of Use Case IDs to add the Dataset to.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DatasetFromFileArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Data set from file

        ## Example Usage

        ```python
        import pulumi
        import pulumi_datarobot as datarobot

        example = datarobot.DatasetFromFile("example",
            file_path="[Path to file to upload]",
            use_case_ids=[datarobot_use_case["example"]["id"]])
        pulumi.export("exampleId", example.id)
        ```

        :param str resource_name: The name of the resource.
        :param DatasetFromFileArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DatasetFromFileArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 file_path: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 use_case_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DatasetFromFileArgs.__new__(DatasetFromFileArgs)

            if file_path is None and not opts.urn:
                raise TypeError("Missing required property 'file_path'")
            __props__.__dict__["file_path"] = file_path
            __props__.__dict__["name"] = name
            __props__.__dict__["use_case_ids"] = use_case_ids
            __props__.__dict__["file_hash"] = None
        super(DatasetFromFile, __self__).__init__(
            'datarobot:index/datasetFromFile:DatasetFromFile',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            file_hash: Optional[pulumi.Input[str]] = None,
            file_path: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            use_case_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None) -> 'DatasetFromFile':
        """
        Get an existing DatasetFromFile resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] file_hash: The hash of the file contents.
        :param pulumi.Input[str] file_path: The path to the file to upload.
        :param pulumi.Input[str] name: The name of the Dataset. Defaults to the file name.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] use_case_ids: The list of Use Case IDs to add the Dataset to.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _DatasetFromFileState.__new__(_DatasetFromFileState)

        __props__.__dict__["file_hash"] = file_hash
        __props__.__dict__["file_path"] = file_path
        __props__.__dict__["name"] = name
        __props__.__dict__["use_case_ids"] = use_case_ids
        return DatasetFromFile(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="fileHash")
    def file_hash(self) -> pulumi.Output[str]:
        """
        The hash of the file contents.
        """
        return pulumi.get(self, "file_hash")

    @property
    @pulumi.getter(name="filePath")
    def file_path(self) -> pulumi.Output[str]:
        """
        The path to the file to upload.
        """
        return pulumi.get(self, "file_path")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the Dataset. Defaults to the file name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="useCaseIds")
    def use_case_ids(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        The list of Use Case IDs to add the Dataset to.
        """
        return pulumi.get(self, "use_case_ids")

