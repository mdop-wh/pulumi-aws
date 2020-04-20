// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.AppAutoScaling.Inputs
{

    public sealed class PolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationGetArgs : Pulumi.ResourceArgs
    {
        [Input("dimensions")]
        private InputList<Inputs.PolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensionGetArgs>? _dimensions;
        public InputList<Inputs.PolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensionGetArgs> Dimensions
        {
            get => _dimensions ?? (_dimensions = new InputList<Inputs.PolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationDimensionGetArgs>());
            set => _dimensions = value;
        }

        [Input("metricName", required: true)]
        public Input<string> MetricName { get; set; } = null!;

        [Input("namespace", required: true)]
        public Input<string> Namespace { get; set; } = null!;

        [Input("statistic", required: true)]
        public Input<string> Statistic { get; set; } = null!;

        [Input("unit")]
        public Input<string>? Unit { get; set; }

        public PolicyTargetTrackingScalingPolicyConfigurationCustomizedMetricSpecificationGetArgs()
        {
        }
    }
}