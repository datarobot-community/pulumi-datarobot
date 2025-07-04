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

__all__ = ['CustomJobArgs', 'CustomJob']

@pulumi.input_type
class CustomJobArgs:
    def __init__(__self__, *,
                 description: Optional[pulumi.Input[builtins.str]] = None,
                 egress_network_policy: Optional[pulumi.Input[builtins.str]] = None,
                 environment_id: Optional[pulumi.Input[builtins.str]] = None,
                 environment_version_id: Optional[pulumi.Input[builtins.str]] = None,
                 files: Optional[Any] = None,
                 folder_path: Optional[pulumi.Input[builtins.str]] = None,
                 job_type: Optional[pulumi.Input[builtins.str]] = None,
                 name: Optional[pulumi.Input[builtins.str]] = None,
                 resource_bundle_id: Optional[pulumi.Input[builtins.str]] = None,
                 runtime_parameter_values: Optional[pulumi.Input[Sequence[pulumi.Input['CustomJobRuntimeParameterValueArgs']]]] = None,
                 schedule: Optional[pulumi.Input['CustomJobScheduleArgs']] = None,
                 schedule_id: Optional[pulumi.Input[builtins.str]] = None):
        """
        The set of arguments for constructing a CustomJob resource.
        :param pulumi.Input[builtins.str] description: The description of the Custom Job.
        :param pulumi.Input[builtins.str] egress_network_policy: The egress network policy for the Job.
        :param pulumi.Input[builtins.str] environment_id: The ID of the environment to use with the Job.
        :param pulumi.Input[builtins.str] environment_version_id: The ID of the environment version to use with the Job.
        :param Any files: The list of tuples, where values in each tuple are the local filesystem path and the path the file should be placed in the Job. If list is of strings, then basenames will be used for tuples.
        :param pulumi.Input[builtins.str] folder_path: The path to a folder containing files to be uploaded. Each file in the folder is uploaded under path relative to a folder path.
        :param pulumi.Input[builtins.str] job_type: The type of the Custom Job.
        :param pulumi.Input[builtins.str] name: The name of the Custom Job.
        :param pulumi.Input[builtins.str] resource_bundle_id: A single identifier that represents a bundle of resources: Memory, CPU, GPU, etc.
        :param pulumi.Input[Sequence[pulumi.Input['CustomJobRuntimeParameterValueArgs']]] runtime_parameter_values: Additional parameters to be injected into a Job at runtime.
        :param pulumi.Input['CustomJobScheduleArgs'] schedule: The schedule configuration for the custom job.
        :param pulumi.Input[builtins.str] schedule_id: The ID of the schedule associated with the custom job.
        """
        if description is not None:
            pulumi.set(__self__, "description", description)
        if egress_network_policy is not None:
            pulumi.set(__self__, "egress_network_policy", egress_network_policy)
        if environment_id is not None:
            pulumi.set(__self__, "environment_id", environment_id)
        if environment_version_id is not None:
            pulumi.set(__self__, "environment_version_id", environment_version_id)
        if files is not None:
            pulumi.set(__self__, "files", files)
        if folder_path is not None:
            pulumi.set(__self__, "folder_path", folder_path)
        if job_type is not None:
            pulumi.set(__self__, "job_type", job_type)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if resource_bundle_id is not None:
            pulumi.set(__self__, "resource_bundle_id", resource_bundle_id)
        if runtime_parameter_values is not None:
            pulumi.set(__self__, "runtime_parameter_values", runtime_parameter_values)
        if schedule is not None:
            pulumi.set(__self__, "schedule", schedule)
        if schedule_id is not None:
            pulumi.set(__self__, "schedule_id", schedule_id)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The description of the Custom Job.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="egressNetworkPolicy")
    def egress_network_policy(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The egress network policy for the Job.
        """
        return pulumi.get(self, "egress_network_policy")

    @egress_network_policy.setter
    def egress_network_policy(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "egress_network_policy", value)

    @property
    @pulumi.getter(name="environmentId")
    def environment_id(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The ID of the environment to use with the Job.
        """
        return pulumi.get(self, "environment_id")

    @environment_id.setter
    def environment_id(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "environment_id", value)

    @property
    @pulumi.getter(name="environmentVersionId")
    def environment_version_id(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The ID of the environment version to use with the Job.
        """
        return pulumi.get(self, "environment_version_id")

    @environment_version_id.setter
    def environment_version_id(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "environment_version_id", value)

    @property
    @pulumi.getter
    def files(self) -> Optional[Any]:
        """
        The list of tuples, where values in each tuple are the local filesystem path and the path the file should be placed in the Job. If list is of strings, then basenames will be used for tuples.
        """
        return pulumi.get(self, "files")

    @files.setter
    def files(self, value: Optional[Any]):
        pulumi.set(self, "files", value)

    @property
    @pulumi.getter(name="folderPath")
    def folder_path(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The path to a folder containing files to be uploaded. Each file in the folder is uploaded under path relative to a folder path.
        """
        return pulumi.get(self, "folder_path")

    @folder_path.setter
    def folder_path(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "folder_path", value)

    @property
    @pulumi.getter(name="jobType")
    def job_type(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The type of the Custom Job.
        """
        return pulumi.get(self, "job_type")

    @job_type.setter
    def job_type(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "job_type", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The name of the Custom Job.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="resourceBundleId")
    def resource_bundle_id(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        A single identifier that represents a bundle of resources: Memory, CPU, GPU, etc.
        """
        return pulumi.get(self, "resource_bundle_id")

    @resource_bundle_id.setter
    def resource_bundle_id(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "resource_bundle_id", value)

    @property
    @pulumi.getter(name="runtimeParameterValues")
    def runtime_parameter_values(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['CustomJobRuntimeParameterValueArgs']]]]:
        """
        Additional parameters to be injected into a Job at runtime.
        """
        return pulumi.get(self, "runtime_parameter_values")

    @runtime_parameter_values.setter
    def runtime_parameter_values(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['CustomJobRuntimeParameterValueArgs']]]]):
        pulumi.set(self, "runtime_parameter_values", value)

    @property
    @pulumi.getter
    def schedule(self) -> Optional[pulumi.Input['CustomJobScheduleArgs']]:
        """
        The schedule configuration for the custom job.
        """
        return pulumi.get(self, "schedule")

    @schedule.setter
    def schedule(self, value: Optional[pulumi.Input['CustomJobScheduleArgs']]):
        pulumi.set(self, "schedule", value)

    @property
    @pulumi.getter(name="scheduleId")
    def schedule_id(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The ID of the schedule associated with the custom job.
        """
        return pulumi.get(self, "schedule_id")

    @schedule_id.setter
    def schedule_id(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "schedule_id", value)


@pulumi.input_type
class _CustomJobState:
    def __init__(__self__, *,
                 description: Optional[pulumi.Input[builtins.str]] = None,
                 egress_network_policy: Optional[pulumi.Input[builtins.str]] = None,
                 environment_id: Optional[pulumi.Input[builtins.str]] = None,
                 environment_version_id: Optional[pulumi.Input[builtins.str]] = None,
                 files: Optional[Any] = None,
                 files_hashes: Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]] = None,
                 folder_path: Optional[pulumi.Input[builtins.str]] = None,
                 folder_path_hash: Optional[pulumi.Input[builtins.str]] = None,
                 job_type: Optional[pulumi.Input[builtins.str]] = None,
                 name: Optional[pulumi.Input[builtins.str]] = None,
                 resource_bundle_id: Optional[pulumi.Input[builtins.str]] = None,
                 runtime_parameter_values: Optional[pulumi.Input[Sequence[pulumi.Input['CustomJobRuntimeParameterValueArgs']]]] = None,
                 schedule: Optional[pulumi.Input['CustomJobScheduleArgs']] = None,
                 schedule_id: Optional[pulumi.Input[builtins.str]] = None):
        """
        Input properties used for looking up and filtering CustomJob resources.
        :param pulumi.Input[builtins.str] description: The description of the Custom Job.
        :param pulumi.Input[builtins.str] egress_network_policy: The egress network policy for the Job.
        :param pulumi.Input[builtins.str] environment_id: The ID of the environment to use with the Job.
        :param pulumi.Input[builtins.str] environment_version_id: The ID of the environment version to use with the Job.
        :param Any files: The list of tuples, where values in each tuple are the local filesystem path and the path the file should be placed in the Job. If list is of strings, then basenames will be used for tuples.
        :param pulumi.Input[Sequence[pulumi.Input[builtins.str]]] files_hashes: The hash of file contents for each file in files.
        :param pulumi.Input[builtins.str] folder_path: The path to a folder containing files to be uploaded. Each file in the folder is uploaded under path relative to a folder path.
        :param pulumi.Input[builtins.str] folder_path_hash: The hash of the folder path contents.
        :param pulumi.Input[builtins.str] job_type: The type of the Custom Job.
        :param pulumi.Input[builtins.str] name: The name of the Custom Job.
        :param pulumi.Input[builtins.str] resource_bundle_id: A single identifier that represents a bundle of resources: Memory, CPU, GPU, etc.
        :param pulumi.Input[Sequence[pulumi.Input['CustomJobRuntimeParameterValueArgs']]] runtime_parameter_values: Additional parameters to be injected into a Job at runtime.
        :param pulumi.Input['CustomJobScheduleArgs'] schedule: The schedule configuration for the custom job.
        :param pulumi.Input[builtins.str] schedule_id: The ID of the schedule associated with the custom job.
        """
        if description is not None:
            pulumi.set(__self__, "description", description)
        if egress_network_policy is not None:
            pulumi.set(__self__, "egress_network_policy", egress_network_policy)
        if environment_id is not None:
            pulumi.set(__self__, "environment_id", environment_id)
        if environment_version_id is not None:
            pulumi.set(__self__, "environment_version_id", environment_version_id)
        if files is not None:
            pulumi.set(__self__, "files", files)
        if files_hashes is not None:
            pulumi.set(__self__, "files_hashes", files_hashes)
        if folder_path is not None:
            pulumi.set(__self__, "folder_path", folder_path)
        if folder_path_hash is not None:
            pulumi.set(__self__, "folder_path_hash", folder_path_hash)
        if job_type is not None:
            pulumi.set(__self__, "job_type", job_type)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if resource_bundle_id is not None:
            pulumi.set(__self__, "resource_bundle_id", resource_bundle_id)
        if runtime_parameter_values is not None:
            pulumi.set(__self__, "runtime_parameter_values", runtime_parameter_values)
        if schedule is not None:
            pulumi.set(__self__, "schedule", schedule)
        if schedule_id is not None:
            pulumi.set(__self__, "schedule_id", schedule_id)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The description of the Custom Job.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="egressNetworkPolicy")
    def egress_network_policy(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The egress network policy for the Job.
        """
        return pulumi.get(self, "egress_network_policy")

    @egress_network_policy.setter
    def egress_network_policy(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "egress_network_policy", value)

    @property
    @pulumi.getter(name="environmentId")
    def environment_id(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The ID of the environment to use with the Job.
        """
        return pulumi.get(self, "environment_id")

    @environment_id.setter
    def environment_id(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "environment_id", value)

    @property
    @pulumi.getter(name="environmentVersionId")
    def environment_version_id(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The ID of the environment version to use with the Job.
        """
        return pulumi.get(self, "environment_version_id")

    @environment_version_id.setter
    def environment_version_id(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "environment_version_id", value)

    @property
    @pulumi.getter
    def files(self) -> Optional[Any]:
        """
        The list of tuples, where values in each tuple are the local filesystem path and the path the file should be placed in the Job. If list is of strings, then basenames will be used for tuples.
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
        The path to a folder containing files to be uploaded. Each file in the folder is uploaded under path relative to a folder path.
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
    @pulumi.getter(name="jobType")
    def job_type(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The type of the Custom Job.
        """
        return pulumi.get(self, "job_type")

    @job_type.setter
    def job_type(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "job_type", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The name of the Custom Job.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="resourceBundleId")
    def resource_bundle_id(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        A single identifier that represents a bundle of resources: Memory, CPU, GPU, etc.
        """
        return pulumi.get(self, "resource_bundle_id")

    @resource_bundle_id.setter
    def resource_bundle_id(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "resource_bundle_id", value)

    @property
    @pulumi.getter(name="runtimeParameterValues")
    def runtime_parameter_values(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['CustomJobRuntimeParameterValueArgs']]]]:
        """
        Additional parameters to be injected into a Job at runtime.
        """
        return pulumi.get(self, "runtime_parameter_values")

    @runtime_parameter_values.setter
    def runtime_parameter_values(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['CustomJobRuntimeParameterValueArgs']]]]):
        pulumi.set(self, "runtime_parameter_values", value)

    @property
    @pulumi.getter
    def schedule(self) -> Optional[pulumi.Input['CustomJobScheduleArgs']]:
        """
        The schedule configuration for the custom job.
        """
        return pulumi.get(self, "schedule")

    @schedule.setter
    def schedule(self, value: Optional[pulumi.Input['CustomJobScheduleArgs']]):
        pulumi.set(self, "schedule", value)

    @property
    @pulumi.getter(name="scheduleId")
    def schedule_id(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The ID of the schedule associated with the custom job.
        """
        return pulumi.get(self, "schedule_id")

    @schedule_id.setter
    def schedule_id(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "schedule_id", value)


class CustomJob(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[builtins.str]] = None,
                 egress_network_policy: Optional[pulumi.Input[builtins.str]] = None,
                 environment_id: Optional[pulumi.Input[builtins.str]] = None,
                 environment_version_id: Optional[pulumi.Input[builtins.str]] = None,
                 files: Optional[Any] = None,
                 folder_path: Optional[pulumi.Input[builtins.str]] = None,
                 job_type: Optional[pulumi.Input[builtins.str]] = None,
                 name: Optional[pulumi.Input[builtins.str]] = None,
                 resource_bundle_id: Optional[pulumi.Input[builtins.str]] = None,
                 runtime_parameter_values: Optional[pulumi.Input[Sequence[pulumi.Input[Union['CustomJobRuntimeParameterValueArgs', 'CustomJobRuntimeParameterValueArgsDict']]]]] = None,
                 schedule: Optional[pulumi.Input[Union['CustomJobScheduleArgs', 'CustomJobScheduleArgsDict']]] = None,
                 schedule_id: Optional[pulumi.Input[builtins.str]] = None,
                 __props__=None):
        """
        Custom Job

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[builtins.str] description: The description of the Custom Job.
        :param pulumi.Input[builtins.str] egress_network_policy: The egress network policy for the Job.
        :param pulumi.Input[builtins.str] environment_id: The ID of the environment to use with the Job.
        :param pulumi.Input[builtins.str] environment_version_id: The ID of the environment version to use with the Job.
        :param Any files: The list of tuples, where values in each tuple are the local filesystem path and the path the file should be placed in the Job. If list is of strings, then basenames will be used for tuples.
        :param pulumi.Input[builtins.str] folder_path: The path to a folder containing files to be uploaded. Each file in the folder is uploaded under path relative to a folder path.
        :param pulumi.Input[builtins.str] job_type: The type of the Custom Job.
        :param pulumi.Input[builtins.str] name: The name of the Custom Job.
        :param pulumi.Input[builtins.str] resource_bundle_id: A single identifier that represents a bundle of resources: Memory, CPU, GPU, etc.
        :param pulumi.Input[Sequence[pulumi.Input[Union['CustomJobRuntimeParameterValueArgs', 'CustomJobRuntimeParameterValueArgsDict']]]] runtime_parameter_values: Additional parameters to be injected into a Job at runtime.
        :param pulumi.Input[Union['CustomJobScheduleArgs', 'CustomJobScheduleArgsDict']] schedule: The schedule configuration for the custom job.
        :param pulumi.Input[builtins.str] schedule_id: The ID of the schedule associated with the custom job.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[CustomJobArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Custom Job

        :param str resource_name: The name of the resource.
        :param CustomJobArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CustomJobArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[builtins.str]] = None,
                 egress_network_policy: Optional[pulumi.Input[builtins.str]] = None,
                 environment_id: Optional[pulumi.Input[builtins.str]] = None,
                 environment_version_id: Optional[pulumi.Input[builtins.str]] = None,
                 files: Optional[Any] = None,
                 folder_path: Optional[pulumi.Input[builtins.str]] = None,
                 job_type: Optional[pulumi.Input[builtins.str]] = None,
                 name: Optional[pulumi.Input[builtins.str]] = None,
                 resource_bundle_id: Optional[pulumi.Input[builtins.str]] = None,
                 runtime_parameter_values: Optional[pulumi.Input[Sequence[pulumi.Input[Union['CustomJobRuntimeParameterValueArgs', 'CustomJobRuntimeParameterValueArgsDict']]]]] = None,
                 schedule: Optional[pulumi.Input[Union['CustomJobScheduleArgs', 'CustomJobScheduleArgsDict']]] = None,
                 schedule_id: Optional[pulumi.Input[builtins.str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = CustomJobArgs.__new__(CustomJobArgs)

            __props__.__dict__["description"] = description
            __props__.__dict__["egress_network_policy"] = egress_network_policy
            __props__.__dict__["environment_id"] = environment_id
            __props__.__dict__["environment_version_id"] = environment_version_id
            __props__.__dict__["files"] = files
            __props__.__dict__["folder_path"] = folder_path
            __props__.__dict__["job_type"] = job_type
            __props__.__dict__["name"] = name
            __props__.__dict__["resource_bundle_id"] = resource_bundle_id
            __props__.__dict__["runtime_parameter_values"] = runtime_parameter_values
            __props__.__dict__["schedule"] = schedule
            __props__.__dict__["schedule_id"] = schedule_id
            __props__.__dict__["files_hashes"] = None
            __props__.__dict__["folder_path_hash"] = None
        super(CustomJob, __self__).__init__(
            'datarobot:index/customJob:CustomJob',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            description: Optional[pulumi.Input[builtins.str]] = None,
            egress_network_policy: Optional[pulumi.Input[builtins.str]] = None,
            environment_id: Optional[pulumi.Input[builtins.str]] = None,
            environment_version_id: Optional[pulumi.Input[builtins.str]] = None,
            files: Optional[Any] = None,
            files_hashes: Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]] = None,
            folder_path: Optional[pulumi.Input[builtins.str]] = None,
            folder_path_hash: Optional[pulumi.Input[builtins.str]] = None,
            job_type: Optional[pulumi.Input[builtins.str]] = None,
            name: Optional[pulumi.Input[builtins.str]] = None,
            resource_bundle_id: Optional[pulumi.Input[builtins.str]] = None,
            runtime_parameter_values: Optional[pulumi.Input[Sequence[pulumi.Input[Union['CustomJobRuntimeParameterValueArgs', 'CustomJobRuntimeParameterValueArgsDict']]]]] = None,
            schedule: Optional[pulumi.Input[Union['CustomJobScheduleArgs', 'CustomJobScheduleArgsDict']]] = None,
            schedule_id: Optional[pulumi.Input[builtins.str]] = None) -> 'CustomJob':
        """
        Get an existing CustomJob resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[builtins.str] description: The description of the Custom Job.
        :param pulumi.Input[builtins.str] egress_network_policy: The egress network policy for the Job.
        :param pulumi.Input[builtins.str] environment_id: The ID of the environment to use with the Job.
        :param pulumi.Input[builtins.str] environment_version_id: The ID of the environment version to use with the Job.
        :param Any files: The list of tuples, where values in each tuple are the local filesystem path and the path the file should be placed in the Job. If list is of strings, then basenames will be used for tuples.
        :param pulumi.Input[Sequence[pulumi.Input[builtins.str]]] files_hashes: The hash of file contents for each file in files.
        :param pulumi.Input[builtins.str] folder_path: The path to a folder containing files to be uploaded. Each file in the folder is uploaded under path relative to a folder path.
        :param pulumi.Input[builtins.str] folder_path_hash: The hash of the folder path contents.
        :param pulumi.Input[builtins.str] job_type: The type of the Custom Job.
        :param pulumi.Input[builtins.str] name: The name of the Custom Job.
        :param pulumi.Input[builtins.str] resource_bundle_id: A single identifier that represents a bundle of resources: Memory, CPU, GPU, etc.
        :param pulumi.Input[Sequence[pulumi.Input[Union['CustomJobRuntimeParameterValueArgs', 'CustomJobRuntimeParameterValueArgsDict']]]] runtime_parameter_values: Additional parameters to be injected into a Job at runtime.
        :param pulumi.Input[Union['CustomJobScheduleArgs', 'CustomJobScheduleArgsDict']] schedule: The schedule configuration for the custom job.
        :param pulumi.Input[builtins.str] schedule_id: The ID of the schedule associated with the custom job.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _CustomJobState.__new__(_CustomJobState)

        __props__.__dict__["description"] = description
        __props__.__dict__["egress_network_policy"] = egress_network_policy
        __props__.__dict__["environment_id"] = environment_id
        __props__.__dict__["environment_version_id"] = environment_version_id
        __props__.__dict__["files"] = files
        __props__.__dict__["files_hashes"] = files_hashes
        __props__.__dict__["folder_path"] = folder_path
        __props__.__dict__["folder_path_hash"] = folder_path_hash
        __props__.__dict__["job_type"] = job_type
        __props__.__dict__["name"] = name
        __props__.__dict__["resource_bundle_id"] = resource_bundle_id
        __props__.__dict__["runtime_parameter_values"] = runtime_parameter_values
        __props__.__dict__["schedule"] = schedule
        __props__.__dict__["schedule_id"] = schedule_id
        return CustomJob(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[builtins.str]]:
        """
        The description of the Custom Job.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="egressNetworkPolicy")
    def egress_network_policy(self) -> pulumi.Output[builtins.str]:
        """
        The egress network policy for the Job.
        """
        return pulumi.get(self, "egress_network_policy")

    @property
    @pulumi.getter(name="environmentId")
    def environment_id(self) -> pulumi.Output[builtins.str]:
        """
        The ID of the environment to use with the Job.
        """
        return pulumi.get(self, "environment_id")

    @property
    @pulumi.getter(name="environmentVersionId")
    def environment_version_id(self) -> pulumi.Output[builtins.str]:
        """
        The ID of the environment version to use with the Job.
        """
        return pulumi.get(self, "environment_version_id")

    @property
    @pulumi.getter
    def files(self) -> pulumi.Output[Optional[Any]]:
        """
        The list of tuples, where values in each tuple are the local filesystem path and the path the file should be placed in the Job. If list is of strings, then basenames will be used for tuples.
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
        The path to a folder containing files to be uploaded. Each file in the folder is uploaded under path relative to a folder path.
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
    @pulumi.getter(name="jobType")
    def job_type(self) -> pulumi.Output[builtins.str]:
        """
        The type of the Custom Job.
        """
        return pulumi.get(self, "job_type")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[builtins.str]:
        """
        The name of the Custom Job.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="resourceBundleId")
    def resource_bundle_id(self) -> pulumi.Output[Optional[builtins.str]]:
        """
        A single identifier that represents a bundle of resources: Memory, CPU, GPU, etc.
        """
        return pulumi.get(self, "resource_bundle_id")

    @property
    @pulumi.getter(name="runtimeParameterValues")
    def runtime_parameter_values(self) -> pulumi.Output[Sequence['outputs.CustomJobRuntimeParameterValue']]:
        """
        Additional parameters to be injected into a Job at runtime.
        """
        return pulumi.get(self, "runtime_parameter_values")

    @property
    @pulumi.getter
    def schedule(self) -> pulumi.Output[Optional['outputs.CustomJobSchedule']]:
        """
        The schedule configuration for the custom job.
        """
        return pulumi.get(self, "schedule")

    @property
    @pulumi.getter(name="scheduleId")
    def schedule_id(self) -> pulumi.Output[builtins.str]:
        """
        The ID of the schedule associated with the custom job.
        """
        return pulumi.get(self, "schedule_id")

