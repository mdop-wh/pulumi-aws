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

__all__ = ['App']


class App(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 campaign_hook: Optional[pulumi.Input[pulumi.InputType['AppCampaignHookArgs']]] = None,
                 limits: Optional[pulumi.Input[pulumi.InputType['AppLimitsArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 name_prefix: Optional[pulumi.Input[str]] = None,
                 quiet_time: Optional[pulumi.Input[pulumi.InputType['AppQuietTimeArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides a Pinpoint App resource.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.pinpoint.App("example",
            limits=aws.pinpoint.AppLimitsArgs(
                maximum_duration=600,
            ),
            quiet_time=aws.pinpoint.AppQuietTimeArgs(
                end="06:00",
                start="00:00",
            ))
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['AppCampaignHookArgs']] campaign_hook: The default campaign limits for the app. These limits apply to each campaign for the app, unless the campaign overrides the default with limits of its own
        :param pulumi.Input[pulumi.InputType['AppLimitsArgs']] limits: The default campaign limits for the app. These limits apply to each campaign for the app, unless the campaign overrides the default with limits of its own
        :param pulumi.Input[str] name: The application name. By default generated by this provider
        :param pulumi.Input[str] name_prefix: The name of the Pinpoint application. Conflicts with `name`
        :param pulumi.Input[pulumi.InputType['AppQuietTimeArgs']] quiet_time: The default quiet time for the app. Each campaign for this app sends no messages during this time unless the campaign overrides the default with a quiet time of its own
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Key-value map of resource tags
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

            __props__['campaign_hook'] = campaign_hook
            __props__['limits'] = limits
            __props__['name'] = name
            __props__['name_prefix'] = name_prefix
            __props__['quiet_time'] = quiet_time
            __props__['tags'] = tags
            __props__['application_id'] = None
            __props__['arn'] = None
        super(App, __self__).__init__(
            'aws:pinpoint/app:App',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            application_id: Optional[pulumi.Input[str]] = None,
            arn: Optional[pulumi.Input[str]] = None,
            campaign_hook: Optional[pulumi.Input[pulumi.InputType['AppCampaignHookArgs']]] = None,
            limits: Optional[pulumi.Input[pulumi.InputType['AppLimitsArgs']]] = None,
            name: Optional[pulumi.Input[str]] = None,
            name_prefix: Optional[pulumi.Input[str]] = None,
            quiet_time: Optional[pulumi.Input[pulumi.InputType['AppQuietTimeArgs']]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None) -> 'App':
        """
        Get an existing App resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] application_id: The Application ID of the Pinpoint App.
        :param pulumi.Input[str] arn: Amazon Resource Name (ARN) of the PinPoint Application
        :param pulumi.Input[pulumi.InputType['AppCampaignHookArgs']] campaign_hook: The default campaign limits for the app. These limits apply to each campaign for the app, unless the campaign overrides the default with limits of its own
        :param pulumi.Input[pulumi.InputType['AppLimitsArgs']] limits: The default campaign limits for the app. These limits apply to each campaign for the app, unless the campaign overrides the default with limits of its own
        :param pulumi.Input[str] name: The application name. By default generated by this provider
        :param pulumi.Input[str] name_prefix: The name of the Pinpoint application. Conflicts with `name`
        :param pulumi.Input[pulumi.InputType['AppQuietTimeArgs']] quiet_time: The default quiet time for the app. Each campaign for this app sends no messages during this time unless the campaign overrides the default with a quiet time of its own
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Key-value map of resource tags
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["application_id"] = application_id
        __props__["arn"] = arn
        __props__["campaign_hook"] = campaign_hook
        __props__["limits"] = limits
        __props__["name"] = name
        __props__["name_prefix"] = name_prefix
        __props__["quiet_time"] = quiet_time
        __props__["tags"] = tags
        return App(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> pulumi.Output[str]:
        """
        The Application ID of the Pinpoint App.
        """
        return pulumi.get(self, "application_id")

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        Amazon Resource Name (ARN) of the PinPoint Application
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="campaignHook")
    def campaign_hook(self) -> pulumi.Output[Optional['outputs.AppCampaignHook']]:
        """
        The default campaign limits for the app. These limits apply to each campaign for the app, unless the campaign overrides the default with limits of its own
        """
        return pulumi.get(self, "campaign_hook")

    @property
    @pulumi.getter
    def limits(self) -> pulumi.Output[Optional['outputs.AppLimits']]:
        """
        The default campaign limits for the app. These limits apply to each campaign for the app, unless the campaign overrides the default with limits of its own
        """
        return pulumi.get(self, "limits")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The application name. By default generated by this provider
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="namePrefix")
    def name_prefix(self) -> pulumi.Output[Optional[str]]:
        """
        The name of the Pinpoint application. Conflicts with `name`
        """
        return pulumi.get(self, "name_prefix")

    @property
    @pulumi.getter(name="quietTime")
    def quiet_time(self) -> pulumi.Output[Optional['outputs.AppQuietTime']]:
        """
        The default quiet time for the app. Each campaign for this app sends no messages during this time unless the campaign overrides the default with a quiet time of its own
        """
        return pulumi.get(self, "quiet_time")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Key-value map of resource tags
        """
        return pulumi.get(self, "tags")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

