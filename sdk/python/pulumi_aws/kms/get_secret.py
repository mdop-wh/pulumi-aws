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

__all__ = [
    'GetSecretResult',
    'AwaitableGetSecretResult',
    'get_secret',
]



@pulumi.output_type
class GetSecretResult:
    """
    A collection of values returned by getSecret.
    """
    def __init__(__self__, id=None, secrets=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if secrets and not isinstance(secrets, list):
            raise TypeError("Expected argument 'secrets' to be a list")
        pulumi.set(__self__, "secrets", secrets)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        ...

    @property
    @pulumi.getter
    def secrets(self) -> List['outputs.GetSecretSecretResult']:
        ...



class AwaitableGetSecretResult(GetSecretResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSecretResult(
            id=self.id,
            secrets=self.secrets)


def get_secret(secrets: Optional[List[pulumi.InputType['GetSecretSecretArgs']]] = None,
               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSecretResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['secrets'] = secrets
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws:kms/getSecret:getSecret', __args__, opts=opts, typ=GetSecretResult).value

    return AwaitableGetSecretResult(
        id=__ret__.id,
        secrets=__ret__.secrets)
