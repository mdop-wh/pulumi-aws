# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class Endpoint(pulumi.CustomResource):
    arn: pulumi.Output[str]
    """
    The Amazon Resource Name (ARN) assigned by AWS to this endpoint.
    """
    endpoint_config_name: pulumi.Output[str]
    """
    The name of the endpoint configuration to use.
    """
    name: pulumi.Output[str]
    """
    The name of the endpoint. If omitted, this provider will assign a random, unique name.
    """
    tags: pulumi.Output[dict]
    """
    A mapping of tags to assign to the resource.
    """
    def __init__(__self__, resource_name, opts=None, endpoint_config_name=None, name=None, tags=None, __props__=None, __name__=None, __opts__=None):
        """
        Provides a SageMaker Endpoint resource.



        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] endpoint_config_name: The name of the endpoint configuration to use.
        :param pulumi.Input[str] name: The name of the endpoint. If omitted, this provider will assign a random, unique name.
        :param pulumi.Input[dict] tags: A mapping of tags to assign to the resource.
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
            opts.version = utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            if endpoint_config_name is None:
                raise TypeError("Missing required property 'endpoint_config_name'")
            __props__['endpoint_config_name'] = endpoint_config_name
            __props__['name'] = name
            __props__['tags'] = tags
            __props__['arn'] = None
        super(Endpoint, __self__).__init__(
            'aws:sagemaker/endpoint:Endpoint',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, arn=None, endpoint_config_name=None, name=None, tags=None):
        """
        Get an existing Endpoint resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] arn: The Amazon Resource Name (ARN) assigned by AWS to this endpoint.
        :param pulumi.Input[str] endpoint_config_name: The name of the endpoint configuration to use.
        :param pulumi.Input[str] name: The name of the endpoint. If omitted, this provider will assign a random, unique name.
        :param pulumi.Input[dict] tags: A mapping of tags to assign to the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["arn"] = arn
        __props__["endpoint_config_name"] = endpoint_config_name
        __props__["name"] = name
        __props__["tags"] = tags
        return Endpoint(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

