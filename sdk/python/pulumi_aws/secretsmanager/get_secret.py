# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from .. import _utilities, _tables
from . import outputs

__all__ = [
    'GetSecretResult',
    'AwaitableGetSecretResult',
    'get_secret',
]


@pulumi.output_type
class _GetSecretResult:
    arn: str = pulumi.property("arn")
    description: str = pulumi.property("description")
    id: str = pulumi.property("id")
    kms_key_id: str = pulumi.property("kmsKeyId")
    name: str = pulumi.property("name")
    policy: str = pulumi.property("policy")
    rotation_enabled: bool = pulumi.property("rotationEnabled")
    rotation_lambda_arn: str = pulumi.property("rotationLambdaArn")
    rotation_rules: List['outputs.GetSecretRotationRuleResult'] = pulumi.property("rotationRules")
    tags: Mapping[str, str] = pulumi.property("tags")


class GetSecretResult:
    """
    A collection of values returned by getSecret.
    """
    def __init__(__self__, arn=None, description=None, id=None, kms_key_id=None, name=None, policy=None, rotation_enabled=None, rotation_lambda_arn=None, rotation_rules=None, tags=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        __self__.arn = arn
        """
        The Amazon Resource Name (ARN) of the secret.
        """
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        __self__.description = description
        """
        A description of the secret.
        """
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        """
        The provider-assigned unique ID for this managed resource.
        """
        if kms_key_id and not isinstance(kms_key_id, str):
            raise TypeError("Expected argument 'kms_key_id' to be a str")
        __self__.kms_key_id = kms_key_id
        """
        The Key Management Service (KMS) Customer Master Key (CMK) associated with the secret.
        """
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        __self__.name = name
        if policy and not isinstance(policy, str):
            raise TypeError("Expected argument 'policy' to be a str")
        __self__.policy = policy
        """
        The resource-based policy document that's attached to the secret.
        """
        if rotation_enabled and not isinstance(rotation_enabled, bool):
            raise TypeError("Expected argument 'rotation_enabled' to be a bool")
        if rotation_enabled is not None:
            warnings.warn("Use the aws_secretsmanager_secret_rotation data source instead", DeprecationWarning)
            pulumi.log.warn("rotation_enabled is deprecated: Use the aws_secretsmanager_secret_rotation data source instead")

        __self__.rotation_enabled = rotation_enabled
        """
        Whether rotation is enabled or not.
        """
        if rotation_lambda_arn and not isinstance(rotation_lambda_arn, str):
            raise TypeError("Expected argument 'rotation_lambda_arn' to be a str")
        if rotation_lambda_arn is not None:
            warnings.warn("Use the aws_secretsmanager_secret_rotation data source instead", DeprecationWarning)
            pulumi.log.warn("rotation_lambda_arn is deprecated: Use the aws_secretsmanager_secret_rotation data source instead")

        __self__.rotation_lambda_arn = rotation_lambda_arn
        """
        Rotation Lambda function Amazon Resource Name (ARN) if rotation is enabled.
        """
        if rotation_rules and not isinstance(rotation_rules, list):
            raise TypeError("Expected argument 'rotation_rules' to be a list")
        if rotation_rules is not None:
            warnings.warn("Use the aws_secretsmanager_secret_rotation data source instead", DeprecationWarning)
            pulumi.log.warn("rotation_rules is deprecated: Use the aws_secretsmanager_secret_rotation data source instead")

        __self__.rotation_rules = rotation_rules
        """
        Rotation rules if rotation is enabled.
        """
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        __self__.tags = tags
        """
        Tags of the secret.
        """


class AwaitableGetSecretResult(GetSecretResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSecretResult(
            arn=self.arn,
            description=self.description,
            id=self.id,
            kms_key_id=self.kms_key_id,
            name=self.name,
            policy=self.policy,
            rotation_enabled=self.rotation_enabled,
            rotation_lambda_arn=self.rotation_lambda_arn,
            rotation_rules=self.rotation_rules,
            tags=self.tags)


def get_secret(arn: Optional[str] = None,
               name: Optional[str] = None,
               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSecretResult:
    """
    Retrieve metadata information about a Secrets Manager secret. To retrieve a secret value, see the `secretsmanager.SecretVersion`.

    ## Example Usage
    ### ARN

    ```python
    import pulumi
    import pulumi_aws as aws

    by_arn = aws.secretsmanager.get_secret(arn="arn:aws:secretsmanager:us-east-1:123456789012:secret:example-123456")
    ```
    ### Name

    ```python
    import pulumi
    import pulumi_aws as aws

    by_name = aws.secretsmanager.get_secret(name="example")
    ```


    :param str arn: The Amazon Resource Name (ARN) of the secret to retrieve.
    :param str name: The name of the secret to retrieve.
    """
    __args__ = dict()
    __args__['arn'] = arn
    __args__['name'] = name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws:secretsmanager/getSecret:getSecret', __args__, opts=opts, typ=_GetSecretResult).value

    return AwaitableGetSecretResult(
        arn=__ret__.arn,
        description=__ret__.description,
        id=__ret__.id,
        kms_key_id=__ret__.kms_key_id,
        name=__ret__.name,
        policy=__ret__.policy,
        rotation_enabled=__ret__.rotation_enabled,
        rotation_lambda_arn=__ret__.rotation_lambda_arn,
        rotation_rules=__ret__.rotation_rules,
        tags=__ret__.tags)
