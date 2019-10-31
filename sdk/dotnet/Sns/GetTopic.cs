// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.Sns
{
    public static partial class Invokes
    {
        /// <summary>
        /// Use this data source to get the ARN of a topic in AWS Simple Notification
        /// Service (SNS). By using this data source, you can reference SNS topics
        /// without having to hard code the ARNs as input.
        /// 
        /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/sns_topic.html.markdown.
        /// </summary>
        public static Task<GetTopicResult> GetTopic(GetTopicArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetTopicResult>("aws:sns/getTopic:getTopic", args, options.WithVersion());
    }

    public sealed class GetTopicArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The friendly name of the topic to match.
        /// </summary>
        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        public GetTopicArgs()
        {
        }
    }

    [OutputType]
    public sealed class GetTopicResult
    {
        /// <summary>
        /// Set to the ARN of the found topic, suitable for referencing in other resources that support SNS topics.
        /// </summary>
        public readonly string Arn;
        public readonly string Name;
        /// <summary>
        /// id is the provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;

        [OutputConstructor]
        private GetTopicResult(
            string arn,
            string name,
            string id)
        {
            Arn = arn;
            Name = name;
            Id = id;
        }
    }
}
