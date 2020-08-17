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

__all__ = ['IdentityPoolRoleAttachment']


class IdentityPoolRoleAttachment(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 identity_pool_id: Optional[pulumi.Input[str]] = None,
                 role_mappings: Optional[pulumi.Input[List[pulumi.Input[pulumi.InputType['IdentityPoolRoleAttachmentRoleMappingArgs']]]]] = None,
                 roles: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides an AWS Cognito Identity Pool Roles Attachment.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        main_identity_pool = aws.cognito.IdentityPool("mainIdentityPool",
            allow_unauthenticated_identities=False,
            identity_pool_name="identity pool",
            supported_login_providers={
                "graph.facebook.com": "7346241598935555",
            })
        authenticated_role = aws.iam.Role("authenticatedRole", assume_role_policy=main_identity_pool.id.apply(lambda id: f\"\"\"{{
          "Version": "2012-10-17",
          "Statement": [
            {{
              "Effect": "Allow",
              "Principal": {{
                "Federated": "cognito-identity.amazonaws.com"
              }},
              "Action": "sts:AssumeRoleWithWebIdentity",
              "Condition": {{
                "StringEquals": {{
                  "cognito-identity.amazonaws.com:aud": "{id}"
                }},
                "ForAnyValue:StringLike": {{
                  "cognito-identity.amazonaws.com:amr": "authenticated"
                }}
              }}
            }}
          ]
        }}

        \"\"\"))
        authenticated_role_policy = aws.iam.RolePolicy("authenticatedRolePolicy",
            policy=\"\"\"{
          "Version": "2012-10-17",
          "Statement": [
            {
              "Effect": "Allow",
              "Action": [
                "mobileanalytics:PutEvents",
                "cognito-sync:*",
                "cognito-identity:*"
              ],
              "Resource": [
                "*"
              ]
            }
          ]
        }

        \"\"\",
            role=authenticated_role.id)
        main_identity_pool_role_attachment = aws.cognito.IdentityPoolRoleAttachment("mainIdentityPoolRoleAttachment",
            identity_pool_id=main_identity_pool.id,
            role_mappings=[{
                "ambiguousRoleResolution": "AuthenticatedRole",
                "identity_provider": "graph.facebook.com",
                "mappingRules": [{
                    "claim": "isAdmin",
                    "matchType": "Equals",
                    "role_arn": authenticated_role.arn,
                    "value": "paid",
                }],
                "type": "Rules",
            }],
            roles={
                "authenticated": authenticated_role.arn,
            })
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] identity_pool_id: An identity pool ID in the format REGION:GUID.
        :param pulumi.Input[List[pulumi.Input[pulumi.InputType['IdentityPoolRoleAttachmentRoleMappingArgs']]]] role_mappings: A List of Role Mapping.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] roles: The map of roles associated with this pool. For a given role, the key will be either "authenticated" or "unauthenticated" and the value will be the Role ARN.
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

            if identity_pool_id is None:
                raise TypeError("Missing required property 'identity_pool_id'")
            __props__['identity_pool_id'] = identity_pool_id
            __props__['role_mappings'] = role_mappings
            if roles is None:
                raise TypeError("Missing required property 'roles'")
            __props__['roles'] = roles
        super(IdentityPoolRoleAttachment, __self__).__init__(
            'aws:cognito/identityPoolRoleAttachment:IdentityPoolRoleAttachment',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: str,
            opts: Optional[pulumi.ResourceOptions] = None,
            identity_pool_id: Optional[pulumi.Input[str]] = None,
            role_mappings: Optional[pulumi.Input[List[pulumi.Input[pulumi.InputType['IdentityPoolRoleAttachmentRoleMappingArgs']]]]] = None,
            roles: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None) -> 'IdentityPoolRoleAttachment':
        """
        Get an existing IdentityPoolRoleAttachment resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] identity_pool_id: An identity pool ID in the format REGION:GUID.
        :param pulumi.Input[List[pulumi.Input[pulumi.InputType['IdentityPoolRoleAttachmentRoleMappingArgs']]]] role_mappings: A List of Role Mapping.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] roles: The map of roles associated with this pool. For a given role, the key will be either "authenticated" or "unauthenticated" and the value will be the Role ARN.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["identity_pool_id"] = identity_pool_id
        __props__["role_mappings"] = role_mappings
        __props__["roles"] = roles
        return IdentityPoolRoleAttachment(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="identityPoolId")
    def identity_pool_id(self) -> str:
        """
        An identity pool ID in the format REGION:GUID.
        """
        ...

    @property
    @pulumi.getter(name="roleMappings")
    def role_mappings(self) -> Optional[List['outputs.IdentityPoolRoleAttachmentRoleMapping']]:
        """
        A List of Role Mapping.
        """
        ...

    @property
    @pulumi.getter
    def roles(self) -> Mapping[str, str]:
        """
        The map of roles associated with this pool. For a given role, the key will be either "authenticated" or "unauthenticated" and the value will be the Role ARN.
        """
        ...

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

