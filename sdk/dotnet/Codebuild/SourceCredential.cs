// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.Codebuild
{
    /// <summary>
    /// Provides a CodeBuild Source Credentials Resource.
    /// 
    /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/codebuild_source_credential.html.markdown.
    /// </summary>
    public partial class SourceCredential : Pulumi.CustomResource
    {
        /// <summary>
        /// The ARN of Source Credential.
        /// </summary>
        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        /// <summary>
        /// The type of authentication used to connect to a GitHub, GitHub Enterprise, or Bitbucket repository. An OAUTH connection is not supported by the API.
        /// </summary>
        [Output("authType")]
        public Output<string> AuthType { get; private set; } = null!;

        /// <summary>
        /// The source provider used for this project.
        /// </summary>
        [Output("serverType")]
        public Output<string> ServerType { get; private set; } = null!;

        /// <summary>
        /// For `GitHub` or `GitHub Enterprise`, this is the personal access token. For `Bitbucket`, this is the app password.
        /// </summary>
        [Output("token")]
        public Output<string> Token { get; private set; } = null!;

        /// <summary>
        /// The Bitbucket username when the authType is `BASIC_AUTH`. This parameter is not valid for other types of source providers or connections.
        /// </summary>
        [Output("userName")]
        public Output<string?> UserName { get; private set; } = null!;


        /// <summary>
        /// Create a SourceCredential resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public SourceCredential(string name, SourceCredentialArgs args, CustomResourceOptions? options = null)
            : base("aws:codebuild/sourceCredential:SourceCredential", name, args, MakeResourceOptions(options, ""))
        {
        }

        private SourceCredential(string name, Input<string> id, SourceCredentialState? state = null, CustomResourceOptions? options = null)
            : base("aws:codebuild/sourceCredential:SourceCredential", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing SourceCredential resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static SourceCredential Get(string name, Input<string> id, SourceCredentialState? state = null, CustomResourceOptions? options = null)
        {
            return new SourceCredential(name, id, state, options);
        }
    }

    public sealed class SourceCredentialArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The type of authentication used to connect to a GitHub, GitHub Enterprise, or Bitbucket repository. An OAUTH connection is not supported by the API.
        /// </summary>
        [Input("authType", required: true)]
        public Input<string> AuthType { get; set; } = null!;

        /// <summary>
        /// The source provider used for this project.
        /// </summary>
        [Input("serverType", required: true)]
        public Input<string> ServerType { get; set; } = null!;

        /// <summary>
        /// For `GitHub` or `GitHub Enterprise`, this is the personal access token. For `Bitbucket`, this is the app password.
        /// </summary>
        [Input("token", required: true)]
        public Input<string> Token { get; set; } = null!;

        /// <summary>
        /// The Bitbucket username when the authType is `BASIC_AUTH`. This parameter is not valid for other types of source providers or connections.
        /// </summary>
        [Input("userName")]
        public Input<string>? UserName { get; set; }

        public SourceCredentialArgs()
        {
        }
    }

    public sealed class SourceCredentialState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The ARN of Source Credential.
        /// </summary>
        [Input("arn")]
        public Input<string>? Arn { get; set; }

        /// <summary>
        /// The type of authentication used to connect to a GitHub, GitHub Enterprise, or Bitbucket repository. An OAUTH connection is not supported by the API.
        /// </summary>
        [Input("authType")]
        public Input<string>? AuthType { get; set; }

        /// <summary>
        /// The source provider used for this project.
        /// </summary>
        [Input("serverType")]
        public Input<string>? ServerType { get; set; }

        /// <summary>
        /// For `GitHub` or `GitHub Enterprise`, this is the personal access token. For `Bitbucket`, this is the app password.
        /// </summary>
        [Input("token")]
        public Input<string>? Token { get; set; }

        /// <summary>
        /// The Bitbucket username when the authType is `BASIC_AUTH`. This parameter is not valid for other types of source providers or connections.
        /// </summary>
        [Input("userName")]
        public Input<string>? UserName { get; set; }

        public SourceCredentialState()
        {
        }
    }
}
