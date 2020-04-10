# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class RouteTableAssociation(pulumi.CustomResource):
    gateway_id: pulumi.Output[str]
    """
    The gateway ID to create an association. Conflicts with `subnet_id`.
    """
    route_table_id: pulumi.Output[str]
    """
    The ID of the routing table to associate with.
    """
    subnet_id: pulumi.Output[str]
    """
    The subnet ID to create an association. Conflicts with `gateway_id`.
    """
    def __init__(__self__, resource_name, opts=None, gateway_id=None, route_table_id=None, subnet_id=None, __props__=None, __name__=None, __opts__=None):
        """
        Provides a resource to create an association between a route table and a subnet or a route table and an
        internet gateway or virtual private gateway.



        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] gateway_id: The gateway ID to create an association. Conflicts with `subnet_id`.
        :param pulumi.Input[str] route_table_id: The ID of the routing table to associate with.
        :param pulumi.Input[str] subnet_id: The subnet ID to create an association. Conflicts with `gateway_id`.
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
            opts.version = utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            __props__['gateway_id'] = gateway_id
            if route_table_id is None:
                raise TypeError("Missing required property 'route_table_id'")
            __props__['route_table_id'] = route_table_id
            __props__['subnet_id'] = subnet_id
        super(RouteTableAssociation, __self__).__init__(
            'aws:ec2/routeTableAssociation:RouteTableAssociation',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, gateway_id=None, route_table_id=None, subnet_id=None):
        """
        Get an existing RouteTableAssociation resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] gateway_id: The gateway ID to create an association. Conflicts with `subnet_id`.
        :param pulumi.Input[str] route_table_id: The ID of the routing table to associate with.
        :param pulumi.Input[str] subnet_id: The subnet ID to create an association. Conflicts with `gateway_id`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["gateway_id"] = gateway_id
        __props__["route_table_id"] = route_table_id
        __props__["subnet_id"] = subnet_id
        return RouteTableAssociation(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

