// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.Sns
{
    /// <summary>
    /// Provides an SNS topic resource
    /// 
    /// ## Message Delivery Status Arguments
    /// 
    /// The `&lt;endpoint&gt;_success_feedback_role_arn` and `&lt;endpoint&gt;_failure_feedback_role_arn` arguments are used to give Amazon SNS write access to use CloudWatch Logs on your behalf. The `&lt;endpoint&gt;_success_feedback_sample_rate` argument is for specifying the sample rate percentage (0-100) of successfully delivered messages. After you configure the  `&lt;endpoint&gt;_failure_feedback_role_arn` argument, then all failed message deliveries generate CloudWatch Logs.
    /// 
    /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/sns_topic.html.markdown.
    /// </summary>
    public partial class Topic : Pulumi.CustomResource
    {
        /// <summary>
        /// IAM role for failure feedback
        /// </summary>
        [Output("applicationFailureFeedbackRoleArn")]
        public Output<string?> ApplicationFailureFeedbackRoleArn { get; private set; } = null!;

        /// <summary>
        /// The IAM role permitted to receive success feedback for this topic
        /// </summary>
        [Output("applicationSuccessFeedbackRoleArn")]
        public Output<string?> ApplicationSuccessFeedbackRoleArn { get; private set; } = null!;

        /// <summary>
        /// Percentage of success to sample
        /// </summary>
        [Output("applicationSuccessFeedbackSampleRate")]
        public Output<int?> ApplicationSuccessFeedbackSampleRate { get; private set; } = null!;

        /// <summary>
        /// The ARN of the SNS topic, as a more obvious property (clone of id)
        /// </summary>
        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        /// <summary>
        /// The SNS delivery policy. More on [AWS documentation](https://docs.aws.amazon.com/sns/latest/dg/DeliveryPolicies.html)
        /// </summary>
        [Output("deliveryPolicy")]
        public Output<string?> DeliveryPolicy { get; private set; } = null!;

        /// <summary>
        /// The display name for the SNS topic
        /// </summary>
        [Output("displayName")]
        public Output<string?> DisplayName { get; private set; } = null!;

        /// <summary>
        /// IAM role for failure feedback
        /// </summary>
        [Output("httpFailureFeedbackRoleArn")]
        public Output<string?> HttpFailureFeedbackRoleArn { get; private set; } = null!;

        /// <summary>
        /// The IAM role permitted to receive success feedback for this topic
        /// </summary>
        [Output("httpSuccessFeedbackRoleArn")]
        public Output<string?> HttpSuccessFeedbackRoleArn { get; private set; } = null!;

        /// <summary>
        /// Percentage of success to sample
        /// </summary>
        [Output("httpSuccessFeedbackSampleRate")]
        public Output<int?> HttpSuccessFeedbackSampleRate { get; private set; } = null!;

        /// <summary>
        /// The ID of an AWS-managed customer master key (CMK) for Amazon SNS or a custom CMK. For more information, see [Key Terms](https://docs.aws.amazon.com/sns/latest/dg/sns-server-side-encryption.html#sse-key-terms)
        /// </summary>
        [Output("kmsMasterKeyId")]
        public Output<string?> KmsMasterKeyId { get; private set; } = null!;

        /// <summary>
        /// IAM role for failure feedback
        /// </summary>
        [Output("lambdaFailureFeedbackRoleArn")]
        public Output<string?> LambdaFailureFeedbackRoleArn { get; private set; } = null!;

        /// <summary>
        /// The IAM role permitted to receive success feedback for this topic
        /// </summary>
        [Output("lambdaSuccessFeedbackRoleArn")]
        public Output<string?> LambdaSuccessFeedbackRoleArn { get; private set; } = null!;

        /// <summary>
        /// Percentage of success to sample
        /// </summary>
        [Output("lambdaSuccessFeedbackSampleRate")]
        public Output<int?> LambdaSuccessFeedbackSampleRate { get; private set; } = null!;

        /// <summary>
        /// The friendly name for the SNS topic. By default generated by this provider.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// The friendly name for the SNS topic. Conflicts with `name`.
        /// </summary>
        [Output("namePrefix")]
        public Output<string?> NamePrefix { get; private set; } = null!;

        /// <summary>
        /// The fully-formed AWS policy as JSON.
        /// </summary>
        [Output("policy")]
        public Output<string> Policy { get; private set; } = null!;

        /// <summary>
        /// IAM role for failure feedback
        /// </summary>
        [Output("sqsFailureFeedbackRoleArn")]
        public Output<string?> SqsFailureFeedbackRoleArn { get; private set; } = null!;

        /// <summary>
        /// The IAM role permitted to receive success feedback for this topic
        /// </summary>
        [Output("sqsSuccessFeedbackRoleArn")]
        public Output<string?> SqsSuccessFeedbackRoleArn { get; private set; } = null!;

        /// <summary>
        /// Percentage of success to sample
        /// </summary>
        [Output("sqsSuccessFeedbackSampleRate")]
        public Output<int?> SqsSuccessFeedbackSampleRate { get; private set; } = null!;

        /// <summary>
        /// Key-value mapping of resource tags
        /// </summary>
        [Output("tags")]
        public Output<ImmutableDictionary<string, object>?> Tags { get; private set; } = null!;


        /// <summary>
        /// Create a Topic resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Topic(string name, TopicArgs? args = null, CustomResourceOptions? options = null)
            : base("aws:sns/topic:Topic", name, args, MakeResourceOptions(options, ""))
        {
        }

        private Topic(string name, Input<string> id, TopicState? state = null, CustomResourceOptions? options = null)
            : base("aws:sns/topic:Topic", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing Topic resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Topic Get(string name, Input<string> id, TopicState? state = null, CustomResourceOptions? options = null)
        {
            return new Topic(name, id, state, options);
        }
    }

    public sealed class TopicArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// IAM role for failure feedback
        /// </summary>
        [Input("applicationFailureFeedbackRoleArn")]
        public Input<string>? ApplicationFailureFeedbackRoleArn { get; set; }

        /// <summary>
        /// The IAM role permitted to receive success feedback for this topic
        /// </summary>
        [Input("applicationSuccessFeedbackRoleArn")]
        public Input<string>? ApplicationSuccessFeedbackRoleArn { get; set; }

        /// <summary>
        /// Percentage of success to sample
        /// </summary>
        [Input("applicationSuccessFeedbackSampleRate")]
        public Input<int>? ApplicationSuccessFeedbackSampleRate { get; set; }

        /// <summary>
        /// The SNS delivery policy. More on [AWS documentation](https://docs.aws.amazon.com/sns/latest/dg/DeliveryPolicies.html)
        /// </summary>
        [Input("deliveryPolicy")]
        public Input<string>? DeliveryPolicy { get; set; }

        /// <summary>
        /// The display name for the SNS topic
        /// </summary>
        [Input("displayName")]
        public Input<string>? DisplayName { get; set; }

        /// <summary>
        /// IAM role for failure feedback
        /// </summary>
        [Input("httpFailureFeedbackRoleArn")]
        public Input<string>? HttpFailureFeedbackRoleArn { get; set; }

        /// <summary>
        /// The IAM role permitted to receive success feedback for this topic
        /// </summary>
        [Input("httpSuccessFeedbackRoleArn")]
        public Input<string>? HttpSuccessFeedbackRoleArn { get; set; }

        /// <summary>
        /// Percentage of success to sample
        /// </summary>
        [Input("httpSuccessFeedbackSampleRate")]
        public Input<int>? HttpSuccessFeedbackSampleRate { get; set; }

        /// <summary>
        /// The ID of an AWS-managed customer master key (CMK) for Amazon SNS or a custom CMK. For more information, see [Key Terms](https://docs.aws.amazon.com/sns/latest/dg/sns-server-side-encryption.html#sse-key-terms)
        /// </summary>
        [Input("kmsMasterKeyId")]
        public Input<string>? KmsMasterKeyId { get; set; }

        /// <summary>
        /// IAM role for failure feedback
        /// </summary>
        [Input("lambdaFailureFeedbackRoleArn")]
        public Input<string>? LambdaFailureFeedbackRoleArn { get; set; }

        /// <summary>
        /// The IAM role permitted to receive success feedback for this topic
        /// </summary>
        [Input("lambdaSuccessFeedbackRoleArn")]
        public Input<string>? LambdaSuccessFeedbackRoleArn { get; set; }

        /// <summary>
        /// Percentage of success to sample
        /// </summary>
        [Input("lambdaSuccessFeedbackSampleRate")]
        public Input<int>? LambdaSuccessFeedbackSampleRate { get; set; }

        /// <summary>
        /// The friendly name for the SNS topic. By default generated by this provider.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The friendly name for the SNS topic. Conflicts with `name`.
        /// </summary>
        [Input("namePrefix")]
        public Input<string>? NamePrefix { get; set; }

        /// <summary>
        /// The fully-formed AWS policy as JSON.
        /// </summary>
        [Input("policy")]
        public Input<string>? Policy { get; set; }

        /// <summary>
        /// IAM role for failure feedback
        /// </summary>
        [Input("sqsFailureFeedbackRoleArn")]
        public Input<string>? SqsFailureFeedbackRoleArn { get; set; }

        /// <summary>
        /// The IAM role permitted to receive success feedback for this topic
        /// </summary>
        [Input("sqsSuccessFeedbackRoleArn")]
        public Input<string>? SqsSuccessFeedbackRoleArn { get; set; }

        /// <summary>
        /// Percentage of success to sample
        /// </summary>
        [Input("sqsSuccessFeedbackSampleRate")]
        public Input<int>? SqsSuccessFeedbackSampleRate { get; set; }

        [Input("tags")]
        private InputMap<object>? _tags;

        /// <summary>
        /// Key-value mapping of resource tags
        /// </summary>
        public InputMap<object> Tags
        {
            get => _tags ?? (_tags = new InputMap<object>());
            set => _tags = value;
        }

        public TopicArgs()
        {
        }
    }

    public sealed class TopicState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// IAM role for failure feedback
        /// </summary>
        [Input("applicationFailureFeedbackRoleArn")]
        public Input<string>? ApplicationFailureFeedbackRoleArn { get; set; }

        /// <summary>
        /// The IAM role permitted to receive success feedback for this topic
        /// </summary>
        [Input("applicationSuccessFeedbackRoleArn")]
        public Input<string>? ApplicationSuccessFeedbackRoleArn { get; set; }

        /// <summary>
        /// Percentage of success to sample
        /// </summary>
        [Input("applicationSuccessFeedbackSampleRate")]
        public Input<int>? ApplicationSuccessFeedbackSampleRate { get; set; }

        /// <summary>
        /// The ARN of the SNS topic, as a more obvious property (clone of id)
        /// </summary>
        [Input("arn")]
        public Input<string>? Arn { get; set; }

        /// <summary>
        /// The SNS delivery policy. More on [AWS documentation](https://docs.aws.amazon.com/sns/latest/dg/DeliveryPolicies.html)
        /// </summary>
        [Input("deliveryPolicy")]
        public Input<string>? DeliveryPolicy { get; set; }

        /// <summary>
        /// The display name for the SNS topic
        /// </summary>
        [Input("displayName")]
        public Input<string>? DisplayName { get; set; }

        /// <summary>
        /// IAM role for failure feedback
        /// </summary>
        [Input("httpFailureFeedbackRoleArn")]
        public Input<string>? HttpFailureFeedbackRoleArn { get; set; }

        /// <summary>
        /// The IAM role permitted to receive success feedback for this topic
        /// </summary>
        [Input("httpSuccessFeedbackRoleArn")]
        public Input<string>? HttpSuccessFeedbackRoleArn { get; set; }

        /// <summary>
        /// Percentage of success to sample
        /// </summary>
        [Input("httpSuccessFeedbackSampleRate")]
        public Input<int>? HttpSuccessFeedbackSampleRate { get; set; }

        /// <summary>
        /// The ID of an AWS-managed customer master key (CMK) for Amazon SNS or a custom CMK. For more information, see [Key Terms](https://docs.aws.amazon.com/sns/latest/dg/sns-server-side-encryption.html#sse-key-terms)
        /// </summary>
        [Input("kmsMasterKeyId")]
        public Input<string>? KmsMasterKeyId { get; set; }

        /// <summary>
        /// IAM role for failure feedback
        /// </summary>
        [Input("lambdaFailureFeedbackRoleArn")]
        public Input<string>? LambdaFailureFeedbackRoleArn { get; set; }

        /// <summary>
        /// The IAM role permitted to receive success feedback for this topic
        /// </summary>
        [Input("lambdaSuccessFeedbackRoleArn")]
        public Input<string>? LambdaSuccessFeedbackRoleArn { get; set; }

        /// <summary>
        /// Percentage of success to sample
        /// </summary>
        [Input("lambdaSuccessFeedbackSampleRate")]
        public Input<int>? LambdaSuccessFeedbackSampleRate { get; set; }

        /// <summary>
        /// The friendly name for the SNS topic. By default generated by this provider.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The friendly name for the SNS topic. Conflicts with `name`.
        /// </summary>
        [Input("namePrefix")]
        public Input<string>? NamePrefix { get; set; }

        /// <summary>
        /// The fully-formed AWS policy as JSON.
        /// </summary>
        [Input("policy")]
        public Input<string>? Policy { get; set; }

        /// <summary>
        /// IAM role for failure feedback
        /// </summary>
        [Input("sqsFailureFeedbackRoleArn")]
        public Input<string>? SqsFailureFeedbackRoleArn { get; set; }

        /// <summary>
        /// The IAM role permitted to receive success feedback for this topic
        /// </summary>
        [Input("sqsSuccessFeedbackRoleArn")]
        public Input<string>? SqsSuccessFeedbackRoleArn { get; set; }

        /// <summary>
        /// Percentage of success to sample
        /// </summary>
        [Input("sqsSuccessFeedbackSampleRate")]
        public Input<int>? SqsSuccessFeedbackSampleRate { get; set; }

        [Input("tags")]
        private InputMap<object>? _tags;

        /// <summary>
        /// Key-value mapping of resource tags
        /// </summary>
        public InputMap<object> Tags
        {
            get => _tags ?? (_tags = new InputMap<object>());
            set => _tags = value;
        }

        public TopicState()
        {
        }
    }
}
