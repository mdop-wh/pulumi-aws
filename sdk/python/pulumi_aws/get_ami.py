# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from . import _utilities, _tables
from . import outputs
from ._inputs import *

__all__ = [
    'GetAmiResult',
    'AwaitableGetAmiResult',
    'get_ami',
]


@pulumi.output_type
class _GetAmiResult:
    architecture: str = pulumi.property("architecture")
    arn: str = pulumi.property("arn")
    block_device_mappings: List['outputs.GetAmiBlockDeviceMappingResult'] = pulumi.property("blockDeviceMappings")
    creation_date: str = pulumi.property("creationDate")
    description: str = pulumi.property("description")
    executable_users: Optional[List[str]] = pulumi.property("executableUsers")
    filters: Optional[List['outputs.GetAmiFilterResult']] = pulumi.property("filters")
    hypervisor: str = pulumi.property("hypervisor")
    id: str = pulumi.property("id")
    image_id: str = pulumi.property("imageId")
    image_location: str = pulumi.property("imageLocation")
    image_owner_alias: str = pulumi.property("imageOwnerAlias")
    image_type: str = pulumi.property("imageType")
    kernel_id: str = pulumi.property("kernelId")
    most_recent: Optional[bool] = pulumi.property("mostRecent")
    name: str = pulumi.property("name")
    name_regex: Optional[str] = pulumi.property("nameRegex")
    owner_id: str = pulumi.property("ownerId")
    owners: List[str] = pulumi.property("owners")
    platform: str = pulumi.property("platform")
    product_codes: List['outputs.GetAmiProductCodeResult'] = pulumi.property("productCodes")
    public: bool = pulumi.property("public")
    ramdisk_id: str = pulumi.property("ramdiskId")
    root_device_name: str = pulumi.property("rootDeviceName")
    root_device_type: str = pulumi.property("rootDeviceType")
    root_snapshot_id: str = pulumi.property("rootSnapshotId")
    sriov_net_support: str = pulumi.property("sriovNetSupport")
    state: str = pulumi.property("state")
    state_reason: Mapping[str, str] = pulumi.property("stateReason")
    tags: Mapping[str, str] = pulumi.property("tags")
    virtualization_type: str = pulumi.property("virtualizationType")


