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
    'DeploymentConfigMinimumHealthyHosts',
    'DeploymentConfigTrafficRoutingConfig',
    'DeploymentConfigTrafficRoutingConfigTimeBasedCanary',
    'DeploymentConfigTrafficRoutingConfigTimeBasedLinear',
    'DeploymentGroupAlarmConfiguration',
    'DeploymentGroupAutoRollbackConfiguration',
    'DeploymentGroupBlueGreenDeploymentConfig',
    'DeploymentGroupBlueGreenDeploymentConfigDeploymentReadyOption',
    'DeploymentGroupBlueGreenDeploymentConfigGreenFleetProvisioningOption',
    'DeploymentGroupBlueGreenDeploymentConfigTerminateBlueInstancesOnDeploymentSuccess',
    'DeploymentGroupDeploymentStyle',
    'DeploymentGroupEc2TagFilter',
    'DeploymentGroupEc2TagSet',
    'DeploymentGroupEc2TagSetEc2TagFilter',
    'DeploymentGroupEcsService',
    'DeploymentGroupLoadBalancerInfo',
    'DeploymentGroupLoadBalancerInfoElbInfo',
    'DeploymentGroupLoadBalancerInfoTargetGroupInfo',
    'DeploymentGroupLoadBalancerInfoTargetGroupPairInfo',
    'DeploymentGroupLoadBalancerInfoTargetGroupPairInfoProdTrafficRoute',
    'DeploymentGroupLoadBalancerInfoTargetGroupPairInfoTargetGroup',
    'DeploymentGroupLoadBalancerInfoTargetGroupPairInfoTestTrafficRoute',
    'DeploymentGroupOnPremisesInstanceTagFilter',
    'DeploymentGroupTriggerConfiguration',
]

