# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from .. import _utilities, _tables

__all__ = ['Application']


class Application(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 compute_platform: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 unique_id: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides a CodeDeploy application to be used as a basis for deployments

        ## Example Usage
        ### ECS Application

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.codedeploy.Application("example", compute_platform="ECS")
        ```
        ### Lambda Application

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.codedeploy.Application("example", compute_platform="Lambda")
        ```
        ### Server Application

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.codedeploy.Application("example", compute_platform="Server")
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] compute_platform: The compute platform can either be `ECS`, `Lambda`, or `Server`. Default is `Server`.
        :param pulumi.Input[str] name: The name of the application.
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

            __props__['compute_platform'] = compute_platform
            __props__['name'] = name
            __props__['unique_id'] = unique_id
        super(Application, __self__).__init__(
            'aws:codedeploy/application:Application',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            compute_platform: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            unique_id: Optional[pulumi.Input[str]] = None) -> 'Application':
        """
        Get an existing Application resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] compute_platform: The compute platform can either be `ECS`, `Lambda`, or `Server`. Default is `Server`.
        :param pulumi.Input[str] name: The name of the application.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["compute_platform"] = compute_platform
        __props__["name"] = name
        __props__["unique_id"] = unique_id
        return Application(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="computePlatform")
    def compute_platform(self) -> pulumi.Output[Optional[str]]:
        """
        The compute platform can either be `ECS`, `Lambda`, or `Server`. Default is `Server`.
        """
        return pulumi.get(self, "compute_platform")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the application.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="uniqueId")
    def unique_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "unique_id")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

