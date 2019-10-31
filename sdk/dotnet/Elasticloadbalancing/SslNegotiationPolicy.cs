// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.Elasticloadbalancing
{
    /// <summary>
    /// Provides a load balancer SSL negotiation policy, which allows an ELB to control the ciphers and protocols that are supported during SSL negotiations between a client and a load balancer.
    /// 
    /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/lb_ssl_negotiation_policy_legacy.html.markdown.
    /// </summary>
    public partial class SslNegotiationPolicy : Pulumi.CustomResource
    {
        /// <summary>
        /// An SSL Negotiation policy attribute. Each has two properties:
        /// </summary>
        [Output("attributes")]
        public Output<ImmutableArray<Outputs.SslNegotiationPolicyAttributes>> Attributes { get; private set; } = null!;

        /// <summary>
        /// The load balancer port to which the policy
        /// should be applied. This must be an active listener on the load
        /// balancer.
        /// </summary>
        [Output("lbPort")]
        public Output<int> LbPort { get; private set; } = null!;

        /// <summary>
        /// The load balancer to which the policy
        /// should be attached.
        /// </summary>
        [Output("loadBalancer")]
        public Output<string> LoadBalancer { get; private set; } = null!;

        /// <summary>
        /// The name of the attribute
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;


        /// <summary>
        /// Create a SslNegotiationPolicy resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public SslNegotiationPolicy(string name, SslNegotiationPolicyArgs args, CustomResourceOptions? options = null)
            : base("aws:elasticloadbalancing/sslNegotiationPolicy:SslNegotiationPolicy", name, args, MakeResourceOptions(options, ""))
        {
        }

        private SslNegotiationPolicy(string name, Input<string> id, SslNegotiationPolicyState? state = null, CustomResourceOptions? options = null)
            : base("aws:elasticloadbalancing/sslNegotiationPolicy:SslNegotiationPolicy", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing SslNegotiationPolicy resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static SslNegotiationPolicy Get(string name, Input<string> id, SslNegotiationPolicyState? state = null, CustomResourceOptions? options = null)
        {
            return new SslNegotiationPolicy(name, id, state, options);
        }
    }

    public sealed class SslNegotiationPolicyArgs : Pulumi.ResourceArgs
    {
        [Input("attributes")]
        private InputList<Inputs.SslNegotiationPolicyAttributesArgs>? _attributes;

        /// <summary>
        /// An SSL Negotiation policy attribute. Each has two properties:
        /// </summary>
        public InputList<Inputs.SslNegotiationPolicyAttributesArgs> Attributes
        {
            get => _attributes ?? (_attributes = new InputList<Inputs.SslNegotiationPolicyAttributesArgs>());
            set => _attributes = value;
        }

        /// <summary>
        /// The load balancer port to which the policy
        /// should be applied. This must be an active listener on the load
        /// balancer.
        /// </summary>
        [Input("lbPort", required: true)]
        public Input<int> LbPort { get; set; } = null!;

        /// <summary>
        /// The load balancer to which the policy
        /// should be attached.
        /// </summary>
        [Input("loadBalancer", required: true)]
        public Input<string> LoadBalancer { get; set; } = null!;

        /// <summary>
        /// The name of the attribute
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        public SslNegotiationPolicyArgs()
        {
        }
    }

    public sealed class SslNegotiationPolicyState : Pulumi.ResourceArgs
    {
        [Input("attributes")]
        private InputList<Inputs.SslNegotiationPolicyAttributesGetArgs>? _attributes;

        /// <summary>
        /// An SSL Negotiation policy attribute. Each has two properties:
        /// </summary>
        public InputList<Inputs.SslNegotiationPolicyAttributesGetArgs> Attributes
        {
            get => _attributes ?? (_attributes = new InputList<Inputs.SslNegotiationPolicyAttributesGetArgs>());
            set => _attributes = value;
        }

        /// <summary>
        /// The load balancer port to which the policy
        /// should be applied. This must be an active listener on the load
        /// balancer.
        /// </summary>
        [Input("lbPort")]
        public Input<int>? LbPort { get; set; }

        /// <summary>
        /// The load balancer to which the policy
        /// should be attached.
        /// </summary>
        [Input("loadBalancer")]
        public Input<string>? LoadBalancer { get; set; }

        /// <summary>
        /// The name of the attribute
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        public SslNegotiationPolicyState()
        {
        }
    }

    namespace Inputs
    {

    public sealed class SslNegotiationPolicyAttributesArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The name of the attribute
        /// </summary>
        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        /// <summary>
        /// The value of the attribute
        /// </summary>
        [Input("value", required: true)]
        public Input<string> Value { get; set; } = null!;

        public SslNegotiationPolicyAttributesArgs()
        {
        }
    }

    public sealed class SslNegotiationPolicyAttributesGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The name of the attribute
        /// </summary>
        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        /// <summary>
        /// The value of the attribute
        /// </summary>
        [Input("value", required: true)]
        public Input<string> Value { get; set; } = null!;

        public SslNegotiationPolicyAttributesGetArgs()
        {
        }
    }
    }

    namespace Outputs
    {

    [OutputType]
    public sealed class SslNegotiationPolicyAttributes
    {
        /// <summary>
        /// The name of the attribute
        /// </summary>
        public readonly string Name;
        /// <summary>
        /// The value of the attribute
        /// </summary>
        public readonly string Value;

        [OutputConstructor]
        private SslNegotiationPolicyAttributes(
            string name,
            string value)
        {
            Name = name;
            Value = value;
        }
    }
    }
}
