// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.Elasticbeanstalk
{
    /// <summary>
    /// Provides an Elastic Beanstalk Application Resource. Elastic Beanstalk allows
    /// you to deploy and manage applications in the AWS cloud without worrying about
    /// the infrastructure that runs those applications.
    /// 
    /// This resource creates an application that has one configuration template named
    /// `default`, and no application versions
    /// 
    /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/elastic_beanstalk_application.html.markdown.
    /// </summary>
    public partial class Application : Pulumi.CustomResource
    {
        [Output("appversionLifecycle")]
        public Output<Outputs.ApplicationAppversionLifecycle?> AppversionLifecycle { get; private set; } = null!;

        /// <summary>
        /// The ARN assigned by AWS for this Elastic Beanstalk Application.
        /// </summary>
        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        /// <summary>
        /// Short description of the application
        /// </summary>
        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        /// <summary>
        /// The name of the application, must be unique within your account
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// Key-value mapping of tags for the Elastic Beanstalk Application.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableDictionary<string, object>?> Tags { get; private set; } = null!;


        /// <summary>
        /// Create a Application resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Application(string name, ApplicationArgs? args = null, CustomResourceOptions? options = null)
            : base("aws:elasticbeanstalk/application:Application", name, args, MakeResourceOptions(options, ""))
        {
        }

        private Application(string name, Input<string> id, ApplicationState? state = null, CustomResourceOptions? options = null)
            : base("aws:elasticbeanstalk/application:Application", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing Application resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Application Get(string name, Input<string> id, ApplicationState? state = null, CustomResourceOptions? options = null)
        {
            return new Application(name, id, state, options);
        }
    }

    public sealed class ApplicationArgs : Pulumi.ResourceArgs
    {
        [Input("appversionLifecycle")]
        public Input<Inputs.ApplicationAppversionLifecycleArgs>? AppversionLifecycle { get; set; }

        /// <summary>
        /// Short description of the application
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// The name of the application, must be unique within your account
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("tags")]
        private InputMap<object>? _tags;

        /// <summary>
        /// Key-value mapping of tags for the Elastic Beanstalk Application.
        /// </summary>
        public InputMap<object> Tags
        {
            get => _tags ?? (_tags = new InputMap<object>());
            set => _tags = value;
        }

        public ApplicationArgs()
        {
        }
    }

    public sealed class ApplicationState : Pulumi.ResourceArgs
    {
        [Input("appversionLifecycle")]
        public Input<Inputs.ApplicationAppversionLifecycleGetArgs>? AppversionLifecycle { get; set; }

        /// <summary>
        /// The ARN assigned by AWS for this Elastic Beanstalk Application.
        /// </summary>
        [Input("arn")]
        public Input<string>? Arn { get; set; }

        /// <summary>
        /// Short description of the application
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// The name of the application, must be unique within your account
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("tags")]
        private InputMap<object>? _tags;

        /// <summary>
        /// Key-value mapping of tags for the Elastic Beanstalk Application.
        /// </summary>
        public InputMap<object> Tags
        {
            get => _tags ?? (_tags = new InputMap<object>());
            set => _tags = value;
        }

        public ApplicationState()
        {
        }
    }

    namespace Inputs
    {

    public sealed class ApplicationAppversionLifecycleArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Set to `true` to delete a version's source bundle from S3 when the application version is deleted.
        /// </summary>
        [Input("deleteSourceFromS3")]
        public Input<bool>? DeleteSourceFromS3 { get; set; }

        /// <summary>
        /// The number of days to retain an application version.
        /// </summary>
        [Input("maxAgeInDays")]
        public Input<int>? MaxAgeInDays { get; set; }

        /// <summary>
        /// The maximum number of application versions to retain.
        /// </summary>
        [Input("maxCount")]
        public Input<int>? MaxCount { get; set; }

        /// <summary>
        /// The ARN of an IAM service role under which the application version is deleted.  Elastic Beanstalk must have permission to assume this role.
        /// </summary>
        [Input("serviceRole", required: true)]
        public Input<string> ServiceRole { get; set; } = null!;

        public ApplicationAppversionLifecycleArgs()
        {
        }
    }

    public sealed class ApplicationAppversionLifecycleGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Set to `true` to delete a version's source bundle from S3 when the application version is deleted.
        /// </summary>
        [Input("deleteSourceFromS3")]
        public Input<bool>? DeleteSourceFromS3 { get; set; }

        /// <summary>
        /// The number of days to retain an application version.
        /// </summary>
        [Input("maxAgeInDays")]
        public Input<int>? MaxAgeInDays { get; set; }

        /// <summary>
        /// The maximum number of application versions to retain.
        /// </summary>
        [Input("maxCount")]
        public Input<int>? MaxCount { get; set; }

        /// <summary>
        /// The ARN of an IAM service role under which the application version is deleted.  Elastic Beanstalk must have permission to assume this role.
        /// </summary>
        [Input("serviceRole", required: true)]
        public Input<string> ServiceRole { get; set; } = null!;

        public ApplicationAppversionLifecycleGetArgs()
        {
        }
    }
    }

    namespace Outputs
    {

    [OutputType]
    public sealed class ApplicationAppversionLifecycle
    {
        /// <summary>
        /// Set to `true` to delete a version's source bundle from S3 when the application version is deleted.
        /// </summary>
        public readonly bool? DeleteSourceFromS3;
        /// <summary>
        /// The number of days to retain an application version.
        /// </summary>
        public readonly int? MaxAgeInDays;
        /// <summary>
        /// The maximum number of application versions to retain.
        /// </summary>
        public readonly int? MaxCount;
        /// <summary>
        /// The ARN of an IAM service role under which the application version is deleted.  Elastic Beanstalk must have permission to assume this role.
        /// </summary>
        public readonly string ServiceRole;

        [OutputConstructor]
        private ApplicationAppversionLifecycle(
            bool? deleteSourceFromS3,
            int? maxAgeInDays,
            int? maxCount,
            string serviceRole)
        {
            DeleteSourceFromS3 = deleteSourceFromS3;
            MaxAgeInDays = maxAgeInDays;
            MaxCount = maxCount;
            ServiceRole = serviceRole;
        }
    }
    }
}
