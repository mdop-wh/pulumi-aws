// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.Autoscaling
{
    /// <summary>
    /// Provides an AutoScaling Lifecycle Hook resource.
    /// 
    /// &gt; **NOTE:** This provider has two types of ways you can add lifecycle hooks - via
    /// the `initial_lifecycle_hook` attribute from the
    /// [`aws.autoscaling.Group`](https://www.terraform.io/docs/providers/aws/r/autoscaling_group.html)
    /// resource, or via this one. Hooks added via this resource will not be added
    /// until the autoscaling group has been created, and depending on your
    /// [capacity](https://www.terraform.io/docs/providers/aws/r/autoscaling_group.html#waiting-for-capacity)
    /// settings, after the initial instances have been launched, creating unintended
    /// behavior. If you need hooks to run on all instances, add them with
    /// `initial_lifecycle_hook` in
    /// [`aws.autoscaling.Group`](https://www.terraform.io/docs/providers/aws/r/autoscaling_group.html),
    /// but take care to not duplicate those hooks with this resource.
    /// 
    /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/autoscaling_lifecycle_hook.html.markdown.
    /// </summary>
    public partial class LifecycleHook : Pulumi.CustomResource
    {
        /// <summary>
        /// The name of the Auto Scaling group to which you want to assign the lifecycle hook
        /// </summary>
        [Output("autoscalingGroupName")]
        public Output<string> AutoscalingGroupName { get; private set; } = null!;

        /// <summary>
        /// Defines the action the Auto Scaling group should take when the lifecycle hook timeout elapses or if an unexpected failure occurs. The value for this parameter can be either CONTINUE or ABANDON. The default value for this parameter is ABANDON.
        /// </summary>
        [Output("defaultResult")]
        public Output<string> DefaultResult { get; private set; } = null!;

        /// <summary>
        /// Defines the amount of time, in seconds, that can elapse before the lifecycle hook times out. When the lifecycle hook times out, Auto Scaling performs the action defined in the DefaultResult parameter
        /// </summary>
        [Output("heartbeatTimeout")]
        public Output<int?> HeartbeatTimeout { get; private set; } = null!;

        /// <summary>
        /// The instance state to which you want to attach the lifecycle hook. For a list of lifecycle hook types, see [describe-lifecycle-hook-types](https://docs.aws.amazon.com/cli/latest/reference/autoscaling/describe-lifecycle-hook-types.html#examples)
        /// </summary>
        [Output("lifecycleTransition")]
        public Output<string> LifecycleTransition { get; private set; } = null!;

        /// <summary>
        /// The name of the lifecycle hook.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// Contains additional information that you want to include any time Auto Scaling sends a message to the notification target.
        /// </summary>
        [Output("notificationMetadata")]
        public Output<string?> NotificationMetadata { get; private set; } = null!;

        /// <summary>
        /// The ARN of the notification target that Auto Scaling will use to notify you when an instance is in the transition state for the lifecycle hook. This ARN target can be either an SQS queue or an SNS topic.
        /// </summary>
        [Output("notificationTargetArn")]
        public Output<string?> NotificationTargetArn { get; private set; } = null!;

        /// <summary>
        /// The ARN of the IAM role that allows the Auto Scaling group to publish to the specified notification target.
        /// </summary>
        [Output("roleArn")]
        public Output<string?> RoleArn { get; private set; } = null!;


        /// <summary>
        /// Create a LifecycleHook resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public LifecycleHook(string name, LifecycleHookArgs args, CustomResourceOptions? options = null)
            : base("aws:autoscaling/lifecycleHook:LifecycleHook", name, args, MakeResourceOptions(options, ""))
        {
        }

        private LifecycleHook(string name, Input<string> id, LifecycleHookState? state = null, CustomResourceOptions? options = null)
            : base("aws:autoscaling/lifecycleHook:LifecycleHook", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing LifecycleHook resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static LifecycleHook Get(string name, Input<string> id, LifecycleHookState? state = null, CustomResourceOptions? options = null)
        {
            return new LifecycleHook(name, id, state, options);
        }
    }

    public sealed class LifecycleHookArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The name of the Auto Scaling group to which you want to assign the lifecycle hook
        /// </summary>
        [Input("autoscalingGroupName", required: true)]
        public Input<string> AutoscalingGroupName { get; set; } = null!;

        /// <summary>
        /// Defines the action the Auto Scaling group should take when the lifecycle hook timeout elapses or if an unexpected failure occurs. The value for this parameter can be either CONTINUE or ABANDON. The default value for this parameter is ABANDON.
        /// </summary>
        [Input("defaultResult")]
        public Input<string>? DefaultResult { get; set; }

        /// <summary>
        /// Defines the amount of time, in seconds, that can elapse before the lifecycle hook times out. When the lifecycle hook times out, Auto Scaling performs the action defined in the DefaultResult parameter
        /// </summary>
        [Input("heartbeatTimeout")]
        public Input<int>? HeartbeatTimeout { get; set; }

        /// <summary>
        /// The instance state to which you want to attach the lifecycle hook. For a list of lifecycle hook types, see [describe-lifecycle-hook-types](https://docs.aws.amazon.com/cli/latest/reference/autoscaling/describe-lifecycle-hook-types.html#examples)
        /// </summary>
        [Input("lifecycleTransition", required: true)]
        public Input<string> LifecycleTransition { get; set; } = null!;

        /// <summary>
        /// The name of the lifecycle hook.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// Contains additional information that you want to include any time Auto Scaling sends a message to the notification target.
        /// </summary>
        [Input("notificationMetadata")]
        public Input<string>? NotificationMetadata { get; set; }

        /// <summary>
        /// The ARN of the notification target that Auto Scaling will use to notify you when an instance is in the transition state for the lifecycle hook. This ARN target can be either an SQS queue or an SNS topic.
        /// </summary>
        [Input("notificationTargetArn")]
        public Input<string>? NotificationTargetArn { get; set; }

        /// <summary>
        /// The ARN of the IAM role that allows the Auto Scaling group to publish to the specified notification target.
        /// </summary>
        [Input("roleArn")]
        public Input<string>? RoleArn { get; set; }

        public LifecycleHookArgs()
        {
        }
    }

    public sealed class LifecycleHookState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The name of the Auto Scaling group to which you want to assign the lifecycle hook
        /// </summary>
        [Input("autoscalingGroupName")]
        public Input<string>? AutoscalingGroupName { get; set; }

        /// <summary>
        /// Defines the action the Auto Scaling group should take when the lifecycle hook timeout elapses or if an unexpected failure occurs. The value for this parameter can be either CONTINUE or ABANDON. The default value for this parameter is ABANDON.
        /// </summary>
        [Input("defaultResult")]
        public Input<string>? DefaultResult { get; set; }

        /// <summary>
        /// Defines the amount of time, in seconds, that can elapse before the lifecycle hook times out. When the lifecycle hook times out, Auto Scaling performs the action defined in the DefaultResult parameter
        /// </summary>
        [Input("heartbeatTimeout")]
        public Input<int>? HeartbeatTimeout { get; set; }

        /// <summary>
        /// The instance state to which you want to attach the lifecycle hook. For a list of lifecycle hook types, see [describe-lifecycle-hook-types](https://docs.aws.amazon.com/cli/latest/reference/autoscaling/describe-lifecycle-hook-types.html#examples)
        /// </summary>
        [Input("lifecycleTransition")]
        public Input<string>? LifecycleTransition { get; set; }

        /// <summary>
        /// The name of the lifecycle hook.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// Contains additional information that you want to include any time Auto Scaling sends a message to the notification target.
        /// </summary>
        [Input("notificationMetadata")]
        public Input<string>? NotificationMetadata { get; set; }

        /// <summary>
        /// The ARN of the notification target that Auto Scaling will use to notify you when an instance is in the transition state for the lifecycle hook. This ARN target can be either an SQS queue or an SNS topic.
        /// </summary>
        [Input("notificationTargetArn")]
        public Input<string>? NotificationTargetArn { get; set; }

        /// <summary>
        /// The ARN of the IAM role that allows the Auto Scaling group to publish to the specified notification target.
        /// </summary>
        [Input("roleArn")]
        public Input<string>? RoleArn { get; set; }

        public LifecycleHookState()
        {
        }
    }
}