class GetAmiResult:
    """
    A collection of values returned by getAmi.
    """
    def __init__(__self__, architecture=None, arn=None, block_device_mappings=None, creation_date=None, description=None, executable_users=None, filters=None, hypervisor=None, id=None, image_id=None, image_location=None, image_owner_alias=None, image_type=None, kernel_id=None, most_recent=None, name=None, name_regex=None, owner_id=None, owners=None, platform=None, product_codes=None, public=None, ramdisk_id=None, root_device_name=None, root_device_type=None, root_snapshot_id=None, sriov_net_support=None, state=None, state_reason=None, tags=None, virtualization_type=None):
        if architecture and not isinstance(architecture, str):
            raise TypeError("Expected argument 'architecture' to be a str")
        __self__.architecture = architecture
        """
        The OS architecture of the AMI (ie: `i386` or `x86_64`).
        """
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        __self__.arn = arn
        """
        The ARN of the AMI.
        """
        if block_device_mappings and not isinstance(block_device_mappings, list):
            raise TypeError("Expected argument 'block_device_mappings' to be a list")
        __self__.block_device_mappings = block_device_mappings
        """
        The block device mappings of the AMI.
        * `block_device_mappings.#.device_name` - The physical name of the device.
        * `block_device_mappings.#.ebs.delete_on_termination` - `true` if the EBS volume
        will be deleted on termination.
        * `block_device_mappings.#.ebs.encrypted` - `true` if the EBS volume
        is encrypted.
        * `block_device_mappings.#.ebs.iops` - `0` if the EBS volume is
        not a provisioned IOPS image, otherwise the supported IOPS count.
        * `block_device_mappings.#.ebs.snapshot_id` - The ID of the snapshot.
        * `block_device_mappings.#.ebs.volume_size` - The size of the volume, in GiB.
        * `block_device_mappings.#.ebs.volume_type` - The volume type.
        * `block_device_mappings.#.no_device` - Suppresses the specified device
        included in the block device mapping of the AMI.
        * `block_device_mappings.#.virtual_name` - The virtual device name (for
        instance stores).
        """
        if creation_date and not isinstance(creation_date, str):
            raise TypeError("Expected argument 'creation_date' to be a str")
        __self__.creation_date = creation_date
        """
        The date and time the image was created.
        """
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        __self__.description = description
        """
        The description of the AMI that was provided during image
        creation.
        """
        if executable_users and not isinstance(executable_users, list):
            raise TypeError("Expected argument 'executable_users' to be a list")
        __self__.executable_users = executable_users
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        __self__.filters = filters
        if hypervisor and not isinstance(hypervisor, str):
            raise TypeError("Expected argument 'hypervisor' to be a str")
        __self__.hypervisor = hypervisor
        """
        The hypervisor type of the image.
        """
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        """
        The provider-assigned unique ID for this managed resource.
        """
        if image_id and not isinstance(image_id, str):
            raise TypeError("Expected argument 'image_id' to be a str")
        __self__.image_id = image_id
        """
        The ID of the AMI. Should be the same as the resource `id`.
        """
        if image_location and not isinstance(image_location, str):
            raise TypeError("Expected argument 'image_location' to be a str")
        __self__.image_location = image_location
        """
        The location of the AMI.
        """
        if image_owner_alias and not isinstance(image_owner_alias, str):
            raise TypeError("Expected argument 'image_owner_alias' to be a str")
        __self__.image_owner_alias = image_owner_alias
        """
        The AWS account alias (for example, `amazon`, `self`) or
        the AWS account ID of the AMI owner.
        """
        if image_type and not isinstance(image_type, str):
            raise TypeError("Expected argument 'image_type' to be a str")
        __self__.image_type = image_type
        """
        The type of image.
        """
        if kernel_id and not isinstance(kernel_id, str):
            raise TypeError("Expected argument 'kernel_id' to be a str")
        __self__.kernel_id = kernel_id
        """
        The kernel associated with the image, if any. Only applicable
        for machine images.
        """
        if most_recent and not isinstance(most_recent, bool):
            raise TypeError("Expected argument 'most_recent' to be a bool")
        __self__.most_recent = most_recent
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        __self__.name = name
        """
        The name of the AMI that was provided during image creation.
        """
        if name_regex and not isinstance(name_regex, str):
            raise TypeError("Expected argument 'name_regex' to be a str")
        __self__.name_regex = name_regex
        if owner_id and not isinstance(owner_id, str):
            raise TypeError("Expected argument 'owner_id' to be a str")
        __self__.owner_id = owner_id
        """
        The AWS account ID of the image owner.
        """
        if owners and not isinstance(owners, list):
            raise TypeError("Expected argument 'owners' to be a list")
        __self__.owners = owners
        if platform and not isinstance(platform, str):
            raise TypeError("Expected argument 'platform' to be a str")
        __self__.platform = platform
        """
        The value is Windows for `Windows` AMIs; otherwise blank.
        """
        if product_codes and not isinstance(product_codes, list):
            raise TypeError("Expected argument 'product_codes' to be a list")
        __self__.product_codes = product_codes
        """
        Any product codes associated with the AMI.
        * `product_codes.#.product_code_id` - The product code.
        * `product_codes.#.product_code_type` - The type of product code.
        """
        if public and not isinstance(public, bool):
            raise TypeError("Expected argument 'public' to be a bool")
        __self__.public = public
        """
        `true` if the image has public launch permissions.
        """
        if ramdisk_id and not isinstance(ramdisk_id, str):
            raise TypeError("Expected argument 'ramdisk_id' to be a str")
        __self__.ramdisk_id = ramdisk_id
        """
        The RAM disk associated with the image, if any. Only applicable
        for machine images.
        """
        if root_device_name and not isinstance(root_device_name, str):
            raise TypeError("Expected argument 'root_device_name' to be a str")
        __self__.root_device_name = root_device_name
        """
        The device name of the root device.
        """
        if root_device_type and not isinstance(root_device_type, str):
            raise TypeError("Expected argument 'root_device_type' to be a str")
        __self__.root_device_type = root_device_type
        """
        The type of root device (ie: `ebs` or `instance-store`).
        """
        if root_snapshot_id and not isinstance(root_snapshot_id, str):
            raise TypeError("Expected argument 'root_snapshot_id' to be a str")
        __self__.root_snapshot_id = root_snapshot_id
        """
        The snapshot id associated with the root device, if any
        (only applies to `ebs` root devices).
        """
        if sriov_net_support and not isinstance(sriov_net_support, str):
            raise TypeError("Expected argument 'sriov_net_support' to be a str")
        __self__.sriov_net_support = sriov_net_support
        """
        Specifies whether enhanced networking is enabled.
        """
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        __self__.state = state
        """
        The current state of the AMI. If the state is `available`, the image
        is successfully registered and can be used to launch an instance.
        """
        if state_reason and not isinstance(state_reason, dict):
            raise TypeError("Expected argument 'state_reason' to be a dict")
        __self__.state_reason = state_reason
        """
        Describes a state change. Fields are `UNSET` if not available.
        * `state_reason.code` - The reason code for the state change.
        * `state_reason.message` - The message for the state change.
        """
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        __self__.tags = tags
        """
        Any tags assigned to the image.
        * `tags.#.key` - The key name of the tag.
        * `tags.#.value` - The value of the tag.
        """
        if virtualization_type and not isinstance(virtualization_type, str):
            raise TypeError("Expected argument 'virtualization_type' to be a str")
        __self__.virtualization_type = virtualization_type
        """
        The type of virtualization of the AMI (ie: `hvm` or
        `paravirtual`).
        """


