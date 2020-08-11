# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import _utilities, _tables


class GetBucketObjectResult:
    """
    A collection of values returned by getBucketObject.
    """
    def __init__(__self__, body=None, bucket=None, cache_control=None, content_disposition=None, content_encoding=None, content_language=None, content_length=None, content_type=None, etag=None, expiration=None, expires=None, id=None, key=None, last_modified=None, metadata=None, object_lock_legal_hold_status=None, object_lock_mode=None, object_lock_retain_until_date=None, range=None, server_side_encryption=None, sse_kms_key_id=None, storage_class=None, tags=None, version_id=None, website_redirect_location=None):
        if body and not isinstance(body, str):
            raise TypeError("Expected argument 'body' to be a str")
        __self__.body = body
        """
        Object data (see **limitations above** to understand cases in which this field is actually available)
        """
        if bucket and not isinstance(bucket, str):
            raise TypeError("Expected argument 'bucket' to be a str")
        __self__.bucket = bucket
        if cache_control and not isinstance(cache_control, str):
            raise TypeError("Expected argument 'cache_control' to be a str")
        __self__.cache_control = cache_control
        """
        Specifies caching behavior along the request/reply chain.
        """
        if content_disposition and not isinstance(content_disposition, str):
            raise TypeError("Expected argument 'content_disposition' to be a str")
        __self__.content_disposition = content_disposition
        """
        Specifies presentational information for the object.
        """
        if content_encoding and not isinstance(content_encoding, str):
            raise TypeError("Expected argument 'content_encoding' to be a str")
        __self__.content_encoding = content_encoding
        """
        Specifies what content encodings have been applied to the object and thus what decoding mechanisms must be applied to obtain the media-type referenced by the Content-Type header field.
        """
        if content_language and not isinstance(content_language, str):
            raise TypeError("Expected argument 'content_language' to be a str")
        __self__.content_language = content_language
        """
        The language the content is in.
        """
        if content_length and not isinstance(content_length, float):
            raise TypeError("Expected argument 'content_length' to be a float")
        __self__.content_length = content_length
        """
        Size of the body in bytes.
        """
        if content_type and not isinstance(content_type, str):
            raise TypeError("Expected argument 'content_type' to be a str")
        __self__.content_type = content_type
        """
        A standard MIME type describing the format of the object data.
        """
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        __self__.etag = etag
        """
        [ETag](https://en.wikipedia.org/wiki/HTTP_ETag) generated for the object (an MD5 sum of the object content in case it's not encrypted)
        """
        if expiration and not isinstance(expiration, str):
            raise TypeError("Expected argument 'expiration' to be a str")
        __self__.expiration = expiration
        """
        If the object expiration is configured (see [object lifecycle management](http://docs.aws.amazon.com/AmazonS3/latest/dev/object-lifecycle-mgmt.html)), the field includes this header. It includes the expiry-date and rule-id key value pairs providing object expiration information. The value of the rule-id is URL encoded.
        """
        if expires and not isinstance(expires, str):
            raise TypeError("Expected argument 'expires' to be a str")
        __self__.expires = expires
        """
        The date and time at which the object is no longer cacheable.
        """
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        """
        The provider-assigned unique ID for this managed resource.
        """
        if key and not isinstance(key, str):
            raise TypeError("Expected argument 'key' to be a str")
        __self__.key = key
        if last_modified and not isinstance(last_modified, str):
            raise TypeError("Expected argument 'last_modified' to be a str")
        __self__.last_modified = last_modified
        """
        Last modified date of the object in RFC1123 format (e.g. `Mon, 02 Jan 2006 15:04:05 MST`)
        """
        if metadata and not isinstance(metadata, dict):
            raise TypeError("Expected argument 'metadata' to be a dict")
        __self__.metadata = metadata
        """
        A map of metadata stored with the object in S3
        """
        if object_lock_legal_hold_status and not isinstance(object_lock_legal_hold_status, str):
            raise TypeError("Expected argument 'object_lock_legal_hold_status' to be a str")
        __self__.object_lock_legal_hold_status = object_lock_legal_hold_status
        """
        Indicates whether this object has an active [legal hold](https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lock-overview.html#object-lock-legal-holds). This field is only returned if you have permission to view an object's legal hold status.
        """
        if object_lock_mode and not isinstance(object_lock_mode, str):
            raise TypeError("Expected argument 'object_lock_mode' to be a str")
        __self__.object_lock_mode = object_lock_mode
        """
        The object lock [retention mode](https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lock-overview.html#object-lock-retention-modes) currently in place for this object.
        """
        if object_lock_retain_until_date and not isinstance(object_lock_retain_until_date, str):
            raise TypeError("Expected argument 'object_lock_retain_until_date' to be a str")
        __self__.object_lock_retain_until_date = object_lock_retain_until_date
        """
        The date and time when this object's object lock will expire.
        """
        if range and not isinstance(range, str):
            raise TypeError("Expected argument 'range' to be a str")
        __self__.range = range
        if server_side_encryption and not isinstance(server_side_encryption, str):
            raise TypeError("Expected argument 'server_side_encryption' to be a str")
        __self__.server_side_encryption = server_side_encryption
        """
        If the object is stored using server-side encryption (KMS or Amazon S3-managed encryption key), this field includes the chosen encryption and algorithm used.
        """
        if sse_kms_key_id and not isinstance(sse_kms_key_id, str):
            raise TypeError("Expected argument 'sse_kms_key_id' to be a str")
        __self__.sse_kms_key_id = sse_kms_key_id
        """
        If present, specifies the ID of the Key Management Service (KMS) master encryption key that was used for the object.
        """
        if storage_class and not isinstance(storage_class, str):
            raise TypeError("Expected argument 'storage_class' to be a str")
        __self__.storage_class = storage_class
        """
        [Storage class](http://docs.aws.amazon.com/AmazonS3/latest/dev/storage-class-intro.html) information of the object. Available for all objects except for `Standard` storage class objects.
        """
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        __self__.tags = tags
        """
        A map of tags assigned to the object.
        """
        if version_id and not isinstance(version_id, str):
            raise TypeError("Expected argument 'version_id' to be a str")
        __self__.version_id = version_id
        """
        The latest version ID of the object returned.
        """
        if website_redirect_location and not isinstance(website_redirect_location, str):
            raise TypeError("Expected argument 'website_redirect_location' to be a str")
        __self__.website_redirect_location = website_redirect_location
        """
        If the bucket is configured as a website, redirects requests for this object to another object in the same bucket or to an external URL. Amazon S3 stores the value of this header in the object metadata.
        """


