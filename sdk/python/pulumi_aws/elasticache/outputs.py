# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from .. import _utilities, _tables

__all__ = [
    'ClusterCacheNode',
    'ParameterGroupParameter',
    'ReplicationGroupClusterMode',
    'GetClusterCacheNodeResult',
]

@pulumi.output_type
class ClusterCacheNode(dict):
    def __init__(__self__, *,
                 address: Optional[str] = None,
                 availability_zone: Optional[str] = None,
                 id: Optional[str] = None,
                 port: Optional[float] = None):
        """
        :param str availability_zone: The Availability Zone for the cache cluster. If you want to create cache nodes in multi-az, use `preferred_availability_zones` instead. Default: System chosen Availability Zone.
        :param float port: The port number on which each of the cache nodes will accept connections. For Memcache the default is 11211, and for Redis the default port is 6379. Cannot be provided with `replication_group_id`.
        """
        if address is not None:
            pulumi.set(__self__, "address", address)
        if availability_zone is not None:
            pulumi.set(__self__, "availability_zone", availability_zone)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if port is not None:
            pulumi.set(__self__, "port", port)

    @property
    @pulumi.getter
    def address(self) -> Optional[str]:
        ...

    @property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> Optional[str]:
        """
        The Availability Zone for the cache cluster. If you want to create cache nodes in multi-az, use `preferred_availability_zones` instead. Default: System chosen Availability Zone.
        """
        ...

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        ...

    @property
    @pulumi.getter
    def port(self) -> Optional[float]:
        """
        The port number on which each of the cache nodes will accept connections. For Memcache the default is 11211, and for Redis the default port is 6379. Cannot be provided with `replication_group_id`.
        """
        ...

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class ParameterGroupParameter(dict):
    def __init__(__self__, *,
                 name: str,
                 value: str):
        """
        :param str name: The name of the ElastiCache parameter.
        :param str value: The value of the ElastiCache parameter.
        """
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the ElastiCache parameter.
        """
        ...

    @property
    @pulumi.getter
    def value(self) -> str:
        """
        The value of the ElastiCache parameter.
        """
        ...

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class ReplicationGroupClusterMode(dict):
    def __init__(__self__, *,
                 num_node_groups: float,
                 replicas_per_node_group: float):
        """
        :param float num_node_groups: Specify the number of node groups (shards) for this Redis replication group. Changing this number will trigger an online resizing operation before other settings modifications.
        :param float replicas_per_node_group: Specify the number of replica nodes in each node group. Valid values are 0 to 5. Changing this number will force a new resource.
        """
        pulumi.set(__self__, "num_node_groups", num_node_groups)
        pulumi.set(__self__, "replicas_per_node_group", replicas_per_node_group)

    @property
    @pulumi.getter(name="numNodeGroups")
    def num_node_groups(self) -> float:
        """
        Specify the number of node groups (shards) for this Redis replication group. Changing this number will trigger an online resizing operation before other settings modifications.
        """
        ...

    @property
    @pulumi.getter(name="replicasPerNodeGroup")
    def replicas_per_node_group(self) -> float:
        """
        Specify the number of replica nodes in each node group. Valid values are 0 to 5. Changing this number will force a new resource.
        """
        ...

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class GetClusterCacheNodeResult(dict):
    def __init__(__self__, *,
                 address: str,
                 availability_zone: str,
                 id: str,
                 port: float):
        """
        :param str availability_zone: The Availability Zone for the cache cluster.
        :param float port: The port number on which each of the cache nodes will
               accept connections.
        """
        pulumi.set(__self__, "address", address)
        pulumi.set(__self__, "availability_zone", availability_zone)
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "port", port)

    @property
    @pulumi.getter
    def address(self) -> str:
        ...

    @property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> str:
        """
        The Availability Zone for the cache cluster.
        """
        ...

    @property
    @pulumi.getter
    def id(self) -> str:
        ...

    @property
    @pulumi.getter
    def port(self) -> float:
        """
        The port number on which each of the cache nodes will
        accept connections.
        """
        ...


