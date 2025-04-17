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

__all__ = ['ApplicationSourceArgs', 'ApplicationSource']

@pulumi.input_type
class ApplicationSourceArgs:
    def __init__(__self__, *,
                 base_environment_id: Optional[pulumi.Input[builtins.str]] = None,
                 base_environment_version_id: Optional[pulumi.Input[builtins.str]] = None,
                 files: Optional[Any] = None,
                 folder_path: Optional[pulumi.Input[builtins.str]] = None,
                 name: Optional[pulumi.Input[builtins.str]] = None,
                 resources: Optional[pulumi.Input['ApplicationSourceResourcesArgs']] = None,
                 runtime_parameter_values: Optional[pulumi.Input[Sequence[pulumi.Input['ApplicationSourceRuntimeParameterValueArgs']]]] = None):
        """
        The set of arguments for constructing a ApplicationSource resource.
        :param pulumi.Input[builtins.str] base_environment_id: The ID of the base environment for the Application Source.
        :param pulumi.Input[builtins.str] base_environment_version_id: The ID of the base environment version for the Application Source.
        :param Any files: The list of tuples, where values in each tuple are the local filesystem path and the path the file should be placed in the Application Source. If list is of strings, then basenames will be used for tuples.
        :param pulumi.Input[builtins.str] folder_path: The path to a folder containing files to build the Application Source. Each file in the folder is uploaded under path relative to a folder path.
        :param pulumi.Input[builtins.str] name: The name of the Application Source.
        :param pulumi.Input['ApplicationSourceResourcesArgs'] resources: The resources for the Application Source.
        :param pulumi.Input[Sequence[pulumi.Input['ApplicationSourceRuntimeParameterValueArgs']]] runtime_parameter_values: The runtime parameter values for the Application Source.
        """
        if base_environment_id is not None:
            pulumi.set(__self__, "base_environment_id", base_environment_id)
        if base_environment_version_id is not None:
            pulumi.set(__self__, "base_environment_version_id", base_environment_version_id)
        if files is not None:
            pulumi.set(__self__, "files", files)
        if folder_path is not None:
            pulumi.set(__self__, "folder_path", folder_path)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if resources is not None:
            pulumi.set(__self__, "resources", resources)
        if runtime_parameter_values is not None:
            pulumi.set(__self__, "runtime_parameter_values", runtime_parameter_values)

    @property
    @pulumi.getter(name="baseEnvironmentId")
    def base_environment_id(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The ID of the base environment for the Application Source.
        """
        return pulumi.get(self, "base_environment_id")

    @base_environment_id.setter
    def base_environment_id(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "base_environment_id", value)

    @property
    @pulumi.getter(name="baseEnvironmentVersionId")
    def base_environment_version_id(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The ID of the base environment version for the Application Source.
        """
        return pulumi.get(self, "base_environment_version_id")

    @base_environment_version_id.setter
    def base_environment_version_id(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "base_environment_version_id", value)

    @property
    @pulumi.getter
    def files(self) -> Optional[Any]:
        """
        The list of tuples, where values in each tuple are the local filesystem path and the path the file should be placed in the Application Source. If list is of strings, then basenames will be used for tuples.
        """
        return pulumi.get(self, "files")

    @files.setter
    def files(self, value: Optional[Any]):
        pulumi.set(self, "files", value)

    @property
    @pulumi.getter(name="folderPath")
    def folder_path(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The path to a folder containing files to build the Application Source. Each file in the folder is uploaded under path relative to a folder path.
        """
        return pulumi.get(self, "folder_path")

    @folder_path.setter
    def folder_path(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "folder_path", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The name of the Application Source.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def resources(self) -> Optional[pulumi.Input['ApplicationSourceResourcesArgs']]:
        """
        The resources for the Application Source.
        """
        return pulumi.get(self, "resources")

    @resources.setter
    def resources(self, value: Optional[pulumi.Input['ApplicationSourceResourcesArgs']]):
        pulumi.set(self, "resources", value)

    @property
    @pulumi.getter(name="runtimeParameterValues")
    def runtime_parameter_values(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ApplicationSourceRuntimeParameterValueArgs']]]]:
        """
        The runtime parameter values for the Application Source.
        """
        return pulumi.get(self, "runtime_parameter_values")

    @runtime_parameter_values.setter
    def runtime_parameter_values(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ApplicationSourceRuntimeParameterValueArgs']]]]):
        pulumi.set(self, "runtime_parameter_values", value)


@pulumi.input_type
class _ApplicationSourceState:
    def __init__(__self__, *,
                 base_environment_id: Optional[pulumi.Input[builtins.str]] = None,
                 base_environment_version_id: Optional[pulumi.Input[builtins.str]] = None,
                 files: Optional[Any] = None,
                 files_hashes: Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]] = None,
                 folder_path: Optional[pulumi.Input[builtins.str]] = None,
                 folder_path_hash: Optional[pulumi.Input[builtins.str]] = None,
                 name: Optional[pulumi.Input[builtins.str]] = None,
                 resources: Optional[pulumi.Input['ApplicationSourceResourcesArgs']] = None,
                 runtime_parameter_values: Optional[pulumi.Input[Sequence[pulumi.Input['ApplicationSourceRuntimeParameterValueArgs']]]] = None,
                 version_id: Optional[pulumi.Input[builtins.str]] = None):
        """
        Input properties used for looking up and filtering ApplicationSource resources.
        :param pulumi.Input[builtins.str] base_environment_id: The ID of the base environment for the Application Source.
        :param pulumi.Input[builtins.str] base_environment_version_id: The ID of the base environment version for the Application Source.
        :param Any files: The list of tuples, where values in each tuple are the local filesystem path and the path the file should be placed in the Application Source. If list is of strings, then basenames will be used for tuples.
        :param pulumi.Input[Sequence[pulumi.Input[builtins.str]]] files_hashes: The hash of file contents for each file in files.
        :param pulumi.Input[builtins.str] folder_path: The path to a folder containing files to build the Application Source. Each file in the folder is uploaded under path relative to a folder path.
        :param pulumi.Input[builtins.str] folder_path_hash: The hash of the folder path contents.
        :param pulumi.Input[builtins.str] name: The name of the Application Source.
        :param pulumi.Input['ApplicationSourceResourcesArgs'] resources: The resources for the Application Source.
        :param pulumi.Input[Sequence[pulumi.Input['ApplicationSourceRuntimeParameterValueArgs']]] runtime_parameter_values: The runtime parameter values for the Application Source.
        :param pulumi.Input[builtins.str] version_id: The version ID of the Application Source.
        """
        if base_environment_id is not None:
            pulumi.set(__self__, "base_environment_id", base_environment_id)
        if base_environment_version_id is not None:
            pulumi.set(__self__, "base_environment_version_id", base_environment_version_id)
        if files is not None:
            pulumi.set(__self__, "files", files)
        if files_hashes is not None:
            pulumi.set(__self__, "files_hashes", files_hashes)
        if folder_path is not None:
            pulumi.set(__self__, "folder_path", folder_path)
        if folder_path_hash is not None:
            pulumi.set(__self__, "folder_path_hash", folder_path_hash)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if resources is not None:
            pulumi.set(__self__, "resources", resources)
        if runtime_parameter_values is not None:
            pulumi.set(__self__, "runtime_parameter_values", runtime_parameter_values)
        if version_id is not None:
            pulumi.set(__self__, "version_id", version_id)

    @property
    @pulumi.getter(name="baseEnvironmentId")
    def base_environment_id(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The ID of the base environment for the Application Source.
        """
        return pulumi.get(self, "base_environment_id")

    @base_environment_id.setter
    def base_environment_id(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "base_environment_id", value)

    @property
    @pulumi.getter(name="baseEnvironmentVersionId")
    def base_environment_version_id(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The ID of the base environment version for the Application Source.
        """
        return pulumi.get(self, "base_environment_version_id")

    @base_environment_version_id.setter
    def base_environment_version_id(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "base_environment_version_id", value)

    @property
    @pulumi.getter
    def files(self) -> Optional[Any]:
        """
        The list of tuples, where values in each tuple are the local filesystem path and the path the file should be placed in the Application Source. If list is of strings, then basenames will be used for tuples.
        """
        return pulumi.get(self, "files")

    @files.setter
    def files(self, value: Optional[Any]):
        pulumi.set(self, "files", value)

    @property
    @pulumi.getter(name="filesHashes")
    def files_hashes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]]:
        """
        The hash of file contents for each file in files.
        """
        return pulumi.get(self, "files_hashes")

    @files_hashes.setter
    def files_hashes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]]):
        pulumi.set(self, "files_hashes", value)

    @property
    @pulumi.getter(name="folderPath")
    def folder_path(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The path to a folder containing files to build the Application Source. Each file in the folder is uploaded under path relative to a folder path.
        """
        return pulumi.get(self, "folder_path")

    @folder_path.setter
    def folder_path(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "folder_path", value)

    @property
    @pulumi.getter(name="folderPathHash")
    def folder_path_hash(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The hash of the folder path contents.
        """
        return pulumi.get(self, "folder_path_hash")

    @folder_path_hash.setter
    def folder_path_hash(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "folder_path_hash", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The name of the Application Source.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def resources(self) -> Optional[pulumi.Input['ApplicationSourceResourcesArgs']]:
        """
        The resources for the Application Source.
        """
        return pulumi.get(self, "resources")

    @resources.setter
    def resources(self, value: Optional[pulumi.Input['ApplicationSourceResourcesArgs']]):
        pulumi.set(self, "resources", value)

    @property
    @pulumi.getter(name="runtimeParameterValues")
    def runtime_parameter_values(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ApplicationSourceRuntimeParameterValueArgs']]]]:
        """
        The runtime parameter values for the Application Source.
        """
        return pulumi.get(self, "runtime_parameter_values")

    @runtime_parameter_values.setter
    def runtime_parameter_values(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ApplicationSourceRuntimeParameterValueArgs']]]]):
        pulumi.set(self, "runtime_parameter_values", value)

    @property
    @pulumi.getter(name="versionId")
    def version_id(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The version ID of the Application Source.
        """
        return pulumi.get(self, "version_id")

    @version_id.setter
    def version_id(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "version_id", value)


class ApplicationSource(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 base_environment_id: Optional[pulumi.Input[builtins.str]] = None,
                 base_environment_version_id: Optional[pulumi.Input[builtins.str]] = None,
                 files: Optional[Any] = None,
                 folder_path: Optional[pulumi.Input[builtins.str]] = None,
                 name: Optional[pulumi.Input[builtins.str]] = None,
                 resources: Optional[pulumi.Input[Union['ApplicationSourceResourcesArgs', 'ApplicationSourceResourcesArgsDict']]] = None,
                 runtime_parameter_values: Optional[pulumi.Input[Sequence[pulumi.Input[Union['ApplicationSourceRuntimeParameterValueArgs', 'ApplicationSourceRuntimeParameterValueArgsDict']]]]] = None,
                 __props__=None):
        """
        Application Source

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[builtins.str] base_environment_id: The ID of the base environment for the Application Source.
        :param pulumi.Input[builtins.str] base_environment_version_id: The ID of the base environment version for the Application Source.
        :param Any files: The list of tuples, where values in each tuple are the local filesystem path and the path the file should be placed in the Application Source. If list is of strings, then basenames will be used for tuples.
        :param pulumi.Input[builtins.str] folder_path: The path to a folder containing files to build the Application Source. Each file in the folder is uploaded under path relative to a folder path.
        :param pulumi.Input[builtins.str] name: The name of the Application Source.
        :param pulumi.Input[Union['ApplicationSourceResourcesArgs', 'ApplicationSourceResourcesArgsDict']] resources: The resources for the Application Source.
        :param pulumi.Input[Sequence[pulumi.Input[Union['ApplicationSourceRuntimeParameterValueArgs', 'ApplicationSourceRuntimeParameterValueArgsDict']]]] runtime_parameter_values: The runtime parameter values for the Application Source.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[ApplicationSourceArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Application Source

        :param str resource_name: The name of the resource.
        :param ApplicationSourceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ApplicationSourceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 base_environment_id: Optional[pulumi.Input[builtins.str]] = None,
                 base_environment_version_id: Optional[pulumi.Input[builtins.str]] = None,
                 files: Optional[Any] = None,
                 folder_path: Optional[pulumi.Input[builtins.str]] = None,
                 name: Optional[pulumi.Input[builtins.str]] = None,
                 resources: Optional[pulumi.Input[Union['ApplicationSourceResourcesArgs', 'ApplicationSourceResourcesArgsDict']]] = None,
                 runtime_parameter_values: Optional[pulumi.Input[Sequence[pulumi.Input[Union['ApplicationSourceRuntimeParameterValueArgs', 'ApplicationSourceRuntimeParameterValueArgsDict']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ApplicationSourceArgs.__new__(ApplicationSourceArgs)

            __props__.__dict__["base_environment_id"] = base_environment_id
            __props__.__dict__["base_environment_version_id"] = base_environment_version_id
            __props__.__dict__["files"] = files
            __props__.__dict__["folder_path"] = folder_path
            __props__.__dict__["name"] = name
            __props__.__dict__["resources"] = resources
            __props__.__dict__["runtime_parameter_values"] = runtime_parameter_values
            __props__.__dict__["files_hashes"] = None
            __props__.__dict__["folder_path_hash"] = None
            __props__.__dict__["version_id"] = None
        super(ApplicationSource, __self__).__init__(
            'datarobot:index/applicationSource:ApplicationSource',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            base_environment_id: Optional[pulumi.Input[builtins.str]] = None,
            base_environment_version_id: Optional[pulumi.Input[builtins.str]] = None,
            files: Optional[Any] = None,
            files_hashes: Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]] = None,
            folder_path: Optional[pulumi.Input[builtins.str]] = None,
            folder_path_hash: Optional[pulumi.Input[builtins.str]] = None,
            name: Optional[pulumi.Input[builtins.str]] = None,
            resources: Optional[pulumi.Input[Union['ApplicationSourceResourcesArgs', 'ApplicationSourceResourcesArgsDict']]] = None,
            runtime_parameter_values: Optional[pulumi.Input[Sequence[pulumi.Input[Union['ApplicationSourceRuntimeParameterValueArgs', 'ApplicationSourceRuntimeParameterValueArgsDict']]]]] = None,
            version_id: Optional[pulumi.Input[builtins.str]] = None) -> 'ApplicationSource':
        """
        Get an existing ApplicationSource resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[builtins.str] base_environment_id: The ID of the base environment for the Application Source.
        :param pulumi.Input[builtins.str] base_environment_version_id: The ID of the base environment version for the Application Source.
        :param Any files: The list of tuples, where values in each tuple are the local filesystem path and the path the file should be placed in the Application Source. If list is of strings, then basenames will be used for tuples.
        :param pulumi.Input[Sequence[pulumi.Input[builtins.str]]] files_hashes: The hash of file contents for each file in files.
        :param pulumi.Input[builtins.str] folder_path: The path to a folder containing files to build the Application Source. Each file in the folder is uploaded under path relative to a folder path.
        :param pulumi.Input[builtins.str] folder_path_hash: The hash of the folder path contents.
        :param pulumi.Input[builtins.str] name: The name of the Application Source.
        :param pulumi.Input[Union['ApplicationSourceResourcesArgs', 'ApplicationSourceResourcesArgsDict']] resources: The resources for the Application Source.
        :param pulumi.Input[Sequence[pulumi.Input[Union['ApplicationSourceRuntimeParameterValueArgs', 'ApplicationSourceRuntimeParameterValueArgsDict']]]] runtime_parameter_values: The runtime parameter values for the Application Source.
        :param pulumi.Input[builtins.str] version_id: The version ID of the Application Source.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ApplicationSourceState.__new__(_ApplicationSourceState)

        __props__.__dict__["base_environment_id"] = base_environment_id
        __props__.__dict__["base_environment_version_id"] = base_environment_version_id
        __props__.__dict__["files"] = files
        __props__.__dict__["files_hashes"] = files_hashes
        __props__.__dict__["folder_path"] = folder_path
        __props__.__dict__["folder_path_hash"] = folder_path_hash
        __props__.__dict__["name"] = name
        __props__.__dict__["resources"] = resources
        __props__.__dict__["runtime_parameter_values"] = runtime_parameter_values
        __props__.__dict__["version_id"] = version_id
        return ApplicationSource(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="baseEnvironmentId")
    def base_environment_id(self) -> pulumi.Output[builtins.str]:
        """
        The ID of the base environment for the Application Source.
        """
        return pulumi.get(self, "base_environment_id")

    @property
    @pulumi.getter(name="baseEnvironmentVersionId")
    def base_environment_version_id(self) -> pulumi.Output[builtins.str]:
        """
        The ID of the base environment version for the Application Source.
        """
        return pulumi.get(self, "base_environment_version_id")

    @property
    @pulumi.getter
    def files(self) -> pulumi.Output[Optional[Any]]:
        """
        The list of tuples, where values in each tuple are the local filesystem path and the path the file should be placed in the Application Source. If list is of strings, then basenames will be used for tuples.
        """
        return pulumi.get(self, "files")

    @property
    @pulumi.getter(name="filesHashes")
    def files_hashes(self) -> pulumi.Output[Sequence[builtins.str]]:
        """
        The hash of file contents for each file in files.
        """
        return pulumi.get(self, "files_hashes")

    @property
    @pulumi.getter(name="folderPath")
    def folder_path(self) -> pulumi.Output[Optional[builtins.str]]:
        """
        The path to a folder containing files to build the Application Source. Each file in the folder is uploaded under path relative to a folder path.
        """
        return pulumi.get(self, "folder_path")

    @property
    @pulumi.getter(name="folderPathHash")
    def folder_path_hash(self) -> pulumi.Output[builtins.str]:
        """
        The hash of the folder path contents.
        """
        return pulumi.get(self, "folder_path_hash")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[builtins.str]:
        """
        The name of the Application Source.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def resources(self) -> pulumi.Output[Optional['outputs.ApplicationSourceResources']]:
        """
        The resources for the Application Source.
        """
        return pulumi.get(self, "resources")

    @property
    @pulumi.getter(name="runtimeParameterValues")
    def runtime_parameter_values(self) -> pulumi.Output[Sequence['outputs.ApplicationSourceRuntimeParameterValue']]:
        """
        The runtime parameter values for the Application Source.
        """
        return pulumi.get(self, "runtime_parameter_values")

    @property
    @pulumi.getter(name="versionId")
    def version_id(self) -> pulumi.Output[builtins.str]:
        """
        The version ID of the Application Source.
        """
        return pulumi.get(self, "version_id")