class AwaitableGetAmiResult(GetAmiResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAmiResult(
            architecture=self.architecture,
            arn=self.arn,
            block_device_mappings=self.block_device_mappings,
            creation_date=self.creation_date,
            description=self.description,
            executable_users=self.executable_users,
            filters=self.filters,
            hypervisor=self.hypervisor,
            id=self.id,
            image_id=self.image_id,
            image_location=self.image_location,
            image_owner_alias=self.image_owner_alias,
            image_type=self.image_type,
            kernel_id=self.kernel_id,
            most_recent=self.most_recent,
            name=self.name,
            name_regex=self.name_regex,
            owner_id=self.owner_id,
            owners=self.owners,
            platform=self.platform,
            product_codes=self.product_codes,
            public=self.public,
            ramdisk_id=self.ramdisk_id,
            root_device_name=self.root_device_name,
            root_device_type=self.root_device_type,
            root_snapshot_id=self.root_snapshot_id,
            sriov_net_support=self.sriov_net_support,
            state=self.state,
            state_reason=self.state_reason,
            tags=self.tags,
            virtualization_type=self.virtualization_type)


def get_ami(executable_users: Optional[List[str]] = None,
            filters: Optional[List[pulumi.InputType['GetAmiFilterArgs']]] = None,
            most_recent: Optional[bool] = None,
            name_regex: Optional[str] = None,
            owners: Optional[List[str]] = None,
            tags: Optional[Mapping[str, str]] = None,
            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAmiResult:
    """
    Use this data source to get the ID of a registered AMI for use in other
    resources.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.get_ami(executable_users=["self"],
        filters=[
            {
                "name": "name",
                "values": ["myami-*"],
            },
            {
                "name": "root-device-type",
                "values": ["ebs"],
            },
            {
                "name": "virtualization-type",
                "values": ["hvm"],
            },
        ],
        most_recent=True,
        name_regex="^myami-\\d{3}",
        owners=["self"])
    ```


    :param List[str] executable_users: Limit search to users with *explicit* launch permission on
           the image. Valid items are the numeric account ID or `self`.
    :param List[pulumi.InputType['GetAmiFilterArgs']] filters: One or more name/value pairs to filter off of. There are
           several valid keys, for a full reference, check out
           [describe-images in the AWS CLI reference][1].
    :param bool most_recent: If more than one result is returned, use the most
           recent AMI.
    :param str name_regex: A regex string to apply to the AMI list returned
           by AWS. This allows more advanced filtering not supported from the AWS API. This
           filtering is done locally on what AWS returns, and could have a performance
           impact if the result is large. It is recommended to combine this with other
           options to narrow down the list AWS returns.
    :param List[str] owners: List of AMI owners to limit search. At least 1 value must be specified. Valid values: an AWS account ID, `self` (the current account), or an AWS owner alias (e.g. `amazon`, `aws-marketplace`, `microsoft`).
    :param Mapping[str, str] tags: Any tags assigned to the image.
           * `tags.#.key` - The key name of the tag.
           * `tags.#.value` - The value of the tag.
    """
    __args__ = dict()
    __args__['executableUsers'] = executable_users
    __args__['filters'] = filters
    __args__['mostRecent'] = most_recent
    __args__['nameRegex'] = name_regex
    __args__['owners'] = owners
    __args__['tags'] = tags
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws:index/getAmi:getAmi', __args__, opts=opts, typ=_GetAmiResult).value

    return AwaitableGetAmiResult(
        architecture=__ret__.architecture,
        arn=__ret__.arn,
        block_device_mappings=__ret__.block_device_mappings,
        creation_date=__ret__.creation_date,
        description=__ret__.description,
        executable_users=__ret__.executable_users,
        filters=__ret__.filters,
        hypervisor=__ret__.hypervisor,
        id=__ret__.id,
        image_id=__ret__.image_id,
        image_location=__ret__.image_location,
        image_owner_alias=__ret__.image_owner_alias,
        image_type=__ret__.image_type,
        kernel_id=__ret__.kernel_id,
        most_recent=__ret__.most_recent,
        name=__ret__.name,
        name_regex=__ret__.name_regex,
        owner_id=__ret__.owner_id,
        owners=__ret__.owners,
        platform=__ret__.platform,
        product_codes=__ret__.product_codes,
        public=__ret__.public,
        ramdisk_id=__ret__.ramdisk_id,
        root_device_name=__ret__.root_device_name,
        root_device_type=__ret__.root_device_type,
        root_snapshot_id=__ret__.root_snapshot_id,
        sriov_net_support=__ret__.sriov_net_support,
        state=__ret__.state,
        state_reason=__ret__.state_reason,
        tags=__ret__.tags,
        virtualization_type=__ret__.virtualization_type)
