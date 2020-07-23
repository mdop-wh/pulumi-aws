# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from .. import _utilities, _tables

__all__ = [
    'RepositoryImageScanningConfigurationArgs',
]

@pulumi.input_type
class RepositoryImageScanningConfigurationArgs:
    def __init__(__self__, *,
                 scan_on_push: pulumi.Input[bool]):
        """
        :param pulumi.Input[bool] scan_on_push: Indicates whether images are scanned after being pushed to the repository (true) or not scanned (false).
        """
        pulumi.set(__self__, "scanOnPush", scan_on_push)

    @property
    @pulumi.getter(name="scanOnPush")
    def scan_on_push(self) -> pulumi.Input[bool]:
        """
        Indicates whether images are scanned after being pushed to the repository (true) or not scanned (false).
        """
        ...

    @scan_on_push.setter
    def scan_on_push(self, value: pulumi.Input[bool]):
        ...

