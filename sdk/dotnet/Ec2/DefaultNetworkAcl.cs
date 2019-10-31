// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.Ec2
{
    /// <summary>
    /// Provides a resource to manage the default AWS Network ACL. VPC Only.
    /// 
    /// Each VPC created in AWS comes with a Default Network ACL that can be managed, but not
    /// destroyed. **This is an advanced resource**, and has special caveats to be aware
    /// of when using it. Please read this document in its entirety before using this
    /// resource.
    /// 
    /// The `aws.ec2.DefaultNetworkAcl` behaves differently from normal resources, in that
    /// this provider does not _create_ this resource, but instead attempts to "adopt" it
    /// into management. We can do this because each VPC created has a Default Network
    /// ACL that cannot be destroyed, and is created with a known set of default rules.
    /// 
    /// When this provider first adopts the Default Network ACL, it **immediately removes all
    /// rules in the ACL**. It then proceeds to create any rules specified in the
    /// configuration. This step is required so that only the rules specified in the
    /// configuration are created.
    /// 
    /// This resource treats its inline rules as absolute; only the rules defined
    /// inline are created, and any additions/removals external to this resource will
    /// result in diffs being shown. For these reasons, this resource is incompatible with the
    /// `aws.ec2.NetworkAclRule` resource.
    /// 
    /// For more information about Network ACLs, see the AWS Documentation on
    /// [Network ACLs][aws-network-acls].
    /// 
    /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/default_network_acl.html.markdown.
    /// </summary>
    public partial class DefaultNetworkAcl : Pulumi.CustomResource
    {
        /// <summary>
        /// The Network ACL ID to manage. This
        /// attribute is exported from `aws.ec2.Vpc`, or manually found via the AWS Console.
        /// </summary>
        [Output("defaultNetworkAclId")]
        public Output<string> DefaultNetworkAclId { get; private set; } = null!;

        /// <summary>
        /// Specifies an egress rule. Parameters defined below.
        /// </summary>
        [Output("egress")]
        public Output<ImmutableArray<Outputs.DefaultNetworkAclEgress>> Egress { get; private set; } = null!;

        /// <summary>
        /// Specifies an ingress rule. Parameters defined below.
        /// </summary>
        [Output("ingress")]
        public Output<ImmutableArray<Outputs.DefaultNetworkAclIngress>> Ingress { get; private set; } = null!;

        /// <summary>
        /// The ID of the AWS account that owns the Default Network ACL
        /// </summary>
        [Output("ownerId")]
        public Output<string> OwnerId { get; private set; } = null!;

        /// <summary>
        /// A list of Subnet IDs to apply the ACL to. See the
        /// notes below on managing Subnets in the Default Network ACL
        /// </summary>
        [Output("subnetIds")]
        public Output<ImmutableArray<string>> SubnetIds { get; private set; } = null!;

        /// <summary>
        /// A mapping of tags to assign to the resource.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableDictionary<string, object>?> Tags { get; private set; } = null!;

        /// <summary>
        /// The ID of the associated VPC
        /// </summary>
        [Output("vpcId")]
        public Output<string> VpcId { get; private set; } = null!;


        /// <summary>
        /// Create a DefaultNetworkAcl resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public DefaultNetworkAcl(string name, DefaultNetworkAclArgs args, CustomResourceOptions? options = null)
            : base("aws:ec2/defaultNetworkAcl:DefaultNetworkAcl", name, args, MakeResourceOptions(options, ""))
        {
        }

        private DefaultNetworkAcl(string name, Input<string> id, DefaultNetworkAclState? state = null, CustomResourceOptions? options = null)
            : base("aws:ec2/defaultNetworkAcl:DefaultNetworkAcl", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing DefaultNetworkAcl resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static DefaultNetworkAcl Get(string name, Input<string> id, DefaultNetworkAclState? state = null, CustomResourceOptions? options = null)
        {
            return new DefaultNetworkAcl(name, id, state, options);
        }
    }

    public sealed class DefaultNetworkAclArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The Network ACL ID to manage. This
        /// attribute is exported from `aws.ec2.Vpc`, or manually found via the AWS Console.
        /// </summary>
        [Input("defaultNetworkAclId", required: true)]
        public Input<string> DefaultNetworkAclId { get; set; } = null!;

        [Input("egress")]
        private InputList<Inputs.DefaultNetworkAclEgressArgs>? _egress;

        /// <summary>
        /// Specifies an egress rule. Parameters defined below.
        /// </summary>
        public InputList<Inputs.DefaultNetworkAclEgressArgs> Egress
        {
            get => _egress ?? (_egress = new InputList<Inputs.DefaultNetworkAclEgressArgs>());
            set => _egress = value;
        }

        [Input("ingress")]
        private InputList<Inputs.DefaultNetworkAclIngressArgs>? _ingress;

        /// <summary>
        /// Specifies an ingress rule. Parameters defined below.
        /// </summary>
        public InputList<Inputs.DefaultNetworkAclIngressArgs> Ingress
        {
            get => _ingress ?? (_ingress = new InputList<Inputs.DefaultNetworkAclIngressArgs>());
            set => _ingress = value;
        }

        [Input("subnetIds")]
        private InputList<string>? _subnetIds;

        /// <summary>
        /// A list of Subnet IDs to apply the ACL to. See the
        /// notes below on managing Subnets in the Default Network ACL
        /// </summary>
        public InputList<string> SubnetIds
        {
            get => _subnetIds ?? (_subnetIds = new InputList<string>());
            set => _subnetIds = value;
        }

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

        public DefaultNetworkAclArgs()
        {
        }
    }

    public sealed class DefaultNetworkAclState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The Network ACL ID to manage. This
        /// attribute is exported from `aws.ec2.Vpc`, or manually found via the AWS Console.
        /// </summary>
        [Input("defaultNetworkAclId")]
        public Input<string>? DefaultNetworkAclId { get; set; }

        [Input("egress")]
        private InputList<Inputs.DefaultNetworkAclEgressGetArgs>? _egress;

        /// <summary>
        /// Specifies an egress rule. Parameters defined below.
        /// </summary>
        public InputList<Inputs.DefaultNetworkAclEgressGetArgs> Egress
        {
            get => _egress ?? (_egress = new InputList<Inputs.DefaultNetworkAclEgressGetArgs>());
            set => _egress = value;
        }

        [Input("ingress")]
        private InputList<Inputs.DefaultNetworkAclIngressGetArgs>? _ingress;

        /// <summary>
        /// Specifies an ingress rule. Parameters defined below.
        /// </summary>
        public InputList<Inputs.DefaultNetworkAclIngressGetArgs> Ingress
        {
            get => _ingress ?? (_ingress = new InputList<Inputs.DefaultNetworkAclIngressGetArgs>());
            set => _ingress = value;
        }

        /// <summary>
        /// The ID of the AWS account that owns the Default Network ACL
        /// </summary>
        [Input("ownerId")]
        public Input<string>? OwnerId { get; set; }

        [Input("subnetIds")]
        private InputList<string>? _subnetIds;

        /// <summary>
        /// A list of Subnet IDs to apply the ACL to. See the
        /// notes below on managing Subnets in the Default Network ACL
        /// </summary>
        public InputList<string> SubnetIds
        {
            get => _subnetIds ?? (_subnetIds = new InputList<string>());
            set => _subnetIds = value;
        }

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

        /// <summary>
        /// The ID of the associated VPC
        /// </summary>
        [Input("vpcId")]
        public Input<string>? VpcId { get; set; }

        public DefaultNetworkAclState()
        {
        }
    }

    namespace Inputs
    {

    public sealed class DefaultNetworkAclEgressArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The action to take.
        /// </summary>
        [Input("action", required: true)]
        public Input<string> Action { get; set; } = null!;

        /// <summary>
        /// The CIDR block to match. This must be a
        /// valid network mask.
        /// </summary>
        [Input("cidrBlock")]
        public Input<string>? CidrBlock { get; set; }

        /// <summary>
        /// The from port to match.
        /// </summary>
        [Input("fromPort", required: true)]
        public Input<int> FromPort { get; set; } = null!;

        /// <summary>
        /// The ICMP type code to be used. Default 0.
        /// </summary>
        [Input("icmpCode")]
        public Input<int>? IcmpCode { get; set; }

        /// <summary>
        /// The ICMP type to be used. Default 0.
        /// </summary>
        [Input("icmpType")]
        public Input<int>? IcmpType { get; set; }

        /// <summary>
        /// The IPv6 CIDR block.
        /// </summary>
        [Input("ipv6CidrBlock")]
        public Input<string>? Ipv6CidrBlock { get; set; }

        /// <summary>
        /// The protocol to match. If using the -1 'all'
        /// protocol, you must specify a from and to port of 0.
        /// </summary>
        [Input("protocol", required: true)]
        public Input<string> Protocol { get; set; } = null!;

        /// <summary>
        /// The rule number. Used for ordering.
        /// </summary>
        [Input("ruleNo", required: true)]
        public Input<int> RuleNo { get; set; } = null!;

        /// <summary>
        /// The to port to match.
        /// </summary>
        [Input("toPort", required: true)]
        public Input<int> ToPort { get; set; } = null!;

        public DefaultNetworkAclEgressArgs()
        {
        }
    }

    public sealed class DefaultNetworkAclEgressGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The action to take.
        /// </summary>
        [Input("action", required: true)]
        public Input<string> Action { get; set; } = null!;

        /// <summary>
        /// The CIDR block to match. This must be a
        /// valid network mask.
        /// </summary>
        [Input("cidrBlock")]
        public Input<string>? CidrBlock { get; set; }

        /// <summary>
        /// The from port to match.
        /// </summary>
        [Input("fromPort", required: true)]
        public Input<int> FromPort { get; set; } = null!;

        /// <summary>
        /// The ICMP type code to be used. Default 0.
        /// </summary>
        [Input("icmpCode")]
        public Input<int>? IcmpCode { get; set; }

        /// <summary>
        /// The ICMP type to be used. Default 0.
        /// </summary>
        [Input("icmpType")]
        public Input<int>? IcmpType { get; set; }

        /// <summary>
        /// The IPv6 CIDR block.
        /// </summary>
        [Input("ipv6CidrBlock")]
        public Input<string>? Ipv6CidrBlock { get; set; }

        /// <summary>
        /// The protocol to match. If using the -1 'all'
        /// protocol, you must specify a from and to port of 0.
        /// </summary>
        [Input("protocol", required: true)]
        public Input<string> Protocol { get; set; } = null!;

        /// <summary>
        /// The rule number. Used for ordering.
        /// </summary>
        [Input("ruleNo", required: true)]
        public Input<int> RuleNo { get; set; } = null!;

        /// <summary>
        /// The to port to match.
        /// </summary>
        [Input("toPort", required: true)]
        public Input<int> ToPort { get; set; } = null!;

        public DefaultNetworkAclEgressGetArgs()
        {
        }
    }

    public sealed class DefaultNetworkAclIngressArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The action to take.
        /// </summary>
        [Input("action", required: true)]
        public Input<string> Action { get; set; } = null!;

        /// <summary>
        /// The CIDR block to match. This must be a
        /// valid network mask.
        /// </summary>
        [Input("cidrBlock")]
        public Input<string>? CidrBlock { get; set; }

        /// <summary>
        /// The from port to match.
        /// </summary>
        [Input("fromPort", required: true)]
        public Input<int> FromPort { get; set; } = null!;

        /// <summary>
        /// The ICMP type code to be used. Default 0.
        /// </summary>
        [Input("icmpCode")]
        public Input<int>? IcmpCode { get; set; }

        /// <summary>
        /// The ICMP type to be used. Default 0.
        /// </summary>
        [Input("icmpType")]
        public Input<int>? IcmpType { get; set; }

        /// <summary>
        /// The IPv6 CIDR block.
        /// </summary>
        [Input("ipv6CidrBlock")]
        public Input<string>? Ipv6CidrBlock { get; set; }

        /// <summary>
        /// The protocol to match. If using the -1 'all'
        /// protocol, you must specify a from and to port of 0.
        /// </summary>
        [Input("protocol", required: true)]
        public Input<string> Protocol { get; set; } = null!;

        /// <summary>
        /// The rule number. Used for ordering.
        /// </summary>
        [Input("ruleNo", required: true)]
        public Input<int> RuleNo { get; set; } = null!;

        /// <summary>
        /// The to port to match.
        /// </summary>
        [Input("toPort", required: true)]
        public Input<int> ToPort { get; set; } = null!;

        public DefaultNetworkAclIngressArgs()
        {
        }
    }

    public sealed class DefaultNetworkAclIngressGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The action to take.
        /// </summary>
        [Input("action", required: true)]
        public Input<string> Action { get; set; } = null!;

        /// <summary>
        /// The CIDR block to match. This must be a
        /// valid network mask.
        /// </summary>
        [Input("cidrBlock")]
        public Input<string>? CidrBlock { get; set; }

        /// <summary>
        /// The from port to match.
        /// </summary>
        [Input("fromPort", required: true)]
        public Input<int> FromPort { get; set; } = null!;

        /// <summary>
        /// The ICMP type code to be used. Default 0.
        /// </summary>
        [Input("icmpCode")]
        public Input<int>? IcmpCode { get; set; }

        /// <summary>
        /// The ICMP type to be used. Default 0.
        /// </summary>
        [Input("icmpType")]
        public Input<int>? IcmpType { get; set; }

        /// <summary>
        /// The IPv6 CIDR block.
        /// </summary>
        [Input("ipv6CidrBlock")]
        public Input<string>? Ipv6CidrBlock { get; set; }

        /// <summary>
        /// The protocol to match. If using the -1 'all'
        /// protocol, you must specify a from and to port of 0.
        /// </summary>
        [Input("protocol", required: true)]
        public Input<string> Protocol { get; set; } = null!;

        /// <summary>
        /// The rule number. Used for ordering.
        /// </summary>
        [Input("ruleNo", required: true)]
        public Input<int> RuleNo { get; set; } = null!;

        /// <summary>
        /// The to port to match.
        /// </summary>
        [Input("toPort", required: true)]
        public Input<int> ToPort { get; set; } = null!;

        public DefaultNetworkAclIngressGetArgs()
        {
        }
    }
    }

    namespace Outputs
    {

    [OutputType]
    public sealed class DefaultNetworkAclEgress
    {
        /// <summary>
        /// The action to take.
        /// </summary>
        public readonly string Action;
        /// <summary>
        /// The CIDR block to match. This must be a
        /// valid network mask.
        /// </summary>
        public readonly string? CidrBlock;
        /// <summary>
        /// The from port to match.
        /// </summary>
        public readonly int FromPort;
        /// <summary>
        /// The ICMP type code to be used. Default 0.
        /// </summary>
        public readonly int? IcmpCode;
        /// <summary>
        /// The ICMP type to be used. Default 0.
        /// </summary>
        public readonly int? IcmpType;
        /// <summary>
        /// The IPv6 CIDR block.
        /// </summary>
        public readonly string? Ipv6CidrBlock;
        /// <summary>
        /// The protocol to match. If using the -1 'all'
        /// protocol, you must specify a from and to port of 0.
        /// </summary>
        public readonly string Protocol;
        /// <summary>
        /// The rule number. Used for ordering.
        /// </summary>
        public readonly int RuleNo;
        /// <summary>
        /// The to port to match.
        /// </summary>
        public readonly int ToPort;

        [OutputConstructor]
        private DefaultNetworkAclEgress(
            string action,
            string? cidrBlock,
            int fromPort,
            int? icmpCode,
            int? icmpType,
            string? ipv6CidrBlock,
            string protocol,
            int ruleNo,
            int toPort)
        {
            Action = action;
            CidrBlock = cidrBlock;
            FromPort = fromPort;
            IcmpCode = icmpCode;
            IcmpType = icmpType;
            Ipv6CidrBlock = ipv6CidrBlock;
            Protocol = protocol;
            RuleNo = ruleNo;
            ToPort = toPort;
        }
    }

    [OutputType]
    public sealed class DefaultNetworkAclIngress
    {
        /// <summary>
        /// The action to take.
        /// </summary>
        public readonly string Action;
        /// <summary>
        /// The CIDR block to match. This must be a
        /// valid network mask.
        /// </summary>
        public readonly string? CidrBlock;
        /// <summary>
        /// The from port to match.
        /// </summary>
        public readonly int FromPort;
        /// <summary>
        /// The ICMP type code to be used. Default 0.
        /// </summary>
        public readonly int? IcmpCode;
        /// <summary>
        /// The ICMP type to be used. Default 0.
        /// </summary>
        public readonly int? IcmpType;
        /// <summary>
        /// The IPv6 CIDR block.
        /// </summary>
        public readonly string? Ipv6CidrBlock;
        /// <summary>
        /// The protocol to match. If using the -1 'all'
        /// protocol, you must specify a from and to port of 0.
        /// </summary>
        public readonly string Protocol;
        /// <summary>
        /// The rule number. Used for ordering.
        /// </summary>
        public readonly int RuleNo;
        /// <summary>
        /// The to port to match.
        /// </summary>
        public readonly int ToPort;

        [OutputConstructor]
        private DefaultNetworkAclIngress(
            string action,
            string? cidrBlock,
            int fromPort,
            int? icmpCode,
            int? icmpType,
            string? ipv6CidrBlock,
            string protocol,
            int ruleNo,
            int toPort)
        {
            Action = action;
            CidrBlock = cidrBlock;
            FromPort = fromPort;
            IcmpCode = icmpCode;
            IcmpType = icmpType;
            Ipv6CidrBlock = ipv6CidrBlock;
            Protocol = protocol;
            RuleNo = ruleNo;
            ToPort = toPort;
        }
    }
    }
}
