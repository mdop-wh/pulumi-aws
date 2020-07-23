# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from .. import _utilities, _tables

__all__ = ['LustreFileSystem']


class LustreFileSystem(pulumi.CustomResource):
    arn: pulumi.Output[str] = pulumi.property("arn")
    """
    Amazon Resource Name of the file system.
    """

    dns_name: pulumi.Output[str] = pulumi.property("dnsName")
    """
    DNS name for the file system, e.g. `fs-12345678.fsx.us-west-2.amazonaws.com`
    """

    export_path: pulumi.Output[str] = pulumi.property("exportPath")
    """
    S3 URI (with optional prefix) where the root of your Amazon FSx file system is exported. Can only be specified with `import_path` argument and the path must use the same Amazon S3 bucket as specified in `import_path`. Set equal to `import_path` to overwrite files on export. Defaults to `s3://{IMPORT BUCKET}/FSxLustre{CREATION TIMESTAMP}`.
    """

    import_path: pulumi.Output[Optional[str]] = pulumi.property("importPath")
    """
    S3 URI (with optional prefix) that you're using as the data repository for your FSx for Lustre file system. For example, `s3://example-bucket/optional-prefix/`.
    """

    imported_file_chunk_size: pulumi.Output[float] = pulumi.property("importedFileChunkSize")
    """
    For files imported from a data repository, this value determines the stripe count and maximum amount of data per file (in MiB) stored on a single physical disk. Can only be specified with `import_path` argument. Defaults to `1024`. Minimum of `1` and maximum of `512000`.
    """

    network_interface_ids: pulumi.Output[List[str]] = pulumi.property("networkInterfaceIds")
    """
    Set of Elastic Network Interface identifiers from which the file system is accessible.
    """

    owner_id: pulumi.Output[str] = pulumi.property("ownerId")
    """
    AWS account identifier that created the file system.
    """

    security_group_ids: pulumi.Output[Optional[List[str]]] = pulumi.property("securityGroupIds")
    """
    A list of IDs for the security groups that apply to the specified network interfaces created for file system access. These security groups will apply to all network interfaces.
    """

    storage_capacity: pulumi.Output[float] = pulumi.property("storageCapacity")
    """
    The storage capacity (GiB) of the file system. Minimum of `1200`. Storage capacity is provisioned in increments of 3,600 GiB.
    """

    subnet_ids: pulumi.Output[str] = pulumi.property("subnetIds")
    """
    A list of IDs for the subnets that the file system will be accessible from. File systems currently support only one subnet. The file server is also launched in that subnet's Availability Zone.
    """

    tags: pulumi.Output[Optional[Mapping[str, str]]] = pulumi.property("tags")
    """
    A map of tags to assign to the file system.
    """

    vpc_id: pulumi.Output[str] = pulumi.property("vpcId")
    """
    Identifier of the Virtual Private Cloud for the file system.
    """

    weekly_maintenance_start_time: pulumi.Output[str] = pulumi.property("weeklyMaintenanceStartTime")
    """
    The preferred start time (in `d:HH:MM` format) to perform weekly maintenance, in the UTC time zone.
    """

    def __init__(__self__,
                 resource_name,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 export_path: Optional[pulumi.Input[str]] = None,
                 import_path: Optional[pulumi.Input[str]] = None,
                 imported_file_chunk_size: Optional[pulumi.Input[float]] = None,
                 security_group_ids: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None,
                 storage_capacity: Optional[pulumi.Input[float]] = None,
                 subnet_ids: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 weekly_maintenance_start_time: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Manages a FSx Lustre File System. See the [FSx Lustre Guide](https://docs.aws.amazon.com/fsx/latest/LustreGuide/what-is.html) for more information.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.fsx.LustreFileSystem("example",
            import_path=f"s3://{aws_s3_bucket['example']['bucket']}",
            storage_capacity=1200,
            subnet_ids=aws_subnet["example"]["id"])
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] export_path: S3 URI (with optional prefix) where the root of your Amazon FSx file system is exported. Can only be specified with `import_path` argument and the path must use the same Amazon S3 bucket as specified in `import_path`. Set equal to `import_path` to overwrite files on export. Defaults to `s3://{IMPORT BUCKET}/FSxLustre{CREATION TIMESTAMP}`.
        :param pulumi.Input[str] import_path: S3 URI (with optional prefix) that you're using as the data repository for your FSx for Lustre file system. For example, `s3://example-bucket/optional-prefix/`.
        :param pulumi.Input[float] imported_file_chunk_size: For files imported from a data repository, this value determines the stripe count and maximum amount of data per file (in MiB) stored on a single physical disk. Can only be specified with `import_path` argument. Defaults to `1024`. Minimum of `1` and maximum of `512000`.
        :param pulumi.Input[List[pulumi.Input[str]]] security_group_ids: A list of IDs for the security groups that apply to the specified network interfaces created for file system access. These security groups will apply to all network interfaces.
        :param pulumi.Input[float] storage_capacity: The storage capacity (GiB) of the file system. Minimum of `1200`. Storage capacity is provisioned in increments of 3,600 GiB.
        :param pulumi.Input[str] subnet_ids: A list of IDs for the subnets that the file system will be accessible from. File systems currently support only one subnet. The file server is also launched in that subnet's Availability Zone.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the file system.
        :param pulumi.Input[str] weekly_maintenance_start_time: The preferred start time (in `d:HH:MM` format) to perform weekly maintenance, in the UTC time zone.
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

            __props__['export_path'] = export_path
            __props__['import_path'] = import_path
            __props__['imported_file_chunk_size'] = imported_file_chunk_size
            __props__['security_group_ids'] = security_group_ids
            if storage_capacity is None:
                raise TypeError("Missing required property 'storage_capacity'")
            __props__['storage_capacity'] = storage_capacity
            if subnet_ids is None:
                raise TypeError("Missing required property 'subnet_ids'")
            __props__['subnet_ids'] = subnet_ids
            __props__['tags'] = tags
            __props__['weekly_maintenance_start_time'] = weekly_maintenance_start_time
            __props__['arn'] = None
            __props__['dns_name'] = None
            __props__['network_interface_ids'] = None
            __props__['owner_id'] = None
            __props__['vpc_id'] = None
        super(LustreFileSystem, __self__).__init__(
            'aws:fsx/lustreFileSystem:LustreFileSystem',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: str,
            opts: Optional[pulumi.ResourceOptions] = None,
            arn: Optional[pulumi.Input[str]] = None,
            dns_name: Optional[pulumi.Input[str]] = None,
            export_path: Optional[pulumi.Input[str]] = None,
            import_path: Optional[pulumi.Input[str]] = None,
            imported_file_chunk_size: Optional[pulumi.Input[float]] = None,
            network_interface_ids: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None,
            owner_id: Optional[pulumi.Input[str]] = None,
            security_group_ids: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None,
            storage_capacity: Optional[pulumi.Input[float]] = None,
            subnet_ids: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            vpc_id: Optional[pulumi.Input[str]] = None,
            weekly_maintenance_start_time: Optional[pulumi.Input[str]] = None) -> 'LustreFileSystem':
        """
        Get an existing LustreFileSystem resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] arn: Amazon Resource Name of the file system.
        :param pulumi.Input[str] dns_name: DNS name for the file system, e.g. `fs-12345678.fsx.us-west-2.amazonaws.com`
        :param pulumi.Input[str] export_path: S3 URI (with optional prefix) where the root of your Amazon FSx file system is exported. Can only be specified with `import_path` argument and the path must use the same Amazon S3 bucket as specified in `import_path`. Set equal to `import_path` to overwrite files on export. Defaults to `s3://{IMPORT BUCKET}/FSxLustre{CREATION TIMESTAMP}`.
        :param pulumi.Input[str] import_path: S3 URI (with optional prefix) that you're using as the data repository for your FSx for Lustre file system. For example, `s3://example-bucket/optional-prefix/`.
        :param pulumi.Input[float] imported_file_chunk_size: For files imported from a data repository, this value determines the stripe count and maximum amount of data per file (in MiB) stored on a single physical disk. Can only be specified with `import_path` argument. Defaults to `1024`. Minimum of `1` and maximum of `512000`.
        :param pulumi.Input[List[pulumi.Input[str]]] network_interface_ids: Set of Elastic Network Interface identifiers from which the file system is accessible.
        :param pulumi.Input[str] owner_id: AWS account identifier that created the file system.
        :param pulumi.Input[List[pulumi.Input[str]]] security_group_ids: A list of IDs for the security groups that apply to the specified network interfaces created for file system access. These security groups will apply to all network interfaces.
        :param pulumi.Input[float] storage_capacity: The storage capacity (GiB) of the file system. Minimum of `1200`. Storage capacity is provisioned in increments of 3,600 GiB.
        :param pulumi.Input[str] subnet_ids: A list of IDs for the subnets that the file system will be accessible from. File systems currently support only one subnet. The file server is also launched in that subnet's Availability Zone.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the file system.
        :param pulumi.Input[str] vpc_id: Identifier of the Virtual Private Cloud for the file system.
        :param pulumi.Input[str] weekly_maintenance_start_time: The preferred start time (in `d:HH:MM` format) to perform weekly maintenance, in the UTC time zone.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["arn"] = arn
        __props__["dns_name"] = dns_name
        __props__["export_path"] = export_path
        __props__["import_path"] = import_path
        __props__["imported_file_chunk_size"] = imported_file_chunk_size
        __props__["network_interface_ids"] = network_interface_ids
        __props__["owner_id"] = owner_id
        __props__["security_group_ids"] = security_group_ids
        __props__["storage_capacity"] = storage_capacity
        __props__["subnet_ids"] = subnet_ids
        __props__["tags"] = tags
        __props__["vpc_id"] = vpc_id
        __props__["weekly_maintenance_start_time"] = weekly_maintenance_start_time
        return LustreFileSystem(resource_name, opts=opts, __props__=__props__)

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

