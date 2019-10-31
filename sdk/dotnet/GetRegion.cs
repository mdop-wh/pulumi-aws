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
        /// `aws..getRegion` provides details about a specific AWS region.
        /// 
        /// As well as validating a given region name this resource can be used to
        /// discover the name of the region configured within the provider. The latter
        /// can be useful in a child module which is inheriting an AWS provider
        /// configuration from its parent module.
        /// 
        /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/region.html.markdown.
        /// </summary>
        public static Task<GetRegionResult> GetRegion(GetRegionArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetRegionResult>("aws:index/getRegion:getRegion", args, options.WithVersion());
    }

    public sealed class GetRegionArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The EC2 endpoint of the region to select.
        /// </summary>
        [Input("endpoint")]
        public Input<string>? Endpoint { get; set; }

        /// <summary>
        /// The full name of the region to select.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        public GetRegionArgs()
        {
        }
    }

    [OutputType]
    public sealed class GetRegionResult
    {
        /// <summary>
        /// The region's description in this format: "Location (Region name)".
        /// </summary>
        public readonly string Description;
        /// <summary>
        /// The EC2 endpoint for the selected region.
        /// </summary>
        public readonly string Endpoint;
        /// <summary>
        /// The name of the selected region.
        /// </summary>
        public readonly string Name;
        /// <summary>
        /// id is the provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;

        [OutputConstructor]
        private GetRegionResult(
            string description,
            string endpoint,
            string name,
            string id)
        {
            Description = description;
            Endpoint = endpoint;
            Name = name;
            Id = id;
        }
    }
}
