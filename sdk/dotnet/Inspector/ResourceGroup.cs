// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.Inspector
{
    /// <summary>
    /// Provides a Inspector resource group
    /// 
    /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/inspector_resource_group.html.markdown.
    /// </summary>
    public partial class ResourceGroup : Pulumi.CustomResource
    {
        /// <summary>
        /// The resource group ARN.
        /// </summary>
        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        /// <summary>
        /// The tags on your EC2 Instance.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableDictionary<string, object>> Tags { get; private set; } = null!;


        /// <summary>
        /// Create a ResourceGroup resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public ResourceGroup(string name, ResourceGroupArgs args, CustomResourceOptions? options = null)
            : base("aws:inspector/resourceGroup:ResourceGroup", name, args, MakeResourceOptions(options, ""))
        {
        }

        private ResourceGroup(string name, Input<string> id, ResourceGroupState? state = null, CustomResourceOptions? options = null)
            : base("aws:inspector/resourceGroup:ResourceGroup", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing ResourceGroup resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static ResourceGroup Get(string name, Input<string> id, ResourceGroupState? state = null, CustomResourceOptions? options = null)
        {
            return new ResourceGroup(name, id, state, options);
        }
    }

    public sealed class ResourceGroupArgs : Pulumi.ResourceArgs
    {
        [Input("tags", required: true)]
        private InputMap<object>? _tags;

        /// <summary>
        /// The tags on your EC2 Instance.
        /// </summary>
        public InputMap<object> Tags
        {
            get => _tags ?? (_tags = new InputMap<object>());
            set => _tags = value;
        }

        public ResourceGroupArgs()
        {
        }
    }

    public sealed class ResourceGroupState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The resource group ARN.
        /// </summary>
        [Input("arn")]
        public Input<string>? Arn { get; set; }

        [Input("tags")]
        private InputMap<object>? _tags;

        /// <summary>
        /// The tags on your EC2 Instance.
        /// </summary>
        public InputMap<object> Tags
        {
            get => _tags ?? (_tags = new InputMap<object>());
            set => _tags = value;
        }

        public ResourceGroupState()
        {
        }
    }
}
