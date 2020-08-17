# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from .. import _utilities, _tables

__all__ = ['ServiceQuota']


class ServiceQuota(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 quota_code: Optional[pulumi.Input[str]] = None,
                 service_code: Optional[pulumi.Input[str]] = None,
                 value: Optional[pulumi.Input[float]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Manages an individual Service Quota.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.servicequotas.ServiceQuota("example",
            quota_code="L-F678F1CE",
            service_code="vpc",
            value=75)
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] quota_code: Code of the service quota to track. For example: `L-F678F1CE`. Available values can be found with the [AWS CLI service-quotas list-service-quotas command](https://docs.aws.amazon.com/cli/latest/reference/service-quotas/list-service-quotas.html).
        :param pulumi.Input[str] service_code: Code of the service to track. For example: `vpc`. Available values can be found with the [AWS CLI service-quotas list-services command](https://docs.aws.amazon.com/cli/latest/reference/service-quotas/list-services.html).
        :param pulumi.Input[float] value: Float specifying the desired value for the service quota. If the desired value is higher than the current value, a quota increase request is submitted. When a known request is submitted and pending, the value reflects the desired value of the pending request.
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

            if quota_code is None:
                raise TypeError("Missing required property 'quota_code'")
            __props__['quota_code'] = quota_code
            if service_code is None:
                raise TypeError("Missing required property 'service_code'")
            __props__['service_code'] = service_code
            if value is None:
                raise TypeError("Missing required property 'value'")
            __props__['value'] = value
            __props__['adjustable'] = None
            __props__['arn'] = None
            __props__['default_value'] = None
            __props__['quota_name'] = None
            __props__['request_id'] = None
            __props__['request_status'] = None
            __props__['service_name'] = None
        super(ServiceQuota, __self__).__init__(
            'aws:servicequotas/serviceQuota:ServiceQuota',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: str,
            opts: Optional[pulumi.ResourceOptions] = None,
            adjustable: Optional[pulumi.Input[bool]] = None,
            arn: Optional[pulumi.Input[str]] = None,
            default_value: Optional[pulumi.Input[float]] = None,
            quota_code: Optional[pulumi.Input[str]] = None,
            quota_name: Optional[pulumi.Input[str]] = None,
            request_id: Optional[pulumi.Input[str]] = None,
            request_status: Optional[pulumi.Input[str]] = None,
            service_code: Optional[pulumi.Input[str]] = None,
            service_name: Optional[pulumi.Input[str]] = None,
            value: Optional[pulumi.Input[float]] = None) -> 'ServiceQuota':
        """
        Get an existing ServiceQuota resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] adjustable: Whether the service quota can be increased.
        :param pulumi.Input[str] arn: Amazon Resource Name (ARN) of the service quota.
        :param pulumi.Input[float] default_value: Default value of the service quota.
        :param pulumi.Input[str] quota_code: Code of the service quota to track. For example: `L-F678F1CE`. Available values can be found with the [AWS CLI service-quotas list-service-quotas command](https://docs.aws.amazon.com/cli/latest/reference/service-quotas/list-service-quotas.html).
        :param pulumi.Input[str] quota_name: Name of the quota.
        :param pulumi.Input[str] service_code: Code of the service to track. For example: `vpc`. Available values can be found with the [AWS CLI service-quotas list-services command](https://docs.aws.amazon.com/cli/latest/reference/service-quotas/list-services.html).
        :param pulumi.Input[str] service_name: Name of the service.
        :param pulumi.Input[float] value: Float specifying the desired value for the service quota. If the desired value is higher than the current value, a quota increase request is submitted. When a known request is submitted and pending, the value reflects the desired value of the pending request.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["adjustable"] = adjustable
        __props__["arn"] = arn
        __props__["default_value"] = default_value
        __props__["quota_code"] = quota_code
        __props__["quota_name"] = quota_name
        __props__["request_id"] = request_id
        __props__["request_status"] = request_status
        __props__["service_code"] = service_code
        __props__["service_name"] = service_name
        __props__["value"] = value
        return ServiceQuota(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def adjustable(self) -> bool:
        """
        Whether the service quota can be increased.
        """
        ...

    @property
    @pulumi.getter
    def arn(self) -> str:
        """
        Amazon Resource Name (ARN) of the service quota.
        """
        ...

    @property
    @pulumi.getter(name="defaultValue")
    def default_value(self) -> float:
        """
        Default value of the service quota.
        """
        ...

    @property
    @pulumi.getter(name="quotaCode")
    def quota_code(self) -> str:
        """
        Code of the service quota to track. For example: `L-F678F1CE`. Available values can be found with the [AWS CLI service-quotas list-service-quotas command](https://docs.aws.amazon.com/cli/latest/reference/service-quotas/list-service-quotas.html).
        """
        ...

    @property
    @pulumi.getter(name="quotaName")
    def quota_name(self) -> str:
        """
        Name of the quota.
        """
        ...

    @property
    @pulumi.getter(name="requestId")
    def request_id(self) -> str:
        ...

    @property
    @pulumi.getter(name="requestStatus")
    def request_status(self) -> str:
        ...

    @property
    @pulumi.getter(name="serviceCode")
    def service_code(self) -> str:
        """
        Code of the service to track. For example: `vpc`. Available values can be found with the [AWS CLI service-quotas list-services command](https://docs.aws.amazon.com/cli/latest/reference/service-quotas/list-services.html).
        """
        ...

    @property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> str:
        """
        Name of the service.
        """
        ...

    @property
    @pulumi.getter
    def value(self) -> float:
        """
        Float specifying the desired value for the service quota. If the desired value is higher than the current value, a quota increase request is submitted. When a known request is submitted and pending, the value reflects the desired value of the pending request.
        """
        ...

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

