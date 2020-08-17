# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from .. import _utilities, _tables

__all__ = ['Attachment']


class Attachment(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 elb: Optional[pulumi.Input[str]] = None,
                 instance: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Attaches an EC2 instance to an Elastic Load Balancer (ELB). For attaching resources with Application Load Balancer (ALB) or Network Load Balancer (NLB), see the `lb.TargetGroupAttachment` resource.

        > **NOTE on ELB Instances and ELB Attachments:** This provider currently provides
        both a standalone ELB Attachment resource (describing an instance attached to
        an ELB), and an Elastic Load Balancer resource with
        `instances` defined in-line. At this time you cannot use an ELB with in-line
        instances in conjunction with an ELB Attachment resource. Doing so will cause a
        conflict and will overwrite attachments.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        # Create a new load balancer attachment
        baz = aws.elb.Attachment("baz",
            elb=aws_elb["bar"]["id"],
            instance=aws_instance["foo"]["id"])
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] elb: The name of the ELB.
        :param pulumi.Input[str] instance: Instance ID to place in the ELB pool.
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

            if elb is None:
                raise TypeError("Missing required property 'elb'")
            __props__['elb'] = elb
            if instance is None:
                raise TypeError("Missing required property 'instance'")
            __props__['instance'] = instance
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="aws:elasticloadbalancing/attachment:Attachment")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Attachment, __self__).__init__(
            'aws:elb/attachment:Attachment',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: str,
            opts: Optional[pulumi.ResourceOptions] = None,
            elb: Optional[pulumi.Input[str]] = None,
            instance: Optional[pulumi.Input[str]] = None) -> 'Attachment':
        """
        Get an existing Attachment resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] elb: The name of the ELB.
        :param pulumi.Input[str] instance: Instance ID to place in the ELB pool.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["elb"] = elb
        __props__["instance"] = instance
        return Attachment(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def elb(self) -> str:
        """
        The name of the ELB.
        """
        ...

    @property
    @pulumi.getter
    def instance(self) -> str:
        """
        Instance ID to place in the ELB pool.
        """
        ...

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

