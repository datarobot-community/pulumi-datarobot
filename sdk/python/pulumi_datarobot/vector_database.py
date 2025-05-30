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

__all__ = ['VectorDatabaseArgs', 'VectorDatabase']

@pulumi.input_type
class VectorDatabaseArgs:
    def __init__(__self__, *,
                 dataset_id: pulumi.Input[builtins.str],
                 use_case_id: pulumi.Input[builtins.str],
                 chunking_parameters: Optional[pulumi.Input['VectorDatabaseChunkingParametersArgs']] = None,
                 name: Optional[pulumi.Input[builtins.str]] = None):
        """
        The set of arguments for constructing a VectorDatabase resource.
        :param pulumi.Input[builtins.str] dataset_id: The id of the Vector Database.
        :param pulumi.Input[builtins.str] use_case_id: The id of the Use Case.
        :param pulumi.Input['VectorDatabaseChunkingParametersArgs'] chunking_parameters: The chunking parameters for the Model.
        :param pulumi.Input[builtins.str] name: The name of the VectorDatabase.
        """
        pulumi.set(__self__, "dataset_id", dataset_id)
        pulumi.set(__self__, "use_case_id", use_case_id)
        if chunking_parameters is not None:
            pulumi.set(__self__, "chunking_parameters", chunking_parameters)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="datasetId")
    def dataset_id(self) -> pulumi.Input[builtins.str]:
        """
        The id of the Vector Database.
        """
        return pulumi.get(self, "dataset_id")

    @dataset_id.setter
    def dataset_id(self, value: pulumi.Input[builtins.str]):
        pulumi.set(self, "dataset_id", value)

    @property
    @pulumi.getter(name="useCaseId")
    def use_case_id(self) -> pulumi.Input[builtins.str]:
        """
        The id of the Use Case.
        """
        return pulumi.get(self, "use_case_id")

    @use_case_id.setter
    def use_case_id(self, value: pulumi.Input[builtins.str]):
        pulumi.set(self, "use_case_id", value)

    @property
    @pulumi.getter(name="chunkingParameters")
    def chunking_parameters(self) -> Optional[pulumi.Input['VectorDatabaseChunkingParametersArgs']]:
        """
        The chunking parameters for the Model.
        """
        return pulumi.get(self, "chunking_parameters")

    @chunking_parameters.setter
    def chunking_parameters(self, value: Optional[pulumi.Input['VectorDatabaseChunkingParametersArgs']]):
        pulumi.set(self, "chunking_parameters", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The name of the VectorDatabase.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _VectorDatabaseState:
    def __init__(__self__, *,
                 chunking_parameters: Optional[pulumi.Input['VectorDatabaseChunkingParametersArgs']] = None,
                 dataset_id: Optional[pulumi.Input[builtins.str]] = None,
                 name: Optional[pulumi.Input[builtins.str]] = None,
                 use_case_id: Optional[pulumi.Input[builtins.str]] = None,
                 version: Optional[pulumi.Input[builtins.int]] = None):
        """
        Input properties used for looking up and filtering VectorDatabase resources.
        :param pulumi.Input['VectorDatabaseChunkingParametersArgs'] chunking_parameters: The chunking parameters for the Model.
        :param pulumi.Input[builtins.str] dataset_id: The id of the Vector Database.
        :param pulumi.Input[builtins.str] name: The name of the VectorDatabase.
        :param pulumi.Input[builtins.str] use_case_id: The id of the Use Case.
        :param pulumi.Input[builtins.int] version: The version of the VectorDatabase.
        """
        if chunking_parameters is not None:
            pulumi.set(__self__, "chunking_parameters", chunking_parameters)
        if dataset_id is not None:
            pulumi.set(__self__, "dataset_id", dataset_id)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if use_case_id is not None:
            pulumi.set(__self__, "use_case_id", use_case_id)
        if version is not None:
            pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter(name="chunkingParameters")
    def chunking_parameters(self) -> Optional[pulumi.Input['VectorDatabaseChunkingParametersArgs']]:
        """
        The chunking parameters for the Model.
        """
        return pulumi.get(self, "chunking_parameters")

    @chunking_parameters.setter
    def chunking_parameters(self, value: Optional[pulumi.Input['VectorDatabaseChunkingParametersArgs']]):
        pulumi.set(self, "chunking_parameters", value)

    @property
    @pulumi.getter(name="datasetId")
    def dataset_id(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The id of the Vector Database.
        """
        return pulumi.get(self, "dataset_id")

    @dataset_id.setter
    def dataset_id(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "dataset_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The name of the VectorDatabase.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="useCaseId")
    def use_case_id(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The id of the Use Case.
        """
        return pulumi.get(self, "use_case_id")

    @use_case_id.setter
    def use_case_id(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "use_case_id", value)

    @property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[builtins.int]]:
        """
        The version of the VectorDatabase.
        """
        return pulumi.get(self, "version")

    @version.setter
    def version(self, value: Optional[pulumi.Input[builtins.int]]):
        pulumi.set(self, "version", value)


@pulumi.type_token("datarobot:index/vectorDatabase:VectorDatabase")
class VectorDatabase(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 chunking_parameters: Optional[pulumi.Input[Union['VectorDatabaseChunkingParametersArgs', 'VectorDatabaseChunkingParametersArgsDict']]] = None,
                 dataset_id: Optional[pulumi.Input[builtins.str]] = None,
                 name: Optional[pulumi.Input[builtins.str]] = None,
                 use_case_id: Optional[pulumi.Input[builtins.str]] = None,
                 __props__=None):
        """
        Vector database

        ## Example Usage

        ```python
        import pulumi
        import pulumi_datarobot as datarobot

        example_use_case = datarobot.UseCase("exampleUseCase", description="Description for the example use case")
        example_dataset_from_file = datarobot.DatasetFromFile("exampleDatasetFromFile",
            file_path="[Path to file to upload]",
            use_case_ids=[example_use_case.id])
        example_vector_database = datarobot.VectorDatabase("exampleVectorDatabase",
            use_case_id=example_use_case.id,
            dataset_id=example_dataset_from_file.id)
        # Optional
        # chunking_parameters = {
        #   chunk_overlap_percentage = 0
        #   chunk_size               = 512
        #   chunking_method          = "recursive"
        #   embedding_model          = "jinaai/jina-embedding-t-en-v1"
        #   separators               = ["\\n", " "]
        # }
        pulumi.export("exampleId", example_vector_database.id)
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union['VectorDatabaseChunkingParametersArgs', 'VectorDatabaseChunkingParametersArgsDict']] chunking_parameters: The chunking parameters for the Model.
        :param pulumi.Input[builtins.str] dataset_id: The id of the Vector Database.
        :param pulumi.Input[builtins.str] name: The name of the VectorDatabase.
        :param pulumi.Input[builtins.str] use_case_id: The id of the Use Case.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: VectorDatabaseArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Vector database

        ## Example Usage

        ```python
        import pulumi
        import pulumi_datarobot as datarobot

        example_use_case = datarobot.UseCase("exampleUseCase", description="Description for the example use case")
        example_dataset_from_file = datarobot.DatasetFromFile("exampleDatasetFromFile",
            file_path="[Path to file to upload]",
            use_case_ids=[example_use_case.id])
        example_vector_database = datarobot.VectorDatabase("exampleVectorDatabase",
            use_case_id=example_use_case.id,
            dataset_id=example_dataset_from_file.id)
        # Optional
        # chunking_parameters = {
        #   chunk_overlap_percentage = 0
        #   chunk_size               = 512
        #   chunking_method          = "recursive"
        #   embedding_model          = "jinaai/jina-embedding-t-en-v1"
        #   separators               = ["\\n", " "]
        # }
        pulumi.export("exampleId", example_vector_database.id)
        ```

        :param str resource_name: The name of the resource.
        :param VectorDatabaseArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(VectorDatabaseArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 chunking_parameters: Optional[pulumi.Input[Union['VectorDatabaseChunkingParametersArgs', 'VectorDatabaseChunkingParametersArgsDict']]] = None,
                 dataset_id: Optional[pulumi.Input[builtins.str]] = None,
                 name: Optional[pulumi.Input[builtins.str]] = None,
                 use_case_id: Optional[pulumi.Input[builtins.str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = VectorDatabaseArgs.__new__(VectorDatabaseArgs)

            __props__.__dict__["chunking_parameters"] = chunking_parameters
            if dataset_id is None and not opts.urn:
                raise TypeError("Missing required property 'dataset_id'")
            __props__.__dict__["dataset_id"] = dataset_id
            __props__.__dict__["name"] = name
            if use_case_id is None and not opts.urn:
                raise TypeError("Missing required property 'use_case_id'")
            __props__.__dict__["use_case_id"] = use_case_id
            __props__.__dict__["version"] = None
        super(VectorDatabase, __self__).__init__(
            'datarobot:index/vectorDatabase:VectorDatabase',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            chunking_parameters: Optional[pulumi.Input[Union['VectorDatabaseChunkingParametersArgs', 'VectorDatabaseChunkingParametersArgsDict']]] = None,
            dataset_id: Optional[pulumi.Input[builtins.str]] = None,
            name: Optional[pulumi.Input[builtins.str]] = None,
            use_case_id: Optional[pulumi.Input[builtins.str]] = None,
            version: Optional[pulumi.Input[builtins.int]] = None) -> 'VectorDatabase':
        """
        Get an existing VectorDatabase resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union['VectorDatabaseChunkingParametersArgs', 'VectorDatabaseChunkingParametersArgsDict']] chunking_parameters: The chunking parameters for the Model.
        :param pulumi.Input[builtins.str] dataset_id: The id of the Vector Database.
        :param pulumi.Input[builtins.str] name: The name of the VectorDatabase.
        :param pulumi.Input[builtins.str] use_case_id: The id of the Use Case.
        :param pulumi.Input[builtins.int] version: The version of the VectorDatabase.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _VectorDatabaseState.__new__(_VectorDatabaseState)

        __props__.__dict__["chunking_parameters"] = chunking_parameters
        __props__.__dict__["dataset_id"] = dataset_id
        __props__.__dict__["name"] = name
        __props__.__dict__["use_case_id"] = use_case_id
        __props__.__dict__["version"] = version
        return VectorDatabase(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="chunkingParameters")
    def chunking_parameters(self) -> pulumi.Output['outputs.VectorDatabaseChunkingParameters']:
        """
        The chunking parameters for the Model.
        """
        return pulumi.get(self, "chunking_parameters")

    @property
    @pulumi.getter(name="datasetId")
    def dataset_id(self) -> pulumi.Output[builtins.str]:
        """
        The id of the Vector Database.
        """
        return pulumi.get(self, "dataset_id")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[builtins.str]:
        """
        The name of the VectorDatabase.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="useCaseId")
    def use_case_id(self) -> pulumi.Output[builtins.str]:
        """
        The id of the Use Case.
        """
        return pulumi.get(self, "use_case_id")

    @property
    @pulumi.getter
    def version(self) -> pulumi.Output[builtins.int]:
        """
        The version of the VectorDatabase.
        """
        return pulumi.get(self, "version")

