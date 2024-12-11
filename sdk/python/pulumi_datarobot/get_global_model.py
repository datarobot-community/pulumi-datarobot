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

__all__ = [
    'GetGlobalModelResult',
    'AwaitableGetGlobalModelResult',
    'get_global_model',
    'get_global_model_output',
]

@pulumi.output_type
class GetGlobalModelResult:
    """
    A collection of values returned by getGlobalModel.
    """
    def __init__(__self__, id=None, name=None, version_id=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if version_id and not isinstance(version_id, str):
            raise TypeError("Expected argument 'version_id' to be a str")
        pulumi.set(__self__, "version_id", version_id)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The ID of the Global Model.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the Registered Model.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="versionId")
    def version_id(self) -> str:
        """
        The ID of the Global Model Version.
        """
        return pulumi.get(self, "version_id")


class AwaitableGetGlobalModelResult(GetGlobalModelResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetGlobalModelResult(
            id=self.id,
            name=self.name,
            version_id=self.version_id)


def get_global_model(name: Optional[str] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetGlobalModelResult:
    """
    Global Model

    ## Example Usage

    ```python
    import pulumi
    import pulumi_datarobot as datarobot

    dummy_binary_classification = datarobot.get_global_model(name="[DataRobot] Dummy Binary Classification")
    ```


    :param str name: The name of the Registered Model.
    """
    __args__ = dict()
    __args__['name'] = name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('datarobot:index/getGlobalModel:getGlobalModel', __args__, opts=opts, typ=GetGlobalModelResult).value

    return AwaitableGetGlobalModelResult(
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        version_id=pulumi.get(__ret__, 'version_id'))
def get_global_model_output(name: Optional[pulumi.Input[str]] = None,
                            opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetGlobalModelResult]:
    """
    Global Model

    ## Example Usage

    ```python
    import pulumi
    import pulumi_datarobot as datarobot

    dummy_binary_classification = datarobot.get_global_model(name="[DataRobot] Dummy Binary Classification")
    ```


    :param str name: The name of the Registered Model.
    """
    __args__ = dict()
    __args__['name'] = name
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('datarobot:index/getGlobalModel:getGlobalModel', __args__, opts=opts, typ=GetGlobalModelResult)
    return __ret__.apply(lambda __response__: GetGlobalModelResult(
        id=pulumi.get(__response__, 'id'),
        name=pulumi.get(__response__, 'name'),
        version_id=pulumi.get(__response__, 'version_id')))
