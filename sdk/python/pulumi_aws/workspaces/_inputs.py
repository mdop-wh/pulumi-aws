# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from .. import _utilities, _tables

__all__ = [
    'DirectorySelfServicePermissionsArgs',
    'IpGroupRuleArgs',
    'WorkspaceWorkspacePropertiesArgs',
]

@pulumi.input_type
class DirectorySelfServicePermissionsArgs:
    def __init__(__self__, *,
                 change_compute_type: Optional[pulumi.Input[bool]] = None,
                 increase_volume_size: Optional[pulumi.Input[bool]] = None,
                 rebuild_workspace: Optional[pulumi.Input[bool]] = None,
                 restart_workspace: Optional[pulumi.Input[bool]] = None,
                 switch_running_mode: Optional[pulumi.Input[bool]] = None):
        """
        :param pulumi.Input[bool] change_compute_type: Whether WorkSpaces directory users can change the compute type (bundle) for their workspace. Default `false`.
        :param pulumi.Input[bool] increase_volume_size: Whether WorkSpaces directory users can increase the volume size of the drives on their workspace. Default `false`.
        :param pulumi.Input[bool] rebuild_workspace: Whether WorkSpaces directory users can rebuild the operating system of a workspace to its original state. Default `false`.
        :param pulumi.Input[bool] restart_workspace: Whether WorkSpaces directory users can restart their workspace. Default `true`.
        :param pulumi.Input[bool] switch_running_mode: Whether WorkSpaces directory users can switch the running mode of their workspace. Default `false`.
        """
        if change_compute_type is not None:
            pulumi.set(__self__, "change_compute_type", change_compute_type)
        if increase_volume_size is not None:
            pulumi.set(__self__, "increase_volume_size", increase_volume_size)
        if rebuild_workspace is not None:
            pulumi.set(__self__, "rebuild_workspace", rebuild_workspace)
        if restart_workspace is not None:
            pulumi.set(__self__, "restart_workspace", restart_workspace)
        if switch_running_mode is not None:
            pulumi.set(__self__, "switch_running_mode", switch_running_mode)

    @property
    @pulumi.getter(name="changeComputeType")
    def change_compute_type(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether WorkSpaces directory users can change the compute type (bundle) for their workspace. Default `false`.
        """
        ...

    @change_compute_type.setter
    def change_compute_type(self, value: Optional[pulumi.Input[bool]]):
        ...

    @property
    @pulumi.getter(name="increaseVolumeSize")
    def increase_volume_size(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether WorkSpaces directory users can increase the volume size of the drives on their workspace. Default `false`.
        """
        ...

    @increase_volume_size.setter
    def increase_volume_size(self, value: Optional[pulumi.Input[bool]]):
        ...

    @property
    @pulumi.getter(name="rebuildWorkspace")
    def rebuild_workspace(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether WorkSpaces directory users can rebuild the operating system of a workspace to its original state. Default `false`.
        """
        ...

    @rebuild_workspace.setter
    def rebuild_workspace(self, value: Optional[pulumi.Input[bool]]):
        ...

    @property
    @pulumi.getter(name="restartWorkspace")
    def restart_workspace(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether WorkSpaces directory users can restart their workspace. Default `true`.
        """
        ...

    @restart_workspace.setter
    def restart_workspace(self, value: Optional[pulumi.Input[bool]]):
        ...

    @property
    @pulumi.getter(name="switchRunningMode")
    def switch_running_mode(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether WorkSpaces directory users can switch the running mode of their workspace. Default `false`.
        """
        ...

    @switch_running_mode.setter
    def switch_running_mode(self, value: Optional[pulumi.Input[bool]]):
        ...


@pulumi.input_type
class IpGroupRuleArgs:
    def __init__(__self__, *,
                 source: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] source: The IP address range, in CIDR notation, e.g. `10.0.0.0/16`
        :param pulumi.Input[str] description: The description.
        """
        pulumi.set(__self__, "source", source)
        if description is not None:
            pulumi.set(__self__, "description", description)

    @property
    @pulumi.getter
    def source(self) -> pulumi.Input[str]:
        """
        The IP address range, in CIDR notation, e.g. `10.0.0.0/16`
        """
        ...

    @source.setter
    def source(self, value: pulumi.Input[str]):
        ...

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description.
        """
        ...

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        ...


@pulumi.input_type
class WorkspaceWorkspacePropertiesArgs:
    def __init__(__self__, *,
                 compute_type_name: Optional[pulumi.Input[str]] = None,
                 root_volume_size_gib: Optional[pulumi.Input[float]] = None,
                 running_mode: Optional[pulumi.Input[str]] = None,
                 running_mode_auto_stop_timeout_in_minutes: Optional[pulumi.Input[float]] = None,
                 user_volume_size_gib: Optional[pulumi.Input[float]] = None):
        """
        :param pulumi.Input[str] compute_type_name: The compute type. For more information, see [Amazon WorkSpaces Bundles](http://aws.amazon.com/workspaces/details/#Amazon_WorkSpaces_Bundles). Valid values are `VALUE`, `STANDARD`, `PERFORMANCE`, `POWER`, `GRAPHICS`, `POWERPRO` and `GRAPHICSPRO`.
        :param pulumi.Input[float] root_volume_size_gib: The size of the root volume.
        :param pulumi.Input[str] running_mode: The running mode. For more information, see [Manage the WorkSpace Running Mode](https://docs.aws.amazon.com/workspaces/latest/adminguide/running-mode.html). Valid values are `AUTO_STOP` and `ALWAYS_ON`.
        :param pulumi.Input[float] running_mode_auto_stop_timeout_in_minutes: The time after a user logs off when WorkSpaces are automatically stopped. Configured in 60-minute intervals.
        :param pulumi.Input[float] user_volume_size_gib: The size of the user storage.
        """
        if compute_type_name is not None:
            pulumi.set(__self__, "compute_type_name", compute_type_name)
        if root_volume_size_gib is not None:
            pulumi.set(__self__, "root_volume_size_gib", root_volume_size_gib)
        if running_mode is not None:
            pulumi.set(__self__, "running_mode", running_mode)
        if running_mode_auto_stop_timeout_in_minutes is not None:
            pulumi.set(__self__, "running_mode_auto_stop_timeout_in_minutes", running_mode_auto_stop_timeout_in_minutes)
        if user_volume_size_gib is not None:
            pulumi.set(__self__, "user_volume_size_gib", user_volume_size_gib)

    @property
    @pulumi.getter(name="computeTypeName")
    def compute_type_name(self) -> Optional[pulumi.Input[str]]:
        """
        The compute type. For more information, see [Amazon WorkSpaces Bundles](http://aws.amazon.com/workspaces/details/#Amazon_WorkSpaces_Bundles). Valid values are `VALUE`, `STANDARD`, `PERFORMANCE`, `POWER`, `GRAPHICS`, `POWERPRO` and `GRAPHICSPRO`.
        """
        ...

    @compute_type_name.setter
    def compute_type_name(self, value: Optional[pulumi.Input[str]]):
        ...

    @property
    @pulumi.getter(name="rootVolumeSizeGib")
    def root_volume_size_gib(self) -> Optional[pulumi.Input[float]]:
        """
        The size of the root volume.
        """
        ...

    @root_volume_size_gib.setter
    def root_volume_size_gib(self, value: Optional[pulumi.Input[float]]):
        ...

    @property
    @pulumi.getter(name="runningMode")
    def running_mode(self) -> Optional[pulumi.Input[str]]:
        """
        The running mode. For more information, see [Manage the WorkSpace Running Mode](https://docs.aws.amazon.com/workspaces/latest/adminguide/running-mode.html). Valid values are `AUTO_STOP` and `ALWAYS_ON`.
        """
        ...

    @running_mode.setter
    def running_mode(self, value: Optional[pulumi.Input[str]]):
        ...

    @property
    @pulumi.getter(name="runningModeAutoStopTimeoutInMinutes")
    def running_mode_auto_stop_timeout_in_minutes(self) -> Optional[pulumi.Input[float]]:
        """
        The time after a user logs off when WorkSpaces are automatically stopped. Configured in 60-minute intervals.
        """
        ...

    @running_mode_auto_stop_timeout_in_minutes.setter
    def running_mode_auto_stop_timeout_in_minutes(self, value: Optional[pulumi.Input[float]]):
        ...

    @property
    @pulumi.getter(name="userVolumeSizeGib")
    def user_volume_size_gib(self) -> Optional[pulumi.Input[float]]:
        """
        The size of the user storage.
        """
        ...

    @user_volume_size_gib.setter
    def user_volume_size_gib(self, value: Optional[pulumi.Input[float]]):
        ...


