# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class SmbFileShare(pulumi.CustomResource):
    arn: pulumi.Output[str]
    """
    Amazon Resource Name (ARN) of the SMB File Share.
    """
    authentication: pulumi.Output[str]
    """
    The authentication method that users use to access the file share. Defaults to `ActiveDirectory`. Valid values: `ActiveDirectory`, `GuestAccess`.
    """
    default_storage_class: pulumi.Output[str]
    """
    The default storage class for objects put into an Amazon S3 bucket by the file gateway. Defaults to `S3_STANDARD`. Valid values: `S3_STANDARD`, `S3_STANDARD_IA`, `S3_ONEZONE_IA`.
    """
    fileshare_id: pulumi.Output[str]
    """
    ID of the SMB File Share.
    """
    gateway_arn: pulumi.Output[str]
    """
    Amazon Resource Name (ARN) of the file gateway.
    """
    guess_mime_type_enabled: pulumi.Output[bool]
    """
    Boolean value that enables guessing of the MIME type for uploaded objects based on file extensions. Defaults to `true`.
    """
    invalid_user_lists: pulumi.Output[list]
    """
    A list of users in the Active Directory that are not allowed to access the file share. Only valid if `authentication` is set to `ActiveDirectory`.
    """
    kms_encrypted: pulumi.Output[bool]
    """
    Boolean value if `true` to use Amazon S3 server side encryption with your own AWS KMS key, or `false` to use a key managed by Amazon S3. Defaults to `false`.
    """
    kms_key_arn: pulumi.Output[str]
    """
    Amazon Resource Name (ARN) for KMS key used for Amazon S3 server side encryption. This value can only be set when `kms_encrypted` is true.
    """
    location_arn: pulumi.Output[str]
    """
    The ARN of the backed storage used for storing file data.
    """
    object_acl: pulumi.Output[str]
    """
    Access Control List permission for S3 bucket objects. Defaults to `private`.
    """
    read_only: pulumi.Output[bool]
    """
    Boolean to indicate write status of file share. File share does not accept writes if `true`. Defaults to `false`.
    """
    requester_pays: pulumi.Output[bool]
    """
    Boolean who pays the cost of the request and the data download from the Amazon S3 bucket. Set this value to `true` if you want the requester to pay instead of the bucket owner. Defaults to `false`.
    """
    role_arn: pulumi.Output[str]
    """
    The ARN of the AWS Identity and Access Management (IAM) role that a file gateway assumes when it accesses the underlying storage.
    """
    tags: pulumi.Output[dict]
    """
    Key-value mapping of resource tags
    """
    valid_user_lists: pulumi.Output[list]
    """
    A list of users in the Active Directory that are allowed to access the file share. Only valid if `authentication` is set to `ActiveDirectory`.
    """
    def __init__(__self__, resource_name, opts=None, authentication=None, default_storage_class=None, gateway_arn=None, guess_mime_type_enabled=None, invalid_user_lists=None, kms_encrypted=None, kms_key_arn=None, location_arn=None, object_acl=None, read_only=None, requester_pays=None, role_arn=None, tags=None, valid_user_lists=None, __props__=None, __name__=None, __opts__=None):
        """
        Manages an AWS Storage Gateway SMB File Share.



        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] authentication: The authentication method that users use to access the file share. Defaults to `ActiveDirectory`. Valid values: `ActiveDirectory`, `GuestAccess`.
        :param pulumi.Input[str] default_storage_class: The default storage class for objects put into an Amazon S3 bucket by the file gateway. Defaults to `S3_STANDARD`. Valid values: `S3_STANDARD`, `S3_STANDARD_IA`, `S3_ONEZONE_IA`.
        :param pulumi.Input[str] gateway_arn: Amazon Resource Name (ARN) of the file gateway.
        :param pulumi.Input[bool] guess_mime_type_enabled: Boolean value that enables guessing of the MIME type for uploaded objects based on file extensions. Defaults to `true`.
        :param pulumi.Input[list] invalid_user_lists: A list of users in the Active Directory that are not allowed to access the file share. Only valid if `authentication` is set to `ActiveDirectory`.
        :param pulumi.Input[bool] kms_encrypted: Boolean value if `true` to use Amazon S3 server side encryption with your own AWS KMS key, or `false` to use a key managed by Amazon S3. Defaults to `false`.
        :param pulumi.Input[str] kms_key_arn: Amazon Resource Name (ARN) for KMS key used for Amazon S3 server side encryption. This value can only be set when `kms_encrypted` is true.
        :param pulumi.Input[str] location_arn: The ARN of the backed storage used for storing file data.
        :param pulumi.Input[str] object_acl: Access Control List permission for S3 bucket objects. Defaults to `private`.
        :param pulumi.Input[bool] read_only: Boolean to indicate write status of file share. File share does not accept writes if `true`. Defaults to `false`.
        :param pulumi.Input[bool] requester_pays: Boolean who pays the cost of the request and the data download from the Amazon S3 bucket. Set this value to `true` if you want the requester to pay instead of the bucket owner. Defaults to `false`.
        :param pulumi.Input[str] role_arn: The ARN of the AWS Identity and Access Management (IAM) role that a file gateway assumes when it accesses the underlying storage.
        :param pulumi.Input[dict] tags: Key-value mapping of resource tags
        :param pulumi.Input[list] valid_user_lists: A list of users in the Active Directory that are allowed to access the file share. Only valid if `authentication` is set to `ActiveDirectory`.
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

            __props__['authentication'] = authentication
            __props__['default_storage_class'] = default_storage_class
            if gateway_arn is None:
                raise TypeError("Missing required property 'gateway_arn'")
            __props__['gateway_arn'] = gateway_arn
            __props__['guess_mime_type_enabled'] = guess_mime_type_enabled
            __props__['invalid_user_lists'] = invalid_user_lists
            __props__['kms_encrypted'] = kms_encrypted
            __props__['kms_key_arn'] = kms_key_arn
            if location_arn is None:
                raise TypeError("Missing required property 'location_arn'")
            __props__['location_arn'] = location_arn
            __props__['object_acl'] = object_acl
            __props__['read_only'] = read_only
            __props__['requester_pays'] = requester_pays
            if role_arn is None:
                raise TypeError("Missing required property 'role_arn'")
            __props__['role_arn'] = role_arn
            __props__['tags'] = tags
            __props__['valid_user_lists'] = valid_user_lists
            __props__['arn'] = None
            __props__['fileshare_id'] = None
        super(SmbFileShare, __self__).__init__(
            'aws:storagegateway/smbFileShare:SmbFileShare',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, arn=None, authentication=None, default_storage_class=None, fileshare_id=None, gateway_arn=None, guess_mime_type_enabled=None, invalid_user_lists=None, kms_encrypted=None, kms_key_arn=None, location_arn=None, object_acl=None, read_only=None, requester_pays=None, role_arn=None, tags=None, valid_user_lists=None):
        """
        Get an existing SmbFileShare resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] arn: Amazon Resource Name (ARN) of the SMB File Share.
        :param pulumi.Input[str] authentication: The authentication method that users use to access the file share. Defaults to `ActiveDirectory`. Valid values: `ActiveDirectory`, `GuestAccess`.
        :param pulumi.Input[str] default_storage_class: The default storage class for objects put into an Amazon S3 bucket by the file gateway. Defaults to `S3_STANDARD`. Valid values: `S3_STANDARD`, `S3_STANDARD_IA`, `S3_ONEZONE_IA`.
        :param pulumi.Input[str] fileshare_id: ID of the SMB File Share.
        :param pulumi.Input[str] gateway_arn: Amazon Resource Name (ARN) of the file gateway.
        :param pulumi.Input[bool] guess_mime_type_enabled: Boolean value that enables guessing of the MIME type for uploaded objects based on file extensions. Defaults to `true`.
        :param pulumi.Input[list] invalid_user_lists: A list of users in the Active Directory that are not allowed to access the file share. Only valid if `authentication` is set to `ActiveDirectory`.
        :param pulumi.Input[bool] kms_encrypted: Boolean value if `true` to use Amazon S3 server side encryption with your own AWS KMS key, or `false` to use a key managed by Amazon S3. Defaults to `false`.
        :param pulumi.Input[str] kms_key_arn: Amazon Resource Name (ARN) for KMS key used for Amazon S3 server side encryption. This value can only be set when `kms_encrypted` is true.
        :param pulumi.Input[str] location_arn: The ARN of the backed storage used for storing file data.
        :param pulumi.Input[str] object_acl: Access Control List permission for S3 bucket objects. Defaults to `private`.
        :param pulumi.Input[bool] read_only: Boolean to indicate write status of file share. File share does not accept writes if `true`. Defaults to `false`.
        :param pulumi.Input[bool] requester_pays: Boolean who pays the cost of the request and the data download from the Amazon S3 bucket. Set this value to `true` if you want the requester to pay instead of the bucket owner. Defaults to `false`.
        :param pulumi.Input[str] role_arn: The ARN of the AWS Identity and Access Management (IAM) role that a file gateway assumes when it accesses the underlying storage.
        :param pulumi.Input[dict] tags: Key-value mapping of resource tags
        :param pulumi.Input[list] valid_user_lists: A list of users in the Active Directory that are allowed to access the file share. Only valid if `authentication` is set to `ActiveDirectory`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["arn"] = arn
        __props__["authentication"] = authentication
        __props__["default_storage_class"] = default_storage_class
        __props__["fileshare_id"] = fileshare_id
        __props__["gateway_arn"] = gateway_arn
        __props__["guess_mime_type_enabled"] = guess_mime_type_enabled
        __props__["invalid_user_lists"] = invalid_user_lists
        __props__["kms_encrypted"] = kms_encrypted
        __props__["kms_key_arn"] = kms_key_arn
        __props__["location_arn"] = location_arn
        __props__["object_acl"] = object_acl
        __props__["read_only"] = read_only
        __props__["requester_pays"] = requester_pays
        __props__["role_arn"] = role_arn
        __props__["tags"] = tags
        __props__["valid_user_lists"] = valid_user_lists
        return SmbFileShare(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

