// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.Elasticloadbalancing
{
    public static partial class Invokes
    {
        /// <summary>
        /// Use this data source to get the HostedZoneId of the AWS Elastic Load Balancing HostedZoneId
        /// in a given region for the purpose of using in an AWS Route53 Alias.
        /// 
        /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/elb_hosted_zone_id_legacy.html.markdown.
        /// </summary>
        public static Task<GetHostedZoneIdResult> GetHostedZoneId(GetHostedZoneIdArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetHostedZoneIdResult>("aws:elasticloadbalancing/getHostedZoneId:getHostedZoneId", args, options.WithVersion());
    }

    public sealed class GetHostedZoneIdArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Name of the region whose AWS ELB HostedZoneId is desired.
        /// Defaults to the region from the AWS provider configuration.
        /// </summary>
        [Input("region")]
        public Input<string>? Region { get; set; }

        public GetHostedZoneIdArgs()
        {
        }
    }

    [OutputType]
    public sealed class GetHostedZoneIdResult
    {
        public readonly string? Region;
        /// <summary>
        /// id is the provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;

        [OutputConstructor]
        private GetHostedZoneIdResult(
            string? region,
            string id)
        {
            Region = region;
            Id = id;
        }
    }
}
