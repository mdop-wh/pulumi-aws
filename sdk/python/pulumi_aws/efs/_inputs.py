# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from .. import _utilities, _tables

__all__ = [
    'AccessPointPosixUserArgs',
    'AccessPointRootDirectoryArgs',
    'AccessPointRootDirectoryCreationInfoArgs',
    'FileSystemLifecyclePolicyArgs',
]

@pulumi.input_type
class AccessPointPosixUserArgs:
    def __init__(__self__, *,
                 gid: pulumi.Input[float],
                 uid: pulumi.Input[float],
                 secondary_gids: Optional[pulumi.Input[List[pulumi.Input[float]]]] = None):
        """
        :param pulumi.Input[float] gid: The POSIX group ID used for all file system operations using this access point.
        :param pulumi.Input[float] uid: The POSIX user ID used for all file system operations using this access point.
        :param pulumi.Input[List[pulumi.Input[float]]] secondary_gids: Secondary POSIX group IDs used for all file system operations using this access point.
        """
        pulumi.set(__self__, "gid", gid)
        pulumi.set(__self__, "uid", uid)
        if secondary_gids is not None:
            pulumi.set(__self__, "secondary_gids", secondary_gids)

    @property
    @pulumi.getter
    def gid(self) -> pulumi.Input[float]:
        """
        The POSIX group ID used for all file system operations using this access point.
        """
        ...

    @gid.setter
    def gid(self, value: pulumi.Input[float]):
        ...

    @property
    @pulumi.getter
    def uid(self) -> pulumi.Input[float]:
        """
        The POSIX user ID used for all file system operations using this access point.
        """
        ...

    @uid.setter
    def uid(self, value: pulumi.Input[float]):
        ...

    @property
    @pulumi.getter(name="secondaryGids")
    def secondary_gids(self) -> Optional[pulumi.Input[List[pulumi.Input[float]]]]:
        """
        Secondary POSIX group IDs used for all file system operations using this access point.
        """
        ...

    @secondary_gids.setter
    def secondary_gids(self, value: Optional[pulumi.Input[List[pulumi.Input[float]]]]):
        ...


@pulumi.input_type
class AccessPointRootDirectoryArgs:
    def __init__(__self__, *,
                 creation_info: Optional[pulumi.Input['AccessPointRootDirectoryCreationInfoArgs']] = None,
                 path: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input['AccessPointRootDirectoryCreationInfoArgs'] creation_info: Specifies the POSIX IDs and permissions to apply to the access point's Root Directory. See Creation Info below.
        :param pulumi.Input[str] path: Specifies the path on the EFS file system to expose as the root directory to NFS clients using the access point to access the EFS file system. A path can have up to four subdirectories. If the specified path does not exist, you are required to provide `creation_info`.
        """
        if creation_info is not None:
            pulumi.set(__self__, "creation_info", creation_info)
        if path is not None:
            pulumi.set(__self__, "path", path)

    @property
    @pulumi.getter(name="creationInfo")
    def creation_info(self) -> Optional[pulumi.Input['AccessPointRootDirectoryCreationInfoArgs']]:
        """
        Specifies the POSIX IDs and permissions to apply to the access point's Root Directory. See Creation Info below.
        """
        ...

    @creation_info.setter
    def creation_info(self, value: Optional[pulumi.Input['AccessPointRootDirectoryCreationInfoArgs']]):
        ...

    @property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the path on the EFS file system to expose as the root directory to NFS clients using the access point to access the EFS file system. A path can have up to four subdirectories. If the specified path does not exist, you are required to provide `creation_info`.
        """
        ...

    @path.setter
    def path(self, value: Optional[pulumi.Input[str]]):
        ...


@pulumi.input_type
class AccessPointRootDirectoryCreationInfoArgs:
    def __init__(__self__, *,
                 owner_gid: pulumi.Input[float],
                 owner_uid: pulumi.Input[float],
                 permissions: pulumi.Input[str]):
        """
        :param pulumi.Input[float] owner_gid: Specifies the POSIX group ID to apply to the `root_directory`.
        :param pulumi.Input[float] owner_uid: Specifies the POSIX user ID to apply to the `root_directory`.
        :param pulumi.Input[str] permissions: Specifies the POSIX permissions to apply to the RootDirectory, in the format of an octal number representing the file's mode bits.
        """
        pulumi.set(__self__, "owner_gid", owner_gid)
        pulumi.set(__self__, "owner_uid", owner_uid)
        pulumi.set(__self__, "permissions", permissions)

    @property
    @pulumi.getter(name="ownerGid")
    def owner_gid(self) -> pulumi.Input[float]:
        """
        Specifies the POSIX group ID to apply to the `root_directory`.
        """
        ...

    @owner_gid.setter
    def owner_gid(self, value: pulumi.Input[float]):
        ...

    @property
    @pulumi.getter(name="ownerUid")
    def owner_uid(self) -> pulumi.Input[float]:
        """
        Specifies the POSIX user ID to apply to the `root_directory`.
        """
        ...

    @owner_uid.setter
    def owner_uid(self, value: pulumi.Input[float]):
        ...

    @property
    @pulumi.getter
    def permissions(self) -> pulumi.Input[str]:
        """
        Specifies the POSIX permissions to apply to the RootDirectory, in the format of an octal number representing the file's mode bits.
        """
        ...

    @permissions.setter
    def permissions(self, value: pulumi.Input[str]):
        ...


@pulumi.input_type
class FileSystemLifecyclePolicyArgs:
    def __init__(__self__, *,
                 transition_to_ia: pulumi.Input[str]):
        """
        :param pulumi.Input[str] transition_to_ia: Indicates how long it takes to transition files to the IA storage class. Valid values: `AFTER_7_DAYS`, `AFTER_14_DAYS`, `AFTER_30_DAYS`, `AFTER_60_DAYS`, or `AFTER_90_DAYS`.
        """
        pulumi.set(__self__, "transition_to_ia", transition_to_ia)

    @property
    @pulumi.getter(name="transitionToIa")
    def transition_to_ia(self) -> pulumi.Input[str]:
        """
        Indicates how long it takes to transition files to the IA storage class. Valid values: `AFTER_7_DAYS`, `AFTER_14_DAYS`, `AFTER_30_DAYS`, `AFTER_60_DAYS`, or `AFTER_90_DAYS`.
        """
        ...

    @transition_to_ia.setter
    def transition_to_ia(self, value: pulumi.Input[str]):
        ...


