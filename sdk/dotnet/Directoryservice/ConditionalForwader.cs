// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.Directoryservice
{
    /// <summary>
    /// Provides a conditional forwarder for managed Microsoft AD in AWS Directory Service.
    /// 
    /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/directory_service_conditional_forwarder.html.markdown.
    /// </summary>
    public partial class ConditionalForwader : Pulumi.CustomResource
    {
        /// <summary>
        /// The id of directory.
        /// </summary>
        [Output("directoryId")]
        public Output<string> DirectoryId { get; private set; } = null!;

        /// <summary>
        /// A list of forwarder IP addresses.
        /// </summary>
        [Output("dnsIps")]
        public Output<ImmutableArray<string>> DnsIps { get; private set; } = null!;

        /// <summary>
        /// The fully qualified domain name of the remote domain for which forwarders will be used.
        /// </summary>
        [Output("remoteDomainName")]
        public Output<string> RemoteDomainName { get; private set; } = null!;


        /// <summary>
        /// Create a ConditionalForwader resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public ConditionalForwader(string name, ConditionalForwaderArgs args, CustomResourceOptions? options = null)
            : base("aws:directoryservice/conditionalForwader:ConditionalForwader", name, args, MakeResourceOptions(options, ""))
        {
        }

        private ConditionalForwader(string name, Input<string> id, ConditionalForwaderState? state = null, CustomResourceOptions? options = null)
            : base("aws:directoryservice/conditionalForwader:ConditionalForwader", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing ConditionalForwader resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static ConditionalForwader Get(string name, Input<string> id, ConditionalForwaderState? state = null, CustomResourceOptions? options = null)
        {
            return new ConditionalForwader(name, id, state, options);
        }
    }

    public sealed class ConditionalForwaderArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The id of directory.
        /// </summary>
        [Input("directoryId", required: true)]
        public Input<string> DirectoryId { get; set; } = null!;

        [Input("dnsIps", required: true)]
        private InputList<string>? _dnsIps;

        /// <summary>
        /// A list of forwarder IP addresses.
        /// </summary>
        public InputList<string> DnsIps
        {
            get => _dnsIps ?? (_dnsIps = new InputList<string>());
            set => _dnsIps = value;
        }

        /// <summary>
        /// The fully qualified domain name of the remote domain for which forwarders will be used.
        /// </summary>
        [Input("remoteDomainName", required: true)]
        public Input<string> RemoteDomainName { get; set; } = null!;

        public ConditionalForwaderArgs()
        {
        }
    }

    public sealed class ConditionalForwaderState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The id of directory.
        /// </summary>
        [Input("directoryId")]
        public Input<string>? DirectoryId { get; set; }

        [Input("dnsIps")]
        private InputList<string>? _dnsIps;

        /// <summary>
        /// A list of forwarder IP addresses.
        /// </summary>
        public InputList<string> DnsIps
        {
            get => _dnsIps ?? (_dnsIps = new InputList<string>());
            set => _dnsIps = value;
        }

        /// <summary>
        /// The fully qualified domain name of the remote domain for which forwarders will be used.
        /// </summary>
        [Input("remoteDomainName")]
        public Input<string>? RemoteDomainName { get; set; }

        public ConditionalForwaderState()
        {
        }
    }
}
