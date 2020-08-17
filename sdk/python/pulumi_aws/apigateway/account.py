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

__all__ = ['Account']


class Account(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cloudwatch_role_arn: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides a settings of an API Gateway Account. Settings is applied region-wide per `provider` block.

        > **Note:** As there is no API method for deleting account settings or resetting it to defaults, destroying this resource will keep your account settings intact

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        cloudwatch_role = aws.iam.Role("cloudwatchRole", assume_role_policy=\"\"\"{
          "Version": "2012-10-17",
          "Statement": [
            {
              "Sid": "",
              "Effect": "Allow",
              "Principal": {
                "Service": "apigateway.amazonaws.com"
              },
              "Action": "sts:AssumeRole"
            }
          ]
        }

        \"\"\")
        demo = aws.apigateway.Account("demo", cloudwatch_role_arn=cloudwatch_role.arn)
        cloudwatch_role_policy = aws.iam.RolePolicy("cloudwatchRolePolicy",
            policy=\"\"\"{
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Effect": "Allow",
                    "Action": [
                        "logs:CreateLogGroup",
                        "logs:CreateLogStream",
                        "logs:DescribeLogGroups",
                        "logs:DescribeLogStreams",
                        "logs:PutLogEvents",
                        "logs:GetLogEvents",
                        "logs:FilterLogEvents"
                    ],
                    "Resource": "*"
                }
            ]
        }

        \"\"\",
            role=cloudwatch_role.id)
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cloudwatch_role_arn: The ARN of an IAM role for CloudWatch (to allow logging & monitoring).
               See more [in AWS Docs](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-stage-settings.html#how-to-stage-settings-console).
               Logging & monitoring can be enabled/disabled and otherwise tuned on the API Gateway Stage level.
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

            __props__['cloudwatch_role_arn'] = cloudwatch_role_arn
            __props__['throttle_settings'] = None
        super(Account, __self__).__init__(
            'aws:apigateway/account:Account',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: str,
            opts: Optional[pulumi.ResourceOptions] = None,
            cloudwatch_role_arn: Optional[pulumi.Input[str]] = None,
            throttle_settings: Optional[pulumi.Input[pulumi.InputType['AccountThrottleSettingsArgs']]] = None) -> 'Account':
        """
        Get an existing Account resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cloudwatch_role_arn: The ARN of an IAM role for CloudWatch (to allow logging & monitoring).
               See more [in AWS Docs](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-stage-settings.html#how-to-stage-settings-console).
               Logging & monitoring can be enabled/disabled and otherwise tuned on the API Gateway Stage level.
        :param pulumi.Input[pulumi.InputType['AccountThrottleSettingsArgs']] throttle_settings: Account-Level throttle settings. See exported fields below.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["cloudwatch_role_arn"] = cloudwatch_role_arn
        __props__["throttle_settings"] = throttle_settings
        return Account(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="cloudwatchRoleArn")
    def cloudwatch_role_arn(self) -> Optional[str]:
        """
        The ARN of an IAM role for CloudWatch (to allow logging & monitoring).
        See more [in AWS Docs](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-stage-settings.html#how-to-stage-settings-console).
        Logging & monitoring can be enabled/disabled and otherwise tuned on the API Gateway Stage level.
        """
        ...

    @property
    @pulumi.getter(name="throttleSettings")
    def throttle_settings(self) -> 'outputs.AccountThrottleSettings':
        """
        Account-Level throttle settings. See exported fields below.
        """
        ...

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

