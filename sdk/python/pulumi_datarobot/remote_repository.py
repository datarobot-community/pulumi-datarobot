# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['RemoteRepositoryArgs', 'RemoteRepository']

@pulumi.input_type
class RemoteRepositoryArgs:
    def __init__(__self__, *,
                 description: pulumi.Input[str],
                 location: pulumi.Input[str],
                 source_type: pulumi.Input[str],
                 name: Optional[pulumi.Input[str]] = None,
                 personal_access_token: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a RemoteRepository resource.
        :param pulumi.Input[str] description: The description of the Remote Repository.
        :param pulumi.Input[str] location: The location of the Remote Repository.
        :param pulumi.Input[str] source_type: The source type of the Remote Repository.
        :param pulumi.Input[str] name: The name of the Remote Repository.
        :param pulumi.Input[str] personal_access_token: The personal access token for the Remote Repository.
        """
        pulumi.set(__self__, "description", description)
        pulumi.set(__self__, "location", location)
        pulumi.set(__self__, "source_type", source_type)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if personal_access_token is not None:
            pulumi.set(__self__, "personal_access_token", personal_access_token)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Input[str]:
        """
        The description of the Remote Repository.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: pulumi.Input[str]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def location(self) -> pulumi.Input[str]:
        """
        The location of the Remote Repository.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: pulumi.Input[str]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="sourceType")
    def source_type(self) -> pulumi.Input[str]:
        """
        The source type of the Remote Repository.
        """
        return pulumi.get(self, "source_type")

    @source_type.setter
    def source_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "source_type", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Remote Repository.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="personalAccessToken")
    def personal_access_token(self) -> Optional[pulumi.Input[str]]:
        """
        The personal access token for the Remote Repository.
        """
        return pulumi.get(self, "personal_access_token")

    @personal_access_token.setter
    def personal_access_token(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "personal_access_token", value)


@pulumi.input_type
class _RemoteRepositoryState:
    def __init__(__self__, *,
                 description: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 personal_access_token: Optional[pulumi.Input[str]] = None,
                 source_type: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering RemoteRepository resources.
        :param pulumi.Input[str] description: The description of the Remote Repository.
        :param pulumi.Input[str] location: The location of the Remote Repository.
        :param pulumi.Input[str] name: The name of the Remote Repository.
        :param pulumi.Input[str] personal_access_token: The personal access token for the Remote Repository.
        :param pulumi.Input[str] source_type: The source type of the Remote Repository.
        """
        if description is not None:
            pulumi.set(__self__, "description", description)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if personal_access_token is not None:
            pulumi.set(__self__, "personal_access_token", personal_access_token)
        if source_type is not None:
            pulumi.set(__self__, "source_type", source_type)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the Remote Repository.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The location of the Remote Repository.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Remote Repository.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="personalAccessToken")
    def personal_access_token(self) -> Optional[pulumi.Input[str]]:
        """
        The personal access token for the Remote Repository.
        """
        return pulumi.get(self, "personal_access_token")

    @personal_access_token.setter
    def personal_access_token(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "personal_access_token", value)

    @property
    @pulumi.getter(name="sourceType")
    def source_type(self) -> Optional[pulumi.Input[str]]:
        """
        The source type of the Remote Repository.
        """
        return pulumi.get(self, "source_type")

    @source_type.setter
    def source_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source_type", value)


class RemoteRepository(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 personal_access_token: Optional[pulumi.Input[str]] = None,
                 source_type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        remote repository

        ## Example Usage

        ```python
        import pulumi
        import pulumi_datarobot as datarobot

        example = datarobot.RemoteRepository("example",
            description="Description for the example remote repository",
            location="https://github.com/datarobot/datarobot-user-models",
            source_type="github")
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The description of the Remote Repository.
        :param pulumi.Input[str] location: The location of the Remote Repository.
        :param pulumi.Input[str] name: The name of the Remote Repository.
        :param pulumi.Input[str] personal_access_token: The personal access token for the Remote Repository.
        :param pulumi.Input[str] source_type: The source type of the Remote Repository.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: RemoteRepositoryArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        remote repository

        ## Example Usage

        ```python
        import pulumi
        import pulumi_datarobot as datarobot

        example = datarobot.RemoteRepository("example",
            description="Description for the example remote repository",
            location="https://github.com/datarobot/datarobot-user-models",
            source_type="github")
        ```

        :param str resource_name: The name of the resource.
        :param RemoteRepositoryArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(RemoteRepositoryArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 personal_access_token: Optional[pulumi.Input[str]] = None,
                 source_type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = RemoteRepositoryArgs.__new__(RemoteRepositoryArgs)

            if description is None and not opts.urn:
                raise TypeError("Missing required property 'description'")
            __props__.__dict__["description"] = description
            if location is None and not opts.urn:
                raise TypeError("Missing required property 'location'")
            __props__.__dict__["location"] = location
            __props__.__dict__["name"] = name
            __props__.__dict__["personal_access_token"] = personal_access_token
            if source_type is None and not opts.urn:
                raise TypeError("Missing required property 'source_type'")
            __props__.__dict__["source_type"] = source_type
        super(RemoteRepository, __self__).__init__(
            'datarobot:index/remoteRepository:RemoteRepository',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            description: Optional[pulumi.Input[str]] = None,
            location: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            personal_access_token: Optional[pulumi.Input[str]] = None,
            source_type: Optional[pulumi.Input[str]] = None) -> 'RemoteRepository':
        """
        Get an existing RemoteRepository resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The description of the Remote Repository.
        :param pulumi.Input[str] location: The location of the Remote Repository.
        :param pulumi.Input[str] name: The name of the Remote Repository.
        :param pulumi.Input[str] personal_access_token: The personal access token for the Remote Repository.
        :param pulumi.Input[str] source_type: The source type of the Remote Repository.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _RemoteRepositoryState.__new__(_RemoteRepositoryState)

        __props__.__dict__["description"] = description
        __props__.__dict__["location"] = location
        __props__.__dict__["name"] = name
        __props__.__dict__["personal_access_token"] = personal_access_token
        __props__.__dict__["source_type"] = source_type
        return RemoteRepository(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        The description of the Remote Repository.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The location of the Remote Repository.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the Remote Repository.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="personalAccessToken")
    def personal_access_token(self) -> pulumi.Output[Optional[str]]:
        """
        The personal access token for the Remote Repository.
        """
        return pulumi.get(self, "personal_access_token")

    @property
    @pulumi.getter(name="sourceType")
    def source_type(self) -> pulumi.Output[str]:
        """
        The source type of the Remote Repository.
        """
        return pulumi.get(self, "source_type")

