// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.Neptune
{
    /// <summary>
    /// ## Attributes
    /// 
    /// The following additional atttributes are provided:
    /// 
    /// * `id` - The name of the Neptune event notification subscription.
    /// * `arn` - The Amazon Resource Name of the Neptune event notification subscription.
    /// * `customer_aws_id` - The AWS customer account associated with the Neptune event notification subscription.
    /// 
    /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/neptune_event_subscription.html.markdown.
    /// </summary>
    public partial class EventSubscription : Pulumi.CustomResource
    {
        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        [Output("customerAwsId")]
        public Output<string> CustomerAwsId { get; private set; } = null!;

        /// <summary>
        /// A boolean flag to enable/disable the subscription. Defaults to true.
        /// </summary>
        [Output("enabled")]
        public Output<bool?> Enabled { get; private set; } = null!;

        /// <summary>
        /// A list of event categories for a `source_type` that you want to subscribe to. Run `aws neptune describe-event-categories` to find all the event categories.
        /// </summary>
        [Output("eventCategories")]
        public Output<ImmutableArray<string>> EventCategories { get; private set; } = null!;

        /// <summary>
        /// The name of the Neptune event subscription. By default generated by this provider.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// The name of the Neptune event subscription. Conflicts with `name`.
        /// </summary>
        [Output("namePrefix")]
        public Output<string> NamePrefix { get; private set; } = null!;

        /// <summary>
        /// The ARN of the SNS topic to send events to.
        /// </summary>
        [Output("snsTopicArn")]
        public Output<string> SnsTopicArn { get; private set; } = null!;

        /// <summary>
        /// A list of identifiers of the event sources for which events will be returned. If not specified, then all sources are included in the response. If specified, a `source_type` must also be specified.
        /// </summary>
        [Output("sourceIds")]
        public Output<ImmutableArray<string>> SourceIds { get; private set; } = null!;

        /// <summary>
        /// The type of source that will be generating the events. Valid options are `db-instance`, `db-security-group`, `db-parameter-group`, `db-snapshot`, `db-cluster` or `db-cluster-snapshot`. If not set, all sources will be subscribed to.
        /// </summary>
        [Output("sourceType")]
        public Output<string?> SourceType { get; private set; } = null!;

        /// <summary>
        /// A mapping of tags to assign to the resource.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableDictionary<string, object>?> Tags { get; private set; } = null!;


        /// <summary>
        /// Create a EventSubscription resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public EventSubscription(string name, EventSubscriptionArgs args, CustomResourceOptions? options = null)
            : base("aws:neptune/eventSubscription:EventSubscription", name, args, MakeResourceOptions(options, ""))
        {
        }

        private EventSubscription(string name, Input<string> id, EventSubscriptionState? state = null, CustomResourceOptions? options = null)
            : base("aws:neptune/eventSubscription:EventSubscription", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing EventSubscription resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static EventSubscription Get(string name, Input<string> id, EventSubscriptionState? state = null, CustomResourceOptions? options = null)
        {
            return new EventSubscription(name, id, state, options);
        }
    }

    public sealed class EventSubscriptionArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// A boolean flag to enable/disable the subscription. Defaults to true.
        /// </summary>
        [Input("enabled")]
        public Input<bool>? Enabled { get; set; }

        [Input("eventCategories")]
        private InputList<string>? _eventCategories;

        /// <summary>
        /// A list of event categories for a `source_type` that you want to subscribe to. Run `aws neptune describe-event-categories` to find all the event categories.
        /// </summary>
        public InputList<string> EventCategories
        {
            get => _eventCategories ?? (_eventCategories = new InputList<string>());
            set => _eventCategories = value;
        }

        /// <summary>
        /// The name of the Neptune event subscription. By default generated by this provider.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The name of the Neptune event subscription. Conflicts with `name`.
        /// </summary>
        [Input("namePrefix")]
        public Input<string>? NamePrefix { get; set; }

        /// <summary>
        /// The ARN of the SNS topic to send events to.
        /// </summary>
        [Input("snsTopicArn", required: true)]
        public Input<string> SnsTopicArn { get; set; } = null!;

        [Input("sourceIds")]
        private InputList<string>? _sourceIds;

        /// <summary>
        /// A list of identifiers of the event sources for which events will be returned. If not specified, then all sources are included in the response. If specified, a `source_type` must also be specified.
        /// </summary>
        public InputList<string> SourceIds
        {
            get => _sourceIds ?? (_sourceIds = new InputList<string>());
            set => _sourceIds = value;
        }

        /// <summary>
        /// The type of source that will be generating the events. Valid options are `db-instance`, `db-security-group`, `db-parameter-group`, `db-snapshot`, `db-cluster` or `db-cluster-snapshot`. If not set, all sources will be subscribed to.
        /// </summary>
        [Input("sourceType")]
        public Input<string>? SourceType { get; set; }

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

        public EventSubscriptionArgs()
        {
        }
    }

    public sealed class EventSubscriptionState : Pulumi.ResourceArgs
    {
        [Input("arn")]
        public Input<string>? Arn { get; set; }

        [Input("customerAwsId")]
        public Input<string>? CustomerAwsId { get; set; }

        /// <summary>
        /// A boolean flag to enable/disable the subscription. Defaults to true.
        /// </summary>
        [Input("enabled")]
        public Input<bool>? Enabled { get; set; }

        [Input("eventCategories")]
        private InputList<string>? _eventCategories;

        /// <summary>
        /// A list of event categories for a `source_type` that you want to subscribe to. Run `aws neptune describe-event-categories` to find all the event categories.
        /// </summary>
        public InputList<string> EventCategories
        {
            get => _eventCategories ?? (_eventCategories = new InputList<string>());
            set => _eventCategories = value;
        }

        /// <summary>
        /// The name of the Neptune event subscription. By default generated by this provider.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The name of the Neptune event subscription. Conflicts with `name`.
        /// </summary>
        [Input("namePrefix")]
        public Input<string>? NamePrefix { get; set; }

        /// <summary>
        /// The ARN of the SNS topic to send events to.
        /// </summary>
        [Input("snsTopicArn")]
        public Input<string>? SnsTopicArn { get; set; }

        [Input("sourceIds")]
        private InputList<string>? _sourceIds;

        /// <summary>
        /// A list of identifiers of the event sources for which events will be returned. If not specified, then all sources are included in the response. If specified, a `source_type` must also be specified.
        /// </summary>
        public InputList<string> SourceIds
        {
            get => _sourceIds ?? (_sourceIds = new InputList<string>());
            set => _sourceIds = value;
        }

        /// <summary>
        /// The type of source that will be generating the events. Valid options are `db-instance`, `db-security-group`, `db-parameter-group`, `db-snapshot`, `db-cluster` or `db-cluster-snapshot`. If not set, all sources will be subscribed to.
        /// </summary>
        [Input("sourceType")]
        public Input<string>? SourceType { get; set; }

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

        public EventSubscriptionState()
        {
        }
    }
}
