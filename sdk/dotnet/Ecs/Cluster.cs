// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.Ecs
{
    /// <summary>
    /// Provides an ECS cluster.
    /// 
    /// ## setting
    /// 
    /// The `setting` configuration block supports the following:
    /// 
    /// * `name` - (Required) Name of the setting to manage. Valid values: `containerInsights`.
    /// * `value` -  (Required) The value to assign to the setting. Value values are `enabled` and `disabled`.
    /// 
    /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ecs_cluster.html.markdown.
    /// </summary>
    public partial class Cluster : Pulumi.CustomResource
    {
        /// <summary>
        /// The Amazon Resource Name (ARN) that identifies the cluster
        /// </summary>
        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        /// <summary>
        /// The name of the cluster (up to 255 letters, numbers, hyphens, and underscores)
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// Configuration block(s) with cluster settings. For example, this can be used to enable CloudWatch Container Insights for a cluster. Defined below.
        /// </summary>
        [Output("settings")]
        public Output<ImmutableArray<Outputs.ClusterSettings>> Settings { get; private set; } = null!;

        /// <summary>
        /// Key-value mapping of resource tags
        /// </summary>
        [Output("tags")]
        public Output<ImmutableDictionary<string, object>?> Tags { get; private set; } = null!;


        /// <summary>
        /// Create a Cluster resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Cluster(string name, ClusterArgs? args = null, CustomResourceOptions? options = null)
            : base("aws:ecs/cluster:Cluster", name, args, MakeResourceOptions(options, ""))
        {
        }

        private Cluster(string name, Input<string> id, ClusterState? state = null, CustomResourceOptions? options = null)
            : base("aws:ecs/cluster:Cluster", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing Cluster resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Cluster Get(string name, Input<string> id, ClusterState? state = null, CustomResourceOptions? options = null)
        {
            return new Cluster(name, id, state, options);
        }
    }

    public sealed class ClusterArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The name of the cluster (up to 255 letters, numbers, hyphens, and underscores)
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("settings")]
        private InputList<Inputs.ClusterSettingsArgs>? _settings;

        /// <summary>
        /// Configuration block(s) with cluster settings. For example, this can be used to enable CloudWatch Container Insights for a cluster. Defined below.
        /// </summary>
        public InputList<Inputs.ClusterSettingsArgs> Settings
        {
            get => _settings ?? (_settings = new InputList<Inputs.ClusterSettingsArgs>());
            set => _settings = value;
        }

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

        public ClusterArgs()
        {
        }
    }

    public sealed class ClusterState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The Amazon Resource Name (ARN) that identifies the cluster
        /// </summary>
        [Input("arn")]
        public Input<string>? Arn { get; set; }

        /// <summary>
        /// The name of the cluster (up to 255 letters, numbers, hyphens, and underscores)
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("settings")]
        private InputList<Inputs.ClusterSettingsGetArgs>? _settings;

        /// <summary>
        /// Configuration block(s) with cluster settings. For example, this can be used to enable CloudWatch Container Insights for a cluster. Defined below.
        /// </summary>
        public InputList<Inputs.ClusterSettingsGetArgs> Settings
        {
            get => _settings ?? (_settings = new InputList<Inputs.ClusterSettingsGetArgs>());
            set => _settings = value;
        }

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

        public ClusterState()
        {
        }
    }

    namespace Inputs
    {

    public sealed class ClusterSettingsArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The name of the cluster (up to 255 letters, numbers, hyphens, and underscores)
        /// </summary>
        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        [Input("value", required: true)]
        public Input<string> Value { get; set; } = null!;

        public ClusterSettingsArgs()
        {
        }
    }

    public sealed class ClusterSettingsGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The name of the cluster (up to 255 letters, numbers, hyphens, and underscores)
        /// </summary>
        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        [Input("value", required: true)]
        public Input<string> Value { get; set; } = null!;

        public ClusterSettingsGetArgs()
        {
        }
    }
    }

    namespace Outputs
    {

    [OutputType]
    public sealed class ClusterSettings
    {
        /// <summary>
        /// The name of the cluster (up to 255 letters, numbers, hyphens, and underscores)
        /// </summary>
        public readonly string Name;
        public readonly string Value;

        [OutputConstructor]
        private ClusterSettings(
            string name,
            string value)
        {
            Name = name;
            Value = value;
        }
    }
    }
}
