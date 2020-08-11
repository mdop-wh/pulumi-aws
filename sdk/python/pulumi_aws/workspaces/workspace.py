# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import _utilities, _tables


class Workspace(pulumi.CustomResource):
    bundle_id: pulumi.Output[str]
    """
    The ID of the bundle for the WorkSpace.
    """
    computer_name: pulumi.Output[str]
    """
    The name of the WorkSpace, as seen by the operating system.
    """
    directory_id: pulumi.Output[str]
    """
    The ID of the directory for the WorkSpace.
    """
    ip_address: pulumi.Output[str]
    """
    The IP address of the WorkSpace.
    """
    root_volume_encryption_enabled: pulumi.Output[bool]
    """
    Indicates whether the data stored on the root volume is encrypted.
    """
    state: pulumi.Output[str]
    """
    The operational state of the WorkSpace.
    """
    tags: pulumi.Output[dict]
    """
    The tags for the WorkSpace.
    """
    user_name: pulumi.Output[str]
    """
    The user name of the user for the WorkSpace. This user name must exist in the directory for the WorkSpace.
    """
    user_volume_encryption_enabled: pulumi.Output[bool]
    """
    Indicates whether the data stored on the user volume is encrypted.
    """
    volume_encryption_key: pulumi.Output[str]
    """
    The symmetric AWS KMS customer master key (CMK) used to encrypt data stored on your WorkSpace. Amazon WorkSpaces does not support asymmetric CMKs.
    """
    workspace_properties: pulumi.Output[dict]
    """
    The WorkSpace properties.

      * `computeTypeName` (`str`) - The compute type. For more information, see [Amazon WorkSpaces Bundles](http://aws.amazon.com/workspaces/details/#Amazon_WorkSpaces_Bundles). Valid values are `VALUE`, `STANDARD`, `PERFORMANCE`, `POWER`, `GRAPHICS`, `POWERPRO` and `GRAPHICSPRO`.
      * `rootVolumeSizeGib` (`float`) - The size of the root volume.
      * `runningMode` (`str`) - The running mode. For more information, see [Manage the WorkSpace Running Mode](https://docs.aws.amazon.com/workspaces/latest/adminguide/running-mode.html). Valid values are `AUTO_STOP` and `ALWAYS_ON`.
      * `runningModeAutoStopTimeoutInMinutes` (`float`) - The time after a user logs off when WorkSpaces are automatically stopped. Configured in 60-minute intervals.
      * `userVolumeSizeGib` (`float`) - The size of the user storage.
    """
    def __init__(__self__, resource_name, opts=None, bundle_id=None, directory_id=None, root_volume_encryption_enabled=None, tags=None, user_name=None, user_volume_encryption_enabled=None, volume_encryption_key=None, workspace_properties=None, __props__=None, __name__=None, __opts__=None):
        """
        Provides a workspace in [AWS Workspaces](https://docs.aws.amazon.com/workspaces/latest/adminguide/amazon-workspaces.html) Service

        > **NOTE:** During deletion of an `workspaces.Workspace` resource, the service role `workspaces_DefaultRole` must be attached to the
        policy `arn:aws:iam::aws:policy/AmazonWorkSpacesServiceAccess`, or it will leak the ENI that the Workspaces service creates for the Workspace.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        value_windows10 = aws.workspaces.get_bundle(bundle_id="wsb-bh8rsxt14")
        example = aws.workspaces.Workspace("example",
            directory_id=aws_workspaces_directory["example"]["id"],
            bundle_id=value_windows10.id,
            user_name="john.doe",
            root_volume_encryption_enabled=True,
            user_volume_encryption_enabled=True,
            volume_encryption_key="alias/aws/workspaces",
            workspace_properties={
                "computeTypeName": "VALUE",
                "userVolumeSizeGib": 10,
                "rootVolumeSizeGib": 80,
                "runningMode": "AUTO_STOP",
                "runningModeAutoStopTimeoutInMinutes": 60,
            },
            tags={
                "Department": "IT",
            })
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] bundle_id: The ID of the bundle for the WorkSpace.
        :param pulumi.Input[str] directory_id: The ID of the directory for the WorkSpace.
        :param pulumi.Input[bool] root_volume_encryption_enabled: Indicates whether the data stored on the root volume is encrypted.
        :param pulumi.Input[dict] tags: The tags for the WorkSpace.
        :param pulumi.Input[str] user_name: The user name of the user for the WorkSpace. This user name must exist in the directory for the WorkSpace.
        :param pulumi.Input[bool] user_volume_encryption_enabled: Indicates whether the data stored on the user volume is encrypted.
        :param pulumi.Input[str] volume_encryption_key: The symmetric AWS KMS customer master key (CMK) used to encrypt data stored on your WorkSpace. Amazon WorkSpaces does not support asymmetric CMKs.
        :param pulumi.Input[dict] workspace_properties: The WorkSpace properties.

        The **workspace_properties** object supports the following:

          * `computeTypeName` (`pulumi.Input[str]`) - The compute type. For more information, see [Amazon WorkSpaces Bundles](http://aws.amazon.com/workspaces/details/#Amazon_WorkSpaces_Bundles). Valid values are `VALUE`, `STANDARD`, `PERFORMANCE`, `POWER`, `GRAPHICS`, `POWERPRO` and `GRAPHICSPRO`.
          * `rootVolumeSizeGib` (`pulumi.Input[float]`) - The size of the root volume.
          * `runningMode` (`pulumi.Input[str]`) - The running mode. For more information, see [Manage the WorkSpace Running Mode](https://docs.aws.amazon.com/workspaces/latest/adminguide/running-mode.html). Valid values are `AUTO_STOP` and `ALWAYS_ON`.
          * `runningModeAutoStopTimeoutInMinutes` (`pulumi.Input[float]`) - The time after a user logs off when WorkSpaces are automatically stopped. Configured in 60-minute intervals.
          * `userVolumeSizeGib` (`pulumi.Input[float]`) - The size of the user storage.
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

            if bundle_id is None:
                raise TypeError("Missing required property 'bundle_id'")
            __props__['bundle_id'] = bundle_id
            if directory_id is None:
                raise TypeError("Missing required property 'directory_id'")
            __props__['directory_id'] = directory_id
            __props__['root_volume_encryption_enabled'] = root_volume_encryption_enabled
            __props__['tags'] = tags
            if user_name is None:
                raise TypeError("Missing required property 'user_name'")
            __props__['user_name'] = user_name
            __props__['user_volume_encryption_enabled'] = user_volume_encryption_enabled
            __props__['volume_encryption_key'] = volume_encryption_key
            __props__['workspace_properties'] = workspace_properties
            __props__['computer_name'] = None
            __props__['ip_address'] = None
            __props__['state'] = None
        super(Workspace, __self__).__init__(
            'aws:workspaces/workspace:Workspace',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, bundle_id=None, computer_name=None, directory_id=None, ip_address=None, root_volume_encryption_enabled=None, state=None, tags=None, user_name=None, user_volume_encryption_enabled=None, volume_encryption_key=None, workspace_properties=None):
        """
        Get an existing Workspace resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] bundle_id: The ID of the bundle for the WorkSpace.
        :param pulumi.Input[str] computer_name: The name of the WorkSpace, as seen by the operating system.
        :param pulumi.Input[str] directory_id: The ID of the directory for the WorkSpace.
        :param pulumi.Input[str] ip_address: The IP address of the WorkSpace.
        :param pulumi.Input[bool] root_volume_encryption_enabled: Indicates whether the data stored on the root volume is encrypted.
        :param pulumi.Input[str] state: The operational state of the WorkSpace.
        :param pulumi.Input[dict] tags: The tags for the WorkSpace.
        :param pulumi.Input[str] user_name: The user name of the user for the WorkSpace. This user name must exist in the directory for the WorkSpace.
        :param pulumi.Input[bool] user_volume_encryption_enabled: Indicates whether the data stored on the user volume is encrypted.
        :param pulumi.Input[str] volume_encryption_key: The symmetric AWS KMS customer master key (CMK) used to encrypt data stored on your WorkSpace. Amazon WorkSpaces does not support asymmetric CMKs.
        :param pulumi.Input[dict] workspace_properties: The WorkSpace properties.

        The **workspace_properties** object supports the following:

          * `computeTypeName` (`pulumi.Input[str]`) - The compute type. For more information, see [Amazon WorkSpaces Bundles](http://aws.amazon.com/workspaces/details/#Amazon_WorkSpaces_Bundles). Valid values are `VALUE`, `STANDARD`, `PERFORMANCE`, `POWER`, `GRAPHICS`, `POWERPRO` and `GRAPHICSPRO`.
          * `rootVolumeSizeGib` (`pulumi.Input[float]`) - The size of the root volume.
          * `runningMode` (`pulumi.Input[str]`) - The running mode. For more information, see [Manage the WorkSpace Running Mode](https://docs.aws.amazon.com/workspaces/latest/adminguide/running-mode.html). Valid values are `AUTO_STOP` and `ALWAYS_ON`.
          * `runningModeAutoStopTimeoutInMinutes` (`pulumi.Input[float]`) - The time after a user logs off when WorkSpaces are automatically stopped. Configured in 60-minute intervals.
          * `userVolumeSizeGib` (`pulumi.Input[float]`) - The size of the user storage.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["bundle_id"] = bundle_id
        __props__["computer_name"] = computer_name
        __props__["directory_id"] = directory_id
        __props__["ip_address"] = ip_address
        __props__["root_volume_encryption_enabled"] = root_volume_encryption_enabled
        __props__["state"] = state
        __props__["tags"] = tags
        __props__["user_name"] = user_name
        __props__["user_volume_encryption_enabled"] = user_volume_encryption_enabled
        __props__["volume_encryption_key"] = volume_encryption_key
        __props__["workspace_properties"] = workspace_properties
        return Workspace(resource_name, opts=opts, __props__=__props__)

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop
