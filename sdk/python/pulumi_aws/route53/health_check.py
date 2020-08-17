# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from .. import _utilities, _tables

__all__ = ['HealthCheck']


class HealthCheck(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 child_health_threshold: Optional[pulumi.Input[float]] = None,
                 child_healthchecks: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None,
                 cloudwatch_alarm_name: Optional[pulumi.Input[str]] = None,
                 cloudwatch_alarm_region: Optional[pulumi.Input[str]] = None,
                 enable_sni: Optional[pulumi.Input[bool]] = None,
                 failure_threshold: Optional[pulumi.Input[float]] = None,
                 fqdn: Optional[pulumi.Input[str]] = None,
                 insufficient_data_health_status: Optional[pulumi.Input[str]] = None,
                 invert_healthcheck: Optional[pulumi.Input[bool]] = None,
                 ip_address: Optional[pulumi.Input[str]] = None,
                 measure_latency: Optional[pulumi.Input[bool]] = None,
                 port: Optional[pulumi.Input[float]] = None,
                 reference_name: Optional[pulumi.Input[str]] = None,
                 regions: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None,
                 request_interval: Optional[pulumi.Input[float]] = None,
                 resource_path: Optional[pulumi.Input[str]] = None,
                 search_string: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides a Route53 health check.

        ## Example Usage
        ### Connectivity and HTTP Status Code Check

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.route53.HealthCheck("example",
            failure_threshold=5,
            fqdn="example.com",
            port=80,
            request_interval=30,
            resource_path="/",
            tags={
                "Name": "tf-test-health-check",
            },
            type="HTTP")
        ```
        ### Connectivity and String Matching Check

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.route53.HealthCheck("example",
            failure_threshold=5,
            fqdn="example.com",
            port=443,
            request_interval=30,
            resource_path="/",
            search_string="example",
            type="HTTPS_STR_MATCH")
        ```
        ### Aggregate Check

        ```python
        import pulumi
        import pulumi_aws as aws

        parent = aws.route53.HealthCheck("parent",
            child_health_threshold=1,
            child_healthchecks=[aws_route53_health_check["child"]["id"]],
            tags={
                "Name": "tf-test-calculated-health-check",
            },
            type="CALCULATED")
        ```
        ### CloudWatch Alarm Check

        ```python
        import pulumi
        import pulumi_aws as aws

        foobar = aws.cloudwatch.MetricAlarm("foobar",
            alarm_description="This metric monitors ec2 cpu utilization",
            comparison_operator="GreaterThanOrEqualToThreshold",
            evaluation_periods=2,
            metric_name="CPUUtilization",
            namespace="AWS/EC2",
            period=120,
            statistic="Average",
            threshold=80)
        foo = aws.route53.HealthCheck("foo",
            cloudwatch_alarm_name=foobar.name,
            cloudwatch_alarm_region="us-west-2",
            insufficient_data_health_status="Healthy",
            type="CLOUDWATCH_METRIC")
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[float] child_health_threshold: The minimum number of child health checks that must be healthy for Route 53 to consider the parent health check to be healthy. Valid values are integers between 0 and 256, inclusive
        :param pulumi.Input[List[pulumi.Input[str]]] child_healthchecks: For a specified parent health check, a list of HealthCheckId values for the associated child health checks.
        :param pulumi.Input[str] cloudwatch_alarm_name: The name of the CloudWatch alarm.
        :param pulumi.Input[str] cloudwatch_alarm_region: The CloudWatchRegion that the CloudWatch alarm was created in.
        :param pulumi.Input[bool] enable_sni: A boolean value that indicates whether Route53 should send the `fqdn` to the endpoint when performing the health check. This defaults to AWS' defaults: when the `type` is "HTTPS" `enable_sni` defaults to `true`, when `type` is anything else `enable_sni` defaults to `false`.
        :param pulumi.Input[float] failure_threshold: The number of consecutive health checks that an endpoint must pass or fail.
        :param pulumi.Input[str] fqdn: The fully qualified domain name of the endpoint to be checked.
        :param pulumi.Input[str] insufficient_data_health_status: The status of the health check when CloudWatch has insufficient data about the state of associated alarm. Valid values are `Healthy` , `Unhealthy` and `LastKnownStatus`.
        :param pulumi.Input[bool] invert_healthcheck: A boolean value that indicates whether the status of health check should be inverted. For example, if a health check is healthy but Inverted is True , then Route 53 considers the health check to be unhealthy.
        :param pulumi.Input[str] ip_address: The IP address of the endpoint to be checked.
        :param pulumi.Input[bool] measure_latency: A Boolean value that indicates whether you want Route 53 to measure the latency between health checkers in multiple AWS regions and your endpoint and to display CloudWatch latency graphs in the Route 53 console.
        :param pulumi.Input[float] port: The port of the endpoint to be checked.
        :param pulumi.Input[str] reference_name: This is a reference name used in Caller Reference
               (helpful for identifying single health_check set amongst others)
        :param pulumi.Input[List[pulumi.Input[str]]] regions: A list of AWS regions that you want Amazon Route 53 health checkers to check the specified endpoint from.
        :param pulumi.Input[float] request_interval: The number of seconds between the time that Amazon Route 53 gets a response from your endpoint and the time that it sends the next health-check request.
        :param pulumi.Input[str] resource_path: The path that you want Amazon Route 53 to request when performing health checks.
        :param pulumi.Input[str] search_string: String searched in the first 5120 bytes of the response body for check to be considered healthy. Only valid with `HTTP_STR_MATCH` and `HTTPS_STR_MATCH`.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the health check.
        :param pulumi.Input[str] type: The protocol to use when performing health checks. Valid values are `HTTP`, `HTTPS`, `HTTP_STR_MATCH`, `HTTPS_STR_MATCH`, `TCP`, `CALCULATED` and `CLOUDWATCH_METRIC`.
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

            __props__['child_health_threshold'] = child_health_threshold
            __props__['child_healthchecks'] = child_healthchecks
            __props__['cloudwatch_alarm_name'] = cloudwatch_alarm_name
            __props__['cloudwatch_alarm_region'] = cloudwatch_alarm_region
            __props__['enable_sni'] = enable_sni
            __props__['failure_threshold'] = failure_threshold
            __props__['fqdn'] = fqdn
            __props__['insufficient_data_health_status'] = insufficient_data_health_status
            __props__['invert_healthcheck'] = invert_healthcheck
            __props__['ip_address'] = ip_address
            __props__['measure_latency'] = measure_latency
            __props__['port'] = port
            __props__['reference_name'] = reference_name
            __props__['regions'] = regions
            __props__['request_interval'] = request_interval
            __props__['resource_path'] = resource_path
            __props__['search_string'] = search_string
            __props__['tags'] = tags
            if type is None:
                raise TypeError("Missing required property 'type'")
            __props__['type'] = type
        super(HealthCheck, __self__).__init__(
            'aws:route53/healthCheck:HealthCheck',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: str,
            opts: Optional[pulumi.ResourceOptions] = None,
            child_health_threshold: Optional[pulumi.Input[float]] = None,
            child_healthchecks: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None,
            cloudwatch_alarm_name: Optional[pulumi.Input[str]] = None,
            cloudwatch_alarm_region: Optional[pulumi.Input[str]] = None,
            enable_sni: Optional[pulumi.Input[bool]] = None,
            failure_threshold: Optional[pulumi.Input[float]] = None,
            fqdn: Optional[pulumi.Input[str]] = None,
            insufficient_data_health_status: Optional[pulumi.Input[str]] = None,
            invert_healthcheck: Optional[pulumi.Input[bool]] = None,
            ip_address: Optional[pulumi.Input[str]] = None,
            measure_latency: Optional[pulumi.Input[bool]] = None,
            port: Optional[pulumi.Input[float]] = None,
            reference_name: Optional[pulumi.Input[str]] = None,
            regions: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None,
            request_interval: Optional[pulumi.Input[float]] = None,
            resource_path: Optional[pulumi.Input[str]] = None,
            search_string: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            type: Optional[pulumi.Input[str]] = None) -> 'HealthCheck':
        """
        Get an existing HealthCheck resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[float] child_health_threshold: The minimum number of child health checks that must be healthy for Route 53 to consider the parent health check to be healthy. Valid values are integers between 0 and 256, inclusive
        :param pulumi.Input[List[pulumi.Input[str]]] child_healthchecks: For a specified parent health check, a list of HealthCheckId values for the associated child health checks.
        :param pulumi.Input[str] cloudwatch_alarm_name: The name of the CloudWatch alarm.
        :param pulumi.Input[str] cloudwatch_alarm_region: The CloudWatchRegion that the CloudWatch alarm was created in.
        :param pulumi.Input[bool] enable_sni: A boolean value that indicates whether Route53 should send the `fqdn` to the endpoint when performing the health check. This defaults to AWS' defaults: when the `type` is "HTTPS" `enable_sni` defaults to `true`, when `type` is anything else `enable_sni` defaults to `false`.
        :param pulumi.Input[float] failure_threshold: The number of consecutive health checks that an endpoint must pass or fail.
        :param pulumi.Input[str] fqdn: The fully qualified domain name of the endpoint to be checked.
        :param pulumi.Input[str] insufficient_data_health_status: The status of the health check when CloudWatch has insufficient data about the state of associated alarm. Valid values are `Healthy` , `Unhealthy` and `LastKnownStatus`.
        :param pulumi.Input[bool] invert_healthcheck: A boolean value that indicates whether the status of health check should be inverted. For example, if a health check is healthy but Inverted is True , then Route 53 considers the health check to be unhealthy.
        :param pulumi.Input[str] ip_address: The IP address of the endpoint to be checked.
        :param pulumi.Input[bool] measure_latency: A Boolean value that indicates whether you want Route 53 to measure the latency between health checkers in multiple AWS regions and your endpoint and to display CloudWatch latency graphs in the Route 53 console.
        :param pulumi.Input[float] port: The port of the endpoint to be checked.
        :param pulumi.Input[str] reference_name: This is a reference name used in Caller Reference
               (helpful for identifying single health_check set amongst others)
        :param pulumi.Input[List[pulumi.Input[str]]] regions: A list of AWS regions that you want Amazon Route 53 health checkers to check the specified endpoint from.
        :param pulumi.Input[float] request_interval: The number of seconds between the time that Amazon Route 53 gets a response from your endpoint and the time that it sends the next health-check request.
        :param pulumi.Input[str] resource_path: The path that you want Amazon Route 53 to request when performing health checks.
        :param pulumi.Input[str] search_string: String searched in the first 5120 bytes of the response body for check to be considered healthy. Only valid with `HTTP_STR_MATCH` and `HTTPS_STR_MATCH`.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the health check.
        :param pulumi.Input[str] type: The protocol to use when performing health checks. Valid values are `HTTP`, `HTTPS`, `HTTP_STR_MATCH`, `HTTPS_STR_MATCH`, `TCP`, `CALCULATED` and `CLOUDWATCH_METRIC`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["child_health_threshold"] = child_health_threshold
        __props__["child_healthchecks"] = child_healthchecks
        __props__["cloudwatch_alarm_name"] = cloudwatch_alarm_name
        __props__["cloudwatch_alarm_region"] = cloudwatch_alarm_region
        __props__["enable_sni"] = enable_sni
        __props__["failure_threshold"] = failure_threshold
        __props__["fqdn"] = fqdn
        __props__["insufficient_data_health_status"] = insufficient_data_health_status
        __props__["invert_healthcheck"] = invert_healthcheck
        __props__["ip_address"] = ip_address
        __props__["measure_latency"] = measure_latency
        __props__["port"] = port
        __props__["reference_name"] = reference_name
        __props__["regions"] = regions
        __props__["request_interval"] = request_interval
        __props__["resource_path"] = resource_path
        __props__["search_string"] = search_string
        __props__["tags"] = tags
        __props__["type"] = type
        return HealthCheck(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="childHealthThreshold")
    def child_health_threshold(self) -> Optional[float]:
        """
        The minimum number of child health checks that must be healthy for Route 53 to consider the parent health check to be healthy. Valid values are integers between 0 and 256, inclusive
        """
        ...

    @property
    @pulumi.getter(name="childHealthchecks")
    def child_healthchecks(self) -> Optional[List[str]]:
        """
        For a specified parent health check, a list of HealthCheckId values for the associated child health checks.
        """
        ...

    @property
    @pulumi.getter(name="cloudwatchAlarmName")
    def cloudwatch_alarm_name(self) -> Optional[str]:
        """
        The name of the CloudWatch alarm.
        """
        ...

    @property
    @pulumi.getter(name="cloudwatchAlarmRegion")
    def cloudwatch_alarm_region(self) -> Optional[str]:
        """
        The CloudWatchRegion that the CloudWatch alarm was created in.
        """
        ...

    @property
    @pulumi.getter(name="enableSni")
    def enable_sni(self) -> bool:
        """
        A boolean value that indicates whether Route53 should send the `fqdn` to the endpoint when performing the health check. This defaults to AWS' defaults: when the `type` is "HTTPS" `enable_sni` defaults to `true`, when `type` is anything else `enable_sni` defaults to `false`.
        """
        ...

    @property
    @pulumi.getter(name="failureThreshold")
    def failure_threshold(self) -> Optional[float]:
        """
        The number of consecutive health checks that an endpoint must pass or fail.
        """
        ...

    @property
    @pulumi.getter
    def fqdn(self) -> Optional[str]:
        """
        The fully qualified domain name of the endpoint to be checked.
        """
        ...

    @property
    @pulumi.getter(name="insufficientDataHealthStatus")
    def insufficient_data_health_status(self) -> Optional[str]:
        """
        The status of the health check when CloudWatch has insufficient data about the state of associated alarm. Valid values are `Healthy` , `Unhealthy` and `LastKnownStatus`.
        """
        ...

    @property
    @pulumi.getter(name="invertHealthcheck")
    def invert_healthcheck(self) -> Optional[bool]:
        """
        A boolean value that indicates whether the status of health check should be inverted. For example, if a health check is healthy but Inverted is True , then Route 53 considers the health check to be unhealthy.
        """
        ...

    @property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> Optional[str]:
        """
        The IP address of the endpoint to be checked.
        """
        ...

    @property
    @pulumi.getter(name="measureLatency")
    def measure_latency(self) -> Optional[bool]:
        """
        A Boolean value that indicates whether you want Route 53 to measure the latency between health checkers in multiple AWS regions and your endpoint and to display CloudWatch latency graphs in the Route 53 console.
        """
        ...

    @property
    @pulumi.getter
    def port(self) -> Optional[float]:
        """
        The port of the endpoint to be checked.
        """
        ...

    @property
    @pulumi.getter(name="referenceName")
    def reference_name(self) -> Optional[str]:
        """
        This is a reference name used in Caller Reference
        (helpful for identifying single health_check set amongst others)
        """
        ...

    @property
    @pulumi.getter
    def regions(self) -> Optional[List[str]]:
        """
        A list of AWS regions that you want Amazon Route 53 health checkers to check the specified endpoint from.
        """
        ...

    @property
    @pulumi.getter(name="requestInterval")
    def request_interval(self) -> Optional[float]:
        """
        The number of seconds between the time that Amazon Route 53 gets a response from your endpoint and the time that it sends the next health-check request.
        """
        ...

    @property
    @pulumi.getter(name="resourcePath")
    def resource_path(self) -> Optional[str]:
        """
        The path that you want Amazon Route 53 to request when performing health checks.
        """
        ...

    @property
    @pulumi.getter(name="searchString")
    def search_string(self) -> Optional[str]:
        """
        String searched in the first 5120 bytes of the response body for check to be considered healthy. Only valid with `HTTP_STR_MATCH` and `HTTPS_STR_MATCH`.
        """
        ...

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        A map of tags to assign to the health check.
        """
        ...

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The protocol to use when performing health checks. Valid values are `HTTP`, `HTTPS`, `HTTP_STR_MATCH`, `HTTPS_STR_MATCH`, `TCP`, `CALCULATED` and `CLOUDWATCH_METRIC`.
        """
        ...

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

