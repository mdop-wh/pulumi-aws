# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from .. import _utilities, _tables

__all__ = ['BucketPolicy']


class BucketPolicy(pulumi.CustomResource):
    bucket: pulumi.Output[str] = pulumi.property("bucket")
    """
    The name of the bucket to which to apply the policy.
    """

    policy: pulumi.Output[str] = pulumi.property("policy")
    """
    The text of the policy.
    """

    def __init__(__self__,
                 resource_name,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bucket: Optional[pulumi.Input[str]] = None,
                 policy: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Attaches a policy to an S3 bucket resource.

        ## Example Usage
        ### Basic Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        bucket = aws.s3.Bucket("bucket")
        bucket_policy = aws.s3.BucketPolicy("bucketPolicy",
            bucket=bucket.id,
            policy=\"\"\"{
          "Version": "2012-10-17",
          "Id": "MYBUCKETPOLICY",
          "Statement": [
            {
              "Sid": "IPAllow",
              "Effect": "Deny",
              "Principal": "*",
              "Action": "s3:*",
              "Resource": "arn:aws:s3:::my_tf_test_bucket/*",
              "Condition": {
                 "IpAddress": {"aws:SourceIp": "8.8.8.8/32"}
              }
            }
          ]
        }

        \"\"\")
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] bucket: The name of the bucket to which to apply the policy.
        :param pulumi.Input[str] policy: The text of the policy.
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

            if bucket is None:
                raise TypeError("Missing required property 'bucket'")
            __props__['bucket'] = bucket
            if policy is None:
                raise TypeError("Missing required property 'policy'")
            __props__['policy'] = policy
        super(BucketPolicy, __self__).__init__(
            'aws:s3/bucketPolicy:BucketPolicy',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: str,
            opts: Optional[pulumi.ResourceOptions] = None,
            bucket: Optional[pulumi.Input[str]] = None,
            policy: Optional[pulumi.Input[str]] = None) -> 'BucketPolicy':
        """
        Get an existing BucketPolicy resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] bucket: The name of the bucket to which to apply the policy.
        :param pulumi.Input[str] policy: The text of the policy.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["bucket"] = bucket
        __props__["policy"] = policy
        return BucketPolicy(resource_name, opts=opts, __props__=__props__)

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

