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

__all__ = ['Directory']


class Directory(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 directory_id: Optional[pulumi.Input[str]] = None,
                 self_service_permissions: Optional[pulumi.Input[pulumi.InputType['DirectorySelfServicePermissionsArgs']]] = None,
                 subnet_ids: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides a directory registration in AWS WorkSpaces Service

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        main_vpc = aws.ec2.Vpc("mainVpc", cidr_block="10.0.0.0/16")
        private_a = aws.ec2.Subnet("private-a",
            availability_zone="us-east-1a",
            cidr_block="10.0.0.0/24",
            vpc_id=main_vpc.id)
        private_b = aws.ec2.Subnet("private-b",
            availability_zone="us-east-1b",
            cidr_block="10.0.1.0/24",
            vpc_id=main_vpc.id)
        main_directory = aws.directoryservice.Directory("mainDirectory",
            password="#S1ncerely",
            size="Small",
            vpc_settings={
                "subnet_ids": [
                    private_a.id,
                    private_b.id,
                ],
                "vpc_id": main_vpc.id,
            })
        main_workspaces_directory_directory = aws.workspaces.Directory("mainWorkspaces/directoryDirectory",
            directory_id=main_directory.id,
            self_service_permissions={
                "increaseVolumeSize": True,
                "rebuildWorkspace": True,
            })
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] directory_id: The directory identifier for registration in WorkSpaces service.
        :param pulumi.Input[pulumi.InputType['DirectorySelfServicePermissionsArgs']] self_service_permissions: The permissions to enable or disable self-service capabilities.
        :param pulumi.Input[List[pulumi.Input[str]]] subnet_ids: The identifiers of the subnets where the directory resides.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags assigned to the WorkSpaces directory.
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

            if directory_id is None:
                raise TypeError("Missing required property 'directory_id'")
            __props__['directory_id'] = directory_id
            __props__['self_service_permissions'] = self_service_permissions
            __props__['subnet_ids'] = subnet_ids
            __props__['tags'] = tags
            __props__['alias'] = None
            __props__['customer_user_name'] = None
            __props__['directory_name'] = None
            __props__['directory_type'] = None
            __props__['dns_ip_addresses'] = None
            __props__['iam_role_id'] = None
            __props__['ip_group_ids'] = None
            __props__['registration_code'] = None
            __props__['workspace_security_group_id'] = None
        super(Directory, __self__).__init__(
            'aws:workspaces/directory:Directory',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: str,
            opts: Optional[pulumi.ResourceOptions] = None,
            alias: Optional[pulumi.Input[str]] = None,
            customer_user_name: Optional[pulumi.Input[str]] = None,
            directory_id: Optional[pulumi.Input[str]] = None,
            directory_name: Optional[pulumi.Input[str]] = None,
            directory_type: Optional[pulumi.Input[str]] = None,
            dns_ip_addresses: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None,
            iam_role_id: Optional[pulumi.Input[str]] = None,
            ip_group_ids: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None,
            registration_code: Optional[pulumi.Input[str]] = None,
            self_service_permissions: Optional[pulumi.Input[pulumi.InputType['DirectorySelfServicePermissionsArgs']]] = None,
            subnet_ids: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            workspace_security_group_id: Optional[pulumi.Input[str]] = None) -> 'Directory':
        """
        Get an existing Directory resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] alias: The directory alias.
        :param pulumi.Input[str] customer_user_name: The user name for the service account.
        :param pulumi.Input[str] directory_id: The directory identifier for registration in WorkSpaces service.
        :param pulumi.Input[str] directory_name: The name of the directory.
        :param pulumi.Input[str] directory_type: The directory type.
        :param pulumi.Input[List[pulumi.Input[str]]] dns_ip_addresses: The IP addresses of the DNS servers for the directory.
        :param pulumi.Input[str] iam_role_id: The identifier of the IAM role. This is the role that allows Amazon WorkSpaces to make calls to other services, such as Amazon EC2, on your behalf.
        :param pulumi.Input[List[pulumi.Input[str]]] ip_group_ids: The identifiers of the IP access control groups associated with the directory.
        :param pulumi.Input[str] registration_code: The registration code for the directory. This is the code that users enter in their Amazon WorkSpaces client application to connect to the directory.
        :param pulumi.Input[pulumi.InputType['DirectorySelfServicePermissionsArgs']] self_service_permissions: The permissions to enable or disable self-service capabilities.
        :param pulumi.Input[List[pulumi.Input[str]]] subnet_ids: The identifiers of the subnets where the directory resides.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags assigned to the WorkSpaces directory.
        :param pulumi.Input[str] workspace_security_group_id: The identifier of the security group that is assigned to new WorkSpaces.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["alias"] = alias
        __props__["customer_user_name"] = customer_user_name
        __props__["directory_id"] = directory_id
        __props__["directory_name"] = directory_name
        __props__["directory_type"] = directory_type
        __props__["dns_ip_addresses"] = dns_ip_addresses
        __props__["iam_role_id"] = iam_role_id
        __props__["ip_group_ids"] = ip_group_ids
        __props__["registration_code"] = registration_code
        __props__["self_service_permissions"] = self_service_permissions
        __props__["subnet_ids"] = subnet_ids
        __props__["tags"] = tags
        __props__["workspace_security_group_id"] = workspace_security_group_id
        return Directory(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def alias(self) -> str:
        """
        The directory alias.
        """
        ...

    @property
    @pulumi.getter(name="customerUserName")
    def customer_user_name(self) -> str:
        """
        The user name for the service account.
        """
        ...

    @property
    @pulumi.getter(name="directoryId")
    def directory_id(self) -> str:
        """
        The directory identifier for registration in WorkSpaces service.
        """
        ...

    @property
    @pulumi.getter(name="directoryName")
    def directory_name(self) -> str:
        """
        The name of the directory.
        """
        ...

    @property
    @pulumi.getter(name="directoryType")
    def directory_type(self) -> str:
        """
        The directory type.
        """
        ...

    @property
    @pulumi.getter(name="dnsIpAddresses")
    def dns_ip_addresses(self) -> List[str]:
        """
        The IP addresses of the DNS servers for the directory.
        """
        ...

    @property
    @pulumi.getter(name="iamRoleId")
    def iam_role_id(self) -> str:
        """
        The identifier of the IAM role. This is the role that allows Amazon WorkSpaces to make calls to other services, such as Amazon EC2, on your behalf.
        """
        ...

    @property
    @pulumi.getter(name="ipGroupIds")
    def ip_group_ids(self) -> List[str]:
        """
        The identifiers of the IP access control groups associated with the directory.
        """
        ...

    @property
    @pulumi.getter(name="registrationCode")
    def registration_code(self) -> str:
        """
        The registration code for the directory. This is the code that users enter in their Amazon WorkSpaces client application to connect to the directory.
        """
        ...

    @property
    @pulumi.getter(name="selfServicePermissions")
    def self_service_permissions(self) -> 'outputs.DirectorySelfServicePermissions':
        """
        The permissions to enable or disable self-service capabilities.
        """
        ...

    @property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> List[str]:
        """
        The identifiers of the subnets where the directory resides.
        """
        ...

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        A map of tags assigned to the WorkSpaces directory.
        """
        ...

    @property
    @pulumi.getter(name="workspaceSecurityGroupId")
    def workspace_security_group_id(self) -> str:
        """
        The identifier of the security group that is assigned to new WorkSpaces.
        """
        ...

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

