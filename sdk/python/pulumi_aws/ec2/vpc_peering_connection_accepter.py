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

__all__ = ['VpcPeeringConnectionAccepter']


class VpcPeeringConnectionAccepter(pulumi.CustomResource):
    accept_status: pulumi.Output[str] = pulumi.property("acceptStatus")
    """
    The status of the VPC Peering Connection request.
    """

    accepter: pulumi.Output['outputs.VpcPeeringConnectionAccepterAccepter'] = pulumi.property("accepter")
    """
    A configuration block that describes [VPC Peering Connection]
    (https://docs.aws.amazon.com/vpc/latest/peering/what-is-vpc-peering.html) options set for the accepter VPC.
    """

    auto_accept: pulumi.Output[Optional[bool]] = pulumi.property("autoAccept")
    """
    Whether or not to accept the peering request. Defaults to `false`.
    """

    peer_owner_id: pulumi.Output[str] = pulumi.property("peerOwnerId")
    """
    The AWS account ID of the owner of the requester VPC.
    """

    peer_region: pulumi.Output[str] = pulumi.property("peerRegion")
    """
    The region of the accepter VPC.
    """

    peer_vpc_id: pulumi.Output[str] = pulumi.property("peerVpcId")
    """
    The ID of the requester VPC.
    """

    requester: pulumi.Output['outputs.VpcPeeringConnectionAccepterRequester'] = pulumi.property("requester")
    """
    A configuration block that describes [VPC Peering Connection]
    (https://docs.aws.amazon.com/vpc/latest/peering/what-is-vpc-peering.html) options set for the requester VPC.
    """

    tags: pulumi.Output[Optional[Mapping[str, str]]] = pulumi.property("tags")
    """
    A map of tags to assign to the resource.
    """

    vpc_id: pulumi.Output[str] = pulumi.property("vpcId")
    """
    The ID of the accepter VPC.
    """

    vpc_peering_connection_id: pulumi.Output[str] = pulumi.property("vpcPeeringConnectionId")
    """
    The VPC Peering Connection ID to manage.
    """

    def __init__(__self__,
                 resource_name,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 accepter: Optional[pulumi.Input[pulumi.InputType['VpcPeeringConnectionAccepterAccepterArgs']]] = None,
                 auto_accept: Optional[pulumi.Input[bool]] = None,
                 requester: Optional[pulumi.Input[pulumi.InputType['VpcPeeringConnectionAccepterRequesterArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 vpc_peering_connection_id: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides a resource to manage the accepter's side of a VPC Peering Connection.

        When a cross-account (requester's AWS account differs from the accepter's AWS account) or an inter-region
        VPC Peering Connection is created, a VPC Peering Connection resource is automatically created in the
        accepter's account.
        The requester can use the `ec2.VpcPeeringConnection` resource to manage its side of the connection
        and the accepter can use the `ec2.VpcPeeringConnectionAccepter` resource to "adopt" its side of the
        connection into management.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws
        import pulumi_pulumi as pulumi

        peer = pulumi.providers.Aws("peer", region="us-west-2")
        main = aws.ec2.Vpc("main", cidr_block="10.0.0.0/16")
        peer_vpc = aws.ec2.Vpc("peerVpc", cidr_block="10.1.0.0/16",
        opts=ResourceOptions(provider="aws.peer"))
        peer_caller_identity = aws.get_caller_identity()
        # Requester's side of the connection.
        peer_vpc_peering_connection = aws.ec2.VpcPeeringConnection("peerVpcPeeringConnection",
            auto_accept=False,
            peer_owner_id=peer_caller_identity.account_id,
            peer_region="us-west-2",
            peer_vpc_id=peer_vpc.id,
            tags={
                "Side": "Requester",
            },
            vpc_id=main.id)
        # Accepter's side of the connection.
        peer_vpc_peering_connection_accepter = aws.ec2.VpcPeeringConnectionAccepter("peerVpcPeeringConnectionAccepter",
            auto_accept=True,
            tags={
                "Side": "Accepter",
            },
            vpc_peering_connection_id=peer_vpc_peering_connection.id,
            opts=ResourceOptions(provider="aws.peer"))
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['VpcPeeringConnectionAccepterAccepterArgs']] accepter: A configuration block that describes [VPC Peering Connection]
               (https://docs.aws.amazon.com/vpc/latest/peering/what-is-vpc-peering.html) options set for the accepter VPC.
        :param pulumi.Input[bool] auto_accept: Whether or not to accept the peering request. Defaults to `false`.
        :param pulumi.Input[pulumi.InputType['VpcPeeringConnectionAccepterRequesterArgs']] requester: A configuration block that describes [VPC Peering Connection]
               (https://docs.aws.amazon.com/vpc/latest/peering/what-is-vpc-peering.html) options set for the requester VPC.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the resource.
        :param pulumi.Input[str] vpc_peering_connection_id: The VPC Peering Connection ID to manage.
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

            __props__['accepter'] = accepter
            __props__['auto_accept'] = auto_accept
            __props__['requester'] = requester
            __props__['tags'] = tags
            if vpc_peering_connection_id is None:
                raise TypeError("Missing required property 'vpc_peering_connection_id'")
            __props__['vpc_peering_connection_id'] = vpc_peering_connection_id
            __props__['accept_status'] = None
            __props__['peer_owner_id'] = None
            __props__['peer_region'] = None
            __props__['peer_vpc_id'] = None
            __props__['vpc_id'] = None
        super(VpcPeeringConnectionAccepter, __self__).__init__(
            'aws:ec2/vpcPeeringConnectionAccepter:VpcPeeringConnectionAccepter',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: str,
            opts: Optional[pulumi.ResourceOptions] = None,
            accept_status: Optional[pulumi.Input[str]] = None,
            accepter: Optional[pulumi.Input[pulumi.InputType['VpcPeeringConnectionAccepterAccepterArgs']]] = None,
            auto_accept: Optional[pulumi.Input[bool]] = None,
            peer_owner_id: Optional[pulumi.Input[str]] = None,
            peer_region: Optional[pulumi.Input[str]] = None,
            peer_vpc_id: Optional[pulumi.Input[str]] = None,
            requester: Optional[pulumi.Input[pulumi.InputType['VpcPeeringConnectionAccepterRequesterArgs']]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            vpc_id: Optional[pulumi.Input[str]] = None,
            vpc_peering_connection_id: Optional[pulumi.Input[str]] = None) -> 'VpcPeeringConnectionAccepter':
        """
        Get an existing VpcPeeringConnectionAccepter resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] accept_status: The status of the VPC Peering Connection request.
        :param pulumi.Input[pulumi.InputType['VpcPeeringConnectionAccepterAccepterArgs']] accepter: A configuration block that describes [VPC Peering Connection]
               (https://docs.aws.amazon.com/vpc/latest/peering/what-is-vpc-peering.html) options set for the accepter VPC.
        :param pulumi.Input[bool] auto_accept: Whether or not to accept the peering request. Defaults to `false`.
        :param pulumi.Input[str] peer_owner_id: The AWS account ID of the owner of the requester VPC.
        :param pulumi.Input[str] peer_region: The region of the accepter VPC.
        :param pulumi.Input[str] peer_vpc_id: The ID of the requester VPC.
        :param pulumi.Input[pulumi.InputType['VpcPeeringConnectionAccepterRequesterArgs']] requester: A configuration block that describes [VPC Peering Connection]
               (https://docs.aws.amazon.com/vpc/latest/peering/what-is-vpc-peering.html) options set for the requester VPC.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the resource.
        :param pulumi.Input[str] vpc_id: The ID of the accepter VPC.
        :param pulumi.Input[str] vpc_peering_connection_id: The VPC Peering Connection ID to manage.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["accept_status"] = accept_status
        __props__["accepter"] = accepter
        __props__["auto_accept"] = auto_accept
        __props__["peer_owner_id"] = peer_owner_id
        __props__["peer_region"] = peer_region
        __props__["peer_vpc_id"] = peer_vpc_id
        __props__["requester"] = requester
        __props__["tags"] = tags
        __props__["vpc_id"] = vpc_id
        __props__["vpc_peering_connection_id"] = vpc_peering_connection_id
        return VpcPeeringConnectionAccepter(resource_name, opts=opts, __props__=__props__)

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

