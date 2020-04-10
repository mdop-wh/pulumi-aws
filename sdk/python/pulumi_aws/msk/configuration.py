# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class Configuration(pulumi.CustomResource):
    arn: pulumi.Output[str]
    """
    Amazon Resource Name (ARN) of the configuration.
    """
    description: pulumi.Output[str]
    """
    Description of the configuration.
    """
    kafka_versions: pulumi.Output[list]
    """
    List of Apache Kafka versions which can use this configuration.
    """
    latest_revision: pulumi.Output[float]
    """
    Latest revision of the configuration.
    """
    name: pulumi.Output[str]
    """
    Name of the configuration.
    """
    server_properties: pulumi.Output[str]
    """
    Contents of the server.properties file. Supported properties are documented in the [MSK Developer Guide](https://docs.aws.amazon.com/msk/latest/developerguide/msk-configuration-properties.html).
    """
    def __init__(__self__, resource_name, opts=None, description=None, kafka_versions=None, name=None, server_properties=None, __props__=None, __name__=None, __opts__=None):
        """
        Manages an Amazon Managed Streaming for Kafka configuration. More information can be found on the [MSK Developer Guide](https://docs.aws.amazon.com/msk/latest/developerguide/msk-configuration.html).

        > **NOTE:** The API does not support deleting MSK configurations. Removing this resource will only remove the this provider state for it.



        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: Description of the configuration.
        :param pulumi.Input[list] kafka_versions: List of Apache Kafka versions which can use this configuration.
        :param pulumi.Input[str] name: Name of the configuration.
        :param pulumi.Input[str] server_properties: Contents of the server.properties file. Supported properties are documented in the [MSK Developer Guide](https://docs.aws.amazon.com/msk/latest/developerguide/msk-configuration-properties.html).
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

            __props__['description'] = description
            if kafka_versions is None:
                raise TypeError("Missing required property 'kafka_versions'")
            __props__['kafka_versions'] = kafka_versions
            __props__['name'] = name
            if server_properties is None:
                raise TypeError("Missing required property 'server_properties'")
            __props__['server_properties'] = server_properties
            __props__['arn'] = None
            __props__['latest_revision'] = None
        super(Configuration, __self__).__init__(
            'aws:msk/configuration:Configuration',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, arn=None, description=None, kafka_versions=None, latest_revision=None, name=None, server_properties=None):
        """
        Get an existing Configuration resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] arn: Amazon Resource Name (ARN) of the configuration.
        :param pulumi.Input[str] description: Description of the configuration.
        :param pulumi.Input[list] kafka_versions: List of Apache Kafka versions which can use this configuration.
        :param pulumi.Input[float] latest_revision: Latest revision of the configuration.
        :param pulumi.Input[str] name: Name of the configuration.
        :param pulumi.Input[str] server_properties: Contents of the server.properties file. Supported properties are documented in the [MSK Developer Guide](https://docs.aws.amazon.com/msk/latest/developerguide/msk-configuration-properties.html).
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["arn"] = arn
        __props__["description"] = description
        __props__["kafka_versions"] = kafka_versions
        __props__["latest_revision"] = latest_revision
        __props__["name"] = name
        __props__["server_properties"] = server_properties
        return Configuration(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

