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

__all__ = ['ExecutionEnvironmentArgs', 'ExecutionEnvironment']

@pulumi.input_type
class ExecutionEnvironmentArgs:
    def __init__(__self__, *,
                 programming_language: pulumi.Input[builtins.str],
                 use_cases: pulumi.Input[Sequence[pulumi.Input[builtins.str]]],
                 description: Optional[pulumi.Input[builtins.str]] = None,
                 docker_context_path: Optional[pulumi.Input[builtins.str]] = None,
                 docker_image: Optional[pulumi.Input[builtins.str]] = None,
                 name: Optional[pulumi.Input[builtins.str]] = None,
                 version_description: Optional[pulumi.Input[builtins.str]] = None):
        """
        The set of arguments for constructing a ExecutionEnvironment resource.
        :param pulumi.Input[builtins.str] programming_language: The programming language of the Execution Environment.
        :param pulumi.Input[Sequence[pulumi.Input[builtins.str]]] use_cases: The list of Use Cases that the Execution Environment supports.
        :param pulumi.Input[builtins.str] description: The description of the Execution Environment.
        :param pulumi.Input[builtins.str] docker_context_path: The path to a docker context archive or folder
        :param pulumi.Input[builtins.str] docker_image: A prebuilt environment image saved as a tarball using the Docker save command.
        :param pulumi.Input[builtins.str] name: The name of the Execution Environment.
        :param pulumi.Input[builtins.str] version_description: The description of the Execution Environment version.
        """
        pulumi.set(__self__, "programming_language", programming_language)
        pulumi.set(__self__, "use_cases", use_cases)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if docker_context_path is not None:
            pulumi.set(__self__, "docker_context_path", docker_context_path)
        if docker_image is not None:
            pulumi.set(__self__, "docker_image", docker_image)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if version_description is not None:
            pulumi.set(__self__, "version_description", version_description)

    @property
    @pulumi.getter(name="programmingLanguage")
    def programming_language(self) -> pulumi.Input[builtins.str]:
        """
        The programming language of the Execution Environment.
        """
        return pulumi.get(self, "programming_language")

    @programming_language.setter
    def programming_language(self, value: pulumi.Input[builtins.str]):
        pulumi.set(self, "programming_language", value)

    @property
    @pulumi.getter(name="useCases")
    def use_cases(self) -> pulumi.Input[Sequence[pulumi.Input[builtins.str]]]:
        """
        The list of Use Cases that the Execution Environment supports.
        """
        return pulumi.get(self, "use_cases")

    @use_cases.setter
    def use_cases(self, value: pulumi.Input[Sequence[pulumi.Input[builtins.str]]]):
        pulumi.set(self, "use_cases", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The description of the Execution Environment.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="dockerContextPath")
    def docker_context_path(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The path to a docker context archive or folder
        """
        return pulumi.get(self, "docker_context_path")

    @docker_context_path.setter
    def docker_context_path(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "docker_context_path", value)

    @property
    @pulumi.getter(name="dockerImage")
    def docker_image(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        A prebuilt environment image saved as a tarball using the Docker save command.
        """
        return pulumi.get(self, "docker_image")

    @docker_image.setter
    def docker_image(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "docker_image", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The name of the Execution Environment.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="versionDescription")
    def version_description(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The description of the Execution Environment version.
        """
        return pulumi.get(self, "version_description")

    @version_description.setter
    def version_description(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "version_description", value)


@pulumi.input_type
class _ExecutionEnvironmentState:
    def __init__(__self__, *,
                 build_status: Optional[pulumi.Input[builtins.str]] = None,
                 description: Optional[pulumi.Input[builtins.str]] = None,
                 docker_context_hash: Optional[pulumi.Input[builtins.str]] = None,
                 docker_context_path: Optional[pulumi.Input[builtins.str]] = None,
                 docker_image: Optional[pulumi.Input[builtins.str]] = None,
                 docker_image_hash: Optional[pulumi.Input[builtins.str]] = None,
                 name: Optional[pulumi.Input[builtins.str]] = None,
                 programming_language: Optional[pulumi.Input[builtins.str]] = None,
                 use_cases: Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]] = None,
                 version_description: Optional[pulumi.Input[builtins.str]] = None,
                 version_id: Optional[pulumi.Input[builtins.str]] = None):
        """
        Input properties used for looking up and filtering ExecutionEnvironment resources.
        :param pulumi.Input[builtins.str] build_status: The status of the Execution Environment version build.
        :param pulumi.Input[builtins.str] description: The description of the Execution Environment.
        :param pulumi.Input[builtins.str] docker_context_hash: The hash of the docker context contents.
        :param pulumi.Input[builtins.str] docker_context_path: The path to a docker context archive or folder
        :param pulumi.Input[builtins.str] docker_image: A prebuilt environment image saved as a tarball using the Docker save command.
        :param pulumi.Input[builtins.str] docker_image_hash: The hash of the docker image file
        :param pulumi.Input[builtins.str] name: The name of the Execution Environment.
        :param pulumi.Input[builtins.str] programming_language: The programming language of the Execution Environment.
        :param pulumi.Input[Sequence[pulumi.Input[builtins.str]]] use_cases: The list of Use Cases that the Execution Environment supports.
        :param pulumi.Input[builtins.str] version_description: The description of the Execution Environment version.
        :param pulumi.Input[builtins.str] version_id: The ID of the Execution Environment Version.
        """
        if build_status is not None:
            pulumi.set(__self__, "build_status", build_status)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if docker_context_hash is not None:
            pulumi.set(__self__, "docker_context_hash", docker_context_hash)
        if docker_context_path is not None:
            pulumi.set(__self__, "docker_context_path", docker_context_path)
        if docker_image is not None:
            pulumi.set(__self__, "docker_image", docker_image)
        if docker_image_hash is not None:
            pulumi.set(__self__, "docker_image_hash", docker_image_hash)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if programming_language is not None:
            pulumi.set(__self__, "programming_language", programming_language)
        if use_cases is not None:
            pulumi.set(__self__, "use_cases", use_cases)
        if version_description is not None:
            pulumi.set(__self__, "version_description", version_description)
        if version_id is not None:
            pulumi.set(__self__, "version_id", version_id)

    @property
    @pulumi.getter(name="buildStatus")
    def build_status(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The status of the Execution Environment version build.
        """
        return pulumi.get(self, "build_status")

    @build_status.setter
    def build_status(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "build_status", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The description of the Execution Environment.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="dockerContextHash")
    def docker_context_hash(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The hash of the docker context contents.
        """
        return pulumi.get(self, "docker_context_hash")

    @docker_context_hash.setter
    def docker_context_hash(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "docker_context_hash", value)

    @property
    @pulumi.getter(name="dockerContextPath")
    def docker_context_path(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The path to a docker context archive or folder
        """
        return pulumi.get(self, "docker_context_path")

    @docker_context_path.setter
    def docker_context_path(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "docker_context_path", value)

    @property
    @pulumi.getter(name="dockerImage")
    def docker_image(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        A prebuilt environment image saved as a tarball using the Docker save command.
        """
        return pulumi.get(self, "docker_image")

    @docker_image.setter
    def docker_image(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "docker_image", value)

    @property
    @pulumi.getter(name="dockerImageHash")
    def docker_image_hash(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The hash of the docker image file
        """
        return pulumi.get(self, "docker_image_hash")

    @docker_image_hash.setter
    def docker_image_hash(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "docker_image_hash", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The name of the Execution Environment.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="programmingLanguage")
    def programming_language(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The programming language of the Execution Environment.
        """
        return pulumi.get(self, "programming_language")

    @programming_language.setter
    def programming_language(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "programming_language", value)

    @property
    @pulumi.getter(name="useCases")
    def use_cases(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]]:
        """
        The list of Use Cases that the Execution Environment supports.
        """
        return pulumi.get(self, "use_cases")

    @use_cases.setter
    def use_cases(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]]):
        pulumi.set(self, "use_cases", value)

    @property
    @pulumi.getter(name="versionDescription")
    def version_description(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The description of the Execution Environment version.
        """
        return pulumi.get(self, "version_description")

    @version_description.setter
    def version_description(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "version_description", value)

    @property
    @pulumi.getter(name="versionId")
    def version_id(self) -> Optional[pulumi.Input[builtins.str]]:
        """
        The ID of the Execution Environment Version.
        """
        return pulumi.get(self, "version_id")

    @version_id.setter
    def version_id(self, value: Optional[pulumi.Input[builtins.str]]):
        pulumi.set(self, "version_id", value)


class ExecutionEnvironment(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[builtins.str]] = None,
                 docker_context_path: Optional[pulumi.Input[builtins.str]] = None,
                 docker_image: Optional[pulumi.Input[builtins.str]] = None,
                 name: Optional[pulumi.Input[builtins.str]] = None,
                 programming_language: Optional[pulumi.Input[builtins.str]] = None,
                 use_cases: Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]] = None,
                 version_description: Optional[pulumi.Input[builtins.str]] = None,
                 __props__=None):
        """
        Execution Environment

        ## Example Usage

        ```python
        import pulumi
        import pulumi_datarobot as datarobot

        example = datarobot.ExecutionEnvironment("example",
            programming_language="python",
            description="Example Execution Environment Description",
            docker_context_path="docker_context.zip",
            docker_image="docker_image.tar",
            use_cases=["customModel"])
        pulumi.export("datarobotExecutionEnvironmentId", example.id)
        pulumi.export("datarobotExecutionEnvironmentVersionId", example.version_id)
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[builtins.str] description: The description of the Execution Environment.
        :param pulumi.Input[builtins.str] docker_context_path: The path to a docker context archive or folder
        :param pulumi.Input[builtins.str] docker_image: A prebuilt environment image saved as a tarball using the Docker save command.
        :param pulumi.Input[builtins.str] name: The name of the Execution Environment.
        :param pulumi.Input[builtins.str] programming_language: The programming language of the Execution Environment.
        :param pulumi.Input[Sequence[pulumi.Input[builtins.str]]] use_cases: The list of Use Cases that the Execution Environment supports.
        :param pulumi.Input[builtins.str] version_description: The description of the Execution Environment version.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ExecutionEnvironmentArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Execution Environment

        ## Example Usage

        ```python
        import pulumi
        import pulumi_datarobot as datarobot

        example = datarobot.ExecutionEnvironment("example",
            programming_language="python",
            description="Example Execution Environment Description",
            docker_context_path="docker_context.zip",
            docker_image="docker_image.tar",
            use_cases=["customModel"])
        pulumi.export("datarobotExecutionEnvironmentId", example.id)
        pulumi.export("datarobotExecutionEnvironmentVersionId", example.version_id)
        ```

        :param str resource_name: The name of the resource.
        :param ExecutionEnvironmentArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ExecutionEnvironmentArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[builtins.str]] = None,
                 docker_context_path: Optional[pulumi.Input[builtins.str]] = None,
                 docker_image: Optional[pulumi.Input[builtins.str]] = None,
                 name: Optional[pulumi.Input[builtins.str]] = None,
                 programming_language: Optional[pulumi.Input[builtins.str]] = None,
                 use_cases: Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]] = None,
                 version_description: Optional[pulumi.Input[builtins.str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ExecutionEnvironmentArgs.__new__(ExecutionEnvironmentArgs)

            __props__.__dict__["description"] = description
            __props__.__dict__["docker_context_path"] = docker_context_path
            __props__.__dict__["docker_image"] = docker_image
            __props__.__dict__["name"] = name
            if programming_language is None and not opts.urn:
                raise TypeError("Missing required property 'programming_language'")
            __props__.__dict__["programming_language"] = programming_language
            if use_cases is None and not opts.urn:
                raise TypeError("Missing required property 'use_cases'")
            __props__.__dict__["use_cases"] = use_cases
            __props__.__dict__["version_description"] = version_description
            __props__.__dict__["build_status"] = None
            __props__.__dict__["docker_context_hash"] = None
            __props__.__dict__["docker_image_hash"] = None
            __props__.__dict__["version_id"] = None
        super(ExecutionEnvironment, __self__).__init__(
            'datarobot:index/executionEnvironment:ExecutionEnvironment',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            build_status: Optional[pulumi.Input[builtins.str]] = None,
            description: Optional[pulumi.Input[builtins.str]] = None,
            docker_context_hash: Optional[pulumi.Input[builtins.str]] = None,
            docker_context_path: Optional[pulumi.Input[builtins.str]] = None,
            docker_image: Optional[pulumi.Input[builtins.str]] = None,
            docker_image_hash: Optional[pulumi.Input[builtins.str]] = None,
            name: Optional[pulumi.Input[builtins.str]] = None,
            programming_language: Optional[pulumi.Input[builtins.str]] = None,
            use_cases: Optional[pulumi.Input[Sequence[pulumi.Input[builtins.str]]]] = None,
            version_description: Optional[pulumi.Input[builtins.str]] = None,
            version_id: Optional[pulumi.Input[builtins.str]] = None) -> 'ExecutionEnvironment':
        """
        Get an existing ExecutionEnvironment resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[builtins.str] build_status: The status of the Execution Environment version build.
        :param pulumi.Input[builtins.str] description: The description of the Execution Environment.
        :param pulumi.Input[builtins.str] docker_context_hash: The hash of the docker context contents.
        :param pulumi.Input[builtins.str] docker_context_path: The path to a docker context archive or folder
        :param pulumi.Input[builtins.str] docker_image: A prebuilt environment image saved as a tarball using the Docker save command.
        :param pulumi.Input[builtins.str] docker_image_hash: The hash of the docker image file
        :param pulumi.Input[builtins.str] name: The name of the Execution Environment.
        :param pulumi.Input[builtins.str] programming_language: The programming language of the Execution Environment.
        :param pulumi.Input[Sequence[pulumi.Input[builtins.str]]] use_cases: The list of Use Cases that the Execution Environment supports.
        :param pulumi.Input[builtins.str] version_description: The description of the Execution Environment version.
        :param pulumi.Input[builtins.str] version_id: The ID of the Execution Environment Version.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ExecutionEnvironmentState.__new__(_ExecutionEnvironmentState)

        __props__.__dict__["build_status"] = build_status
        __props__.__dict__["description"] = description
        __props__.__dict__["docker_context_hash"] = docker_context_hash
        __props__.__dict__["docker_context_path"] = docker_context_path
        __props__.__dict__["docker_image"] = docker_image
        __props__.__dict__["docker_image_hash"] = docker_image_hash
        __props__.__dict__["name"] = name
        __props__.__dict__["programming_language"] = programming_language
        __props__.__dict__["use_cases"] = use_cases
        __props__.__dict__["version_description"] = version_description
        __props__.__dict__["version_id"] = version_id
        return ExecutionEnvironment(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="buildStatus")
    def build_status(self) -> pulumi.Output[builtins.str]:
        """
        The status of the Execution Environment version build.
        """
        return pulumi.get(self, "build_status")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[builtins.str]]:
        """
        The description of the Execution Environment.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="dockerContextHash")
    def docker_context_hash(self) -> pulumi.Output[builtins.str]:
        """
        The hash of the docker context contents.
        """
        return pulumi.get(self, "docker_context_hash")

    @property
    @pulumi.getter(name="dockerContextPath")
    def docker_context_path(self) -> pulumi.Output[Optional[builtins.str]]:
        """
        The path to a docker context archive or folder
        """
        return pulumi.get(self, "docker_context_path")

    @property
    @pulumi.getter(name="dockerImage")
    def docker_image(self) -> pulumi.Output[Optional[builtins.str]]:
        """
        A prebuilt environment image saved as a tarball using the Docker save command.
        """
        return pulumi.get(self, "docker_image")

    @property
    @pulumi.getter(name="dockerImageHash")
    def docker_image_hash(self) -> pulumi.Output[builtins.str]:
        """
        The hash of the docker image file
        """
        return pulumi.get(self, "docker_image_hash")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[builtins.str]:
        """
        The name of the Execution Environment.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="programmingLanguage")
    def programming_language(self) -> pulumi.Output[builtins.str]:
        """
        The programming language of the Execution Environment.
        """
        return pulumi.get(self, "programming_language")

    @property
    @pulumi.getter(name="useCases")
    def use_cases(self) -> pulumi.Output[Sequence[builtins.str]]:
        """
        The list of Use Cases that the Execution Environment supports.
        """
        return pulumi.get(self, "use_cases")

    @property
    @pulumi.getter(name="versionDescription")
    def version_description(self) -> pulumi.Output[Optional[builtins.str]]:
        """
        The description of the Execution Environment version.
        """
        return pulumi.get(self, "version_description")

    @property
    @pulumi.getter(name="versionId")
    def version_id(self) -> pulumi.Output[builtins.str]:
        """
        The ID of the Execution Environment Version.
        """
        return pulumi.get(self, "version_id")

