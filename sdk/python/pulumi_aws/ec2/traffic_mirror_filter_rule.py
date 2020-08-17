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

__all__ = ['TrafficMirrorFilterRule']


class TrafficMirrorFilterRule(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 destination_cidr_block: Optional[pulumi.Input[str]] = None,
                 destination_port_range: Optional[pulumi.Input[pulumi.InputType['TrafficMirrorFilterRuleDestinationPortRangeArgs']]] = None,
                 protocol: Optional[pulumi.Input[float]] = None,
                 rule_action: Optional[pulumi.Input[str]] = None,
                 rule_number: Optional[pulumi.Input[float]] = None,
                 source_cidr_block: Optional[pulumi.Input[str]] = None,
                 source_port_range: Optional[pulumi.Input[pulumi.InputType['TrafficMirrorFilterRuleSourcePortRangeArgs']]] = None,
                 traffic_direction: Optional[pulumi.Input[str]] = None,
                 traffic_mirror_filter_id: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides an Traffic mirror filter rule.\
        Read [limits and considerations](https://docs.aws.amazon.com/vpc/latest/mirroring/traffic-mirroring-considerations.html) for traffic mirroring

        ## Example Usage

        To create a basic traffic mirror session

        ```python
        import pulumi
        import pulumi_aws as aws

        filter = aws.ec2.TrafficMirrorFilter("filter",
            description="traffic mirror filter - example",
            network_services=["amazon-dns"])
        ruleout = aws.ec2.TrafficMirrorFilterRule("ruleout",
            description="test rule",
            destination_cidr_block="10.0.0.0/8",
            rule_action="accept",
            rule_number=1,
            source_cidr_block="10.0.0.0/8",
            traffic_direction="egress",
            traffic_mirror_filter_id=filter.id)
        rulein = aws.ec2.TrafficMirrorFilterRule("rulein",
            description="test rule",
            destination_cidr_block="10.0.0.0/8",
            destination_port_range={
                "from_port": 22,
                "to_port": 53,
            },
            protocol=6,
            rule_action="accept",
            rule_number=1,
            source_cidr_block="10.0.0.0/8",
            source_port_range={
                "from_port": 0,
                "to_port": 10,
            },
            traffic_direction="ingress",
            traffic_mirror_filter_id=filter.id)
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: A description of the traffic mirror filter rule.
        :param pulumi.Input[str] destination_cidr_block: The destination CIDR block to assign to the Traffic Mirror rule.
        :param pulumi.Input[pulumi.InputType['TrafficMirrorFilterRuleDestinationPortRangeArgs']] destination_port_range: The destination port range. Supported only when the protocol is set to TCP(6) or UDP(17). See Traffic mirror port range documented below
        :param pulumi.Input[float] protocol: The protocol number, for example 17 (UDP), to assign to the Traffic Mirror rule. For information about the protocol value, see [Protocol Numbers](https://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml) on the Internet Assigned Numbers Authority (IANA) website.
        :param pulumi.Input[str] rule_action: The action to take (accept | reject) on the filtered traffic. Valid values are `accept` and `reject`
        :param pulumi.Input[float] rule_number: The number of the Traffic Mirror rule. This number must be unique for each Traffic Mirror rule in a given direction. The rules are processed in ascending order by rule number.
        :param pulumi.Input[str] source_cidr_block: The source CIDR block to assign to the Traffic Mirror rule.
        :param pulumi.Input[pulumi.InputType['TrafficMirrorFilterRuleSourcePortRangeArgs']] source_port_range: The source port range. Supported only when the protocol is set to TCP(6) or UDP(17). See Traffic mirror port range documented below
        :param pulumi.Input[str] traffic_direction: The direction of traffic to be captured. Valid values are `ingress` and `egress`
        :param pulumi.Input[str] traffic_mirror_filter_id: ID of the traffic mirror filter to which this rule should be added
        """
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

            __props__['description'] = description
            if destination_cidr_block is None:
                raise TypeError("Missing required property 'destination_cidr_block'")
            __props__['destination_cidr_block'] = destination_cidr_block
            __props__['destination_port_range'] = destination_port_range
            __props__['protocol'] = protocol
            if rule_action is None:
                raise TypeError("Missing required property 'rule_action'")
            __props__['rule_action'] = rule_action
            if rule_number is None:
                raise TypeError("Missing required property 'rule_number'")
            __props__['rule_number'] = rule_number
            if source_cidr_block is None:
                raise TypeError("Missing required property 'source_cidr_block'")
            __props__['source_cidr_block'] = source_cidr_block
            __props__['source_port_range'] = source_port_range
            if traffic_direction is None:
                raise TypeError("Missing required property 'traffic_direction'")
            __props__['traffic_direction'] = traffic_direction
            if traffic_mirror_filter_id is None:
                raise TypeError("Missing required property 'traffic_mirror_filter_id'")
            __props__['traffic_mirror_filter_id'] = traffic_mirror_filter_id
        super(TrafficMirrorFilterRule, __self__).__init__(
            'aws:ec2/trafficMirrorFilterRule:TrafficMirrorFilterRule',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: str,
            opts: Optional[pulumi.ResourceOptions] = None,
            description: Optional[pulumi.Input[str]] = None,
            destination_cidr_block: Optional[pulumi.Input[str]] = None,
            destination_port_range: Optional[pulumi.Input[pulumi.InputType['TrafficMirrorFilterRuleDestinationPortRangeArgs']]] = None,
            protocol: Optional[pulumi.Input[float]] = None,
            rule_action: Optional[pulumi.Input[str]] = None,
            rule_number: Optional[pulumi.Input[float]] = None,
            source_cidr_block: Optional[pulumi.Input[str]] = None,
            source_port_range: Optional[pulumi.Input[pulumi.InputType['TrafficMirrorFilterRuleSourcePortRangeArgs']]] = None,
            traffic_direction: Optional[pulumi.Input[str]] = None,
            traffic_mirror_filter_id: Optional[pulumi.Input[str]] = None) -> 'TrafficMirrorFilterRule':
        """
        Get an existing TrafficMirrorFilterRule resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: A description of the traffic mirror filter rule.
        :param pulumi.Input[str] destination_cidr_block: The destination CIDR block to assign to the Traffic Mirror rule.
        :param pulumi.Input[pulumi.InputType['TrafficMirrorFilterRuleDestinationPortRangeArgs']] destination_port_range: The destination port range. Supported only when the protocol is set to TCP(6) or UDP(17). See Traffic mirror port range documented below
        :param pulumi.Input[float] protocol: The protocol number, for example 17 (UDP), to assign to the Traffic Mirror rule. For information about the protocol value, see [Protocol Numbers](https://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml) on the Internet Assigned Numbers Authority (IANA) website.
        :param pulumi.Input[str] rule_action: The action to take (accept | reject) on the filtered traffic. Valid values are `accept` and `reject`
        :param pulumi.Input[float] rule_number: The number of the Traffic Mirror rule. This number must be unique for each Traffic Mirror rule in a given direction. The rules are processed in ascending order by rule number.
        :param pulumi.Input[str] source_cidr_block: The source CIDR block to assign to the Traffic Mirror rule.
        :param pulumi.Input[pulumi.InputType['TrafficMirrorFilterRuleSourcePortRangeArgs']] source_port_range: The source port range. Supported only when the protocol is set to TCP(6) or UDP(17). See Traffic mirror port range documented below
        :param pulumi.Input[str] traffic_direction: The direction of traffic to be captured. Valid values are `ingress` and `egress`
        :param pulumi.Input[str] traffic_mirror_filter_id: ID of the traffic mirror filter to which this rule should be added
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["description"] = description
        __props__["destination_cidr_block"] = destination_cidr_block
        __props__["destination_port_range"] = destination_port_range
        __props__["protocol"] = protocol
        __props__["rule_action"] = rule_action
        __props__["rule_number"] = rule_number
        __props__["source_cidr_block"] = source_cidr_block
        __props__["source_port_range"] = source_port_range
        __props__["traffic_direction"] = traffic_direction
        __props__["traffic_mirror_filter_id"] = traffic_mirror_filter_id
        return TrafficMirrorFilterRule(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        A description of the traffic mirror filter rule.
        """
        ...

    @property
    @pulumi.getter(name="destinationCidrBlock")
    def destination_cidr_block(self) -> str:
        """
        The destination CIDR block to assign to the Traffic Mirror rule.
        """
        ...

    @property
    @pulumi.getter(name="destinationPortRange")
    def destination_port_range(self) -> Optional['outputs.TrafficMirrorFilterRuleDestinationPortRange']:
        """
        The destination port range. Supported only when the protocol is set to TCP(6) or UDP(17). See Traffic mirror port range documented below
        """
        ...

    @property
    @pulumi.getter
    def protocol(self) -> Optional[float]:
        """
        The protocol number, for example 17 (UDP), to assign to the Traffic Mirror rule. For information about the protocol value, see [Protocol Numbers](https://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml) on the Internet Assigned Numbers Authority (IANA) website.
        """
        ...

    @property
    @pulumi.getter(name="ruleAction")
    def rule_action(self) -> str:
        """
        The action to take (accept | reject) on the filtered traffic. Valid values are `accept` and `reject`
        """
        ...

    @property
    @pulumi.getter(name="ruleNumber")
    def rule_number(self) -> float:
        """
        The number of the Traffic Mirror rule. This number must be unique for each Traffic Mirror rule in a given direction. The rules are processed in ascending order by rule number.
        """
        ...

    @property
    @pulumi.getter(name="sourceCidrBlock")
    def source_cidr_block(self) -> str:
        """
        The source CIDR block to assign to the Traffic Mirror rule.
        """
        ...

    @property
    @pulumi.getter(name="sourcePortRange")
    def source_port_range(self) -> Optional['outputs.TrafficMirrorFilterRuleSourcePortRange']:
        """
        The source port range. Supported only when the protocol is set to TCP(6) or UDP(17). See Traffic mirror port range documented below
        """
        ...

    @property
    @pulumi.getter(name="trafficDirection")
    def traffic_direction(self) -> str:
        """
        The direction of traffic to be captured. Valid values are `ingress` and `egress`
        """
        ...

    @property
    @pulumi.getter(name="trafficMirrorFilterId")
    def traffic_mirror_filter_id(self) -> str:
        """
        ID of the traffic mirror filter to which this rule should be added
        """
        ...

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

