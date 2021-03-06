# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from .. import _utilities, _tables

__all__ = ['LocalGatewayRoute']


class LocalGatewayRoute(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 destination_cidr_block: Optional[pulumi.Input[str]] = None,
                 local_gateway_route_table_id: Optional[pulumi.Input[str]] = None,
                 local_gateway_virtual_interface_group_id: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Manages an EC2 Local Gateway Route. More information can be found in the [Outposts User Guide](https://docs.aws.amazon.com/outposts/latest/userguide/outposts-networking-components.html#routing).

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.ec2.LocalGatewayRoute("example",
            destination_cidr_block="172.16.0.0/16",
            local_gateway_route_table_id=data["aws_ec2_local_gateway_route_table"]["example"]["id"],
            local_gateway_virtual_interface_group_id=data["aws_ec2_local_gateway_virtual_interface_group"]["example"]["id"])
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] destination_cidr_block: IPv4 CIDR range used for destination matches. Routing decisions are based on the most specific match.
        :param pulumi.Input[str] local_gateway_route_table_id: Identifier of EC2 Local Gateway Route Table.
        :param pulumi.Input[str] local_gateway_virtual_interface_group_id: Identifier of EC2 Local Gateway Virtual Interface Group.
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

            if destination_cidr_block is None:
                raise TypeError("Missing required property 'destination_cidr_block'")
            __props__['destination_cidr_block'] = destination_cidr_block
            if local_gateway_route_table_id is None:
                raise TypeError("Missing required property 'local_gateway_route_table_id'")
            __props__['local_gateway_route_table_id'] = local_gateway_route_table_id
            if local_gateway_virtual_interface_group_id is None:
                raise TypeError("Missing required property 'local_gateway_virtual_interface_group_id'")
            __props__['local_gateway_virtual_interface_group_id'] = local_gateway_virtual_interface_group_id
        super(LocalGatewayRoute, __self__).__init__(
            'aws:ec2/localGatewayRoute:LocalGatewayRoute',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            destination_cidr_block: Optional[pulumi.Input[str]] = None,
            local_gateway_route_table_id: Optional[pulumi.Input[str]] = None,
            local_gateway_virtual_interface_group_id: Optional[pulumi.Input[str]] = None) -> 'LocalGatewayRoute':
        """
        Get an existing LocalGatewayRoute resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] destination_cidr_block: IPv4 CIDR range used for destination matches. Routing decisions are based on the most specific match.
        :param pulumi.Input[str] local_gateway_route_table_id: Identifier of EC2 Local Gateway Route Table.
        :param pulumi.Input[str] local_gateway_virtual_interface_group_id: Identifier of EC2 Local Gateway Virtual Interface Group.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["destination_cidr_block"] = destination_cidr_block
        __props__["local_gateway_route_table_id"] = local_gateway_route_table_id
        __props__["local_gateway_virtual_interface_group_id"] = local_gateway_virtual_interface_group_id
        return LocalGatewayRoute(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="destinationCidrBlock")
    def destination_cidr_block(self) -> pulumi.Output[str]:
        """
        IPv4 CIDR range used for destination matches. Routing decisions are based on the most specific match.
        """
        return pulumi.get(self, "destination_cidr_block")

    @property
    @pulumi.getter(name="localGatewayRouteTableId")
    def local_gateway_route_table_id(self) -> pulumi.Output[str]:
        """
        Identifier of EC2 Local Gateway Route Table.
        """
        return pulumi.get(self, "local_gateway_route_table_id")

    @property
    @pulumi.getter(name="localGatewayVirtualInterfaceGroupId")
    def local_gateway_virtual_interface_group_id(self) -> pulumi.Output[str]:
        """
        Identifier of EC2 Local Gateway Virtual Interface Group.
        """
        return pulumi.get(self, "local_gateway_virtual_interface_group_id")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