@pulumi.output_type
class DeploymentConfigMinimumHealthyHosts(dict):
    def __init__(__self__, *,
                 type: Optional[str] = None,
                 value: Optional[float] = None):
        """
        :param str type: The type can either be `FLEET_PERCENT` or `HOST_COUNT`.
        :param float value: The value when the type is `FLEET_PERCENT` represents the minimum number of healthy instances as
               a percentage of the total number of instances in the deployment. If you specify FLEET_PERCENT, at the start of the
               deployment, AWS CodeDeploy converts the percentage to the equivalent number of instance and rounds up fractional instances.
               When the type is `HOST_COUNT`, the value represents the minimum number of healthy instances as an absolute value.
        """
        if type is not None:
            pulumi.set(__self__, "type", type)
        if value is not None:
            pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[str]:
        """
        The type can either be `FLEET_PERCENT` or `HOST_COUNT`.
        """
        ...

    @property
    @pulumi.getter
    def value(self) -> Optional[float]:
        """
        The value when the type is `FLEET_PERCENT` represents the minimum number of healthy instances as
        a percentage of the total number of instances in the deployment. If you specify FLEET_PERCENT, at the start of the
        deployment, AWS CodeDeploy converts the percentage to the equivalent number of instance and rounds up fractional instances.
        When the type is `HOST_COUNT`, the value represents the minimum number of healthy instances as an absolute value.
        """
        ...

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class DeploymentConfigTrafficRoutingConfig(dict):
    def __init__(__self__, *,
                 time_based_canary: Optional['outputs.DeploymentConfigTrafficRoutingConfigTimeBasedCanary'] = None,
                 time_based_linear: Optional['outputs.DeploymentConfigTrafficRoutingConfigTimeBasedLinear'] = None,
                 type: Optional[str] = None):
        """
        :param 'DeploymentConfigTrafficRoutingConfigTimeBasedCanaryArgs' time_based_canary: The time based canary configuration information. If `type` is `TimeBasedLinear`, use `time_based_linear` instead.
        :param 'DeploymentConfigTrafficRoutingConfigTimeBasedLinearArgs' time_based_linear: The time based linear configuration information. If `type` is `TimeBasedCanary`, use `time_based_canary` instead.
        :param str type: Type of traffic routing config. One of `TimeBasedCanary`, `TimeBasedLinear`, `AllAtOnce`.
        """
        if time_based_canary is not None:
            pulumi.set(__self__, "time_based_canary", time_based_canary)
        if time_based_linear is not None:
            pulumi.set(__self__, "time_based_linear", time_based_linear)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="timeBasedCanary")
    def time_based_canary(self) -> Optional['outputs.DeploymentConfigTrafficRoutingConfigTimeBasedCanary']:
        """
        The time based canary configuration information. If `type` is `TimeBasedLinear`, use `time_based_linear` instead.
        """
        ...

    @property
    @pulumi.getter(name="timeBasedLinear")
    def time_based_linear(self) -> Optional['outputs.DeploymentConfigTrafficRoutingConfigTimeBasedLinear']:
        """
        The time based linear configuration information. If `type` is `TimeBasedCanary`, use `time_based_canary` instead.
        """
        ...

    @property
    @pulumi.getter
    def type(self) -> Optional[str]:
        """
        Type of traffic routing config. One of `TimeBasedCanary`, `TimeBasedLinear`, `AllAtOnce`.
        """
        ...

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class DeploymentConfigTrafficRoutingConfigTimeBasedCanary(dict):
    def __init__(__self__, *,
                 interval: Optional[float] = None,
                 percentage: Optional[float] = None):
        """
        :param float interval: The number of minutes between the first and second traffic shifts of a `TimeBasedCanary` deployment.
        :param float percentage: The percentage of traffic to shift in the first increment of a `TimeBasedCanary` deployment.
        """
        if interval is not None:
            pulumi.set(__self__, "interval", interval)
        if percentage is not None:
            pulumi.set(__self__, "percentage", percentage)

    @property
    @pulumi.getter
    def interval(self) -> Optional[float]:
        """
        The number of minutes between the first and second traffic shifts of a `TimeBasedCanary` deployment.
        """
        ...

    @property
    @pulumi.getter
    def percentage(self) -> Optional[float]:
        """
        The percentage of traffic to shift in the first increment of a `TimeBasedCanary` deployment.
        """
        ...

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class DeploymentConfigTrafficRoutingConfigTimeBasedLinear(dict):
    def __init__(__self__, *,
                 interval: Optional[float] = None,
                 percentage: Optional[float] = None):
        """
        :param float interval: The number of minutes between each incremental traffic shift of a `TimeBasedLinear` deployment.
        :param float percentage: The percentage of traffic that is shifted at the start of each increment of a `TimeBasedLinear` deployment.
        """
        if interval is not None:
            pulumi.set(__self__, "interval", interval)
        if percentage is not None:
            pulumi.set(__self__, "percentage", percentage)

    @property
    @pulumi.getter
    def interval(self) -> Optional[float]:
        """
        The number of minutes between each incremental traffic shift of a `TimeBasedLinear` deployment.
        """
        ...

    @property
    @pulumi.getter
    def percentage(self) -> Optional[float]:
        """
        The percentage of traffic that is shifted at the start of each increment of a `TimeBasedLinear` deployment.
        """
        ...

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class DeploymentGroupAlarmConfiguration(dict):
    def __init__(__self__, *,
                 alarms: Optional[List[str]] = None,
                 enabled: Optional[bool] = None,
                 ignore_poll_alarm_failure: Optional[bool] = None):
        """
        :param List[str] alarms: A list of alarms configured for the deployment group. _A maximum of 10 alarms can be added to a deployment group_.
        :param bool enabled: Indicates whether the alarm configuration is enabled. This option is useful when you want to temporarily deactivate alarm monitoring for a deployment group without having to add the same alarms again later.
        :param bool ignore_poll_alarm_failure: Indicates whether a deployment should continue if information about the current state of alarms cannot be retrieved from CloudWatch. The default value is `false`.
               * `true`: The deployment will proceed even if alarm status information can't be retrieved.
               * `false`: The deployment will stop if alarm status information can't be retrieved.
        """
        if alarms is not None:
            pulumi.set(__self__, "alarms", alarms)
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if ignore_poll_alarm_failure is not None:
            pulumi.set(__self__, "ignore_poll_alarm_failure", ignore_poll_alarm_failure)

    @property
    @pulumi.getter
    def alarms(self) -> Optional[List[str]]:
        """
        A list of alarms configured for the deployment group. _A maximum of 10 alarms can be added to a deployment group_.
        """
        ...

    @property
    @pulumi.getter
    def enabled(self) -> Optional[bool]:
        """
        Indicates whether the alarm configuration is enabled. This option is useful when you want to temporarily deactivate alarm monitoring for a deployment group without having to add the same alarms again later.
        """
        ...

    @property
    @pulumi.getter(name="ignorePollAlarmFailure")
    def ignore_poll_alarm_failure(self) -> Optional[bool]:
        """
        Indicates whether a deployment should continue if information about the current state of alarms cannot be retrieved from CloudWatch. The default value is `false`.
        * `true`: The deployment will proceed even if alarm status information can't be retrieved.
        * `false`: The deployment will stop if alarm status information can't be retrieved.
        """
        ...

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class DeploymentGroupAutoRollbackConfiguration(dict):
    def __init__(__self__, *,
                 enabled: Optional[bool] = None,
                 events: Optional[List[str]] = None):
        """
        :param bool enabled: Indicates whether a defined automatic rollback configuration is currently enabled for this Deployment Group. If you enable automatic rollback, you must specify at least one event type.
        :param List[str] events: The event type or types that trigger a rollback. Supported types are `DEPLOYMENT_FAILURE` and `DEPLOYMENT_STOP_ON_ALARM`.
        """
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if events is not None:
            pulumi.set(__self__, "events", events)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[bool]:
        """
        Indicates whether a defined automatic rollback configuration is currently enabled for this Deployment Group. If you enable automatic rollback, you must specify at least one event type.
        """
        ...

    @property
    @pulumi.getter
    def events(self) -> Optional[List[str]]:
        """
        The event type or types that trigger a rollback. Supported types are `DEPLOYMENT_FAILURE` and `DEPLOYMENT_STOP_ON_ALARM`.
        """
        ...

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class DeploymentGroupBlueGreenDeploymentConfig(dict):
    def __init__(__self__, *,
                 deployment_ready_option: Optional['outputs.DeploymentGroupBlueGreenDeploymentConfigDeploymentReadyOption'] = None,
                 green_fleet_provisioning_option: Optional['outputs.DeploymentGroupBlueGreenDeploymentConfigGreenFleetProvisioningOption'] = None,
                 terminate_blue_instances_on_deployment_success: Optional['outputs.DeploymentGroupBlueGreenDeploymentConfigTerminateBlueInstancesOnDeploymentSuccess'] = None):
        """
        :param 'DeploymentGroupBlueGreenDeploymentConfigDeploymentReadyOptionArgs' deployment_ready_option: Information about the action to take when newly provisioned instances are ready to receive traffic in a blue/green deployment (documented below).
        :param 'DeploymentGroupBlueGreenDeploymentConfigGreenFleetProvisioningOptionArgs' green_fleet_provisioning_option: Information about how instances are provisioned for a replacement environment in a blue/green deployment (documented below).
        :param 'DeploymentGroupBlueGreenDeploymentConfigTerminateBlueInstancesOnDeploymentSuccessArgs' terminate_blue_instances_on_deployment_success: Information about whether to terminate instances in the original fleet during a blue/green deployment (documented below).
        """
        if deployment_ready_option is not None:
            pulumi.set(__self__, "deployment_ready_option", deployment_ready_option)
        if green_fleet_provisioning_option is not None:
            pulumi.set(__self__, "green_fleet_provisioning_option", green_fleet_provisioning_option)
        if terminate_blue_instances_on_deployment_success is not None:
            pulumi.set(__self__, "terminate_blue_instances_on_deployment_success", terminate_blue_instances_on_deployment_success)

    @property
    @pulumi.getter(name="deploymentReadyOption")
    def deployment_ready_option(self) -> Optional['outputs.DeploymentGroupBlueGreenDeploymentConfigDeploymentReadyOption']:
        """
        Information about the action to take when newly provisioned instances are ready to receive traffic in a blue/green deployment (documented below).
        """
        ...

    @property
    @pulumi.getter(name="greenFleetProvisioningOption")
    def green_fleet_provisioning_option(self) -> Optional['outputs.DeploymentGroupBlueGreenDeploymentConfigGreenFleetProvisioningOption']:
        """
        Information about how instances are provisioned for a replacement environment in a blue/green deployment (documented below).
        """
        ...

    @property
    @pulumi.getter(name="terminateBlueInstancesOnDeploymentSuccess")
    def terminate_blue_instances_on_deployment_success(self) -> Optional['outputs.DeploymentGroupBlueGreenDeploymentConfigTerminateBlueInstancesOnDeploymentSuccess']:
        """
        Information about whether to terminate instances in the original fleet during a blue/green deployment (documented below).
        """
        ...

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class DeploymentGroupBlueGreenDeploymentConfigDeploymentReadyOption(dict):
    def __init__(__self__, *,
                 action_on_timeout: Optional[str] = None,
                 wait_time_in_minutes: Optional[float] = None):
        """
        :param str action_on_timeout: When to reroute traffic from an original environment to a replacement environment in a blue/green deployment.
               * `CONTINUE_DEPLOYMENT`: Register new instances with the load balancer immediately after the new application revision is installed on the instances in the replacement environment.
               * `STOP_DEPLOYMENT`: Do not register new instances with load balancer unless traffic is rerouted manually. If traffic is not rerouted manually before the end of the specified wait period, the deployment status is changed to Stopped.
        :param float wait_time_in_minutes: The number of minutes to wait before the status of a blue/green deployment changed to Stopped if rerouting is not started manually. Applies only to the `STOP_DEPLOYMENT` option for `action_on_timeout`.
        """
        if action_on_timeout is not None:
            pulumi.set(__self__, "action_on_timeout", action_on_timeout)
        if wait_time_in_minutes is not None:
            pulumi.set(__self__, "wait_time_in_minutes", wait_time_in_minutes)

    @property
    @pulumi.getter(name="actionOnTimeout")
    def action_on_timeout(self) -> Optional[str]:
        """
        When to reroute traffic from an original environment to a replacement environment in a blue/green deployment.
        * `CONTINUE_DEPLOYMENT`: Register new instances with the load balancer immediately after the new application revision is installed on the instances in the replacement environment.
        * `STOP_DEPLOYMENT`: Do not register new instances with load balancer unless traffic is rerouted manually. If traffic is not rerouted manually before the end of the specified wait period, the deployment status is changed to Stopped.
        """
        ...

    @property
    @pulumi.getter(name="waitTimeInMinutes")
    def wait_time_in_minutes(self) -> Optional[float]:
        """
        The number of minutes to wait before the status of a blue/green deployment changed to Stopped if rerouting is not started manually. Applies only to the `STOP_DEPLOYMENT` option for `action_on_timeout`.
        """
        ...

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class DeploymentGroupBlueGreenDeploymentConfigGreenFleetProvisioningOption(dict):
    def __init__(__self__, *,
                 action: Optional[str] = None):
        """
        :param str action: The method used to add instances to a replacement environment.
               * `DISCOVER_EXISTING`: Use instances that already exist or will be created manually.
               * `COPY_AUTO_SCALING_GROUP`: Use settings from a specified **Auto Scaling** group to define and create instances in a new Auto Scaling group. _Exactly one Auto Scaling group must be specified_ when selecting `COPY_AUTO_SCALING_GROUP`. Use `autoscaling_groups` to specify the Auto Scaling group.
        """
        if action is not None:
            pulumi.set(__self__, "action", action)

    @property
    @pulumi.getter
    def action(self) -> Optional[str]:
        """
        The method used to add instances to a replacement environment.
        * `DISCOVER_EXISTING`: Use instances that already exist or will be created manually.
        * `COPY_AUTO_SCALING_GROUP`: Use settings from a specified **Auto Scaling** group to define and create instances in a new Auto Scaling group. _Exactly one Auto Scaling group must be specified_ when selecting `COPY_AUTO_SCALING_GROUP`. Use `autoscaling_groups` to specify the Auto Scaling group.
        """
        ...

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class DeploymentGroupBlueGreenDeploymentConfigTerminateBlueInstancesOnDeploymentSuccess(dict):
    def __init__(__self__, *,
                 action: Optional[str] = None,
                 termination_wait_time_in_minutes: Optional[float] = None):
        """
        :param str action: The action to take on instances in the original environment after a successful blue/green deployment.
               * `TERMINATE`: Instances are terminated after a specified wait time.
               * `KEEP_ALIVE`: Instances are left running after they are deregistered from the load balancer and removed from the deployment group.
        :param float termination_wait_time_in_minutes: The number of minutes to wait after a successful blue/green deployment before terminating instances from the original environment.
        """
        if action is not None:
            pulumi.set(__self__, "action", action)
        if termination_wait_time_in_minutes is not None:
            pulumi.set(__self__, "termination_wait_time_in_minutes", termination_wait_time_in_minutes)

    @property
    @pulumi.getter
    def action(self) -> Optional[str]:
        """
        The action to take on instances in the original environment after a successful blue/green deployment.
        * `TERMINATE`: Instances are terminated after a specified wait time.
        * `KEEP_ALIVE`: Instances are left running after they are deregistered from the load balancer and removed from the deployment group.
        """
        ...

    @property
    @pulumi.getter(name="terminationWaitTimeInMinutes")
    def termination_wait_time_in_minutes(self) -> Optional[float]:
        """
        The number of minutes to wait after a successful blue/green deployment before terminating instances from the original environment.
        """
        ...

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class DeploymentGroupDeploymentStyle(dict):
    def __init__(__self__, *,
                 deployment_option: Optional[str] = None,
                 deployment_type: Optional[str] = None):
        """
        :param str deployment_option: Indicates whether to route deployment traffic behind a load balancer. Valid Values are `WITH_TRAFFIC_CONTROL` or `WITHOUT_TRAFFIC_CONTROL`. Default is `WITHOUT_TRAFFIC_CONTROL`.
        :param str deployment_type: Indicates whether to run an in-place deployment or a blue/green deployment. Valid Values are `IN_PLACE` or `BLUE_GREEN`. Default is `IN_PLACE`.
        """
        if deployment_option is not None:
            pulumi.set(__self__, "deployment_option", deployment_option)
        if deployment_type is not None:
            pulumi.set(__self__, "deployment_type", deployment_type)

    @property
    @pulumi.getter(name="deploymentOption")
    def deployment_option(self) -> Optional[str]:
        """
        Indicates whether to route deployment traffic behind a load balancer. Valid Values are `WITH_TRAFFIC_CONTROL` or `WITHOUT_TRAFFIC_CONTROL`. Default is `WITHOUT_TRAFFIC_CONTROL`.
        """
        ...

    @property
    @pulumi.getter(name="deploymentType")
    def deployment_type(self) -> Optional[str]:
        """
        Indicates whether to run an in-place deployment or a blue/green deployment. Valid Values are `IN_PLACE` or `BLUE_GREEN`. Default is `IN_PLACE`.
        """
        ...

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class DeploymentGroupEc2TagFilter(dict):
    def __init__(__self__, *,
                 key: Optional[str] = None,
                 type: Optional[str] = None,
                 value: Optional[str] = None):
        """
        :param str key: The key of the tag filter.
        :param str type: The type of the tag filter, either `KEY_ONLY`, `VALUE_ONLY`, or `KEY_AND_VALUE`.
        :param str value: The value of the tag filter.
        """
        if key is not None:
            pulumi.set(__self__, "key", key)
        if type is not None:
            pulumi.set(__self__, "type", type)
        if value is not None:
            pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> Optional[str]:
        """
        The key of the tag filter.
        """
        ...

    @property
    @pulumi.getter
    def type(self) -> Optional[str]:
        """
        The type of the tag filter, either `KEY_ONLY`, `VALUE_ONLY`, or `KEY_AND_VALUE`.
        """
        ...

    @property
    @pulumi.getter
    def value(self) -> Optional[str]:
        """
        The value of the tag filter.
        """
        ...

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class DeploymentGroupEc2TagSet(dict):
    def __init__(__self__, *,
                 ec2_tag_filters: Optional[List['outputs.DeploymentGroupEc2TagSetEc2TagFilter']] = None):
        """
        :param List['DeploymentGroupEc2TagSetEc2TagFilterArgs'] ec2_tag_filters: Tag filters associated with the deployment group. See the AWS docs for details.
        """
        if ec2_tag_filters is not None:
            pulumi.set(__self__, "ec2_tag_filters", ec2_tag_filters)

    @property
    @pulumi.getter(name="ec2TagFilters")
    def ec2_tag_filters(self) -> Optional[List['outputs.DeploymentGroupEc2TagSetEc2TagFilter']]:
        """
        Tag filters associated with the deployment group. See the AWS docs for details.
        """
        ...

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class DeploymentGroupEc2TagSetEc2TagFilter(dict):
    def __init__(__self__, *,
                 key: Optional[str] = None,
                 type: Optional[str] = None,
                 value: Optional[str] = None):
        """
        :param str key: The key of the tag filter.
        :param str type: The type of the tag filter, either `KEY_ONLY`, `VALUE_ONLY`, or `KEY_AND_VALUE`.
        :param str value: The value of the tag filter.
        """
        if key is not None:
            pulumi.set(__self__, "key", key)
        if type is not None:
            pulumi.set(__self__, "type", type)
        if value is not None:
            pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> Optional[str]:
        """
        The key of the tag filter.
        """
        ...

    @property
    @pulumi.getter
    def type(self) -> Optional[str]:
        """
        The type of the tag filter, either `KEY_ONLY`, `VALUE_ONLY`, or `KEY_AND_VALUE`.
        """
        ...

    @property
    @pulumi.getter
    def value(self) -> Optional[str]:
        """
        The value of the tag filter.
        """
        ...

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class DeploymentGroupEcsService(dict):
    def __init__(__self__, *,
                 cluster_name: str,
                 service_name: str):
        """
        :param str cluster_name: The name of the ECS cluster.
        :param str service_name: The name of the ECS service.
        """
        pulumi.set(__self__, "cluster_name", cluster_name)
        pulumi.set(__self__, "service_name", service_name)

    @property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> str:
        """
        The name of the ECS cluster.
        """
        ...

    @property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> str:
        """
        The name of the ECS service.
        """
        ...

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class DeploymentGroupLoadBalancerInfo(dict):
    def __init__(__self__, *,
                 elb_infos: Optional[List['outputs.DeploymentGroupLoadBalancerInfoElbInfo']] = None,
                 target_group_infos: Optional[List['outputs.DeploymentGroupLoadBalancerInfoTargetGroupInfo']] = None,
                 target_group_pair_info: Optional['outputs.DeploymentGroupLoadBalancerInfoTargetGroupPairInfo'] = None):
        """
        :param List['DeploymentGroupLoadBalancerInfoElbInfoArgs'] elb_infos: The Classic Elastic Load Balancer to use in a deployment. Conflicts with `target_group_info` and `target_group_pair_info`.
        :param List['DeploymentGroupLoadBalancerInfoTargetGroupInfoArgs'] target_group_infos: The (Application/Network Load Balancer) target group to use in a deployment. Conflicts with `elb_info` and `target_group_pair_info`.
        :param 'DeploymentGroupLoadBalancerInfoTargetGroupPairInfoArgs' target_group_pair_info: The (Application/Network Load Balancer) target group pair to use in a deployment. Conflicts with `elb_info` and `target_group_info`.
        """
        if elb_infos is not None:
            pulumi.set(__self__, "elb_infos", elb_infos)
        if target_group_infos is not None:
            pulumi.set(__self__, "target_group_infos", target_group_infos)
        if target_group_pair_info is not None:
            pulumi.set(__self__, "target_group_pair_info", target_group_pair_info)

    @property
    @pulumi.getter(name="elbInfos")
    def elb_infos(self) -> Optional[List['outputs.DeploymentGroupLoadBalancerInfoElbInfo']]:
        """
        The Classic Elastic Load Balancer to use in a deployment. Conflicts with `target_group_info` and `target_group_pair_info`.
        """
        ...

    @property
    @pulumi.getter(name="targetGroupInfos")
    def target_group_infos(self) -> Optional[List['outputs.DeploymentGroupLoadBalancerInfoTargetGroupInfo']]:
        """
        The (Application/Network Load Balancer) target group to use in a deployment. Conflicts with `elb_info` and `target_group_pair_info`.
        """
        ...

    @property
    @pulumi.getter(name="targetGroupPairInfo")
    def target_group_pair_info(self) -> Optional['outputs.DeploymentGroupLoadBalancerInfoTargetGroupPairInfo']:
        """
        The (Application/Network Load Balancer) target group pair to use in a deployment. Conflicts with `elb_info` and `target_group_info`.
        """
        ...

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class DeploymentGroupLoadBalancerInfoElbInfo(dict):
    def __init__(__self__, *,
                 name: Optional[str] = None):
        """
        :param str name: The name of the load balancer that will be used to route traffic from original instances to replacement instances in a blue/green deployment. For in-place deployments, the name of the load balancer that instances are deregistered from so they are not serving traffic during a deployment, and then re-registered with after the deployment completes.
        """
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        The name of the load balancer that will be used to route traffic from original instances to replacement instances in a blue/green deployment. For in-place deployments, the name of the load balancer that instances are deregistered from so they are not serving traffic during a deployment, and then re-registered with after the deployment completes.
        """
        ...

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class DeploymentGroupLoadBalancerInfoTargetGroupInfo(dict):
    def __init__(__self__, *,
                 name: Optional[str] = None):
        """
        :param str name: The name of the target group that instances in the original environment are deregistered from, and instances in the replacement environment registered with. For in-place deployments, the name of the target group that instances are deregistered from, so they are not serving traffic during a deployment, and then re-registered with after the deployment completes.
        """
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        The name of the target group that instances in the original environment are deregistered from, and instances in the replacement environment registered with. For in-place deployments, the name of the target group that instances are deregistered from, so they are not serving traffic during a deployment, and then re-registered with after the deployment completes.
        """
        ...

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class DeploymentGroupLoadBalancerInfoTargetGroupPairInfo(dict):
    def __init__(__self__, *,
                 prod_traffic_route: 'outputs.DeploymentGroupLoadBalancerInfoTargetGroupPairInfoProdTrafficRoute',
                 target_groups: List['outputs.DeploymentGroupLoadBalancerInfoTargetGroupPairInfoTargetGroup'],
                 test_traffic_route: Optional['outputs.DeploymentGroupLoadBalancerInfoTargetGroupPairInfoTestTrafficRoute'] = None):
        """
        :param 'DeploymentGroupLoadBalancerInfoTargetGroupPairInfoProdTrafficRouteArgs' prod_traffic_route: Configuration block for the production traffic route (documented below).
        :param List['DeploymentGroupLoadBalancerInfoTargetGroupPairInfoTargetGroupArgs'] target_groups: Configuration blocks for a target group within a target group pair (documented below).
        :param 'DeploymentGroupLoadBalancerInfoTargetGroupPairInfoTestTrafficRouteArgs' test_traffic_route: Configuration block for the test traffic route (documented below).
        """
        pulumi.set(__self__, "prod_traffic_route", prod_traffic_route)
        pulumi.set(__self__, "target_groups", target_groups)
        if test_traffic_route is not None:
            pulumi.set(__self__, "test_traffic_route", test_traffic_route)

    @property
    @pulumi.getter(name="prodTrafficRoute")
    def prod_traffic_route(self) -> 'outputs.DeploymentGroupLoadBalancerInfoTargetGroupPairInfoProdTrafficRoute':
        """
        Configuration block for the production traffic route (documented below).
        """
        ...

    @property
    @pulumi.getter(name="targetGroups")
    def target_groups(self) -> List['outputs.DeploymentGroupLoadBalancerInfoTargetGroupPairInfoTargetGroup']:
        """
        Configuration blocks for a target group within a target group pair (documented below).
        """
        ...

    @property
    @pulumi.getter(name="testTrafficRoute")
    def test_traffic_route(self) -> Optional['outputs.DeploymentGroupLoadBalancerInfoTargetGroupPairInfoTestTrafficRoute']:
        """
        Configuration block for the test traffic route (documented below).
        """
        ...

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class DeploymentGroupLoadBalancerInfoTargetGroupPairInfoProdTrafficRoute(dict):
    def __init__(__self__, *,
                 listener_arns: List[str]):
        """
        :param List[str] listener_arns: List of Amazon Resource Names (ARNs) of the load balancer listeners.
        """
        pulumi.set(__self__, "listener_arns", listener_arns)

    @property
    @pulumi.getter(name="listenerArns")
    def listener_arns(self) -> List[str]:
        """
        List of Amazon Resource Names (ARNs) of the load balancer listeners.
        """
        ...

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class DeploymentGroupLoadBalancerInfoTargetGroupPairInfoTargetGroup(dict):
    def __init__(__self__, *,
                 name: str):
        """
        :param str name: Name of the target group.
        """
        pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of the target group.
        """
        ...

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class DeploymentGroupLoadBalancerInfoTargetGroupPairInfoTestTrafficRoute(dict):
    def __init__(__self__, *,
                 listener_arns: List[str]):
        """
        :param List[str] listener_arns: List of Amazon Resource Names (ARNs) of the load balancer listeners.
        """
        pulumi.set(__self__, "listener_arns", listener_arns)

    @property
    @pulumi.getter(name="listenerArns")
    def listener_arns(self) -> List[str]:
        """
        List of Amazon Resource Names (ARNs) of the load balancer listeners.
        """
        ...

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class DeploymentGroupOnPremisesInstanceTagFilter(dict):
    def __init__(__self__, *,
                 key: Optional[str] = None,
                 type: Optional[str] = None,
                 value: Optional[str] = None):
        """
        :param str key: The key of the tag filter.
        :param str type: The type of the tag filter, either `KEY_ONLY`, `VALUE_ONLY`, or `KEY_AND_VALUE`.
        :param str value: The value of the tag filter.
        """
        if key is not None:
            pulumi.set(__self__, "key", key)
        if type is not None:
            pulumi.set(__self__, "type", type)
        if value is not None:
            pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> Optional[str]:
        """
        The key of the tag filter.
        """
        ...

    @property
    @pulumi.getter
    def type(self) -> Optional[str]:
        """
        The type of the tag filter, either `KEY_ONLY`, `VALUE_ONLY`, or `KEY_AND_VALUE`.
        """
        ...

    @property
    @pulumi.getter
    def value(self) -> Optional[str]:
        """
        The value of the tag filter.
        """
        ...

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class DeploymentGroupTriggerConfiguration(dict):
    def __init__(__self__, *,
                 trigger_events: List[str],
                 trigger_name: str,
                 trigger_target_arn: str):
        """
        :param List[str] trigger_events: The event type or types for which notifications are triggered. Some values that are supported: `DeploymentStart`, `DeploymentSuccess`, `DeploymentFailure`, `DeploymentStop`, `DeploymentRollback`, `InstanceStart`, `InstanceSuccess`, `InstanceFailure`.  See [the CodeDeploy documentation](http://docs.aws.amazon.com/codedeploy/latest/userguide/monitoring-sns-event-notifications-create-trigger.html) for all possible values.
        :param str trigger_name: The name of the notification trigger.
        :param str trigger_target_arn: The ARN of the SNS topic through which notifications are sent.
        """
        pulumi.set(__self__, "trigger_events", trigger_events)
        pulumi.set(__self__, "trigger_name", trigger_name)
        pulumi.set(__self__, "trigger_target_arn", trigger_target_arn)

    @property
    @pulumi.getter(name="triggerEvents")
    def trigger_events(self) -> List[str]:
        """
        The event type or types for which notifications are triggered. Some values that are supported: `DeploymentStart`, `DeploymentSuccess`, `DeploymentFailure`, `DeploymentStop`, `DeploymentRollback`, `InstanceStart`, `InstanceSuccess`, `InstanceFailure`.  See [the CodeDeploy documentation](http://docs.aws.amazon.com/codedeploy/latest/userguide/monitoring-sns-event-notifications-create-trigger.html) for all possible values.
        """
        ...

    @property
    @pulumi.getter(name="triggerName")
    def trigger_name(self) -> str:
        """
        The name of the notification trigger.
        """
        ...

    @property
    @pulumi.getter(name="triggerTargetArn")
    def trigger_target_arn(self) -> str:
        """
        The ARN of the SNS topic through which notifications are sent.
        """
        ...

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


