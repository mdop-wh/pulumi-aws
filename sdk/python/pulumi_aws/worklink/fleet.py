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

__all__ = ['Fleet']


class Fleet(pulumi.CustomResource):
    arn: pulumi.Output[str] = pulumi.property("arn")
    """
    The ARN of the created WorkLink Fleet.
    """

    audit_stream_arn: pulumi.Output[Optional[str]] = pulumi.property("auditStreamArn")
    """
    The ARN of the Amazon Kinesis data stream that receives the audit events.
    """

    company_code: pulumi.Output[str] = pulumi.property("companyCode")
    """
    The identifier used by users to sign in to the Amazon WorkLink app.
    """

    created_time: pulumi.Output[str] = pulumi.property("createdTime")
    """
    The time that the fleet was created.
    """

    device_ca_certificate: pulumi.Output[Optional[str]] = pulumi.property("deviceCaCertificate")
    """
    The certificate chain, including intermediate certificates and the root certificate authority certificate used to issue device certificates.
    """

    display_name: pulumi.Output[Optional[str]] = pulumi.property("displayName")
    """
    The name of the fleet.
    """

    identity_provider: pulumi.Output[Optional['outputs.FleetIdentityProvider']] = pulumi.property("identityProvider")
    """
    Provide this to allow manage the identity provider configuration for the fleet. Fields documented below.
    """

    last_updated_time: pulumi.Output[str] = pulumi.property("lastUpdatedTime")
    """
    The time that the fleet was last updated.
    """

    name: pulumi.Output[str] = pulumi.property("name")
    """
    A region-unique name for the AMI.
    """

    network: pulumi.Output[Optional['outputs.FleetNetwork']] = pulumi.property("network")
    """
    Provide this to allow manage the company network configuration for the fleet. Fields documented below.
    """

    optimize_for_end_user_location: pulumi.Output[Optional[bool]] = pulumi.property("optimizeForEndUserLocation")
    """
    The option to optimize for better performance by routing traffic through the closest AWS Region to users, which may be outside of your home Region. Defaults to `true`.
    """

    def __init__(__self__,
                 resource_name,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 audit_stream_arn: Optional[pulumi.Input[str]] = None,
                 device_ca_certificate: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 identity_provider: Optional[pulumi.Input[pulumi.InputType['FleetIdentityProviderArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 network: Optional[pulumi.Input[pulumi.InputType['FleetNetworkArgs']]] = None,
                 optimize_for_end_user_location: Optional[pulumi.Input[bool]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        ## Example Usage

        Basic usage:

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.worklink.Fleet("example")
        ```

        Network Configuration Usage:

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.worklink.Fleet("example", network={
            "security_group_ids": [aws_security_group["test"]["id"]],
            "subnet_ids": [[__item["id"] for __item in aws_subnet["test"]]],
            "vpc_id": aws_vpc["test"]["id"],
        })
        ```

        Identity Provider Configuration Usage:

        ```python
        import pulumi
        import pulumi_aws as aws

        test = aws.worklink.Fleet("test", identity_provider={
            "samlMetadata": (lambda path: open(path).read())("saml-metadata.xml"),
            "type": "SAML",
        })
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] audit_stream_arn: The ARN of the Amazon Kinesis data stream that receives the audit events.
        :param pulumi.Input[str] device_ca_certificate: The certificate chain, including intermediate certificates and the root certificate authority certificate used to issue device certificates.
        :param pulumi.Input[str] display_name: The name of the fleet.
        :param pulumi.Input[pulumi.InputType['FleetIdentityProviderArgs']] identity_provider: Provide this to allow manage the identity provider configuration for the fleet. Fields documented below.
        :param pulumi.Input[str] name: A region-unique name for the AMI.
        :param pulumi.Input[pulumi.InputType['FleetNetworkArgs']] network: Provide this to allow manage the company network configuration for the fleet. Fields documented below.
        :param pulumi.Input[bool] optimize_for_end_user_location: The option to optimize for better performance by routing traffic through the closest AWS Region to users, which may be outside of your home Region. Defaults to `true`.
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

            __props__['audit_stream_arn'] = audit_stream_arn
            __props__['device_ca_certificate'] = device_ca_certificate
            __props__['display_name'] = display_name
            __props__['identity_provider'] = identity_provider
            __props__['name'] = name
            __props__['network'] = network
            __props__['optimize_for_end_user_location'] = optimize_for_end_user_location
            __props__['arn'] = None
            __props__['company_code'] = None
            __props__['created_time'] = None
            __props__['last_updated_time'] = None
        super(Fleet, __self__).__init__(
            'aws:worklink/fleet:Fleet',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: str,
            opts: Optional[pulumi.ResourceOptions] = None,
            arn: Optional[pulumi.Input[str]] = None,
            audit_stream_arn: Optional[pulumi.Input[str]] = None,
            company_code: Optional[pulumi.Input[str]] = None,
            created_time: Optional[pulumi.Input[str]] = None,
            device_ca_certificate: Optional[pulumi.Input[str]] = None,
            display_name: Optional[pulumi.Input[str]] = None,
            identity_provider: Optional[pulumi.Input[pulumi.InputType['FleetIdentityProviderArgs']]] = None,
            last_updated_time: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            network: Optional[pulumi.Input[pulumi.InputType['FleetNetworkArgs']]] = None,
            optimize_for_end_user_location: Optional[pulumi.Input[bool]] = None) -> 'Fleet':
        """
        Get an existing Fleet resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] arn: The ARN of the created WorkLink Fleet.
        :param pulumi.Input[str] audit_stream_arn: The ARN of the Amazon Kinesis data stream that receives the audit events.
        :param pulumi.Input[str] company_code: The identifier used by users to sign in to the Amazon WorkLink app.
        :param pulumi.Input[str] created_time: The time that the fleet was created.
        :param pulumi.Input[str] device_ca_certificate: The certificate chain, including intermediate certificates and the root certificate authority certificate used to issue device certificates.
        :param pulumi.Input[str] display_name: The name of the fleet.
        :param pulumi.Input[pulumi.InputType['FleetIdentityProviderArgs']] identity_provider: Provide this to allow manage the identity provider configuration for the fleet. Fields documented below.
        :param pulumi.Input[str] last_updated_time: The time that the fleet was last updated.
        :param pulumi.Input[str] name: A region-unique name for the AMI.
        :param pulumi.Input[pulumi.InputType['FleetNetworkArgs']] network: Provide this to allow manage the company network configuration for the fleet. Fields documented below.
        :param pulumi.Input[bool] optimize_for_end_user_location: The option to optimize for better performance by routing traffic through the closest AWS Region to users, which may be outside of your home Region. Defaults to `true`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["arn"] = arn
        __props__["audit_stream_arn"] = audit_stream_arn
        __props__["company_code"] = company_code
        __props__["created_time"] = created_time
        __props__["device_ca_certificate"] = device_ca_certificate
        __props__["display_name"] = display_name
        __props__["identity_provider"] = identity_provider
        __props__["last_updated_time"] = last_updated_time
        __props__["name"] = name
        __props__["network"] = network
        __props__["optimize_for_end_user_location"] = optimize_for_end_user_location
        return Fleet(resource_name, opts=opts, __props__=__props__)

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

