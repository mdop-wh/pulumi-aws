// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.Redshift
{
    /// <summary>
    /// Creates a snapshot copy grant that allows AWS Redshift to encrypt copied snapshots with a customer master key from AWS KMS in a destination region.
    /// 
    /// Note that the grant must exist in the destination region, and not in the region of the cluster.
    /// 
    /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/redshift_snapshot_copy_grant.html.markdown.
    /// </summary>
    public partial class SnapshotCopyGrant : Pulumi.CustomResource
    {
        /// <summary>
        /// Amazon Resource Name (ARN) of snapshot copy grant
        /// </summary>
        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        /// <summary>
        /// The unique identifier for the customer master key (CMK) that the grant applies to. Specify the key ID or the Amazon Resource Name (ARN) of the CMK. To specify a CMK in a different AWS account, you must use the key ARN. If not specified, the default key is used.
        /// </summary>
        [Output("kmsKeyId")]
        public Output<string> KmsKeyId { get; private set; } = null!;

        /// <summary>
        /// A friendly name for identifying the grant.
        /// </summary>
        [Output("snapshotCopyGrantName")]
        public Output<string> SnapshotCopyGrantName { get; private set; } = null!;

        /// <summary>
        /// A mapping of tags to assign to the resource.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableDictionary<string, object>?> Tags { get; private set; } = null!;


        /// <summary>
        /// Create a SnapshotCopyGrant resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public SnapshotCopyGrant(string name, SnapshotCopyGrantArgs args, CustomResourceOptions? options = null)
            : base("aws:redshift/snapshotCopyGrant:SnapshotCopyGrant", name, args, MakeResourceOptions(options, ""))
        {
        }

        private SnapshotCopyGrant(string name, Input<string> id, SnapshotCopyGrantState? state = null, CustomResourceOptions? options = null)
            : base("aws:redshift/snapshotCopyGrant:SnapshotCopyGrant", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing SnapshotCopyGrant resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static SnapshotCopyGrant Get(string name, Input<string> id, SnapshotCopyGrantState? state = null, CustomResourceOptions? options = null)
        {
            return new SnapshotCopyGrant(name, id, state, options);
        }
    }

    public sealed class SnapshotCopyGrantArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The unique identifier for the customer master key (CMK) that the grant applies to. Specify the key ID or the Amazon Resource Name (ARN) of the CMK. To specify a CMK in a different AWS account, you must use the key ARN. If not specified, the default key is used.
        /// </summary>
        [Input("kmsKeyId")]
        public Input<string>? KmsKeyId { get; set; }

        /// <summary>
        /// A friendly name for identifying the grant.
        /// </summary>
        [Input("snapshotCopyGrantName", required: true)]
        public Input<string> SnapshotCopyGrantName { get; set; } = null!;

        [Input("tags")]
        private InputMap<object>? _tags;

        /// <summary>
        /// A mapping of tags to assign to the resource.
        /// </summary>
        public InputMap<object> Tags
        {
            get => _tags ?? (_tags = new InputMap<object>());
            set => _tags = value;
        }

        public SnapshotCopyGrantArgs()
        {
        }
    }

    public sealed class SnapshotCopyGrantState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Amazon Resource Name (ARN) of snapshot copy grant
        /// </summary>
        [Input("arn")]
        public Input<string>? Arn { get; set; }

        /// <summary>
        /// The unique identifier for the customer master key (CMK) that the grant applies to. Specify the key ID or the Amazon Resource Name (ARN) of the CMK. To specify a CMK in a different AWS account, you must use the key ARN. If not specified, the default key is used.
        /// </summary>
        [Input("kmsKeyId")]
        public Input<string>? KmsKeyId { get; set; }

        /// <summary>
        /// A friendly name for identifying the grant.
        /// </summary>
        [Input("snapshotCopyGrantName")]
        public Input<string>? SnapshotCopyGrantName { get; set; }

        [Input("tags")]
        private InputMap<object>? _tags;

        /// <summary>
        /// A mapping of tags to assign to the resource.
        /// </summary>
        public InputMap<object> Tags
        {
            get => _tags ?? (_tags = new InputMap<object>());
            set => _tags = value;
        }

        public SnapshotCopyGrantState()
        {
        }
    }
}
