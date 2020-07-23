# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from .. import _utilities, _tables

__all__ = [
    'GetOutpostInstanceTypeResult',
    'AwaitableGetOutpostInstanceTypeResult',
    'get_outpost_instance_type',
]


@pulumi.output_type
class _GetOutpostInstanceTypeResult:
    arn: str = pulumi.property("arn")
    id: str = pulumi.property("id")
    instance_type: str = pulumi.property("instanceType")
    preferred_instance_types: Optional[List[str]] = pulumi.property("preferredInstanceTypes")


class GetOutpostInstanceTypeResult:
    """
    A collection of values returned by getOutpostInstanceType.
    """
    def __init__(__self__, arn=None, id=None, instance_type=None, preferred_instance_types=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        __self__.arn = arn
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        """
        The provider-assigned unique ID for this managed resource.
        """
        if instance_type and not isinstance(instance_type, str):
            raise TypeError("Expected argument 'instance_type' to be a str")
        __self__.instance_type = instance_type
        if preferred_instance_types and not isinstance(preferred_instance_types, list):
            raise TypeError("Expected argument 'preferred_instance_types' to be a list")
        __self__.preferred_instance_types = preferred_instance_types


class AwaitableGetOutpostInstanceTypeResult(GetOutpostInstanceTypeResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetOutpostInstanceTypeResult(
            arn=self.arn,
            id=self.id,
            instance_type=self.instance_type,
            preferred_instance_types=self.preferred_instance_types)


def get_outpost_instance_type(arn: Optional[str] = None,
                              instance_type: Optional[str] = None,
                              preferred_instance_types: Optional[List[str]] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetOutpostInstanceTypeResult:
    """
    Information about single Outpost Instance Type.


    :param str arn: Outpost Amazon Resource Name (ARN).
    :param str instance_type: Desired instance type. Conflicts with `preferred_instance_types`.
    :param List[str] preferred_instance_types: Ordered list of preferred instance types. The first match in this list will be returned. If no preferred matches are found and the original search returned more than one result, an error is returned. Conflicts with `instance_type`.
    """
    __args__ = dict()
    __args__['arn'] = arn
    __args__['instanceType'] = instance_type
    __args__['preferredInstanceTypes'] = preferred_instance_types
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws:outposts/getOutpostInstanceType:getOutpostInstanceType', __args__, opts=opts, typ=_GetOutpostInstanceTypeResult).value

    return AwaitableGetOutpostInstanceTypeResult(
        arn=__ret__.arn,
        id=__ret__.id,
        instance_type=__ret__.instance_type,
        preferred_instance_types=__ret__.preferred_instance_types)
