// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.Redshift
{
    /// <summary>
    /// Creates a new Amazon Redshift security group. You use security groups to control access to non-VPC clusters
    /// 
    /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/redshift_security_group.html.markdown.
    /// </summary>
    public partial class SecurityGroup : Pulumi.CustomResource
    {
        /// <summary>
        /// The description of the Redshift security group. Defaults to "Managed by Pulumi".
        /// </summary>
        [Output("description")]
        public Output<string> Description { get; private set; } = null!;

        /// <summary>
        /// A list of ingress rules.
        /// </summary>
        [Output("ingress")]
        public Output<ImmutableArray<Outputs.SecurityGroupIngress>> Ingress { get; private set; } = null!;

        /// <summary>
        /// The name of the Redshift security group.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;


        /// <summary>
        /// Create a SecurityGroup resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public SecurityGroup(string name, SecurityGroupArgs args, CustomResourceOptions? options = null)
            : base("aws:redshift/securityGroup:SecurityGroup", name, args, MakeResourceOptions(options, ""))
        {
        }

        private SecurityGroup(string name, Input<string> id, SecurityGroupState? state = null, CustomResourceOptions? options = null)
            : base("aws:redshift/securityGroup:SecurityGroup", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing SecurityGroup resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static SecurityGroup Get(string name, Input<string> id, SecurityGroupState? state = null, CustomResourceOptions? options = null)
        {
            return new SecurityGroup(name, id, state, options);
        }
    }

    public sealed class SecurityGroupArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The description of the Redshift security group. Defaults to "Managed by Pulumi".
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        [Input("ingress", required: true)]
        private InputList<Inputs.SecurityGroupIngressArgs>? _ingress;

        /// <summary>
        /// A list of ingress rules.
        /// </summary>
        public InputList<Inputs.SecurityGroupIngressArgs> Ingress
        {
            get => _ingress ?? (_ingress = new InputList<Inputs.SecurityGroupIngressArgs>());
            set => _ingress = value;
        }

        /// <summary>
        /// The name of the Redshift security group.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        public SecurityGroupArgs()
        {
            Description = "Managed by Pulumi";
        }
    }

    public sealed class SecurityGroupState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The description of the Redshift security group. Defaults to "Managed by Pulumi".
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        [Input("ingress")]
        private InputList<Inputs.SecurityGroupIngressGetArgs>? _ingress;

        /// <summary>
        /// A list of ingress rules.
        /// </summary>
        public InputList<Inputs.SecurityGroupIngressGetArgs> Ingress
        {
            get => _ingress ?? (_ingress = new InputList<Inputs.SecurityGroupIngressGetArgs>());
            set => _ingress = value;
        }

        /// <summary>
        /// The name of the Redshift security group.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        public SecurityGroupState()
        {
            Description = "Managed by Pulumi";
        }
    }

    namespace Inputs
    {

    public sealed class SecurityGroupIngressArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The CIDR block to accept
        /// </summary>
        [Input("cidr")]
        public Input<string>? Cidr { get; set; }

        /// <summary>
        /// The name of the security group to authorize
        /// </summary>
        [Input("securityGroupName")]
        public Input<string>? SecurityGroupName { get; set; }

        /// <summary>
        /// The owner Id of the security group provided
        /// by `security_group_name`.
        /// </summary>
        [Input("securityGroupOwnerId")]
        public Input<string>? SecurityGroupOwnerId { get; set; }

        public SecurityGroupIngressArgs()
        {
        }
    }

    public sealed class SecurityGroupIngressGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The CIDR block to accept
        /// </summary>
        [Input("cidr")]
        public Input<string>? Cidr { get; set; }

        /// <summary>
        /// The name of the security group to authorize
        /// </summary>
        [Input("securityGroupName")]
        public Input<string>? SecurityGroupName { get; set; }

        /// <summary>
        /// The owner Id of the security group provided
        /// by `security_group_name`.
        /// </summary>
        [Input("securityGroupOwnerId")]
        public Input<string>? SecurityGroupOwnerId { get; set; }

        public SecurityGroupIngressGetArgs()
        {
        }
    }
    }

    namespace Outputs
    {

    [OutputType]
    public sealed class SecurityGroupIngress
    {
        /// <summary>
        /// The CIDR block to accept
        /// </summary>
        public readonly string? Cidr;
        /// <summary>
        /// The name of the security group to authorize
        /// </summary>
        public readonly string SecurityGroupName;
        /// <summary>
        /// The owner Id of the security group provided
        /// by `security_group_name`.
        /// </summary>
        public readonly string SecurityGroupOwnerId;

        [OutputConstructor]
        private SecurityGroupIngress(
            string? cidr,
            string securityGroupName,
            string securityGroupOwnerId)
        {
            Cidr = cidr;
            SecurityGroupName = securityGroupName;
            SecurityGroupOwnerId = securityGroupOwnerId;
        }
    }
    }
}
