# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from .. import _utilities, _tables
from . import outputs

__all__ = [
    'PlanRule',
    'PlanRuleCopyAction',
    'PlanRuleCopyActionLifecycle',
    'PlanRuleLifecycle',
    'SelectionSelectionTag',
]

@pulumi.output_type
class PlanRule(dict):
    def __init__(__self__, *,
                 rule_name: str,
                 target_vault_name: str,
                 completion_window: Optional[float] = None,
                 copy_actions: Optional[List['outputs.PlanRuleCopyAction']] = None,
                 lifecycle: Optional['outputs.PlanRuleLifecycle'] = None,
                 recovery_point_tags: Optional[Mapping[str, str]] = None,
                 schedule: Optional[str] = None,
                 start_window: Optional[float] = None):
        """
        :param str rule_name: An display name for a backup rule.
        :param str target_vault_name: The name of a logical container where backups are stored.
        :param float completion_window: The amount of time AWS Backup attempts a backup before canceling the job and returning an error.
        :param List['PlanRuleCopyActionArgs'] copy_actions: Configuration block(s) with copy operation settings. Detailed below.
        :param 'PlanRuleLifecycleArgs' lifecycle: The lifecycle defines when a protected resource is copied over to a backup vault and when it expires.  Fields documented above.
        :param Mapping[str, str] recovery_point_tags: Metadata that you can assign to help organize the resources that you create.
        :param str schedule: A CRON expression specifying when AWS Backup initiates a backup job.
        :param float start_window: The amount of time in minutes before beginning a backup.
        """
        pulumi.set(__self__, "rule_name", rule_name)
        pulumi.set(__self__, "target_vault_name", target_vault_name)
        if completion_window is not None:
            pulumi.set(__self__, "completion_window", completion_window)
        if copy_actions is not None:
            pulumi.set(__self__, "copy_actions", copy_actions)
        if lifecycle is not None:
            pulumi.set(__self__, "lifecycle", lifecycle)
        if recovery_point_tags is not None:
            pulumi.set(__self__, "recovery_point_tags", recovery_point_tags)
        if schedule is not None:
            pulumi.set(__self__, "schedule", schedule)
        if start_window is not None:
            pulumi.set(__self__, "start_window", start_window)

    @property
    @pulumi.getter(name="ruleName")
    def rule_name(self) -> str:
        """
        An display name for a backup rule.
        """
        ...

    @property
    @pulumi.getter(name="targetVaultName")
    def target_vault_name(self) -> str:
        """
        The name of a logical container where backups are stored.
        """
        ...

    @property
    @pulumi.getter(name="completionWindow")
    def completion_window(self) -> Optional[float]:
        """
        The amount of time AWS Backup attempts a backup before canceling the job and returning an error.
        """
        ...

    @property
    @pulumi.getter(name="copyActions")
    def copy_actions(self) -> Optional[List['outputs.PlanRuleCopyAction']]:
        """
        Configuration block(s) with copy operation settings. Detailed below.
        """
        ...

    @property
    @pulumi.getter
    def lifecycle(self) -> Optional['outputs.PlanRuleLifecycle']:
        """
        The lifecycle defines when a protected resource is copied over to a backup vault and when it expires.  Fields documented above.
        """
        ...

    @property
    @pulumi.getter(name="recoveryPointTags")
    def recovery_point_tags(self) -> Optional[Mapping[str, str]]:
        """
        Metadata that you can assign to help organize the resources that you create.
        """
        ...

    @property
    @pulumi.getter
    def schedule(self) -> Optional[str]:
        """
        A CRON expression specifying when AWS Backup initiates a backup job.
        """
        ...

    @property
    @pulumi.getter(name="startWindow")
    def start_window(self) -> Optional[float]:
        """
        The amount of time in minutes before beginning a backup.
        """
        ...

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class PlanRuleCopyAction(dict):
    def __init__(__self__, *,
                 destination_vault_arn: str,
                 lifecycle: Optional['outputs.PlanRuleCopyActionLifecycle'] = None):
        """
        :param str destination_vault_arn: An Amazon Resource Name (ARN) that uniquely identifies the destination backup vault for the copied backup.
        :param 'PlanRuleCopyActionLifecycleArgs' lifecycle: The lifecycle defines when a protected resource is copied over to a backup vault and when it expires.  Fields documented above.
        """
        pulumi.set(__self__, "destination_vault_arn", destination_vault_arn)
        if lifecycle is not None:
            pulumi.set(__self__, "lifecycle", lifecycle)

    @property
    @pulumi.getter(name="destinationVaultArn")
    def destination_vault_arn(self) -> str:
        """
        An Amazon Resource Name (ARN) that uniquely identifies the destination backup vault for the copied backup.
        """
        ...

    @property
    @pulumi.getter
    def lifecycle(self) -> Optional['outputs.PlanRuleCopyActionLifecycle']:
        """
        The lifecycle defines when a protected resource is copied over to a backup vault and when it expires.  Fields documented above.
        """
        ...

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class PlanRuleCopyActionLifecycle(dict):
    def __init__(__self__, *,
                 cold_storage_after: Optional[float] = None,
                 delete_after: Optional[float] = None):
        """
        :param float cold_storage_after: Specifies the number of days after creation that a recovery point is moved to cold storage.
        :param float delete_after: Specifies the number of days after creation that a recovery point is deleted. Must be 90 days greater than `cold_storage_after`.
        """
        if cold_storage_after is not None:
            pulumi.set(__self__, "cold_storage_after", cold_storage_after)
        if delete_after is not None:
            pulumi.set(__self__, "delete_after", delete_after)

    @property
    @pulumi.getter(name="coldStorageAfter")
    def cold_storage_after(self) -> Optional[float]:
        """
        Specifies the number of days after creation that a recovery point is moved to cold storage.
        """
        ...

    @property
    @pulumi.getter(name="deleteAfter")
    def delete_after(self) -> Optional[float]:
        """
        Specifies the number of days after creation that a recovery point is deleted. Must be 90 days greater than `cold_storage_after`.
        """
        ...

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class PlanRuleLifecycle(dict):
    def __init__(__self__, *,
                 cold_storage_after: Optional[float] = None,
                 delete_after: Optional[float] = None):
        """
        :param float cold_storage_after: Specifies the number of days after creation that a recovery point is moved to cold storage.
        :param float delete_after: Specifies the number of days after creation that a recovery point is deleted. Must be 90 days greater than `cold_storage_after`.
        """
        if cold_storage_after is not None:
            pulumi.set(__self__, "cold_storage_after", cold_storage_after)
        if delete_after is not None:
            pulumi.set(__self__, "delete_after", delete_after)

    @property
    @pulumi.getter(name="coldStorageAfter")
    def cold_storage_after(self) -> Optional[float]:
        """
        Specifies the number of days after creation that a recovery point is moved to cold storage.
        """
        ...

    @property
    @pulumi.getter(name="deleteAfter")
    def delete_after(self) -> Optional[float]:
        """
        Specifies the number of days after creation that a recovery point is deleted. Must be 90 days greater than `cold_storage_after`.
        """
        ...

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class SelectionSelectionTag(dict):
    def __init__(__self__, *,
                 key: str,
                 type: str,
                 value: str):
        """
        :param str key: The key in a key-value pair.
        :param str type: An operation, such as `StringEquals`, that is applied to a key-value pair used to filter resources in a selection.
        :param str value: The value in a key-value pair.
        """
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "type", type)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> str:
        """
        The key in a key-value pair.
        """
        ...

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        An operation, such as `StringEquals`, that is applied to a key-value pair used to filter resources in a selection.
        """
        ...

    @property
    @pulumi.getter
    def value(self) -> str:
        """
        The value in a key-value pair.
        """
        ...

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


