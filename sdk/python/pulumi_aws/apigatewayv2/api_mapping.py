# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from .. import _utilities, _tables

__all__ = ['ApiMapping']


class ApiMapping(pulumi.CustomResource):
    api_id: pulumi.Output[str] = pulumi.property("apiId")
    """
    The API identifier.
    """

    api_mapping_key: pulumi.Output[Optional[str]] = pulumi.property("apiMappingKey")
    """
    The [API mapping key](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-mapping-template-reference.html).
    """

    domain_name: pulumi.Output[str] = pulumi.property("domainName")
    """
    The domain name. Use the `apigatewayv2.DomainName` resource to configure a domain name.
    """

    stage: pulumi.Output[str] = pulumi.property("stage")
    """
    The API stage. Use the `apigatewayv2.Stage` resource to configure an API stage.
    """

    def __init__(__self__,
                 resource_name,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 api_id: Optional[pulumi.Input[str]] = None,
                 api_mapping_key: Optional[pulumi.Input[str]] = None,
                 domain_name: Optional[pulumi.Input[str]] = None,
                 stage: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Manages an Amazon API Gateway Version 2 API mapping.
        More information can be found in the [Amazon API Gateway Developer Guide](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-custom-domains.html).

        ## Example Usage
        ### Basic

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.apigatewayv2.ApiMapping("example",
            api_id=aws_apigatewayv2_api["example"]["id"],
            domain_name=aws_apigatewayv2_domain_name["example"]["id"],
            stage=aws_apigatewayv2_stage["example"]["id"])
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] api_id: The API identifier.
        :param pulumi.Input[str] api_mapping_key: The [API mapping key](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-mapping-template-reference.html).
        :param pulumi.Input[str] domain_name: The domain name. Use the `apigatewayv2.DomainName` resource to configure a domain name.
        :param pulumi.Input[str] stage: The API stage. Use the `apigatewayv2.Stage` resource to configure an API stage.
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
            __props__['api_mapping_key'] = api_mapping_key
            if domain_name is None:
                raise TypeError("Missing required property 'domain_name'")
            __props__['domain_name'] = domain_name
            if stage is None:
                raise TypeError("Missing required property 'stage'")
            __props__['stage'] = stage
        super(ApiMapping, __self__).__init__(
            'aws:apigatewayv2/apiMapping:ApiMapping',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: str,
            opts: Optional[pulumi.ResourceOptions] = None,
            api_id: Optional[pulumi.Input[str]] = None,
            api_mapping_key: Optional[pulumi.Input[str]] = None,
            domain_name: Optional[pulumi.Input[str]] = None,
            stage: Optional[pulumi.Input[str]] = None) -> 'ApiMapping':
        """
        Get an existing ApiMapping resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] api_id: The API identifier.
        :param pulumi.Input[str] api_mapping_key: The [API mapping key](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-mapping-template-reference.html).
        :param pulumi.Input[str] domain_name: The domain name. Use the `apigatewayv2.DomainName` resource to configure a domain name.
        :param pulumi.Input[str] stage: The API stage. Use the `apigatewayv2.Stage` resource to configure an API stage.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["api_id"] = api_id
        __props__["api_mapping_key"] = api_mapping_key
        __props__["domain_name"] = domain_name
        __props__["stage"] = stage
        return ApiMapping(resource_name, opts=opts, __props__=__props__)

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

