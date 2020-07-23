# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from .. import _utilities, _tables

__all__ = [
    'AppCampaignHookArgs',
    'AppLimitsArgs',
    'AppQuietTimeArgs',
]

@pulumi.input_type
class AppCampaignHookArgs:
    def __init__(__self__, *,
                 lambda_function_name: Optional[pulumi.Input[str]] = None,
                 mode: Optional[pulumi.Input[str]] = None,
                 web_url: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] lambda_function_name: Lambda function name or ARN to be called for delivery. Conflicts with `web_url`
        :param pulumi.Input[str] mode: What mode Lambda should be invoked in. Valid values for this parameter are `DELIVERY`, `FILTER`.
        :param pulumi.Input[str] web_url: Web URL to call for hook. If the URL has authentication specified it will be added as authentication to the request. Conflicts with `lambda_function_name`
        """
        pulumi.set(__self__, "lambdaFunctionName", lambda_function_name)
        pulumi.set(__self__, "mode", mode)
        pulumi.set(__self__, "webUrl", web_url)

    @property
    @pulumi.getter(name="lambdaFunctionName")
    def lambda_function_name(self) -> Optional[pulumi.Input[str]]:
        """
        Lambda function name or ARN to be called for delivery. Conflicts with `web_url`
        """
        ...

    @lambda_function_name.setter
    def lambda_function_name(self, value: Optional[pulumi.Input[str]]):
        ...

    @property
    @pulumi.getter
    def mode(self) -> Optional[pulumi.Input[str]]:
        """
        What mode Lambda should be invoked in. Valid values for this parameter are `DELIVERY`, `FILTER`.
        """
        ...

    @mode.setter
    def mode(self, value: Optional[pulumi.Input[str]]):
        ...

    @property
    @pulumi.getter(name="webUrl")
    def web_url(self) -> Optional[pulumi.Input[str]]:
        """
        Web URL to call for hook. If the URL has authentication specified it will be added as authentication to the request. Conflicts with `lambda_function_name`
        """
        ...

    @web_url.setter
    def web_url(self, value: Optional[pulumi.Input[str]]):
        ...


@pulumi.input_type
class AppLimitsArgs:
    def __init__(__self__, *,
                 daily: Optional[pulumi.Input[float]] = None,
                 maximum_duration: Optional[pulumi.Input[float]] = None,
                 messages_per_second: Optional[pulumi.Input[float]] = None,
                 total: Optional[pulumi.Input[float]] = None):
        """
        :param pulumi.Input[float] daily: The maximum number of messages that the campaign can send daily.
        :param pulumi.Input[float] maximum_duration: The length of time (in seconds) that the campaign can run before it ends and message deliveries stop. This duration begins at the scheduled start time for the campaign. The minimum value is 60.
        :param pulumi.Input[float] messages_per_second: The number of messages that the campaign can send per second. The minimum value is 50, and the maximum is 20000.
        :param pulumi.Input[float] total: The maximum total number of messages that the campaign can send.
        """
        pulumi.set(__self__, "daily", daily)
        pulumi.set(__self__, "maximumDuration", maximum_duration)
        pulumi.set(__self__, "messagesPerSecond", messages_per_second)
        pulumi.set(__self__, "total", total)

    @property
    @pulumi.getter
    def daily(self) -> Optional[pulumi.Input[float]]:
        """
        The maximum number of messages that the campaign can send daily.
        """
        ...

    @daily.setter
    def daily(self, value: Optional[pulumi.Input[float]]):
        ...

    @property
    @pulumi.getter(name="maximumDuration")
    def maximum_duration(self) -> Optional[pulumi.Input[float]]:
        """
        The length of time (in seconds) that the campaign can run before it ends and message deliveries stop. This duration begins at the scheduled start time for the campaign. The minimum value is 60.
        """
        ...

    @maximum_duration.setter
    def maximum_duration(self, value: Optional[pulumi.Input[float]]):
        ...

    @property
    @pulumi.getter(name="messagesPerSecond")
    def messages_per_second(self) -> Optional[pulumi.Input[float]]:
        """
        The number of messages that the campaign can send per second. The minimum value is 50, and the maximum is 20000.
        """
        ...

    @messages_per_second.setter
    def messages_per_second(self, value: Optional[pulumi.Input[float]]):
        ...

    @property
    @pulumi.getter
    def total(self) -> Optional[pulumi.Input[float]]:
        """
        The maximum total number of messages that the campaign can send.
        """
        ...

    @total.setter
    def total(self, value: Optional[pulumi.Input[float]]):
        ...


@pulumi.input_type
class AppQuietTimeArgs:
    def __init__(__self__, *,
                 end: Optional[pulumi.Input[str]] = None,
                 start: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] end: The default end time for quiet time in ISO 8601 format. Required if `start` is set
        :param pulumi.Input[str] start: The default start time for quiet time in ISO 8601 format. Required if `end` is set
        """
        pulumi.set(__self__, "end", end)
        pulumi.set(__self__, "start", start)

    @property
    @pulumi.getter
    def end(self) -> Optional[pulumi.Input[str]]:
        """
        The default end time for quiet time in ISO 8601 format. Required if `start` is set
        """
        ...

    @end.setter
    def end(self, value: Optional[pulumi.Input[str]]):
        ...

    @property
    @pulumi.getter
    def start(self) -> Optional[pulumi.Input[str]]:
        """
        The default start time for quiet time in ISO 8601 format. Required if `end` is set
        """
        ...

    @start.setter
    def start(self, value: Optional[pulumi.Input[str]]):
        ...


