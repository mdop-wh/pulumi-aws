# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import _utilities, _tables


class Rule(pulumi.CustomResource):
    arn: pulumi.Output[str]
    """
    The ARN of the config rule
    """
    description: pulumi.Output[str]
    """
    Description of the rule
    """
    input_parameters: pulumi.Output[str]
    """
    A string in JSON format that is passed to the AWS Config rule Lambda function.
    """
    maximum_execution_frequency: pulumi.Output[str]
    """
    The frequency that you want AWS Config to run evaluations for a rule that
    is triggered periodically. If specified, requires `message_type` to be `ScheduledNotification`.
    """
    name: pulumi.Output[str]
    """
    The name of the rule
    """
    rule_id: pulumi.Output[str]
    """
    The ID of the config rule
    """
    scope: pulumi.Output[dict]
    """
    Scope defines which resources can trigger an evaluation for the rule as documented below.

      * `complianceResourceId` (`str`) - The IDs of the only AWS resource that you want to trigger an evaluation for the rule.
        If you specify a resource ID, you must specify one resource type for `compliance_resource_types`.
      * `complianceResourceTypes` (`list`) - A list of resource types of only those AWS resources that you want to trigger an
        evaluation for the rule. e.g. `AWS::EC2::Instance`. You can only specify one type if you also specify
        a resource ID for `compliance_resource_id`. See [relevant part of AWS Docs](http://docs.aws.amazon.com/config/latest/APIReference/API_ResourceIdentifier.html#config-Type-ResourceIdentifier-resourceType) for available types.
      * `tagKey` (`str`) - The tag key that is applied to only those AWS resources that you want you
        want to trigger an evaluation for the rule.
      * `tagValue` (`str`) - The tag value applied to only those AWS resources that you want to trigger an evaluation for the rule.
    """
    source: pulumi.Output[dict]
    """
    Source specifies the rule owner, the rule identifier, and the notifications that cause
    the function to evaluate your AWS resources as documented below.

      * `owner` (`str`) - Indicates whether AWS or the customer owns and manages the AWS Config rule. Valid values are `AWS` or `CUSTOM_LAMBDA`. For more information about managed rules, see the [AWS Config Managed Rules documentation](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_use-managed-rules.html). For more information about custom rules, see the [AWS Config Custom Rules documentation](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_develop-rules.html). Custom Lambda Functions require permissions to allow the AWS Config service to invoke them, e.g. via the `lambda.Permission` resource.
      * `sourceDetails` (`list`) - Provides the source and type of the event that causes AWS Config to evaluate your AWS resources. Only valid if `owner` is `CUSTOM_LAMBDA`.
        * `eventSource` (`str`) - The source of the event, such as an AWS service, that triggers AWS Config
          to evaluate your AWS resources. This defaults to `aws.config` and is the only valid value.
        * `maximum_execution_frequency` (`str`) - The frequency that you want AWS Config to run evaluations for a rule that
          is triggered periodically. If specified, requires `message_type` to be `ScheduledNotification`.
        * `messageType` (`str`) - The type of notification that triggers AWS Config to run an evaluation for a rule. You can specify the following notification types:

      * `sourceIdentifier` (`str`) - For AWS Config managed rules, a predefined identifier, e.g `IAM_PASSWORD_POLICY`. For custom Lambda rules, the identifier is the ARN of the Lambda Function, such as `arn:aws:lambda:us-east-1:123456789012:function:custom_rule_name` or the `arn` attribute of the `lambda.Function` resource.
    """
    tags: pulumi.Output[dict]
    """
    A map of tags to assign to the resource.
    """
    def __init__(__self__, resource_name, opts=None, description=None, input_parameters=None, maximum_execution_frequency=None, name=None, scope=None, source=None, tags=None, __props__=None, __name__=None, __opts__=None):
        """
        Provides an AWS Config Rule.

        > **Note:** Config Rule requires an existing `Configuration Recorder` to be present. Use of `depends_on` is recommended (as shown below) to avoid race conditions.

        ## Example Usage
        ### AWS Managed Rules

        AWS managed rules can be used by setting the source owner to `AWS` and the source identifier to the name of the managed rule. More information about AWS managed rules can be found in the [AWS Config Developer Guide](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_use-managed-rules.html).

        ```python
        import pulumi
        import pulumi_aws as aws

        role = aws.iam.Role("role", assume_role_policy=\"\"\"{
          "Version": "2012-10-17",
          "Statement": [
            {
              "Action": "sts:AssumeRole",
              "Principal": {
                "Service": "config.amazonaws.com"
              },
              "Effect": "Allow",
              "Sid": ""
            }
          ]
        }
        \"\"\")
        foo = aws.cfg.Recorder("foo", role_arn=role.arn)
        rule = aws.cfg.Rule("rule", source={
            "owner": "AWS",
            "sourceIdentifier": "S3_BUCKET_VERSIONING_ENABLED",
        },
        opts=ResourceOptions(depends_on=[foo]))
        role_policy = aws.iam.RolePolicy("rolePolicy",
            role=role.id,
            policy=\"\"\"{
          "Version": "2012-10-17",
          "Statement": [
          	{
          		"Action": "config:Put*",
          		"Effect": "Allow",
          		"Resource": "*"

          	}
          ]
        }
        \"\"\")
        ```
        ### Custom Rules

        Custom rules can be used by setting the source owner to `CUSTOM_LAMBDA` and the source identifier to the Amazon Resource Name (ARN) of the Lambda Function. The AWS Config service must have permissions to invoke the Lambda Function, e.g. via the `lambda.Permission` resource. More information about custom rules can be found in the [AWS Config Developer Guide](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_develop-rules.html).

        ```python
        import pulumi
        import pulumi_aws as aws

        example_recorder = aws.cfg.Recorder("exampleRecorder")
        # ... other configuration ...
        example_function = aws.lambda_.Function("exampleFunction")
        # ... other configuration ...
        example_permission = aws.lambda_.Permission("examplePermission",
            action="lambda:InvokeFunction",
            function=example_function.arn,
            principal="config.amazonaws.com")
        # ... other configuration ...
        example_rule = aws.cfg.Rule("exampleRule", source={
            "owner": "CUSTOM_LAMBDA",
            "sourceIdentifier": example_function.arn,
        },
        opts=ResourceOptions(depends_on=[
                example_recorder,
                example_permission,
            ]))
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: Description of the rule
        :param pulumi.Input[str] input_parameters: A string in JSON format that is passed to the AWS Config rule Lambda function.
        :param pulumi.Input[str] maximum_execution_frequency: The frequency that you want AWS Config to run evaluations for a rule that
               is triggered periodically. If specified, requires `message_type` to be `ScheduledNotification`.
        :param pulumi.Input[str] name: The name of the rule
        :param pulumi.Input[dict] scope: Scope defines which resources can trigger an evaluation for the rule as documented below.
        :param pulumi.Input[dict] source: Source specifies the rule owner, the rule identifier, and the notifications that cause
               the function to evaluate your AWS resources as documented below.
        :param pulumi.Input[dict] tags: A map of tags to assign to the resource.

        The **scope** object supports the following:

          * `complianceResourceId` (`pulumi.Input[str]`) - The IDs of the only AWS resource that you want to trigger an evaluation for the rule.
            If you specify a resource ID, you must specify one resource type for `compliance_resource_types`.
          * `complianceResourceTypes` (`pulumi.Input[list]`) - A list of resource types of only those AWS resources that you want to trigger an
            evaluation for the rule. e.g. `AWS::EC2::Instance`. You can only specify one type if you also specify
            a resource ID for `compliance_resource_id`. See [relevant part of AWS Docs](http://docs.aws.amazon.com/config/latest/APIReference/API_ResourceIdentifier.html#config-Type-ResourceIdentifier-resourceType) for available types.
          * `tagKey` (`pulumi.Input[str]`) - The tag key that is applied to only those AWS resources that you want you
            want to trigger an evaluation for the rule.
          * `tagValue` (`pulumi.Input[str]`) - The tag value applied to only those AWS resources that you want to trigger an evaluation for the rule.

        The **source** object supports the following:

          * `owner` (`pulumi.Input[str]`) - Indicates whether AWS or the customer owns and manages the AWS Config rule. Valid values are `AWS` or `CUSTOM_LAMBDA`. For more information about managed rules, see the [AWS Config Managed Rules documentation](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_use-managed-rules.html). For more information about custom rules, see the [AWS Config Custom Rules documentation](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_develop-rules.html). Custom Lambda Functions require permissions to allow the AWS Config service to invoke them, e.g. via the `lambda.Permission` resource.
          * `sourceDetails` (`pulumi.Input[list]`) - Provides the source and type of the event that causes AWS Config to evaluate your AWS resources. Only valid if `owner` is `CUSTOM_LAMBDA`.
            * `eventSource` (`pulumi.Input[str]`) - The source of the event, such as an AWS service, that triggers AWS Config
              to evaluate your AWS resources. This defaults to `aws.config` and is the only valid value.
            * `maximum_execution_frequency` (`pulumi.Input[str]`) - The frequency that you want AWS Config to run evaluations for a rule that
              is triggered periodically. If specified, requires `message_type` to be `ScheduledNotification`.
            * `messageType` (`pulumi.Input[str]`) - The type of notification that triggers AWS Config to run an evaluation for a rule. You can specify the following notification types:

          * `sourceIdentifier` (`pulumi.Input[str]`) - For AWS Config managed rules, a predefined identifier, e.g `IAM_PASSWORD_POLICY`. For custom Lambda rules, the identifier is the ARN of the Lambda Function, such as `arn:aws:lambda:us-east-1:123456789012:function:custom_rule_name` or the `arn` attribute of the `lambda.Function` resource.
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
            __props__['input_parameters'] = input_parameters
            __props__['maximum_execution_frequency'] = maximum_execution_frequency
            __props__['name'] = name
            __props__['scope'] = scope
            if source is None:
                raise TypeError("Missing required property 'source'")
            __props__['source'] = source
            __props__['tags'] = tags
            __props__['arn'] = None
            __props__['rule_id'] = None
        super(Rule, __self__).__init__(
            'aws:cfg/rule:Rule',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, arn=None, description=None, input_parameters=None, maximum_execution_frequency=None, name=None, rule_id=None, scope=None, source=None, tags=None):
        """
        Get an existing Rule resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] arn: The ARN of the config rule
        :param pulumi.Input[str] description: Description of the rule
        :param pulumi.Input[str] input_parameters: A string in JSON format that is passed to the AWS Config rule Lambda function.
        :param pulumi.Input[str] maximum_execution_frequency: The frequency that you want AWS Config to run evaluations for a rule that
               is triggered periodically. If specified, requires `message_type` to be `ScheduledNotification`.
        :param pulumi.Input[str] name: The name of the rule
        :param pulumi.Input[str] rule_id: The ID of the config rule
        :param pulumi.Input[dict] scope: Scope defines which resources can trigger an evaluation for the rule as documented below.
        :param pulumi.Input[dict] source: Source specifies the rule owner, the rule identifier, and the notifications that cause
               the function to evaluate your AWS resources as documented below.
        :param pulumi.Input[dict] tags: A map of tags to assign to the resource.

        The **scope** object supports the following:

          * `complianceResourceId` (`pulumi.Input[str]`) - The IDs of the only AWS resource that you want to trigger an evaluation for the rule.
            If you specify a resource ID, you must specify one resource type for `compliance_resource_types`.
          * `complianceResourceTypes` (`pulumi.Input[list]`) - A list of resource types of only those AWS resources that you want to trigger an
            evaluation for the rule. e.g. `AWS::EC2::Instance`. You can only specify one type if you also specify
            a resource ID for `compliance_resource_id`. See [relevant part of AWS Docs](http://docs.aws.amazon.com/config/latest/APIReference/API_ResourceIdentifier.html#config-Type-ResourceIdentifier-resourceType) for available types.
          * `tagKey` (`pulumi.Input[str]`) - The tag key that is applied to only those AWS resources that you want you
            want to trigger an evaluation for the rule.
          * `tagValue` (`pulumi.Input[str]`) - The tag value applied to only those AWS resources that you want to trigger an evaluation for the rule.

        The **source** object supports the following:

          * `owner` (`pulumi.Input[str]`) - Indicates whether AWS or the customer owns and manages the AWS Config rule. Valid values are `AWS` or `CUSTOM_LAMBDA`. For more information about managed rules, see the [AWS Config Managed Rules documentation](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_use-managed-rules.html). For more information about custom rules, see the [AWS Config Custom Rules documentation](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_develop-rules.html). Custom Lambda Functions require permissions to allow the AWS Config service to invoke them, e.g. via the `lambda.Permission` resource.
          * `sourceDetails` (`pulumi.Input[list]`) - Provides the source and type of the event that causes AWS Config to evaluate your AWS resources. Only valid if `owner` is `CUSTOM_LAMBDA`.
            * `eventSource` (`pulumi.Input[str]`) - The source of the event, such as an AWS service, that triggers AWS Config
              to evaluate your AWS resources. This defaults to `aws.config` and is the only valid value.
            * `maximum_execution_frequency` (`pulumi.Input[str]`) - The frequency that you want AWS Config to run evaluations for a rule that
              is triggered periodically. If specified, requires `message_type` to be `ScheduledNotification`.
            * `messageType` (`pulumi.Input[str]`) - The type of notification that triggers AWS Config to run an evaluation for a rule. You can specify the following notification types:

          * `sourceIdentifier` (`pulumi.Input[str]`) - For AWS Config managed rules, a predefined identifier, e.g `IAM_PASSWORD_POLICY`. For custom Lambda rules, the identifier is the ARN of the Lambda Function, such as `arn:aws:lambda:us-east-1:123456789012:function:custom_rule_name` or the `arn` attribute of the `lambda.Function` resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["arn"] = arn
        __props__["description"] = description
        __props__["input_parameters"] = input_parameters
        __props__["maximum_execution_frequency"] = maximum_execution_frequency
        __props__["name"] = name
        __props__["rule_id"] = rule_id
        __props__["scope"] = scope
        __props__["source"] = source
        __props__["tags"] = tags
        return Rule(resource_name, opts=opts, __props__=__props__)

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop
