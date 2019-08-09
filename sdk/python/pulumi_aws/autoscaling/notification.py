# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from .. import utilities, tables

class Notification(pulumi.CustomResource):
    group_names: pulumi.Output[list]
    """
    A list of AutoScaling Group Names
    """
    notifications: pulumi.Output[list]
    """
    A list of Notification Types that trigger
    notifications. Acceptable values are documented [in the AWS documentation here][1]
    """
    topic_arn: pulumi.Output[str]
    """
    The Topic ARN for notifications to be sent through
    """
    def __init__(__self__, resource_name, opts=None, group_names=None, notifications=None, topic_arn=None, __props__=None, __name__=None, __opts__=None):
        """
        Provides an AutoScaling Group with Notification support, via SNS Topics. Each of
        the `notifications` map to a [Notification Configuration][2] inside Amazon Web
        Services, and are applied to each AutoScaling Group you supply.
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[list] group_names: A list of AutoScaling Group Names
        :param pulumi.Input[list] notifications: A list of Notification Types that trigger
               notifications. Acceptable values are documented [in the AWS documentation here][1]
        :param pulumi.Input[str] topic_arn: The Topic ARN for notifications to be sent through

        > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/autoscaling_notification.html.markdown.
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

            if group_names is None:
                raise TypeError("Missing required property 'group_names'")
            __props__['group_names'] = group_names
            if notifications is None:
                raise TypeError("Missing required property 'notifications'")
            __props__['notifications'] = notifications
            if topic_arn is None:
                raise TypeError("Missing required property 'topic_arn'")
            __props__['topic_arn'] = topic_arn
        super(Notification, __self__).__init__(
            'aws:autoscaling/notification:Notification',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, group_names=None, notifications=None, topic_arn=None):
        """
        Get an existing Notification resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.
        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[list] group_names: A list of AutoScaling Group Names
        :param pulumi.Input[list] notifications: A list of Notification Types that trigger
               notifications. Acceptable values are documented [in the AWS documentation here][1]
        :param pulumi.Input[str] topic_arn: The Topic ARN for notifications to be sent through

        > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/autoscaling_notification.html.markdown.
        """
        opts = pulumi.ResourceOptions(id=id) if opts is None else opts.merge(pulumi.ResourceOptions(id=id))

        __props__ = dict()
        __props__["group_names"] = group_names
        __props__["notifications"] = notifications
        __props__["topic_arn"] = topic_arn
        return Notification(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

