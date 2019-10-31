// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.Ec2
{
    /// <summary>
    /// Adds launch permission to Amazon Machine Image (AMI) from another AWS account.
    /// 
    /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ami_launch_permission.html.markdown.
    /// </summary>
    public partial class AmiLaunchPermission : Pulumi.CustomResource
    {
        /// <summary>
        /// An AWS Account ID to add launch permissions.
        /// </summary>
        [Output("accountId")]
        public Output<string> AccountId { get; private set; } = null!;

        /// <summary>
        /// A region-unique name for the AMI.
        /// </summary>
        [Output("imageId")]
        public Output<string> ImageId { get; private set; } = null!;


        /// <summary>
        /// Create a AmiLaunchPermission resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public AmiLaunchPermission(string name, AmiLaunchPermissionArgs args, CustomResourceOptions? options = null)
            : base("aws:ec2/amiLaunchPermission:AmiLaunchPermission", name, args, MakeResourceOptions(options, ""))
        {
        }

        private AmiLaunchPermission(string name, Input<string> id, AmiLaunchPermissionState? state = null, CustomResourceOptions? options = null)
            : base("aws:ec2/amiLaunchPermission:AmiLaunchPermission", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing AmiLaunchPermission resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static AmiLaunchPermission Get(string name, Input<string> id, AmiLaunchPermissionState? state = null, CustomResourceOptions? options = null)
        {
            return new AmiLaunchPermission(name, id, state, options);
        }
    }

    public sealed class AmiLaunchPermissionArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// An AWS Account ID to add launch permissions.
        /// </summary>
        [Input("accountId", required: true)]
        public Input<string> AccountId { get; set; } = null!;

        /// <summary>
        /// A region-unique name for the AMI.
        /// </summary>
        [Input("imageId", required: true)]
        public Input<string> ImageId { get; set; } = null!;

        public AmiLaunchPermissionArgs()
        {
        }
    }

    public sealed class AmiLaunchPermissionState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// An AWS Account ID to add launch permissions.
        /// </summary>
        [Input("accountId")]
        public Input<string>? AccountId { get; set; }

        /// <summary>
        /// A region-unique name for the AMI.
        /// </summary>
        [Input("imageId")]
        public Input<string>? ImageId { get; set; }

        public AmiLaunchPermissionState()
        {
        }
    }
}
