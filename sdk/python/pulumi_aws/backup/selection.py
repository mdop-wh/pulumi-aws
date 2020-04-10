# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class Selection(pulumi.CustomResource):
    iam_role_arn: pulumi.Output[str]
    """
    The ARN of the IAM role that AWS Backup uses to authenticate when restoring and backing up the target resource. See the [AWS Backup Developer Guide](https://docs.aws.amazon.com/aws-backup/latest/devguide/access-control.html#managed-policies) for additional information about using AWS managed policies or creating custom policies attached to the IAM role.
    """
    name: pulumi.Output[str]
    """
    The display name of a resource selection document.
    """
    plan_id: pulumi.Output[str]
    """
    The backup plan ID to be associated with the selection of resources.
    """
    resources: pulumi.Output[list]
    """
    An array of strings that either contain Amazon Resource Names (ARNs) or match patterns of resources to assign to a backup plan..
    """
    selection_tags: pulumi.Output[list]
    """
    Tag-based conditions used to specify a set of resources to assign to a backup plan.

      * `key` (`str`) - The key in a key-value pair.
      * `type` (`str`) - An operation, such as `StringEquals`, that is applied to a key-value pair used to filter resources in a selection.
      * `value` (`str`) - The value in a key-value pair.
    """
    def __init__(__self__, resource_name, opts=None, iam_role_arn=None, name=None, plan_id=None, resources=None, selection_tags=None, __props__=None, __name__=None, __opts__=None):
        """
        Manages selection conditions for AWS Backup plan resources.



        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] iam_role_arn: The ARN of the IAM role that AWS Backup uses to authenticate when restoring and backing up the target resource. See the [AWS Backup Developer Guide](https://docs.aws.amazon.com/aws-backup/latest/devguide/access-control.html#managed-policies) for additional information about using AWS managed policies or creating custom policies attached to the IAM role.
        :param pulumi.Input[str] name: The display name of a resource selection document.
        :param pulumi.Input[str] plan_id: The backup plan ID to be associated with the selection of resources.
        :param pulumi.Input[list] resources: An array of strings that either contain Amazon Resource Names (ARNs) or match patterns of resources to assign to a backup plan..
        :param pulumi.Input[list] selection_tags: Tag-based conditions used to specify a set of resources to assign to a backup plan.

        The **selection_tags** object supports the following:

          * `key` (`pulumi.Input[str]`) - The key in a key-value pair.
          * `type` (`pulumi.Input[str]`) - An operation, such as `StringEquals`, that is applied to a key-value pair used to filter resources in a selection.
          * `value` (`pulumi.Input[str]`) - The value in a key-value pair.
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

            if iam_role_arn is None:
                raise TypeError("Missing required property 'iam_role_arn'")
            __props__['iam_role_arn'] = iam_role_arn
            __props__['name'] = name
            if plan_id is None:
                raise TypeError("Missing required property 'plan_id'")
            __props__['plan_id'] = plan_id
            __props__['resources'] = resources
            __props__['selection_tags'] = selection_tags
        super(Selection, __self__).__init__(
            'aws:backup/selection:Selection',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, iam_role_arn=None, name=None, plan_id=None, resources=None, selection_tags=None):
        """
        Get an existing Selection resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] iam_role_arn: The ARN of the IAM role that AWS Backup uses to authenticate when restoring and backing up the target resource. See the [AWS Backup Developer Guide](https://docs.aws.amazon.com/aws-backup/latest/devguide/access-control.html#managed-policies) for additional information about using AWS managed policies or creating custom policies attached to the IAM role.
        :param pulumi.Input[str] name: The display name of a resource selection document.
        :param pulumi.Input[str] plan_id: The backup plan ID to be associated with the selection of resources.
        :param pulumi.Input[list] resources: An array of strings that either contain Amazon Resource Names (ARNs) or match patterns of resources to assign to a backup plan..
        :param pulumi.Input[list] selection_tags: Tag-based conditions used to specify a set of resources to assign to a backup plan.

        The **selection_tags** object supports the following:

          * `key` (`pulumi.Input[str]`) - The key in a key-value pair.
          * `type` (`pulumi.Input[str]`) - An operation, such as `StringEquals`, that is applied to a key-value pair used to filter resources in a selection.
          * `value` (`pulumi.Input[str]`) - The value in a key-value pair.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["iam_role_arn"] = iam_role_arn
        __props__["name"] = name
        __props__["plan_id"] = plan_id
        __props__["resources"] = resources
        __props__["selection_tags"] = selection_tags
        return Selection(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

