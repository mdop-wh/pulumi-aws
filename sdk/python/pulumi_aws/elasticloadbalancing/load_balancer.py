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

warnings.warn("aws.elasticloadbalancing.LoadBalancer has been deprecated in favor of aws.elb.LoadBalancer", DeprecationWarning)


class LoadBalancer(pulumi.CustomResource):
    warnings.warn("aws.elasticloadbalancing.LoadBalancer has been deprecated in favor of aws.elb.LoadBalancer", DeprecationWarning)

    def __init__(__self__,
                 resource_name,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 access_logs: Optional[pulumi.Input[pulumi.InputType['LoadBalancerAccessLogsArgs']]] = None,
                 availability_zones: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None,
                 connection_draining: Optional[pulumi.Input[bool]] = None,
                 connection_draining_timeout: Optional[pulumi.Input[float]] = None,
                 cross_zone_load_balancing: Optional[pulumi.Input[bool]] = None,
                 health_check: Optional[pulumi.Input[pulumi.InputType['LoadBalancerHealthCheckArgs']]] = None,
                 idle_timeout: Optional[pulumi.Input[float]] = None,
                 instances: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None,
                 internal: Optional[pulumi.Input[bool]] = None,
                 listeners: Optional[pulumi.Input[List[pulumi.Input[pulumi.InputType['LoadBalancerListenerArgs']]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 name_prefix: Optional[pulumi.Input[str]] = None,
                 security_groups: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None,
                 source_security_group: Optional[pulumi.Input[str]] = None,
                 subnets: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides an Elastic Load Balancer resource, also known as a "Classic
        Load Balancer" after the release of
        `Application/Network Load Balancers`.

        > **NOTE on ELB Instances and ELB Attachments:** This provider currently
        provides both a standalone ELB Attachment resource
        (describing an instance attached to an ELB), and an ELB resource with
        `instances` defined in-line. At this time you cannot use an ELB with in-line
        instances in conjunction with a ELB Attachment resources. Doing so will cause a
        conflict and will overwrite attachments.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        # Create a new load balancer
        bar = aws.elb.LoadBalancer("bar",
            access_logs={
                "bucket": "foo",
                "bucket_prefix": "bar",
                "interval": 60,
            },
            availability_zones=[
                "us-west-2a",
                "us-west-2b",
                "us-west-2c",
            ],
            connection_draining=True,
            connection_draining_timeout=400,
            cross_zone_load_balancing=True,
            health_check={
                "healthyThreshold": 2,
                "interval": 30,
                "target": "HTTP:8000/",
                "timeout": 3,
                "unhealthyThreshold": 2,
            },
            idle_timeout=400,
            instances=[aws_instance["foo"]["id"]],
            listeners=[
                {
                    "instance_port": 8000,
                    "instanceProtocol": "http",
                    "lb_port": 80,
                    "lbProtocol": "http",
                },
                {
                    "instance_port": 8000,
                    "instanceProtocol": "http",
                    "lb_port": 443,
                    "lbProtocol": "https",
                    "sslCertificateId": "arn:aws:iam::123456789012:server-certificate/certName",
                },
            ],
            tags={
                "Name": "foobar-elb",
            })
        ```
        ## Note on ECDSA Key Algorithm

        If the ARN of the `ssl_certificate_id` that is pointed to references a
        certificate that was signed by an ECDSA key, note that ELB only supports the
        P256 and P384 curves.  Using a certificate signed by a key using a different
        curve could produce the error `ERR_SSL_VERSION_OR_CIPHER_MISMATCH` in your
        browser.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['LoadBalancerAccessLogsArgs']] access_logs: An Access Logs block. Access Logs documented below.
        :param pulumi.Input[List[pulumi.Input[str]]] availability_zones: The AZ's to serve traffic in.
        :param pulumi.Input[bool] connection_draining: Boolean to enable connection draining. Default: `false`
        :param pulumi.Input[float] connection_draining_timeout: The time in seconds to allow for connections to drain. Default: `300`
        :param pulumi.Input[bool] cross_zone_load_balancing: Enable cross-zone load balancing. Default: `true`
        :param pulumi.Input[pulumi.InputType['LoadBalancerHealthCheckArgs']] health_check: A health_check block. Health Check documented below.
        :param pulumi.Input[float] idle_timeout: The time in seconds that the connection is allowed to be idle. Default: `60`
        :param pulumi.Input[List[pulumi.Input[str]]] instances: A list of instance ids to place in the ELB pool.
        :param pulumi.Input[bool] internal: If true, ELB will be an internal ELB.
        :param pulumi.Input[List[pulumi.Input[pulumi.InputType['LoadBalancerListenerArgs']]]] listeners: A list of listener blocks. Listeners documented below.
        :param pulumi.Input[str] name: The name of the ELB. By default generated by this provider.
        :param pulumi.Input[str] name_prefix: Creates a unique name beginning with the specified
               prefix. Conflicts with `name`.
        :param pulumi.Input[List[pulumi.Input[str]]] security_groups: A list of security group IDs to assign to the ELB.
               Only valid if creating an ELB within a VPC
        :param pulumi.Input[str] source_security_group: The name of the security group that you can use as
               part of your inbound rules for your load balancer's back-end application
               instances. Use this for Classic or Default VPC only.
        :param pulumi.Input[List[pulumi.Input[str]]] subnets: A list of subnet IDs to attach to the ELB.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the resource.
        """
        pulumi.log.warn("LoadBalancer is deprecated: aws.elasticloadbalancing.LoadBalancer has been deprecated in favor of aws.elb.LoadBalancer")
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
            __props__['availability_zones'] = availability_zones
            __props__['connection_draining'] = connection_draining
            __props__['connection_draining_timeout'] = connection_draining_timeout
            __props__['cross_zone_load_balancing'] = cross_zone_load_balancing
            __props__['health_check'] = health_check
            __props__['idle_timeout'] = idle_timeout
            __props__['instances'] = instances
            __props__['internal'] = internal
            if listeners is None:
                raise TypeError("Missing required property 'listeners'")
            __props__['listeners'] = listeners
            __props__['name'] = name
            __props__['name_prefix'] = name_prefix
            __props__['security_groups'] = security_groups
            __props__['source_security_group'] = source_security_group
            __props__['subnets'] = subnets
            __props__['tags'] = tags
            __props__['arn'] = None
            __props__['dns_name'] = None
            __props__['source_security_group_id'] = None
            __props__['zone_id'] = None
        super(LoadBalancer, __self__).__init__(
            'aws:elasticloadbalancing/loadBalancer:LoadBalancer',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: str,
            opts: Optional[pulumi.ResourceOptions] = None,
            access_logs: Optional[pulumi.Input[pulumi.InputType['LoadBalancerAccessLogsArgs']]] = None,
            arn: Optional[pulumi.Input[str]] = None,
            availability_zones: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None,
            connection_draining: Optional[pulumi.Input[bool]] = None,
            connection_draining_timeout: Optional[pulumi.Input[float]] = None,
            cross_zone_load_balancing: Optional[pulumi.Input[bool]] = None,
            dns_name: Optional[pulumi.Input[str]] = None,
            health_check: Optional[pulumi.Input[pulumi.InputType['LoadBalancerHealthCheckArgs']]] = None,
            idle_timeout: Optional[pulumi.Input[float]] = None,
            instances: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None,
            internal: Optional[pulumi.Input[bool]] = None,
            listeners: Optional[pulumi.Input[List[pulumi.Input[pulumi.InputType['LoadBalancerListenerArgs']]]]] = None,
            name: Optional[pulumi.Input[str]] = None,
            name_prefix: Optional[pulumi.Input[str]] = None,
            security_groups: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None,
            source_security_group: Optional[pulumi.Input[str]] = None,
            source_security_group_id: Optional[pulumi.Input[str]] = None,
            subnets: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            zone_id: Optional[pulumi.Input[str]] = None) -> 'LoadBalancer':
        """
        Get an existing LoadBalancer resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['LoadBalancerAccessLogsArgs']] access_logs: An Access Logs block. Access Logs documented below.
        :param pulumi.Input[str] arn: The ARN of the ELB
        :param pulumi.Input[List[pulumi.Input[str]]] availability_zones: The AZ's to serve traffic in.
        :param pulumi.Input[bool] connection_draining: Boolean to enable connection draining. Default: `false`
        :param pulumi.Input[float] connection_draining_timeout: The time in seconds to allow for connections to drain. Default: `300`
        :param pulumi.Input[bool] cross_zone_load_balancing: Enable cross-zone load balancing. Default: `true`
        :param pulumi.Input[str] dns_name: The DNS name of the ELB
        :param pulumi.Input[pulumi.InputType['LoadBalancerHealthCheckArgs']] health_check: A health_check block. Health Check documented below.
        :param pulumi.Input[float] idle_timeout: The time in seconds that the connection is allowed to be idle. Default: `60`
        :param pulumi.Input[List[pulumi.Input[str]]] instances: A list of instance ids to place in the ELB pool.
        :param pulumi.Input[bool] internal: If true, ELB will be an internal ELB.
        :param pulumi.Input[List[pulumi.Input[pulumi.InputType['LoadBalancerListenerArgs']]]] listeners: A list of listener blocks. Listeners documented below.
        :param pulumi.Input[str] name: The name of the ELB. By default generated by this provider.
        :param pulumi.Input[str] name_prefix: Creates a unique name beginning with the specified
               prefix. Conflicts with `name`.
        :param pulumi.Input[List[pulumi.Input[str]]] security_groups: A list of security group IDs to assign to the ELB.
               Only valid if creating an ELB within a VPC
        :param pulumi.Input[str] source_security_group: The name of the security group that you can use as
               part of your inbound rules for your load balancer's back-end application
               instances. Use this for Classic or Default VPC only.
        :param pulumi.Input[str] source_security_group_id: The ID of the security group that you can use as
               part of your inbound rules for your load balancer's back-end application
               instances. Only available on ELBs launched in a VPC.
        :param pulumi.Input[List[pulumi.Input[str]]] subnets: A list of subnet IDs to attach to the ELB.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the resource.
        :param pulumi.Input[str] zone_id: The canonical hosted zone ID of the ELB (to be used in a Route 53 Alias record)
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["access_logs"] = access_logs
        __props__["arn"] = arn
        __props__["availability_zones"] = availability_zones
        __props__["connection_draining"] = connection_draining
        __props__["connection_draining_timeout"] = connection_draining_timeout
        __props__["cross_zone_load_balancing"] = cross_zone_load_balancing
        __props__["dns_name"] = dns_name
        __props__["health_check"] = health_check
        __props__["idle_timeout"] = idle_timeout
        __props__["instances"] = instances
        __props__["internal"] = internal
        __props__["listeners"] = listeners
        __props__["name"] = name
        __props__["name_prefix"] = name_prefix
        __props__["security_groups"] = security_groups
        __props__["source_security_group"] = source_security_group
        __props__["source_security_group_id"] = source_security_group_id
        __props__["subnets"] = subnets
        __props__["tags"] = tags
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
        The ARN of the ELB
        """
        ...

    @property
    @pulumi.getter(name="availabilityZones")
    def availability_zones(self) -> List[str]:
        """
        The AZ's to serve traffic in.
        """
        ...

    @property
    @pulumi.getter(name="connectionDraining")
    def connection_draining(self) -> Optional[bool]:
        """
        Boolean to enable connection draining. Default: `false`
        """
        ...

    @property
    @pulumi.getter(name="connectionDrainingTimeout")
    def connection_draining_timeout(self) -> Optional[float]:
        """
        The time in seconds to allow for connections to drain. Default: `300`
        """
        ...

    @property
    @pulumi.getter(name="crossZoneLoadBalancing")
    def cross_zone_load_balancing(self) -> Optional[bool]:
        """
        Enable cross-zone load balancing. Default: `true`
        """
        ...

    @property
    @pulumi.getter(name="dnsName")
    def dns_name(self) -> str:
        """
        The DNS name of the ELB
        """
        ...

    @property
    @pulumi.getter(name="healthCheck")
    def health_check(self) -> 'outputs.LoadBalancerHealthCheck':
        """
        A health_check block. Health Check documented below.
        """
        ...

    @property
    @pulumi.getter(name="idleTimeout")
    def idle_timeout(self) -> Optional[float]:
        """
        The time in seconds that the connection is allowed to be idle. Default: `60`
        """
        ...

    @property
    @pulumi.getter
    def instances(self) -> List[str]:
        """
        A list of instance ids to place in the ELB pool.
        """
        ...

    @property
    @pulumi.getter
    def internal(self) -> bool:
        """
        If true, ELB will be an internal ELB.
        """
        ...

    @property
    @pulumi.getter
    def listeners(self) -> List['outputs.LoadBalancerListener']:
        """
        A list of listener blocks. Listeners documented below.
        """
        ...

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the ELB. By default generated by this provider.
        """
        ...

    @property
    @pulumi.getter(name="namePrefix")
    def name_prefix(self) -> Optional[str]:
        """
        Creates a unique name beginning with the specified
        prefix. Conflicts with `name`.
        """
        ...

    @property
    @pulumi.getter(name="securityGroups")
    def security_groups(self) -> List[str]:
        """
        A list of security group IDs to assign to the ELB.
        Only valid if creating an ELB within a VPC
        """
        ...

    @property
    @pulumi.getter(name="sourceSecurityGroup")
    def source_security_group(self) -> str:
        """
        The name of the security group that you can use as
        part of your inbound rules for your load balancer's back-end application
        instances. Use this for Classic or Default VPC only.
        """
        ...

    @property
    @pulumi.getter(name="sourceSecurityGroupId")
    def source_security_group_id(self) -> str:
        """
        The ID of the security group that you can use as
        part of your inbound rules for your load balancer's back-end application
        instances. Only available on ELBs launched in a VPC.
        """
        ...

    @property
    @pulumi.getter
    def subnets(self) -> List[str]:
        """
        A list of subnet IDs to attach to the ELB.
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
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> str:
        """
        The canonical hosted zone ID of the ELB (to be used in a Route 53 Alias record)
        """
        ...

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

