# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import _utilities, _tables


class VpcEndpoint(pulumi.CustomResource):
    arn: pulumi.Output[str]
    """
    The Amazon Resource Name (ARN) of the VPC endpoint.
    """
    auto_accept: pulumi.Output[bool]
    """
    Accept the VPC endpoint (the VPC endpoint and service need to be in the same AWS account).
    """
    cidr_blocks: pulumi.Output[list]
    """
    The list of CIDR blocks for the exposed AWS service. Applicable for endpoints of type `Gateway`.
    """
    dns_entries: pulumi.Output[list]
    """
    The DNS entries for the VPC Endpoint. Applicable for endpoints of type `Interface`. DNS blocks are documented below.

      * `dns_name` (`str`) - The DNS name.
      * `hosted_zone_id` (`str`) - The ID of the private hosted zone.
    """
    network_interface_ids: pulumi.Output[list]
    """
    One or more network interfaces for the VPC Endpoint. Applicable for endpoints of type `Interface`.
    """
    owner_id: pulumi.Output[str]
    """
    The ID of the AWS account that owns the VPC endpoint.
    """
    policy: pulumi.Output[str]
    """
    A policy to attach to the endpoint that controls access to the service. Defaults to full access. All `Gateway` and some `Interface` endpoints support policies - see the [relevant AWS documentation](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-endpoints-access.html) for more details.
    """
    prefix_list_id: pulumi.Output[str]
    """
    The prefix list ID of the exposed AWS service. Applicable for endpoints of type `Gateway`.
    """
    private_dns_enabled: pulumi.Output[bool]
    """
    Whether or not to associate a private hosted zone with the specified VPC. Applicable for endpoints of type `Interface`.
    Defaults to `false`.
    """
    requester_managed: pulumi.Output[bool]
    """
    Whether or not the VPC Endpoint is being managed by its service - `true` or `false`.
    """
    route_table_ids: pulumi.Output[list]
    """
    One or more route table IDs. Applicable for endpoints of type `Gateway`.
    """
    security_group_ids: pulumi.Output[list]
    """
    The ID of one or more security groups to associate with the network interface. Required for endpoints of type `Interface`.
    """
    service_name: pulumi.Output[str]
    """
    The service name. For AWS services the service name is usually in the form `com.amazonaws.<region>.<service>` (the SageMaker Notebook service is an exception to this rule, the service name is in the form `aws.sagemaker.<region>.notebook`).
    """
    state: pulumi.Output[str]
    """
    The state of the VPC endpoint.
    """
    subnet_ids: pulumi.Output[list]
    """
    The ID of one or more subnets in which to create a network interface for the endpoint. Applicable for endpoints of type `Interface`.
    """
    tags: pulumi.Output[dict]
    """
    A map of tags to assign to the resource.
    """
    vpc_endpoint_type: pulumi.Output[str]
    """
    The VPC endpoint type, `Gateway` or `Interface`. Defaults to `Gateway`.
    """
    vpc_id: pulumi.Output[str]
    """
    The ID of the VPC in which the endpoint will be used.
    """
    def __init__(__self__, resource_name, opts=None, auto_accept=None, policy=None, private_dns_enabled=None, route_table_ids=None, security_group_ids=None, service_name=None, subnet_ids=None, tags=None, vpc_endpoint_type=None, vpc_id=None, __props__=None, __name__=None, __opts__=None):
        """
        Provides a VPC Endpoint resource.

        > **NOTE on VPC Endpoints and VPC Endpoint Associations:** This provider provides both standalone VPC Endpoint Associations for
        Route Tables - (an association between a VPC endpoint and a single `route_table_id`) and
        Subnets - (an association between a VPC endpoint and a single `subnet_id`) and
        a VPC Endpoint resource with `route_table_ids` and `subnet_ids` attributes.
        Do not use the same resource ID in both a VPC Endpoint resource and a VPC Endpoint Association resource.
        Doing so will cause a conflict of associations and will overwrite the association.

        ## Example Usage
        ### Basic

        ```python
        import pulumi
        import pulumi_aws as aws

        s3 = aws.ec2.VpcEndpoint("s3",
            vpc_id=aws_vpc["main"]["id"],
            service_name="com.amazonaws.us-west-2.s3")
        ```
        ### Basic w/ Tags

        ```python
        import pulumi
        import pulumi_aws as aws

        s3 = aws.ec2.VpcEndpoint("s3",
            vpc_id=aws_vpc["main"]["id"],
            service_name="com.amazonaws.us-west-2.s3",
            tags={
                "Environment": "test",
            })
        ```
        ### Interface Endpoint Type

        ```python
        import pulumi
        import pulumi_aws as aws

        ec2 = aws.ec2.VpcEndpoint("ec2",
            vpc_id=aws_vpc["main"]["id"],
            service_name="com.amazonaws.us-west-2.ec2",
            vpc_endpoint_type="Interface",
            security_group_ids=[aws_security_group["sg1"]["id"]],
            private_dns_enabled=True)
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] auto_accept: Accept the VPC endpoint (the VPC endpoint and service need to be in the same AWS account).
        :param pulumi.Input[str] policy: A policy to attach to the endpoint that controls access to the service. Defaults to full access. All `Gateway` and some `Interface` endpoints support policies - see the [relevant AWS documentation](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-endpoints-access.html) for more details.
        :param pulumi.Input[bool] private_dns_enabled: Whether or not to associate a private hosted zone with the specified VPC. Applicable for endpoints of type `Interface`.
               Defaults to `false`.
        :param pulumi.Input[list] route_table_ids: One or more route table IDs. Applicable for endpoints of type `Gateway`.
        :param pulumi.Input[list] security_group_ids: The ID of one or more security groups to associate with the network interface. Required for endpoints of type `Interface`.
        :param pulumi.Input[str] service_name: The service name. For AWS services the service name is usually in the form `com.amazonaws.<region>.<service>` (the SageMaker Notebook service is an exception to this rule, the service name is in the form `aws.sagemaker.<region>.notebook`).
        :param pulumi.Input[list] subnet_ids: The ID of one or more subnets in which to create a network interface for the endpoint. Applicable for endpoints of type `Interface`.
        :param pulumi.Input[dict] tags: A map of tags to assign to the resource.
        :param pulumi.Input[str] vpc_endpoint_type: The VPC endpoint type, `Gateway` or `Interface`. Defaults to `Gateway`.
        :param pulumi.Input[str] vpc_id: The ID of the VPC in which the endpoint will be used.
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

            __props__['auto_accept'] = auto_accept
            __props__['policy'] = policy
            __props__['private_dns_enabled'] = private_dns_enabled
            __props__['route_table_ids'] = route_table_ids
            __props__['security_group_ids'] = security_group_ids
            if service_name is None:
                raise TypeError("Missing required property 'service_name'")
            __props__['service_name'] = service_name
            __props__['subnet_ids'] = subnet_ids
            __props__['tags'] = tags
            __props__['vpc_endpoint_type'] = vpc_endpoint_type
            if vpc_id is None:
                raise TypeError("Missing required property 'vpc_id'")
            __props__['vpc_id'] = vpc_id
            __props__['arn'] = None
            __props__['cidr_blocks'] = None
            __props__['dns_entries'] = None
            __props__['network_interface_ids'] = None
            __props__['owner_id'] = None
            __props__['prefix_list_id'] = None
            __props__['requester_managed'] = None
            __props__['state'] = None
        super(VpcEndpoint, __self__).__init__(
            'aws:ec2/vpcEndpoint:VpcEndpoint',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, arn=None, auto_accept=None, cidr_blocks=None, dns_entries=None, network_interface_ids=None, owner_id=None, policy=None, prefix_list_id=None, private_dns_enabled=None, requester_managed=None, route_table_ids=None, security_group_ids=None, service_name=None, state=None, subnet_ids=None, tags=None, vpc_endpoint_type=None, vpc_id=None):
        """
        Get an existing VpcEndpoint resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] arn: The Amazon Resource Name (ARN) of the VPC endpoint.
        :param pulumi.Input[bool] auto_accept: Accept the VPC endpoint (the VPC endpoint and service need to be in the same AWS account).
        :param pulumi.Input[list] cidr_blocks: The list of CIDR blocks for the exposed AWS service. Applicable for endpoints of type `Gateway`.
        :param pulumi.Input[list] dns_entries: The DNS entries for the VPC Endpoint. Applicable for endpoints of type `Interface`. DNS blocks are documented below.
        :param pulumi.Input[list] network_interface_ids: One or more network interfaces for the VPC Endpoint. Applicable for endpoints of type `Interface`.
        :param pulumi.Input[str] owner_id: The ID of the AWS account that owns the VPC endpoint.
        :param pulumi.Input[str] policy: A policy to attach to the endpoint that controls access to the service. Defaults to full access. All `Gateway` and some `Interface` endpoints support policies - see the [relevant AWS documentation](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-endpoints-access.html) for more details.
        :param pulumi.Input[str] prefix_list_id: The prefix list ID of the exposed AWS service. Applicable for endpoints of type `Gateway`.
        :param pulumi.Input[bool] private_dns_enabled: Whether or not to associate a private hosted zone with the specified VPC. Applicable for endpoints of type `Interface`.
               Defaults to `false`.
        :param pulumi.Input[bool] requester_managed: Whether or not the VPC Endpoint is being managed by its service - `true` or `false`.
        :param pulumi.Input[list] route_table_ids: One or more route table IDs. Applicable for endpoints of type `Gateway`.
        :param pulumi.Input[list] security_group_ids: The ID of one or more security groups to associate with the network interface. Required for endpoints of type `Interface`.
        :param pulumi.Input[str] service_name: The service name. For AWS services the service name is usually in the form `com.amazonaws.<region>.<service>` (the SageMaker Notebook service is an exception to this rule, the service name is in the form `aws.sagemaker.<region>.notebook`).
        :param pulumi.Input[str] state: The state of the VPC endpoint.
        :param pulumi.Input[list] subnet_ids: The ID of one or more subnets in which to create a network interface for the endpoint. Applicable for endpoints of type `Interface`.
        :param pulumi.Input[dict] tags: A map of tags to assign to the resource.
        :param pulumi.Input[str] vpc_endpoint_type: The VPC endpoint type, `Gateway` or `Interface`. Defaults to `Gateway`.
        :param pulumi.Input[str] vpc_id: The ID of the VPC in which the endpoint will be used.

        The **dns_entries** object supports the following:

          * `dns_name` (`pulumi.Input[str]`) - The DNS name.
          * `hosted_zone_id` (`pulumi.Input[str]`) - The ID of the private hosted zone.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["arn"] = arn
        __props__["auto_accept"] = auto_accept
        __props__["cidr_blocks"] = cidr_blocks
        __props__["dns_entries"] = dns_entries
        __props__["network_interface_ids"] = network_interface_ids
        __props__["owner_id"] = owner_id
        __props__["policy"] = policy
        __props__["prefix_list_id"] = prefix_list_id
        __props__["private_dns_enabled"] = private_dns_enabled
        __props__["requester_managed"] = requester_managed
        __props__["route_table_ids"] = route_table_ids
        __props__["security_group_ids"] = security_group_ids
        __props__["service_name"] = service_name
        __props__["state"] = state
        __props__["subnet_ids"] = subnet_ids
        __props__["tags"] = tags
        __props__["vpc_endpoint_type"] = vpc_endpoint_type
        __props__["vpc_id"] = vpc_id
        return VpcEndpoint(resource_name, opts=opts, __props__=__props__)

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop
