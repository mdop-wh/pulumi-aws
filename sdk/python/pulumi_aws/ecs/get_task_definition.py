# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from .. import _utilities, _tables

__all__ = [
    'GetTaskDefinitionResult',
    'AwaitableGetTaskDefinitionResult',
    'get_task_definition',
]



@pulumi.output_type
class GetTaskDefinitionResult:
    """
    A collection of values returned by getTaskDefinition.
    """
    def __init__(__self__, family=None, id=None, network_mode=None, revision=None, status=None, task_definition=None, task_role_arn=None):
        if family and not isinstance(family, str):
            raise TypeError("Expected argument 'family' to be a str")
        pulumi.set(__self__, "family", family)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if network_mode and not isinstance(network_mode, str):
            raise TypeError("Expected argument 'network_mode' to be a str")
        pulumi.set(__self__, "network_mode", network_mode)
        if revision and not isinstance(revision, float):
            raise TypeError("Expected argument 'revision' to be a float")
        pulumi.set(__self__, "revision", revision)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if task_definition and not isinstance(task_definition, str):
            raise TypeError("Expected argument 'task_definition' to be a str")
        pulumi.set(__self__, "task_definition", task_definition)
        if task_role_arn and not isinstance(task_role_arn, str):
            raise TypeError("Expected argument 'task_role_arn' to be a str")
        pulumi.set(__self__, "task_role_arn", task_role_arn)

    @property
    @pulumi.getter
    def family(self) -> str:
        """
        The family of this task definition
        """
        ...

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        ...

    @property
    @pulumi.getter(name="networkMode")
    def network_mode(self) -> str:
        """
        The Docker networking mode to use for the containers in this task.
        """
        ...

    @property
    @pulumi.getter
    def revision(self) -> float:
        """
        The revision of this task definition
        """
        ...

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        The status of this task definition
        """
        ...

    @property
    @pulumi.getter(name="taskDefinition")
    def task_definition(self) -> str:
        ...

    @property
    @pulumi.getter(name="taskRoleArn")
    def task_role_arn(self) -> str:
        """
        The ARN of the IAM role that containers in this task can assume
        """
        ...



class AwaitableGetTaskDefinitionResult(GetTaskDefinitionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetTaskDefinitionResult(
            family=self.family,
            id=self.id,
            network_mode=self.network_mode,
            revision=self.revision,
            status=self.status,
            task_definition=self.task_definition,
            task_role_arn=self.task_role_arn)


def get_task_definition(task_definition: Optional[str] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetTaskDefinitionResult:
    """
    The ECS task definition data source allows access to details of
    a specific AWS ECS task definition.


    :param str task_definition: The family for the latest ACTIVE revision, family and revision (family:revision) for a specific revision in the family, the ARN of the task definition to access to.
    """
    __args__ = dict()
    __args__['taskDefinition'] = task_definition
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws:ecs/getTaskDefinition:getTaskDefinition', __args__, opts=opts, typ=GetTaskDefinitionResult).value

    return AwaitableGetTaskDefinitionResult(
        family=__ret__.family,
        id=__ret__.id,
        network_mode=__ret__.network_mode,
        revision=__ret__.revision,
        status=__ret__.status,
        task_definition=__ret__.task_definition,
        task_role_arn=__ret__.task_role_arn)
