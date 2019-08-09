# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from .. import utilities, tables

class GetRoleResult:
    """
    A collection of values returned by getRole.
    """
    def __init__(__self__, arn=None, assume_role_policy=None, create_date=None, description=None, max_session_duration=None, name=None, path=None, permissions_boundary=None, unique_id=None, id=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        __self__.arn = arn
        """
        The Amazon Resource Name (ARN) specifying the role.
        """
        if assume_role_policy and not isinstance(assume_role_policy, str):
            raise TypeError("Expected argument 'assume_role_policy' to be a str")
        __self__.assume_role_policy = assume_role_policy
        """
        The policy document associated with the role.
        """
        if create_date and not isinstance(create_date, str):
            raise TypeError("Expected argument 'create_date' to be a str")
        __self__.create_date = create_date
        """
        Creation date of the role in RFC 3339 format.
        """
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        __self__.description = description
        """
        Description for the role.
        """
        if max_session_duration and not isinstance(max_session_duration, float):
            raise TypeError("Expected argument 'max_session_duration' to be a float")
        __self__.max_session_duration = max_session_duration
        """
        Maximum session duration.
        """
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        __self__.name = name
        if path and not isinstance(path, str):
            raise TypeError("Expected argument 'path' to be a str")
        __self__.path = path
        """
        The path to the role.
        """
        if permissions_boundary and not isinstance(permissions_boundary, str):
            raise TypeError("Expected argument 'permissions_boundary' to be a str")
        __self__.permissions_boundary = permissions_boundary
        """
        The ARN of the policy that is used to set the permissions boundary for the role.
        """
        if unique_id and not isinstance(unique_id, str):
            raise TypeError("Expected argument 'unique_id' to be a str")
        __self__.unique_id = unique_id
        """
        The stable and unique string identifying the role.
        """
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        """
        id is the provider-assigned unique ID for this managed resource.
        """
class AwaitableGetRoleResult(GetRoleResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetRoleResult(
            arn=self.arn,
            assume_role_policy=self.assume_role_policy,
            create_date=self.create_date,
            description=self.description,
            max_session_duration=self.max_session_duration,
            name=self.name,
            path=self.path,
            permissions_boundary=self.permissions_boundary,
            unique_id=self.unique_id,
            id=self.id)

def get_role(name=None,opts=None):
    """
    This data source can be used to fetch information about a specific
    IAM role. By using this data source, you can reference IAM role
    properties without having to hard code ARNs as input.

    > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/iam_role.html.markdown.
    """
    __args__ = dict()

    __args__['name'] = name
    if opts is None:
        opts = pulumi.ResourceOptions()
    if opts.version is None:
        opts.version = utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws:iam/getRole:getRole', __args__, opts=opts).value

    return AwaitableGetRoleResult(
        arn=__ret__.get('arn'),
        assume_role_policy=__ret__.get('assumeRolePolicy'),
        create_date=__ret__.get('createDate'),
        description=__ret__.get('description'),
        max_session_duration=__ret__.get('maxSessionDuration'),
        name=__ret__.get('name'),
        path=__ret__.get('path'),
        permissions_boundary=__ret__.get('permissionsBoundary'),
        unique_id=__ret__.get('uniqueId'),
        id=__ret__.get('id'))
