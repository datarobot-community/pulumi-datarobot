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

__all__ = ['ApplicationSourceFromTemplateArgs', 'ApplicationSourceFromTemplate']

@pulumi.input_type
class ApplicationSourceFromTemplateArgs:
    def __init__(__self__, *,
                 template_id: pulumi.Input[str],
                 base_environment_id: Optional[pulumi.Input[str]] = None,
                 base_environment_version_id: Optional[pulumi.Input[str]] = None,
                 files: Optional[Any] = None,
                 folder_path: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resources: Optional[pulumi.Input['ApplicationSourceFromTemplateResourcesArgs']] = None,
                 runtime_parameter_values: Optional[pulumi.Input[Sequence[pulumi.Input['ApplicationSourceFromTemplateRuntimeParameterValueArgs']]]] = None):
        """
        The set of arguments for constructing a ApplicationSourceFromTemplate resource.
        :param pulumi.Input[str] template_id: The ID of the template used to create the Application Source.
        :param pulumi.Input[str] base_environment_id: The ID of the base environment for the Application Source.
        :param pulumi.Input[str] base_environment_version_id: The ID of the base environment version for the Application Source.
        :param Any files: The list of tuples, where values in each tuple are the local filesystem path and the path the file should be placed in the Application Source. If list is of strings, then basenames will be used for tuples.
        :param pulumi.Input[str] folder_path: The path to a folder containing files to build the Application Source. Each file in the folder is uploaded under path relative to a folder path.
        :param pulumi.Input[str] name: The name of the Application Source.
        :param pulumi.Input['ApplicationSourceFromTemplateResourcesArgs'] resources: The resources for the Application Source.
        :param pulumi.Input[Sequence[pulumi.Input['ApplicationSourceFromTemplateRuntimeParameterValueArgs']]] runtime_parameter_values: The runtime parameter values for the Application Source.
        """
        pulumi.set(__self__, "template_id", template_id)
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
    @pulumi.getter(name="templateId")
    def template_id(self) -> pulumi.Input[str]:
        """
        The ID of the template used to create the Application Source.
        """
        return pulumi.get(self, "template_id")

    @template_id.setter
    def template_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "template_id", value)

    @property
    @pulumi.getter(name="baseEnvironmentId")
    def base_environment_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the base environment for the Application Source.
        """
        return pulumi.get(self, "base_environment_id")

    @base_environment_id.setter
    def base_environment_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "base_environment_id", value)

    @property
    @pulumi.getter(name="baseEnvironmentVersionId")
    def base_environment_version_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the base environment version for the Application Source.
        """
        return pulumi.get(self, "base_environment_version_id")

    @base_environment_version_id.setter
    def base_environment_version_id(self, value: Optional[pulumi.Input[str]]):
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
    def folder_path(self) -> Optional[pulumi.Input[str]]:
        """
        The path to a folder containing files to build the Application Source. Each file in the folder is uploaded under path relative to a folder path.
        """
        return pulumi.get(self, "folder_path")

    @folder_path.setter
    def folder_path(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "folder_path", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Application Source.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def resources(self) -> Optional[pulumi.Input['ApplicationSourceFromTemplateResourcesArgs']]:
        """
        The resources for the Application Source.
        """
        return pulumi.get(self, "resources")

    @resources.setter
    def resources(self, value: Optional[pulumi.Input['ApplicationSourceFromTemplateResourcesArgs']]):
        pulumi.set(self, "resources", value)

    @property
    @pulumi.getter(name="runtimeParameterValues")
    def runtime_parameter_values(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ApplicationSourceFromTemplateRuntimeParameterValueArgs']]]]:
        """
        The runtime parameter values for the Application Source.
        """
        return pulumi.get(self, "runtime_parameter_values")

    @runtime_parameter_values.setter
    def runtime_parameter_values(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ApplicationSourceFromTemplateRuntimeParameterValueArgs']]]]):
        pulumi.set(self, "runtime_parameter_values", value)


@pulumi.input_type
class _ApplicationSourceFromTemplateState:
    def __init__(__self__, *,
                 base_environment_id: Optional[pulumi.Input[str]] = None,
                 base_environment_version_id: Optional[pulumi.Input[str]] = None,
                 files: Optional[Any] = None,
                 files_hashes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 folder_path: Optional[pulumi.Input[str]] = None,
                 folder_path_hash: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resources: Optional[pulumi.Input['ApplicationSourceFromTemplateResourcesArgs']] = None,
                 runtime_parameter_values: Optional[pulumi.Input[Sequence[pulumi.Input['ApplicationSourceFromTemplateRuntimeParameterValueArgs']]]] = None,
                 template_id: Optional[pulumi.Input[str]] = None,
                 version_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering ApplicationSourceFromTemplate resources.
        :param pulumi.Input[str] base_environment_id: The ID of the base environment for the Application Source.
        :param pulumi.Input[str] base_environment_version_id: The ID of the base environment version for the Application Source.
        :param Any files: The list of tuples, where values in each tuple are the local filesystem path and the path the file should be placed in the Application Source. If list is of strings, then basenames will be used for tuples.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] files_hashes: The hash of file contents for each file in files.
        :param pulumi.Input[str] folder_path: The path to a folder containing files to build the Application Source. Each file in the folder is uploaded under path relative to a folder path.
        :param pulumi.Input[str] folder_path_hash: The hash of the folder path contents.
        :param pulumi.Input[str] name: The name of the Application Source.
        :param pulumi.Input['ApplicationSourceFromTemplateResourcesArgs'] resources: The resources for the Application Source.
        :param pulumi.Input[Sequence[pulumi.Input['ApplicationSourceFromTemplateRuntimeParameterValueArgs']]] runtime_parameter_values: The runtime parameter values for the Application Source.
        :param pulumi.Input[str] template_id: The ID of the template used to create the Application Source.
        :param pulumi.Input[str] version_id: The version ID of the Application Source.
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
        if template_id is not None:
            pulumi.set(__self__, "template_id", template_id)
        if version_id is not None:
            pulumi.set(__self__, "version_id", version_id)

    @property
    @pulumi.getter(name="baseEnvironmentId")
    def base_environment_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the base environment for the Application Source.
        """
        return pulumi.get(self, "base_environment_id")

    @base_environment_id.setter
    def base_environment_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "base_environment_id", value)

    @property
    @pulumi.getter(name="baseEnvironmentVersionId")
    def base_environment_version_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the base environment version for the Application Source.
        """
        return pulumi.get(self, "base_environment_version_id")

    @base_environment_version_id.setter
    def base_environment_version_id(self, value: Optional[pulumi.Input[str]]):
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
    def files_hashes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The hash of file contents for each file in files.
        """
        return pulumi.get(self, "files_hashes")

    @files_hashes.setter
    def files_hashes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "files_hashes", value)

    @property
    @pulumi.getter(name="folderPath")
    def folder_path(self) -> Optional[pulumi.Input[str]]:
        """
        The path to a folder containing files to build the Application Source. Each file in the folder is uploaded under path relative to a folder path.
        """
        return pulumi.get(self, "folder_path")

    @folder_path.setter
    def folder_path(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "folder_path", value)

    @property
    @pulumi.getter(name="folderPathHash")
    def folder_path_hash(self) -> Optional[pulumi.Input[str]]:
        """
        The hash of the folder path contents.
        """
        return pulumi.get(self, "folder_path_hash")

    @folder_path_hash.setter
    def folder_path_hash(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "folder_path_hash", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Application Source.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def resources(self) -> Optional[pulumi.Input['ApplicationSourceFromTemplateResourcesArgs']]:
        """
        The resources for the Application Source.
        """
        return pulumi.get(self, "resources")

    @resources.setter
    def resources(self, value: Optional[pulumi.Input['ApplicationSourceFromTemplateResourcesArgs']]):
        pulumi.set(self, "resources", value)

    @property
    @pulumi.getter(name="runtimeParameterValues")
    def runtime_parameter_values(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ApplicationSourceFromTemplateRuntimeParameterValueArgs']]]]:
        """
        The runtime parameter values for the Application Source.
        """
        return pulumi.get(self, "runtime_parameter_values")

    @runtime_parameter_values.setter
    def runtime_parameter_values(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ApplicationSourceFromTemplateRuntimeParameterValueArgs']]]]):
        pulumi.set(self, "runtime_parameter_values", value)

    @property
    @pulumi.getter(name="templateId")
    def template_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the template used to create the Application Source.
        """
        return pulumi.get(self, "template_id")

    @template_id.setter
    def template_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "template_id", value)

    @property
    @pulumi.getter(name="versionId")
    def version_id(self) -> Optional[pulumi.Input[str]]:
        """
        The version ID of the Application Source.
        """
        return pulumi.get(self, "version_id")

    @version_id.setter
    def version_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "version_id", value)


class ApplicationSourceFromTemplate(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 base_environment_id: Optional[pulumi.Input[str]] = None,
                 base_environment_version_id: Optional[pulumi.Input[str]] = None,
                 files: Optional[Any] = None,
                 folder_path: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resources: Optional[pulumi.Input[Union['ApplicationSourceFromTemplateResourcesArgs', 'ApplicationSourceFromTemplateResourcesArgsDict']]] = None,
                 runtime_parameter_values: Optional[pulumi.Input[Sequence[pulumi.Input[Union['ApplicationSourceFromTemplateRuntimeParameterValueArgs', 'ApplicationSourceFromTemplateRuntimeParameterValueArgsDict']]]]] = None,
                 template_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Application Source

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] base_environment_id: The ID of the base environment for the Application Source.
        :param pulumi.Input[str] base_environment_version_id: The ID of the base environment version for the Application Source.
        :param Any files: The list of tuples, where values in each tuple are the local filesystem path and the path the file should be placed in the Application Source. If list is of strings, then basenames will be used for tuples.
        :param pulumi.Input[str] folder_path: The path to a folder containing files to build the Application Source. Each file in the folder is uploaded under path relative to a folder path.
        :param pulumi.Input[str] name: The name of the Application Source.
        :param pulumi.Input[Union['ApplicationSourceFromTemplateResourcesArgs', 'ApplicationSourceFromTemplateResourcesArgsDict']] resources: The resources for the Application Source.
        :param pulumi.Input[Sequence[pulumi.Input[Union['ApplicationSourceFromTemplateRuntimeParameterValueArgs', 'ApplicationSourceFromTemplateRuntimeParameterValueArgsDict']]]] runtime_parameter_values: The runtime parameter values for the Application Source.
        :param pulumi.Input[str] template_id: The ID of the template used to create the Application Source.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ApplicationSourceFromTemplateArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Application Source

        :param str resource_name: The name of the resource.
        :param ApplicationSourceFromTemplateArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ApplicationSourceFromTemplateArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 base_environment_id: Optional[pulumi.Input[str]] = None,
                 base_environment_version_id: Optional[pulumi.Input[str]] = None,
                 files: Optional[Any] = None,
                 folder_path: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resources: Optional[pulumi.Input[Union['ApplicationSourceFromTemplateResourcesArgs', 'ApplicationSourceFromTemplateResourcesArgsDict']]] = None,
                 runtime_parameter_values: Optional[pulumi.Input[Sequence[pulumi.Input[Union['ApplicationSourceFromTemplateRuntimeParameterValueArgs', 'ApplicationSourceFromTemplateRuntimeParameterValueArgsDict']]]]] = None,
                 template_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ApplicationSourceFromTemplateArgs.__new__(ApplicationSourceFromTemplateArgs)

            __props__.__dict__["base_environment_id"] = base_environment_id
            __props__.__dict__["base_environment_version_id"] = base_environment_version_id
            __props__.__dict__["files"] = files
            __props__.__dict__["folder_path"] = folder_path
            __props__.__dict__["name"] = name
            __props__.__dict__["resources"] = resources
            __props__.__dict__["runtime_parameter_values"] = runtime_parameter_values
            if template_id is None and not opts.urn:
                raise TypeError("Missing required property 'template_id'")
            __props__.__dict__["template_id"] = template_id
            __props__.__dict__["files_hashes"] = None
            __props__.__dict__["folder_path_hash"] = None
            __props__.__dict__["version_id"] = None
        super(ApplicationSourceFromTemplate, __self__).__init__(
            'datarobot:index/applicationSourceFromTemplate:ApplicationSourceFromTemplate',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            base_environment_id: Optional[pulumi.Input[str]] = None,
            base_environment_version_id: Optional[pulumi.Input[str]] = None,
            files: Optional[Any] = None,
            files_hashes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            folder_path: Optional[pulumi.Input[str]] = None,
            folder_path_hash: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            resources: Optional[pulumi.Input[Union['ApplicationSourceFromTemplateResourcesArgs', 'ApplicationSourceFromTemplateResourcesArgsDict']]] = None,
            runtime_parameter_values: Optional[pulumi.Input[Sequence[pulumi.Input[Union['ApplicationSourceFromTemplateRuntimeParameterValueArgs', 'ApplicationSourceFromTemplateRuntimeParameterValueArgsDict']]]]] = None,
            template_id: Optional[pulumi.Input[str]] = None,
            version_id: Optional[pulumi.Input[str]] = None) -> 'ApplicationSourceFromTemplate':
        """
        Get an existing ApplicationSourceFromTemplate resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] base_environment_id: The ID of the base environment for the Application Source.
        :param pulumi.Input[str] base_environment_version_id: The ID of the base environment version for the Application Source.
        :param Any files: The list of tuples, where values in each tuple are the local filesystem path and the path the file should be placed in the Application Source. If list is of strings, then basenames will be used for tuples.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] files_hashes: The hash of file contents for each file in files.
        :param pulumi.Input[str] folder_path: The path to a folder containing files to build the Application Source. Each file in the folder is uploaded under path relative to a folder path.
        :param pulumi.Input[str] folder_path_hash: The hash of the folder path contents.
        :param pulumi.Input[str] name: The name of the Application Source.
        :param pulumi.Input[Union['ApplicationSourceFromTemplateResourcesArgs', 'ApplicationSourceFromTemplateResourcesArgsDict']] resources: The resources for the Application Source.
        :param pulumi.Input[Sequence[pulumi.Input[Union['ApplicationSourceFromTemplateRuntimeParameterValueArgs', 'ApplicationSourceFromTemplateRuntimeParameterValueArgsDict']]]] runtime_parameter_values: The runtime parameter values for the Application Source.
        :param pulumi.Input[str] template_id: The ID of the template used to create the Application Source.
        :param pulumi.Input[str] version_id: The version ID of the Application Source.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ApplicationSourceFromTemplateState.__new__(_ApplicationSourceFromTemplateState)

        __props__.__dict__["base_environment_id"] = base_environment_id
        __props__.__dict__["base_environment_version_id"] = base_environment_version_id
        __props__.__dict__["files"] = files
        __props__.__dict__["files_hashes"] = files_hashes
        __props__.__dict__["folder_path"] = folder_path
        __props__.__dict__["folder_path_hash"] = folder_path_hash
        __props__.__dict__["name"] = name
        __props__.__dict__["resources"] = resources
        __props__.__dict__["runtime_parameter_values"] = runtime_parameter_values
        __props__.__dict__["template_id"] = template_id
        __props__.__dict__["version_id"] = version_id
        return ApplicationSourceFromTemplate(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="baseEnvironmentId")
    def base_environment_id(self) -> pulumi.Output[str]:
        """
        The ID of the base environment for the Application Source.
        """
        return pulumi.get(self, "base_environment_id")

    @property
    @pulumi.getter(name="baseEnvironmentVersionId")
    def base_environment_version_id(self) -> pulumi.Output[str]:
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
    def files_hashes(self) -> pulumi.Output[Sequence[str]]:
        """
        The hash of file contents for each file in files.
        """
        return pulumi.get(self, "files_hashes")

    @property
    @pulumi.getter(name="folderPath")
    def folder_path(self) -> pulumi.Output[Optional[str]]:
        """
        The path to a folder containing files to build the Application Source. Each file in the folder is uploaded under path relative to a folder path.
        """
        return pulumi.get(self, "folder_path")

    @property
    @pulumi.getter(name="folderPathHash")
    def folder_path_hash(self) -> pulumi.Output[str]:
        """
        The hash of the folder path contents.
        """
        return pulumi.get(self, "folder_path_hash")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the Application Source.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def resources(self) -> pulumi.Output[Optional['outputs.ApplicationSourceFromTemplateResources']]:
        """
        The resources for the Application Source.
        """
        return pulumi.get(self, "resources")

    @property
    @pulumi.getter(name="runtimeParameterValues")
    def runtime_parameter_values(self) -> pulumi.Output[Sequence['outputs.ApplicationSourceFromTemplateRuntimeParameterValue']]:
        """
        The runtime parameter values for the Application Source.
        """
        return pulumi.get(self, "runtime_parameter_values")

    @property
    @pulumi.getter(name="templateId")
    def template_id(self) -> pulumi.Output[str]:
        """
        The ID of the template used to create the Application Source.
        """
        return pulumi.get(self, "template_id")

    @property
    @pulumi.getter(name="versionId")
    def version_id(self) -> pulumi.Output[str]:
        """
        The version ID of the Application Source.
        """
        return pulumi.get(self, "version_id")

