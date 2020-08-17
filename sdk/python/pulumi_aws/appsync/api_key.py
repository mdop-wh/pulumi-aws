# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from .. import _utilities, _tables

__all__ = ['ApiKey']


class ApiKey(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 api_id: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 expires: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides an AppSync API Key.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example_graph_ql_api = aws.appsync.GraphQLApi("exampleGraphQLApi", authentication_type="API_KEY")
        example_api_key = aws.appsync.ApiKey("exampleApiKey",
            api_id=example_graph_ql_api.id,
            expires="2018-05-03T04:00:00Z")
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] api_id: The ID of the associated AppSync API
        :param pulumi.Input[str] description: The API key description. Defaults to "Managed by Pulumi".
        :param pulumi.Input[str] expires: RFC3339 string representation of the expiry date. Rounded down to nearest hour. By default, it is 7 days from the date of creation.
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

            if api_id is None:
                raise TypeError("Missing required property 'api_id'")
            __props__['api_id'] = api_id
            if description is None:
                description = 'Managed by Pulumi'
            __props__['description'] = description
            __props__['expires'] = expires
            __props__['key'] = None
        super(ApiKey, __self__).__init__(
            'aws:appsync/apiKey:ApiKey',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: str,
            opts: Optional[pulumi.ResourceOptions] = None,
            api_id: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            expires: Optional[pulumi.Input[str]] = None,
            key: Optional[pulumi.Input[str]] = None) -> 'ApiKey':
        """
        Get an existing ApiKey resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] api_id: The ID of the associated AppSync API
        :param pulumi.Input[str] description: The API key description. Defaults to "Managed by Pulumi".
        :param pulumi.Input[str] expires: RFC3339 string representation of the expiry date. Rounded down to nearest hour. By default, it is 7 days from the date of creation.
        :param pulumi.Input[str] key: The API key
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["api_id"] = api_id
        __props__["description"] = description
        __props__["expires"] = expires
        __props__["key"] = key
        return ApiKey(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="apiId")
    def api_id(self) -> str:
        """
        The ID of the associated AppSync API
        """
        ...

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        The API key description. Defaults to "Managed by Pulumi".
        """
        ...

    @property
    @pulumi.getter
    def expires(self) -> Optional[str]:
        """
        RFC3339 string representation of the expiry date. Rounded down to nearest hour. By default, it is 7 days from the date of creation.
        """
        ...

    @property
    @pulumi.getter
    def key(self) -> str:
        """
        The API key
        """
        ...

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

