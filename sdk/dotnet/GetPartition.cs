// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws
{
    public static partial class Invokes
    {
        /// <summary>
        /// Use this data source to lookup current AWS partition in which this provider is working
        /// 
        /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/partition.html.markdown.
        /// </summary>
        public static Task<GetPartitionResult> GetPartition(InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetPartitionResult>("aws:index/getPartition:getPartition", null, options.WithVersion());
    }

    [OutputType]
    public sealed class GetPartitionResult
    {
        public readonly string DnsSuffix;
        public readonly string Partition;
        /// <summary>
        /// id is the provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;

        [OutputConstructor]
        private GetPartitionResult(
            string dnsSuffix,
            string partition,
            string id)
        {
            DnsSuffix = dnsSuffix;
            Partition = partition;
            Id = id;
        }
    }
}
