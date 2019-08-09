# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from .. import utilities, tables

class BucketPublicAccessBlock(pulumi.CustomResource):
    block_public_acls: pulumi.Output[bool]
    """
    Whether Amazon S3 should block public ACLs for this bucket. Defaults to `false`. Enabling this setting does not affect existing policies or ACLs. When set to `true` causes the following behavior:
    * PUT Bucket acl and PUT Object acl calls will fail if the specified ACL allows public access.
    * PUT Object calls will fail if the request includes an object ACL.
    """
    block_public_policy: pulumi.Output[bool]
    """
    Whether Amazon S3 should block public bucket policies for this bucket. Defaults to `false`. Enabling this setting does not affect the existing bucket policy. When set to `true` causes Amazon S3 to:
    * Reject calls to PUT Bucket policy if the specified bucket policy allows public access.
    """
    bucket: pulumi.Output[str]
    """
    S3 Bucket to which this Public Access Block configuration should be applied.
    """
    ignore_public_acls: pulumi.Output[bool]
    """
    Whether Amazon S3 should ignore public ACLs for this bucket. Defaults to `false`. Enabling this setting does not affect the persistence of any existing ACLs and doesn't prevent new public ACLs from being set. When set to `true` causes Amazon S3 to:
    * Ignore public ACLs on this bucket and any objects that it contains.
    """
    restrict_public_buckets: pulumi.Output[bool]
    """
    Whether Amazon S3 should restrict public bucket policies for this bucket. Defaults to `false`. Enabling this setting does not affect the previously stored bucket policy, except that public and cross-account access within the public bucket policy, including non-public delegation to specific accounts, is blocked. When set to `true`:
    * Only the bucket owner and AWS Services can access this buckets if it has a public policy.
    """
    def __init__(__self__, resource_name, opts=None, block_public_acls=None, block_public_policy=None, bucket=None, ignore_public_acls=None, restrict_public_buckets=None, __props__=None, __name__=None, __opts__=None):
        """
        Manages S3 bucket-level Public Access Block configuration. For more information about these settings, see the [AWS S3 Block Public Access documentation](https://docs.aws.amazon.com/AmazonS3/latest/dev/access-control-block-public-access.html).
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] block_public_acls: Whether Amazon S3 should block public ACLs for this bucket. Defaults to `false`. Enabling this setting does not affect existing policies or ACLs. When set to `true` causes the following behavior:
               * PUT Bucket acl and PUT Object acl calls will fail if the specified ACL allows public access.
               * PUT Object calls will fail if the request includes an object ACL.
        :param pulumi.Input[bool] block_public_policy: Whether Amazon S3 should block public bucket policies for this bucket. Defaults to `false`. Enabling this setting does not affect the existing bucket policy. When set to `true` causes Amazon S3 to:
               * Reject calls to PUT Bucket policy if the specified bucket policy allows public access.
        :param pulumi.Input[str] bucket: S3 Bucket to which this Public Access Block configuration should be applied.
        :param pulumi.Input[bool] ignore_public_acls: Whether Amazon S3 should ignore public ACLs for this bucket. Defaults to `false`. Enabling this setting does not affect the persistence of any existing ACLs and doesn't prevent new public ACLs from being set. When set to `true` causes Amazon S3 to:
               * Ignore public ACLs on this bucket and any objects that it contains.
        :param pulumi.Input[bool] restrict_public_buckets: Whether Amazon S3 should restrict public bucket policies for this bucket. Defaults to `false`. Enabling this setting does not affect the previously stored bucket policy, except that public and cross-account access within the public bucket policy, including non-public delegation to specific accounts, is blocked. When set to `true`:
               * Only the bucket owner and AWS Services can access this buckets if it has a public policy.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/s3_bucket_public_access_block.html.markdown.
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

            __props__['block_public_acls'] = block_public_acls
            __props__['block_public_policy'] = block_public_policy
            if bucket is None:
                raise TypeError("Missing required property 'bucket'")
            __props__['bucket'] = bucket
            __props__['ignore_public_acls'] = ignore_public_acls
            __props__['restrict_public_buckets'] = restrict_public_buckets
        super(BucketPublicAccessBlock, __self__).__init__(
            'aws:s3/bucketPublicAccessBlock:BucketPublicAccessBlock',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, block_public_acls=None, block_public_policy=None, bucket=None, ignore_public_acls=None, restrict_public_buckets=None):
        """
        Get an existing BucketPublicAccessBlock resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.
        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] block_public_acls: Whether Amazon S3 should block public ACLs for this bucket. Defaults to `false`. Enabling this setting does not affect existing policies or ACLs. When set to `true` causes the following behavior:
               * PUT Bucket acl and PUT Object acl calls will fail if the specified ACL allows public access.
               * PUT Object calls will fail if the request includes an object ACL.
        :param pulumi.Input[bool] block_public_policy: Whether Amazon S3 should block public bucket policies for this bucket. Defaults to `false`. Enabling this setting does not affect the existing bucket policy. When set to `true` causes Amazon S3 to:
               * Reject calls to PUT Bucket policy if the specified bucket policy allows public access.
        :param pulumi.Input[str] bucket: S3 Bucket to which this Public Access Block configuration should be applied.
        :param pulumi.Input[bool] ignore_public_acls: Whether Amazon S3 should ignore public ACLs for this bucket. Defaults to `false`. Enabling this setting does not affect the persistence of any existing ACLs and doesn't prevent new public ACLs from being set. When set to `true` causes Amazon S3 to:
               * Ignore public ACLs on this bucket and any objects that it contains.
        :param pulumi.Input[bool] restrict_public_buckets: Whether Amazon S3 should restrict public bucket policies for this bucket. Defaults to `false`. Enabling this setting does not affect the previously stored bucket policy, except that public and cross-account access within the public bucket policy, including non-public delegation to specific accounts, is blocked. When set to `true`:
               * Only the bucket owner and AWS Services can access this buckets if it has a public policy.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/s3_bucket_public_access_block.html.markdown.
        """
        opts = pulumi.ResourceOptions(id=id) if opts is None else opts.merge(pulumi.ResourceOptions(id=id))

        __props__ = dict()
        __props__["block_public_acls"] = block_public_acls
        __props__["block_public_policy"] = block_public_policy
        __props__["bucket"] = bucket
        __props__["ignore_public_acls"] = ignore_public_acls
        __props__["restrict_public_buckets"] = restrict_public_buckets
        return BucketPublicAccessBlock(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

