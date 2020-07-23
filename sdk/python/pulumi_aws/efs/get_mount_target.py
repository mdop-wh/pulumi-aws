# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from .. import _utilities, _tables

__all__ = [
    'GetMountTargetResult',
    'AwaitableGetMountTargetResult',
    'get_mount_target',
]


@pulumi.output_type
class _GetMountTargetResult:
    availability_zone_id: str = pulumi.property("availabilityZoneId")
    availability_zone_name: str = pulumi.property("availabilityZoneName")
    dns_name: str = pulumi.property("dnsName")
    file_system_arn: str = pulumi.property("fileSystemArn")
    file_system_id: str = pulumi.property("fileSystemId")
    id: str = pulumi.property("id")
    ip_address: str = pulumi.property("ipAddress")
    mount_target_dns_name: str = pulumi.property("mountTargetDnsName")
    mount_target_id: str = pulumi.property("mountTargetId")
    network_interface_id: str = pulumi.property("networkInterfaceId")
    owner_id: str = pulumi.property("ownerId")
    security_groups: List[str] = pulumi.property("securityGroups")
    subnet_id: str = pulumi.property("subnetId")


class GetMountTargetResult:
    """
    A collection of values returned by getMountTarget.
    """
    def __init__(__self__, availability_zone_id=None, availability_zone_name=None, dns_name=None, file_system_arn=None, file_system_id=None, id=None, ip_address=None, mount_target_dns_name=None, mount_target_id=None, network_interface_id=None, owner_id=None, security_groups=None, subnet_id=None):
        if availability_zone_id and not isinstance(availability_zone_id, str):
            raise TypeError("Expected argument 'availability_zone_id' to be a str")
        __self__.availability_zone_id = availability_zone_id
        """
        The unique and consistent identifier of the Availability Zone (AZ) that the mount target resides in.
        """
        if availability_zone_name and not isinstance(availability_zone_name, str):
            raise TypeError("Expected argument 'availability_zone_name' to be a str")
        __self__.availability_zone_name = availability_zone_name
        """
        The name of the Availability Zone (AZ) that the mount target resides in.
        """
        if dns_name and not isinstance(dns_name, str):
            raise TypeError("Expected argument 'dns_name' to be a str")
        __self__.dns_name = dns_name
        """
        The DNS name for the EFS file system.
        """
        if file_system_arn and not isinstance(file_system_arn, str):
            raise TypeError("Expected argument 'file_system_arn' to be a str")
        __self__.file_system_arn = file_system_arn
        """
        Amazon Resource Name of the file system for which the mount target is intended.
        """
        if file_system_id and not isinstance(file_system_id, str):
            raise TypeError("Expected argument 'file_system_id' to be a str")
        __self__.file_system_id = file_system_id
        """
        ID of the file system for which the mount target is intended.
        """
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        """
        The provider-assigned unique ID for this managed resource.
        """
        if ip_address and not isinstance(ip_address, str):
            raise TypeError("Expected argument 'ip_address' to be a str")
        __self__.ip_address = ip_address
        """
        Address at which the file system may be mounted via the mount target.
        """
        if mount_target_dns_name and not isinstance(mount_target_dns_name, str):
            raise TypeError("Expected argument 'mount_target_dns_name' to be a str")
        __self__.mount_target_dns_name = mount_target_dns_name
        """
        The DNS name for the given subnet/AZ per [documented convention](http://docs.aws.amazon.com/efs/latest/ug/mounting-fs-mount-cmd-dns-name.html).
        """
        if mount_target_id and not isinstance(mount_target_id, str):
            raise TypeError("Expected argument 'mount_target_id' to be a str")
        __self__.mount_target_id = mount_target_id
        if network_interface_id and not isinstance(network_interface_id, str):
            raise TypeError("Expected argument 'network_interface_id' to be a str")
        __self__.network_interface_id = network_interface_id
        """
        The ID of the network interface that Amazon EFS created when it created the mount target.
        """
        if owner_id and not isinstance(owner_id, str):
            raise TypeError("Expected argument 'owner_id' to be a str")
        __self__.owner_id = owner_id
        """
        AWS account ID that owns the resource.
        """
        if security_groups and not isinstance(security_groups, list):
            raise TypeError("Expected argument 'security_groups' to be a list")
        __self__.security_groups = security_groups
        """
        List of VPC security group IDs attached to the mount target.
        """
        if subnet_id and not isinstance(subnet_id, str):
            raise TypeError("Expected argument 'subnet_id' to be a str")
        __self__.subnet_id = subnet_id
        """
        ID of the mount target's subnet.
        """


class AwaitableGetMountTargetResult(GetMountTargetResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetMountTargetResult(
            availability_zone_id=self.availability_zone_id,
            availability_zone_name=self.availability_zone_name,
            dns_name=self.dns_name,
            file_system_arn=self.file_system_arn,
            file_system_id=self.file_system_id,
            id=self.id,
            ip_address=self.ip_address,
            mount_target_dns_name=self.mount_target_dns_name,
            mount_target_id=self.mount_target_id,
            network_interface_id=self.network_interface_id,
            owner_id=self.owner_id,
            security_groups=self.security_groups,
            subnet_id=self.subnet_id)


def get_mount_target(mount_target_id: Optional[str] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetMountTargetResult:
    """
    Provides information about an Elastic File System Mount Target (EFS).

    ## Example Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    config = pulumi.Config()
    mount_target_id = config.get("mountTargetId")
    if mount_target_id is None:
        mount_target_id = ""
    by_id = aws.efs.get_mount_target(mount_target_id=mount_target_id)
    ```


    :param str mount_target_id: ID of the mount target that you want to have described
    """
    __args__ = dict()
    __args__['mountTargetId'] = mount_target_id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws:efs/getMountTarget:getMountTarget', __args__, opts=opts, typ=_GetMountTargetResult).value

    return AwaitableGetMountTargetResult(
        availability_zone_id=__ret__.availability_zone_id,
        availability_zone_name=__ret__.availability_zone_name,
        dns_name=__ret__.dns_name,
        file_system_arn=__ret__.file_system_arn,
        file_system_id=__ret__.file_system_id,
        id=__ret__.id,
        ip_address=__ret__.ip_address,
        mount_target_dns_name=__ret__.mount_target_dns_name,
        mount_target_id=__ret__.mount_target_id,
        network_interface_id=__ret__.network_interface_id,
        owner_id=__ret__.owner_id,
        security_groups=__ret__.security_groups,
        subnet_id=__ret__.subnet_id)
