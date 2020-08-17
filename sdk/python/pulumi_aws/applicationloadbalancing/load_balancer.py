# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from .. import _utilities, _tables
from . import outputs
from ._inputs import *

__all__ = ['LoadBalancer']

warnings.warn("aws.applicationloadbalancing.LoadBalancer has been deprecated in favor of aws.alb.LoadBalancer", DeprecationWarning)


class LoadBalancer(pulumi.CustomResource):
    warnings.warn("aws.applicationloadbalancing.LoadBalancer has been deprecated in favor of aws.alb.LoadBalancer", DeprecationWarning)

    def __init__(__self__,
                 resource_name,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 access_logs: Optional[pulumi.Input[pulumi.InputType['LoadBalancerAccessLogsArgs']]] = None,
                 drop_invalid_header_fields: Optional[pulumi.Input[bool]] = None,
                 enable_cross_zone_load_balancing: Optional[pulumi.Input[bool]] = None,
                 enable_deletion_protection: Optional[pulumi.Input[bool]] = None,
                 enable_http2: Optional[pulumi.Input[bool]] = None,
                 idle_timeout: Optional[pulumi.Input[float]] = None,
                 internal: Optional[pulumi.Input[bool]] = None,
                 ip_address_type: Optional[pulumi.Input[str]] = None,
                 load_balancer_type: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 name_prefix: Optional[pulumi.Input[str]] = None,
                 security_groups: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None,
                 subnet_mappings: Optional[pulumi.Input[List[pulumi.Input[pulumi.InputType['LoadBalancerSubnetMappingArgs']]]]] = None,
                 subnets: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides a Load Balancer resource.

        > **Note:** `alb.LoadBalancer` is known as `lb.LoadBalancer`. The functionality is identical.

        ## Example Usage
        ### Application Load Balancer

        ```python
        import pulumi
        import pulumi_aws as aws

        test = aws.lb.LoadBalancer("test",
            access_logs={
                "bucket": aws_s3_bucket["lb_logs"]["bucket"],
                "enabled": True,
                "prefix": "test-lb",
            },
            enable_deletion_protection=True,
            internal=False,
            load_balancer_type="application",
            security_groups=[aws_security_group["lb_sg"]["id"]],
            subnets=[[__item["id"] for __item in aws_subnet["public"]]],
            tags={
                "Environment": "production",
            })
        ```
        ### Network Load Balancer

        ```python
        import pulumi
        import pulumi_aws as aws

        test = aws.lb.LoadBalancer("test",
            enable_deletion_protection=True,
            internal=False,
            load_balancer_type="network",
            subnets=[[__item["id"] for __item in aws_subnet["public"]]],
            tags={
                "Environment": "production",
            })
        ```
        ### Specifying Elastic IPs

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.lb.LoadBalancer("example",
            load_balancer_type="network",
            subnet_mappings=[
                {
                    "allocation_id": aws_eip["example1"]["id"],
                    "subnet_id": aws_subnet["example1"]["id"],
                },
                {
                    "allocation_id": aws_eip["example2"]["id"],
                    "subnet_id": aws_subnet["example2"]["id"],
                },
            ])
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['LoadBalancerAccessLogsArgs']] access_logs: An Access Logs block. Access Logs documented below.
        :param pulumi.Input[bool] drop_invalid_header_fields: Indicates whether HTTP headers with header fields that are not valid are removed by the load balancer (true) or routed to targets (false). The default is false. Elastic Load Balancing requires that message header names contain only alphanumeric characters and hyphens. Only valid for Load Balancers of type `application`.
        :param pulumi.Input[bool] enable_cross_zone_load_balancing: If true, cross-zone load balancing of the load balancer will be enabled.
               This is a `network` load balancer feature. Defaults to `false`.
        :param pulumi.Input[bool] enable_deletion_protection: If true, deletion of the load balancer will be disabled via
               the AWS API. This will prevent this provider from deleting the load balancer. Defaults to `false`.
        :param pulumi.Input[bool] enable_http2: Indicates whether HTTP/2 is enabled in `application` load balancers. Defaults to `true`.
        :param pulumi.Input[float] idle_timeout: The time in seconds that the connection is allowed to be idle. Only valid for Load Balancers of type `application`. Default: 60.
        :param pulumi.Input[bool] internal: If true, the LB will be internal.
        :param pulumi.Input[str] ip_address_type: The type of IP addresses used by the subnets for your load balancer. The possible values are `ipv4` and `dualstack`
        :param pulumi.Input[str] load_balancer_type: The type of load balancer to create. Possible values are `application` or `network`. The default value is `application`.
        :param pulumi.Input[str] name: The name of the LB. This name must be unique within your AWS account, can have a maximum of 32 characters,
               must contain only alphanumeric characters or hyphens, and must not begin or end with a hyphen. If not specified,
               this provider will autogenerate a name beginning with `tf-lb`.
        :param pulumi.Input[str] name_prefix: Creates a unique name beginning with the specified prefix. Conflicts with `name`.
        :param pulumi.Input[List[pulumi.Input[str]]] security_groups: A list of security group IDs to assign to the LB. Only valid for Load Balancers of type `application`.
        :param pulumi.Input[List[pulumi.Input[pulumi.InputType['LoadBalancerSubnetMappingArgs']]]] subnet_mappings: A subnet mapping block as documented below.
        :param pulumi.Input[List[pulumi.Input[str]]] subnets: A list of subnet IDs to attach to the LB. Subnets
               cannot be updated for Load Balancers of type `network`. Changing this value
               for load balancers of type `network` will force a recreation of the resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the resource.
        """
        pulumi.log.warn("LoadBalancer is deprecated: aws.applicationloadbalancing.LoadBalancer has been deprecated in favor of aws.alb.LoadBalancer")
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            __props__['access_logs'] = access_logs
            __props__['drop_invalid_header_fields'] = drop_invalid_header_fields
            __props__['enable_cross_zone_load_balancing'] = enable_cross_zone_load_balancing
            __props__['enable_deletion_protection'] = enable_deletion_protection
            __props__['enable_http2'] = enable_http2
            __props__['idle_timeout'] = idle_timeout
            __props__['internal'] = internal
            __props__['ip_address_type'] = ip_address_type
            __props__['load_balancer_type'] = load_balancer_type
            __props__['name'] = name
            __props__['name_prefix'] = name_prefix
            __props__['security_groups'] = security_groups
            __props__['subnet_mappings'] = subnet_mappings
            __props__['subnets'] = subnets
            __props__['tags'] = tags
            __props__['arn'] = None
            __props__['arn_suffix'] = None
            __props__['dns_name'] = None
            __props__['vpc_id'] = None
            __props__['zone_id'] = None
        super(LoadBalancer, __self__).__init__(
            'aws:applicationloadbalancing/loadBalancer:LoadBalancer',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: str,
            opts: Optional[pulumi.ResourceOptions] = None,
            access_logs: Optional[pulumi.Input[pulumi.InputType['LoadBalancerAccessLogsArgs']]] = None,
            arn: Optional[pulumi.Input[str]] = None,
            arn_suffix: Optional[pulumi.Input[str]] = None,
            dns_name: Optional[pulumi.Input[str]] = None,
            drop_invalid_header_fields: Optional[pulumi.Input[bool]] = None,
            enable_cross_zone_load_balancing: Optional[pulumi.Input[bool]] = None,
            enable_deletion_protection: Optional[pulumi.Input[bool]] = None,
            enable_http2: Optional[pulumi.Input[bool]] = None,
            idle_timeout: Optional[pulumi.Input[float]] = None,
            internal: Optional[pulumi.Input[bool]] = None,
            ip_address_type: Optional[pulumi.Input[str]] = None,
            load_balancer_type: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            name_prefix: Optional[pulumi.Input[str]] = None,
            security_groups: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None,
            subnet_mappings: Optional[pulumi.Input[List[pulumi.Input[pulumi.InputType['LoadBalancerSubnetMappingArgs']]]]] = None,
            subnets: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            vpc_id: Optional[pulumi.Input[str]] = None,
            zone_id: Optional[pulumi.Input[str]] = None) -> 'LoadBalancer':
        """
        Get an existing LoadBalancer resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['LoadBalancerAccessLogsArgs']] access_logs: An Access Logs block. Access Logs documented below.
        :param pulumi.Input[str] arn: The ARN of the load balancer (matches `id`).
        :param pulumi.Input[str] arn_suffix: The ARN suffix for use with CloudWatch Metrics.
        :param pulumi.Input[str] dns_name: The DNS name of the load balancer.
        :param pulumi.Input[bool] drop_invalid_header_fields: Indicates whether HTTP headers with header fields that are not valid are removed by the load balancer (true) or routed to targets (false). The default is false. Elastic Load Balancing requires that message header names contain only alphanumeric characters and hyphens. Only valid for Load Balancers of type `application`.
        :param pulumi.Input[bool] enable_cross_zone_load_balancing: If true, cross-zone load balancing of the load balancer will be enabled.
               This is a `network` load balancer feature. Defaults to `false`.
        :param pulumi.Input[bool] enable_deletion_protection: If true, deletion of the load balancer will be disabled via
               the AWS API. This will prevent this provider from deleting the load balancer. Defaults to `false`.
        :param pulumi.Input[bool] enable_http2: Indicates whether HTTP/2 is enabled in `application` load balancers. Defaults to `true`.
        :param pulumi.Input[float] idle_timeout: The time in seconds that the connection is allowed to be idle. Only valid for Load Balancers of type `application`. Default: 60.
        :param pulumi.Input[bool] internal: If true, the LB will be internal.
        :param pulumi.Input[str] ip_address_type: The type of IP addresses used by the subnets for your load balancer. The possible values are `ipv4` and `dualstack`
        :param pulumi.Input[str] load_balancer_type: The type of load balancer to create. Possible values are `application` or `network`. The default value is `application`.
        :param pulumi.Input[str] name: The name of the LB. This name must be unique within your AWS account, can have a maximum of 32 characters,
               must contain only alphanumeric characters or hyphens, and must not begin or end with a hyphen. If not specified,
               this provider will autogenerate a name beginning with `tf-lb`.
        :param pulumi.Input[str] name_prefix: Creates a unique name beginning with the specified prefix. Conflicts with `name`.
        :param pulumi.Input[List[pulumi.Input[str]]] security_groups: A list of security group IDs to assign to the LB. Only valid for Load Balancers of type `application`.
        :param pulumi.Input[List[pulumi.Input[pulumi.InputType['LoadBalancerSubnetMappingArgs']]]] subnet_mappings: A subnet mapping block as documented below.
        :param pulumi.Input[List[pulumi.Input[str]]] subnets: A list of subnet IDs to attach to the LB. Subnets
               cannot be updated for Load Balancers of type `network`. Changing this value
               for load balancers of type `network` will force a recreation of the resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the resource.
        :param pulumi.Input[str] zone_id: The canonical hosted zone ID of the load balancer (to be used in a Route 53 Alias record).
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["access_logs"] = access_logs
        __props__["arn"] = arn
        __props__["arn_suffix"] = arn_suffix
        __props__["dns_name"] = dns_name
        __props__["drop_invalid_header_fields"] = drop_invalid_header_fields
        __props__["enable_cross_zone_load_balancing"] = enable_cross_zone_load_balancing
        __props__["enable_deletion_protection"] = enable_deletion_protection
        __props__["enable_http2"] = enable_http2
        __props__["idle_timeout"] = idle_timeout
        __props__["internal"] = internal
        __props__["ip_address_type"] = ip_address_type
        __props__["load_balancer_type"] = load_balancer_type
        __props__["name"] = name
        __props__["name_prefix"] = name_prefix
        __props__["security_groups"] = security_groups
        __props__["subnet_mappings"] = subnet_mappings
        __props__["subnets"] = subnets
        __props__["tags"] = tags
        __props__["vpc_id"] = vpc_id
        __props__["zone_id"] = zone_id
        return LoadBalancer(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accessLogs")
    def access_logs(self) -> Optional['outputs.LoadBalancerAccessLogs']:
        """
        An Access Logs block. Access Logs documented below.
        """
        ...

    @property
    @pulumi.getter
    def arn(self) -> str:
        """
        The ARN of the load balancer (matches `id`).
        """
        ...

    @property
    @pulumi.getter(name="arnSuffix")
    def arn_suffix(self) -> str:
        """
        The ARN suffix for use with CloudWatch Metrics.
        """
        ...

    @property
    @pulumi.getter(name="dnsName")
    def dns_name(self) -> str:
        """
        The DNS name of the load balancer.
        """
        ...

    @property
    @pulumi.getter(name="dropInvalidHeaderFields")
    def drop_invalid_header_fields(self) -> Optional[bool]:
        """
        Indicates whether HTTP headers with header fields that are not valid are removed by the load balancer (true) or routed to targets (false). The default is false. Elastic Load Balancing requires that message header names contain only alphanumeric characters and hyphens. Only valid for Load Balancers of type `application`.
        """
        ...

    @property
    @pulumi.getter(name="enableCrossZoneLoadBalancing")
    def enable_cross_zone_load_balancing(self) -> Optional[bool]:
        """
        If true, cross-zone load balancing of the load balancer will be enabled.
        This is a `network` load balancer feature. Defaults to `false`.
        """
        ...

    @property
    @pulumi.getter(name="enableDeletionProtection")
    def enable_deletion_protection(self) -> Optional[bool]:
        """
        If true, deletion of the load balancer will be disabled via
        the AWS API. This will prevent this provider from deleting the load balancer. Defaults to `false`.
        """
        ...

    @property
    @pulumi.getter(name="enableHttp2")
    def enable_http2(self) -> Optional[bool]:
        """
        Indicates whether HTTP/2 is enabled in `application` load balancers. Defaults to `true`.
        """
        ...

    @property
    @pulumi.getter(name="idleTimeout")
    def idle_timeout(self) -> Optional[float]:
        """
        The time in seconds that the connection is allowed to be idle. Only valid for Load Balancers of type `application`. Default: 60.
        """
        ...

    @property
    @pulumi.getter
    def internal(self) -> bool:
        """
        If true, the LB will be internal.
        """
        ...

    @property
    @pulumi.getter(name="ipAddressType")
    def ip_address_type(self) -> str:
        """
        The type of IP addresses used by the subnets for your load balancer. The possible values are `ipv4` and `dualstack`
        """
        ...

    @property
    @pulumi.getter(name="loadBalancerType")
    def load_balancer_type(self) -> Optional[str]:
        """
        The type of load balancer to create. Possible values are `application` or `network`. The default value is `application`.
        """
        ...

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the LB. This name must be unique within your AWS account, can have a maximum of 32 characters,
        must contain only alphanumeric characters or hyphens, and must not begin or end with a hyphen. If not specified,
        this provider will autogenerate a name beginning with `tf-lb`.
        """
        ...

    @property
    @pulumi.getter(name="namePrefix")
    def name_prefix(self) -> Optional[str]:
        """
        Creates a unique name beginning with the specified prefix. Conflicts with `name`.
        """
        ...

    @property
    @pulumi.getter(name="securityGroups")
    def security_groups(self) -> List[str]:
        """
        A list of security group IDs to assign to the LB. Only valid for Load Balancers of type `application`.
        """
        ...

    @property
    @pulumi.getter(name="subnetMappings")
    def subnet_mappings(self) -> List['outputs.LoadBalancerSubnetMapping']:
        """
        A subnet mapping block as documented below.
        """
        ...

    @property
    @pulumi.getter
    def subnets(self) -> List[str]:
        """
        A list of subnet IDs to attach to the LB. Subnets
        cannot be updated for Load Balancers of type `network`. Changing this value
        for load balancers of type `network` will force a recreation of the resource.
        """
        ...

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        A map of tags to assign to the resource.
        """
        ...

    @property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> str:
        ...

    @property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> str:
        """
        The canonical hosted zone ID of the load balancer (to be used in a Route 53 Alias record).
        """
        ...

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

