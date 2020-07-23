# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from . import _utilities, _tables
from . import outputs
from ._inputs import *

__all__ = [
    'GetAutoscalingGroupsResult',
    'AwaitableGetAutoscalingGroupsResult',
    'get_autoscaling_groups',
]


@pulumi.output_type
class _GetAutoscalingGroupsResult:
    arns: List[str] = pulumi.property("arns")
    filters: Optional[List['outputs.GetAutoscalingGroupsFilterResult']] = pulumi.property("filters")
    id: str = pulumi.property("id")
    names: List[str] = pulumi.property("names")


class GetAutoscalingGroupsResult:
    """
    A collection of values returned by getAutoscalingGroups.
    """
    def __init__(__self__, arns=None, filters=None, id=None, names=None):
        if arns and not isinstance(arns, list):
            raise TypeError("Expected argument 'arns' to be a list")
        __self__.arns = arns
        """
        A list of the Autoscaling Groups Arns in the current region.
        """
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        __self__.filters = filters
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        """
        The provider-assigned unique ID for this managed resource.
        """
        if names and not isinstance(names, list):
            raise TypeError("Expected argument 'names' to be a list")
        __self__.names = names
        """
        A list of the Autoscaling Groups in the current region.
        """


class AwaitableGetAutoscalingGroupsResult(GetAutoscalingGroupsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAutoscalingGroupsResult(
            arns=self.arns,
            filters=self.filters,
            id=self.id,
            names=self.names)


def get_autoscaling_groups(filters: Optional[List[pulumi.InputType['GetAutoscalingGroupsFilterArgs']]] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAutoscalingGroupsResult:
    """
    The Autoscaling Groups data source allows access to the list of AWS
    ASGs within a specific region. This will allow you to pass a list of AutoScaling Groups to other resources.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    groups = aws.get_autoscaling_groups(filters=[
        {
            "name": "key",
            "values": ["Team"],
        },
        {
            "name": "value",
            "values": ["Pets"],
        },
    ])
    slack_notifications = aws.autoscaling.Notification("slackNotifications",
        group_names=groups.names,
        notifications=[
            "autoscaling:EC2_INSTANCE_LAUNCH",
            "autoscaling:EC2_INSTANCE_TERMINATE",
            "autoscaling:EC2_INSTANCE_LAUNCH_ERROR",
            "autoscaling:EC2_INSTANCE_TERMINATE_ERROR",
        ],
        topic_arn="TOPIC ARN")
    ```


    :param List[pulumi.InputType['GetAutoscalingGroupsFilterArgs']] filters: A filter used to scope the list e.g. by tags. See [related docs](http://docs.aws.amazon.com/AutoScaling/latest/APIReference/API_Filter.html).
    """
    __args__ = dict()
    __args__['filters'] = filters
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws:index/getAutoscalingGroups:getAutoscalingGroups', __args__, opts=opts, typ=_GetAutoscalingGroupsResult).value

    return AwaitableGetAutoscalingGroupsResult(
        arns=__ret__.arns,
        filters=__ret__.filters,
        id=__ret__.id,
        names=__ret__.names)
