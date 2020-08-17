# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from .. import _utilities, _tables

__all__ = [
    'RegexPatternSetRegularExpressionArgs',
]

@pulumi.input_type
class RegexPatternSetRegularExpressionArgs:
    def __init__(__self__, *,
                 regex_string: pulumi.Input[str]):
        """
        :param pulumi.Input[str] regex_string: The string representing the regular expression, see the AWS WAF [documentation](https://docs.aws.amazon.com/waf/latest/developerguide/waf-regex-pattern-set-creating.html) for more information.
        """
        pulumi.set(__self__, "regex_string", regex_string)

    @property
    @pulumi.getter(name="regexString")
    def regex_string(self) -> pulumi.Input[str]:
        """
        The string representing the regular expression, see the AWS WAF [documentation](https://docs.aws.amazon.com/waf/latest/developerguide/waf-regex-pattern-set-creating.html) for more information.
        """
        ...

    @regex_string.setter
    def regex_string(self, value: pulumi.Input[str]):
        ...


