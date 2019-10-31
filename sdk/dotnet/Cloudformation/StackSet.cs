// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.Cloudformation
{
    /// <summary>
    /// Manages a CloudFormation Stack Set. Stack Sets allow CloudFormation templates to be easily deployed across multiple accounts and regions via Stack Set Instances ([`aws.cloudformation.StackSetInstance` resource](https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set_instance.html)). Additional information about Stack Sets can be found in the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/what-is-cfnstacksets.html).
    /// 
    /// &gt; **NOTE:** All template parameters, including those with a `Default`, must be configured or ignored with the `lifecycle` configuration block `ignore_changes` argument.
    /// 
    /// &gt; **NOTE:** All `NoEcho` template parameters must be ignored with the `lifecycle` configuration block `ignore_changes` argument.
    /// 
    /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/cloudformation_stack_set.html.markdown.
    /// </summary>
    public partial class StackSet : Pulumi.CustomResource
    {
        /// <summary>
        /// Amazon Resource Number (ARN) of the IAM Role in the administrator account.
        /// </summary>
        [Output("administrationRoleArn")]
        public Output<string> AdministrationRoleArn { get; private set; } = null!;

        /// <summary>
        /// Amazon Resource Name (ARN) of the Stack Set.
        /// </summary>
        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        /// <summary>
        /// A list of capabilities. Valid values: `CAPABILITY_IAM`, `CAPABILITY_NAMED_IAM`, `CAPABILITY_AUTO_EXPAND`.
        /// </summary>
        [Output("capabilities")]
        public Output<ImmutableArray<string>> Capabilities { get; private set; } = null!;

        /// <summary>
        /// Description of the Stack Set.
        /// </summary>
        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        /// <summary>
        /// Name of the IAM Role in all target accounts for Stack Set operations. Defaults to `AWSCloudFormationStackSetExecutionRole`.
        /// </summary>
        [Output("executionRoleName")]
        public Output<string?> ExecutionRoleName { get; private set; } = null!;

        /// <summary>
        /// Name of the Stack Set. The name must be unique in the region where you create your Stack Set. The name can contain only alphanumeric characters (case-sensitive) and hyphens. It must start with an alphabetic character and cannot be longer than 128 characters.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// Key-value map of input parameters for the Stack Set template. All template parameters, including those with a `Default`, must be configured or ignored with `lifecycle` configuration block `ignore_changes` argument. All `NoEcho` template parameters must be ignored with the `lifecycle` configuration block `ignore_changes` argument.
        /// </summary>
        [Output("parameters")]
        public Output<ImmutableDictionary<string, string>?> Parameters { get; private set; } = null!;

        /// <summary>
        /// Unique identifier of the Stack Set.
        /// </summary>
        [Output("stackSetId")]
        public Output<string> StackSetId { get; private set; } = null!;

        /// <summary>
        /// Key-value map of tags to associate with this Stack Set and the Stacks created from it. AWS CloudFormation also propagates these tags to supported resources that are created in the Stacks. A maximum number of 50 tags can be specified.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableDictionary<string, string>?> Tags { get; private set; } = null!;

        /// <summary>
        /// String containing the CloudFormation template body. Maximum size: 51,200 bytes. Conflicts with `template_url`.
        /// </summary>
        [Output("templateBody")]
        public Output<string> TemplateBody { get; private set; } = null!;

        /// <summary>
        /// String containing the location of a file containing the CloudFormation template body. The URL must point to a template that is located in an Amazon S3 bucket. Maximum location file size: 460,800 bytes. Conflicts with `template_body`.
        /// </summary>
        [Output("templateUrl")]
        public Output<string?> TemplateUrl { get; private set; } = null!;


        /// <summary>
        /// Create a StackSet resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public StackSet(string name, StackSetArgs args, CustomResourceOptions? options = null)
            : base("aws:cloudformation/stackSet:StackSet", name, args, MakeResourceOptions(options, ""))
        {
        }

        private StackSet(string name, Input<string> id, StackSetState? state = null, CustomResourceOptions? options = null)
            : base("aws:cloudformation/stackSet:StackSet", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing StackSet resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static StackSet Get(string name, Input<string> id, StackSetState? state = null, CustomResourceOptions? options = null)
        {
            return new StackSet(name, id, state, options);
        }
    }

    public sealed class StackSetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Amazon Resource Number (ARN) of the IAM Role in the administrator account.
        /// </summary>
        [Input("administrationRoleArn", required: true)]
        public Input<string> AdministrationRoleArn { get; set; } = null!;

        [Input("capabilities")]
        private InputList<string>? _capabilities;

        /// <summary>
        /// A list of capabilities. Valid values: `CAPABILITY_IAM`, `CAPABILITY_NAMED_IAM`, `CAPABILITY_AUTO_EXPAND`.
        /// </summary>
        public InputList<string> Capabilities
        {
            get => _capabilities ?? (_capabilities = new InputList<string>());
            set => _capabilities = value;
        }

        /// <summary>
        /// Description of the Stack Set.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// Name of the IAM Role in all target accounts for Stack Set operations. Defaults to `AWSCloudFormationStackSetExecutionRole`.
        /// </summary>
        [Input("executionRoleName")]
        public Input<string>? ExecutionRoleName { get; set; }

        /// <summary>
        /// Name of the Stack Set. The name must be unique in the region where you create your Stack Set. The name can contain only alphanumeric characters (case-sensitive) and hyphens. It must start with an alphabetic character and cannot be longer than 128 characters.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("parameters")]
        private InputMap<string>? _parameters;

        /// <summary>
        /// Key-value map of input parameters for the Stack Set template. All template parameters, including those with a `Default`, must be configured or ignored with `lifecycle` configuration block `ignore_changes` argument. All `NoEcho` template parameters must be ignored with the `lifecycle` configuration block `ignore_changes` argument.
        /// </summary>
        public InputMap<string> Parameters
        {
            get => _parameters ?? (_parameters = new InputMap<string>());
            set => _parameters = value;
        }

        [Input("tags")]
        private InputMap<string>? _tags;

        /// <summary>
        /// Key-value map of tags to associate with this Stack Set and the Stacks created from it. AWS CloudFormation also propagates these tags to supported resources that are created in the Stacks. A maximum number of 50 tags can be specified.
        /// </summary>
        public InputMap<string> Tags
        {
            get => _tags ?? (_tags = new InputMap<string>());
            set => _tags = value;
        }

        /// <summary>
        /// String containing the CloudFormation template body. Maximum size: 51,200 bytes. Conflicts with `template_url`.
        /// </summary>
        [Input("templateBody")]
        public Input<string>? TemplateBody { get; set; }

        /// <summary>
        /// String containing the location of a file containing the CloudFormation template body. The URL must point to a template that is located in an Amazon S3 bucket. Maximum location file size: 460,800 bytes. Conflicts with `template_body`.
        /// </summary>
        [Input("templateUrl")]
        public Input<string>? TemplateUrl { get; set; }

        public StackSetArgs()
        {
        }
    }

    public sealed class StackSetState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Amazon Resource Number (ARN) of the IAM Role in the administrator account.
        /// </summary>
        [Input("administrationRoleArn")]
        public Input<string>? AdministrationRoleArn { get; set; }

        /// <summary>
        /// Amazon Resource Name (ARN) of the Stack Set.
        /// </summary>
        [Input("arn")]
        public Input<string>? Arn { get; set; }

        [Input("capabilities")]
        private InputList<string>? _capabilities;

        /// <summary>
        /// A list of capabilities. Valid values: `CAPABILITY_IAM`, `CAPABILITY_NAMED_IAM`, `CAPABILITY_AUTO_EXPAND`.
        /// </summary>
        public InputList<string> Capabilities
        {
            get => _capabilities ?? (_capabilities = new InputList<string>());
            set => _capabilities = value;
        }

        /// <summary>
        /// Description of the Stack Set.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// Name of the IAM Role in all target accounts for Stack Set operations. Defaults to `AWSCloudFormationStackSetExecutionRole`.
        /// </summary>
        [Input("executionRoleName")]
        public Input<string>? ExecutionRoleName { get; set; }

        /// <summary>
        /// Name of the Stack Set. The name must be unique in the region where you create your Stack Set. The name can contain only alphanumeric characters (case-sensitive) and hyphens. It must start with an alphabetic character and cannot be longer than 128 characters.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("parameters")]
        private InputMap<string>? _parameters;

        /// <summary>
        /// Key-value map of input parameters for the Stack Set template. All template parameters, including those with a `Default`, must be configured or ignored with `lifecycle` configuration block `ignore_changes` argument. All `NoEcho` template parameters must be ignored with the `lifecycle` configuration block `ignore_changes` argument.
        /// </summary>
        public InputMap<string> Parameters
        {
            get => _parameters ?? (_parameters = new InputMap<string>());
            set => _parameters = value;
        }

        /// <summary>
        /// Unique identifier of the Stack Set.
        /// </summary>
        [Input("stackSetId")]
        public Input<string>? StackSetId { get; set; }

        [Input("tags")]
        private InputMap<string>? _tags;

        /// <summary>
        /// Key-value map of tags to associate with this Stack Set and the Stacks created from it. AWS CloudFormation also propagates these tags to supported resources that are created in the Stacks. A maximum number of 50 tags can be specified.
        /// </summary>
        public InputMap<string> Tags
        {
            get => _tags ?? (_tags = new InputMap<string>());
            set => _tags = value;
        }

        /// <summary>
        /// String containing the CloudFormation template body. Maximum size: 51,200 bytes. Conflicts with `template_url`.
        /// </summary>
        [Input("templateBody")]
        public Input<string>? TemplateBody { get; set; }

        /// <summary>
        /// String containing the location of a file containing the CloudFormation template body. The URL must point to a template that is located in an Amazon S3 bucket. Maximum location file size: 460,800 bytes. Conflicts with `template_body`.
        /// </summary>
        [Input("templateUrl")]
        public Input<string>? TemplateUrl { get; set; }

        public StackSetState()
        {
        }
    }
}
