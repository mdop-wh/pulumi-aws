// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.Msk
{
    /// <summary>
    /// Manages an Amazon Managed Streaming for Kafka configuration. More information can be found on the [MSK Developer Guide](https://docs.aws.amazon.com/msk/latest/developerguide/msk-configuration.html).
    /// 
    /// &gt; **NOTE:** The API does not support deleting MSK configurations. Removing this resource will only remove the this provider state for it.
    /// 
    /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/msk_configuration.html.markdown.
    /// </summary>
    public partial class Configuration : Pulumi.CustomResource
    {
        /// <summary>
        /// Amazon Resource Name (ARN) of the configuration.
        /// </summary>
        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        /// <summary>
        /// Description of the configuration.
        /// </summary>
        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        /// <summary>
        /// List of Apache Kafka versions which can use this configuration.
        /// </summary>
        [Output("kafkaVersions")]
        public Output<ImmutableArray<string>> KafkaVersions { get; private set; } = null!;

        /// <summary>
        /// Latest revision of the configuration.
        /// </summary>
        [Output("latestRevision")]
        public Output<int> LatestRevision { get; private set; } = null!;

        /// <summary>
        /// Name of the configuration.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// Contents of the server.properties file. Supported properties are documented in the [MSK Developer Guide](https://docs.aws.amazon.com/msk/latest/developerguide/msk-configuration-properties.html).
        /// </summary>
        [Output("serverProperties")]
        public Output<string> ServerProperties { get; private set; } = null!;


        /// <summary>
        /// Create a Configuration resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Configuration(string name, ConfigurationArgs args, CustomResourceOptions? options = null)
            : base("aws:msk/configuration:Configuration", name, args, MakeResourceOptions(options, ""))
        {
        }

        private Configuration(string name, Input<string> id, ConfigurationState? state = null, CustomResourceOptions? options = null)
            : base("aws:msk/configuration:Configuration", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing Configuration resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Configuration Get(string name, Input<string> id, ConfigurationState? state = null, CustomResourceOptions? options = null)
        {
            return new Configuration(name, id, state, options);
        }
    }

    public sealed class ConfigurationArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Description of the configuration.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        [Input("kafkaVersions", required: true)]
        private InputList<string>? _kafkaVersions;

        /// <summary>
        /// List of Apache Kafka versions which can use this configuration.
        /// </summary>
        public InputList<string> KafkaVersions
        {
            get => _kafkaVersions ?? (_kafkaVersions = new InputList<string>());
            set => _kafkaVersions = value;
        }

        /// <summary>
        /// Name of the configuration.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// Contents of the server.properties file. Supported properties are documented in the [MSK Developer Guide](https://docs.aws.amazon.com/msk/latest/developerguide/msk-configuration-properties.html).
        /// </summary>
        [Input("serverProperties", required: true)]
        public Input<string> ServerProperties { get; set; } = null!;

        public ConfigurationArgs()
        {
        }
    }

    public sealed class ConfigurationState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Amazon Resource Name (ARN) of the configuration.
        /// </summary>
        [Input("arn")]
        public Input<string>? Arn { get; set; }

        /// <summary>
        /// Description of the configuration.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        [Input("kafkaVersions")]
        private InputList<string>? _kafkaVersions;

        /// <summary>
        /// List of Apache Kafka versions which can use this configuration.
        /// </summary>
        public InputList<string> KafkaVersions
        {
            get => _kafkaVersions ?? (_kafkaVersions = new InputList<string>());
            set => _kafkaVersions = value;
        }

        /// <summary>
        /// Latest revision of the configuration.
        /// </summary>
        [Input("latestRevision")]
        public Input<int>? LatestRevision { get; set; }

        /// <summary>
        /// Name of the configuration.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// Contents of the server.properties file. Supported properties are documented in the [MSK Developer Guide](https://docs.aws.amazon.com/msk/latest/developerguide/msk-configuration-properties.html).
        /// </summary>
        [Input("serverProperties")]
        public Input<string>? ServerProperties { get; set; }

        public ConfigurationState()
        {
        }
    }
}
