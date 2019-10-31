// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.Autoscaling
{
    /// <summary>
    /// Provides an AutoScaling Group with Notification support, via SNS Topics. Each of
    /// the `notifications` map to a [Notification Configuration][2] inside Amazon Web
    /// Services, and are applied to each AutoScaling Group you supply.
    /// 
    /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/autoscaling_notification.html.markdown.
    /// </summary>
    public partial class Notification : Pulumi.CustomResource
    {
        /// <summary>
        /// A list of AutoScaling Group Names
        /// </summary>
        [Output("groupNames")]
        public Output<ImmutableArray<string>> GroupNames { get; private set; } = null!;

        /// <summary>
        /// A list of Notification Types that trigger
        /// notifications. Acceptable values are documented [in the AWS documentation here][1]
        /// </summary>
        [Output("notifications")]
        public Output<ImmutableArray<string>> Notifications { get; private set; } = null!;

        /// <summary>
        /// The Topic ARN for notifications to be sent through
        /// </summary>
        [Output("topicArn")]
        public Output<string> TopicArn { get; private set; } = null!;


        /// <summary>
        /// Create a Notification resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Notification(string name, NotificationArgs args, CustomResourceOptions? options = null)
            : base("aws:autoscaling/notification:Notification", name, args, MakeResourceOptions(options, ""))
        {
        }

        private Notification(string name, Input<string> id, NotificationState? state = null, CustomResourceOptions? options = null)
            : base("aws:autoscaling/notification:Notification", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing Notification resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Notification Get(string name, Input<string> id, NotificationState? state = null, CustomResourceOptions? options = null)
        {
            return new Notification(name, id, state, options);
        }
    }

    public sealed class NotificationArgs : Pulumi.ResourceArgs
    {
        [Input("groupNames", required: true)]
        private InputList<string>? _groupNames;

        /// <summary>
        /// A list of AutoScaling Group Names
        /// </summary>
        public InputList<string> GroupNames
        {
            get => _groupNames ?? (_groupNames = new InputList<string>());
            set => _groupNames = value;
        }

        [Input("notifications", required: true)]
        private InputList<string>? _notifications;

        /// <summary>
        /// A list of Notification Types that trigger
        /// notifications. Acceptable values are documented [in the AWS documentation here][1]
        /// </summary>
        public InputList<string> Notifications
        {
            get => _notifications ?? (_notifications = new InputList<string>());
            set => _notifications = value;
        }

        /// <summary>
        /// The Topic ARN for notifications to be sent through
        /// </summary>
        [Input("topicArn", required: true)]
        public Input<string> TopicArn { get; set; } = null!;

        public NotificationArgs()
        {
        }
    }

    public sealed class NotificationState : Pulumi.ResourceArgs
    {
        [Input("groupNames")]
        private InputList<string>? _groupNames;

        /// <summary>
        /// A list of AutoScaling Group Names
        /// </summary>
        public InputList<string> GroupNames
        {
            get => _groupNames ?? (_groupNames = new InputList<string>());
            set => _groupNames = value;
        }

        [Input("notifications")]
        private InputList<string>? _notifications;

        /// <summary>
        /// A list of Notification Types that trigger
        /// notifications. Acceptable values are documented [in the AWS documentation here][1]
        /// </summary>
        public InputList<string> Notifications
        {
            get => _notifications ?? (_notifications = new InputList<string>());
            set => _notifications = value;
        }

        /// <summary>
        /// The Topic ARN for notifications to be sent through
        /// </summary>
        [Input("topicArn")]
        public Input<string>? TopicArn { get; set; }

        public NotificationState()
        {
        }
    }
}
