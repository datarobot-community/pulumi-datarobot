# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['PlaygroundArgs', 'Playground']

@pulumi.input_type
class PlaygroundArgs:
    def __init__(__self__, *,
                 description: pulumi.Input[str],
                 use_case_id: pulumi.Input[str],
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Playground resource.
        :param pulumi.Input[str] description: The description of the Playground.
        :param pulumi.Input[str] use_case_id: The id of the Playground.
        :param pulumi.Input[str] name: The name of the Playground.
        """
        pulumi.set(__self__, "description", description)
        pulumi.set(__self__, "use_case_id", use_case_id)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Input[str]:
        """
        The description of the Playground.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: pulumi.Input[str]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="useCaseId")
    def use_case_id(self) -> pulumi.Input[str]:
        """
        The id of the Playground.
        """
        return pulumi.get(self, "use_case_id")

    @use_case_id.setter
    def use_case_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "use_case_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Playground.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _PlaygroundState:
    def __init__(__self__, *,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 use_case_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Playground resources.
        :param pulumi.Input[str] description: The description of the Playground.
        :param pulumi.Input[str] name: The name of the Playground.
        :param pulumi.Input[str] use_case_id: The id of the Playground.
        """
        if description is not None:
            pulumi.set(__self__, "description", description)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if use_case_id is not None:
            pulumi.set(__self__, "use_case_id", use_case_id)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the Playground.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Playground.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="useCaseId")
    def use_case_id(self) -> Optional[pulumi.Input[str]]:
        """
        The id of the Playground.
        """
        return pulumi.get(self, "use_case_id")

    @use_case_id.setter
    def use_case_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "use_case_id", value)


class Playground(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 use_case_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Playground

        ## Example Usage

        ```python
        import pulumi
        import pulumi_datarobot as datarobot

        example = datarobot.Playground("example",
            description="Description for the example playground",
            use_case_id=datarobot_use_case["example"]["id"])
        pulumi.export("exampleId", example.id)
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The description of the Playground.
        :param pulumi.Input[str] name: The name of the Playground.
        :param pulumi.Input[str] use_case_id: The id of the Playground.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: PlaygroundArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Playground

        ## Example Usage

        ```python
        import pulumi
        import pulumi_datarobot as datarobot

        example = datarobot.Playground("example",
            description="Description for the example playground",
            use_case_id=datarobot_use_case["example"]["id"])
        pulumi.export("exampleId", example.id)
        ```

        :param str resource_name: The name of the resource.
        :param PlaygroundArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(PlaygroundArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 use_case_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = PlaygroundArgs.__new__(PlaygroundArgs)

            if description is None and not opts.urn:
                raise TypeError("Missing required property 'description'")
            __props__.__dict__["description"] = description
            __props__.__dict__["name"] = name
            if use_case_id is None and not opts.urn:
                raise TypeError("Missing required property 'use_case_id'")
            __props__.__dict__["use_case_id"] = use_case_id
        super(Playground, __self__).__init__(
            'datarobot:index/playground:Playground',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            description: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            use_case_id: Optional[pulumi.Input[str]] = None) -> 'Playground':
        """
        Get an existing Playground resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The description of the Playground.
        :param pulumi.Input[str] name: The name of the Playground.
        :param pulumi.Input[str] use_case_id: The id of the Playground.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _PlaygroundState.__new__(_PlaygroundState)

        __props__.__dict__["description"] = description
        __props__.__dict__["name"] = name
        __props__.__dict__["use_case_id"] = use_case_id
        return Playground(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        The description of the Playground.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the Playground.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="useCaseId")
    def use_case_id(self) -> pulumi.Output[str]:
        """
        The id of the Playground.
        """
        return pulumi.get(self, "use_case_id")