class AwaitableGetBucketObjectResult(GetBucketObjectResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetBucketObjectResult(
            body=self.body,
            bucket=self.bucket,
            cache_control=self.cache_control,
            content_disposition=self.content_disposition,
            content_encoding=self.content_encoding,
            content_language=self.content_language,
            content_length=self.content_length,
            content_type=self.content_type,
            etag=self.etag,
            expiration=self.expiration,
            expires=self.expires,
            id=self.id,
            key=self.key,
            last_modified=self.last_modified,
            metadata=self.metadata,
            object_lock_legal_hold_status=self.object_lock_legal_hold_status,
            object_lock_mode=self.object_lock_mode,
            object_lock_retain_until_date=self.object_lock_retain_until_date,
            range=self.range,
            server_side_encryption=self.server_side_encryption,
            sse_kms_key_id=self.sse_kms_key_id,
            storage_class=self.storage_class,
            tags=self.tags,
            version_id=self.version_id,
            website_redirect_location=self.website_redirect_location)


def get_bucket_object(bucket=None, key=None, range=None, tags=None, version_id=None, opts=None):
    """
    The S3 object data source allows access to the metadata and
    _optionally_ (see below) content of an object stored inside S3 bucket.

    > **Note:** The content of an object (`body` field) is available only for objects which have a human-readable `Content-Type` (`text/*` and `application/json`). This is to prevent printing unsafe characters and potentially downloading large amount of data which would be thrown away in favour of metadata.

    ## Example Usage

    The following example retrieves a text object (which must have a `Content-Type`
    value starting with `text/`) and uses it as the `user_data` for an EC2 instance:

    ```python
    import pulumi
    import pulumi_aws as aws

    bootstrap_script = aws.s3.get_bucket_object(bucket="ourcorp-deploy-config",
        key="ec2-bootstrap-script.sh")
    example = aws.ec2.Instance("example",
        instance_type="t2.micro",
        ami="ami-2757f631",
        user_data=bootstrap_script.body)
    ```

    The following, more-complex example retrieves only the metadata for a zip
    file stored in S3, which is then used to pass the most recent `version_id`
    to AWS Lambda for use as a function implementation. More information about
    Lambda functions is available in the documentation for
    `lambda.Function`.

    ```python
    import pulumi
    import pulumi_aws as aws

    lambda_ = aws.s3.get_bucket_object(bucket="ourcorp-lambda-functions",
        key="hello-world.zip")
    test_lambda = aws.lambda_.Function("testLambda",
        s3_bucket=lambda_.bucket,
        s3_key=lambda_.key,
        s3_object_version=lambda_.version_id,
        role=aws_iam_role["iam_for_lambda"]["arn"],
        handler="exports.test")
    ```


    :param str bucket: The name of the bucket to read the object from. Alternatively, an [S3 access point](https://docs.aws.amazon.com/AmazonS3/latest/dev/using-access-points.html) ARN can be specified
    :param str key: The full path to the object inside the bucket
    :param dict tags: A map of tags assigned to the object.
    :param str version_id: Specific version ID of the object returned (defaults to latest version)
    """
    __args__ = dict()
    __args__['bucket'] = bucket
    __args__['key'] = key
    __args__['range'] = range
    __args__['tags'] = tags
    __args__['versionId'] = version_id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws:s3/getBucketObject:getBucketObject', __args__, opts=opts).value

    return AwaitableGetBucketObjectResult(
        body=__ret__.get('body'),
        bucket=__ret__.get('bucket'),
        cache_control=__ret__.get('cacheControl'),
        content_disposition=__ret__.get('contentDisposition'),
        content_encoding=__ret__.get('contentEncoding'),
        content_language=__ret__.get('contentLanguage'),
        content_length=__ret__.get('contentLength'),
        content_type=__ret__.get('contentType'),
        etag=__ret__.get('etag'),
        expiration=__ret__.get('expiration'),
        expires=__ret__.get('expires'),
        id=__ret__.get('id'),
        key=__ret__.get('key'),
        last_modified=__ret__.get('lastModified'),
        metadata=__ret__.get('metadata'),
        object_lock_legal_hold_status=__ret__.get('objectLockLegalHoldStatus'),
        object_lock_mode=__ret__.get('objectLockMode'),
        object_lock_retain_until_date=__ret__.get('objectLockRetainUntilDate'),
        range=__ret__.get('range'),
        server_side_encryption=__ret__.get('serverSideEncryption'),
        sse_kms_key_id=__ret__.get('sseKmsKeyId'),
        storage_class=__ret__.get('storageClass'),
        tags=__ret__.get('tags'),
        version_id=__ret__.get('versionId'),
        website_redirect_location=__ret__.get('websiteRedirectLocation'))
