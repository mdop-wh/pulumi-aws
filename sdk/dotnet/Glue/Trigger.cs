// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.Glue
{
    /// <summary>
    /// Manages a Glue Trigger resource.
    /// 
    /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/glue_trigger.html.markdown.
    /// </summary>
    public partial class Trigger : Pulumi.CustomResource
    {
        /// <summary>
        /// List of actions initiated by this trigger when it fires. Defined below.
        /// </summary>
        [Output("actions")]
        public Output<ImmutableArray<Outputs.TriggerActions>> Actions { get; private set; } = null!;

        /// <summary>
        /// A description of the new trigger.
        /// </summary>
        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        /// <summary>
        /// Start the trigger. Defaults to `true`. Not valid to disable for `ON_DEMAND` type.
        /// </summary>
        [Output("enabled")]
        public Output<bool?> Enabled { get; private set; } = null!;

        /// <summary>
        /// The name of the trigger.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// A predicate to specify when the new trigger should fire. Required when trigger type is `CONDITIONAL`. Defined below.
        /// </summary>
        [Output("predicate")]
        public Output<Outputs.TriggerPredicate?> Predicate { get; private set; } = null!;

        /// <summary>
        /// A cron expression used to specify the schedule. [Time-Based Schedules for Jobs and Crawlers](https://docs.aws.amazon.com/glue/latest/dg/monitor-data-warehouse-schedule.html)
        /// </summary>
        [Output("schedule")]
        public Output<string?> Schedule { get; private set; } = null!;

        /// <summary>
        /// The type of trigger. Valid values are `CONDITIONAL`, `ON_DEMAND`, and `SCHEDULED`.
        /// </summary>
        [Output("type")]
        public Output<string> Type { get; private set; } = null!;


        /// <summary>
        /// Create a Trigger resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Trigger(string name, TriggerArgs args, CustomResourceOptions? options = null)
            : base("aws:glue/trigger:Trigger", name, args, MakeResourceOptions(options, ""))
        {
        }

        private Trigger(string name, Input<string> id, TriggerState? state = null, CustomResourceOptions? options = null)
            : base("aws:glue/trigger:Trigger", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing Trigger resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Trigger Get(string name, Input<string> id, TriggerState? state = null, CustomResourceOptions? options = null)
        {
            return new Trigger(name, id, state, options);
        }
    }

    public sealed class TriggerArgs : Pulumi.ResourceArgs
    {
        [Input("actions", required: true)]
        private InputList<Inputs.TriggerActionsArgs>? _actions;

        /// <summary>
        /// List of actions initiated by this trigger when it fires. Defined below.
        /// </summary>
        public InputList<Inputs.TriggerActionsArgs> Actions
        {
            get => _actions ?? (_actions = new InputList<Inputs.TriggerActionsArgs>());
            set => _actions = value;
        }

        /// <summary>
        /// A description of the new trigger.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// Start the trigger. Defaults to `true`. Not valid to disable for `ON_DEMAND` type.
        /// </summary>
        [Input("enabled")]
        public Input<bool>? Enabled { get; set; }

        /// <summary>
        /// The name of the trigger.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// A predicate to specify when the new trigger should fire. Required when trigger type is `CONDITIONAL`. Defined below.
        /// </summary>
        [Input("predicate")]
        public Input<Inputs.TriggerPredicateArgs>? Predicate { get; set; }

        /// <summary>
        /// A cron expression used to specify the schedule. [Time-Based Schedules for Jobs and Crawlers](https://docs.aws.amazon.com/glue/latest/dg/monitor-data-warehouse-schedule.html)
        /// </summary>
        [Input("schedule")]
        public Input<string>? Schedule { get; set; }

        /// <summary>
        /// The type of trigger. Valid values are `CONDITIONAL`, `ON_DEMAND`, and `SCHEDULED`.
        /// </summary>
        [Input("type", required: true)]
        public Input<string> Type { get; set; } = null!;

        public TriggerArgs()
        {
        }
    }

    public sealed class TriggerState : Pulumi.ResourceArgs
    {
        [Input("actions")]
        private InputList<Inputs.TriggerActionsGetArgs>? _actions;

        /// <summary>
        /// List of actions initiated by this trigger when it fires. Defined below.
        /// </summary>
        public InputList<Inputs.TriggerActionsGetArgs> Actions
        {
            get => _actions ?? (_actions = new InputList<Inputs.TriggerActionsGetArgs>());
            set => _actions = value;
        }

        /// <summary>
        /// A description of the new trigger.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// Start the trigger. Defaults to `true`. Not valid to disable for `ON_DEMAND` type.
        /// </summary>
        [Input("enabled")]
        public Input<bool>? Enabled { get; set; }

        /// <summary>
        /// The name of the trigger.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// A predicate to specify when the new trigger should fire. Required when trigger type is `CONDITIONAL`. Defined below.
        /// </summary>
        [Input("predicate")]
        public Input<Inputs.TriggerPredicateGetArgs>? Predicate { get; set; }

        /// <summary>
        /// A cron expression used to specify the schedule. [Time-Based Schedules for Jobs and Crawlers](https://docs.aws.amazon.com/glue/latest/dg/monitor-data-warehouse-schedule.html)
        /// </summary>
        [Input("schedule")]
        public Input<string>? Schedule { get; set; }

        /// <summary>
        /// The type of trigger. Valid values are `CONDITIONAL`, `ON_DEMAND`, and `SCHEDULED`.
        /// </summary>
        [Input("type")]
        public Input<string>? Type { get; set; }

        public TriggerState()
        {
        }
    }

    namespace Inputs
    {

    public sealed class TriggerActionsArgs : Pulumi.ResourceArgs
    {
        [Input("arguments")]
        private InputMap<object>? _arguments;

        /// <summary>
        /// Arguments to be passed to the job. You can specify arguments here that your own job-execution script consumes, as well as arguments that AWS Glue itself consumes.
        /// </summary>
        public InputMap<object> Arguments
        {
            get => _arguments ?? (_arguments = new InputMap<object>());
            set => _arguments = value;
        }

        /// <summary>
        /// The name of the job to watch.
        /// </summary>
        [Input("jobName", required: true)]
        public Input<string> JobName { get; set; } = null!;

        /// <summary>
        /// The job run timeout in minutes. It overrides the timeout value of the job.
        /// </summary>
        [Input("timeout")]
        public Input<int>? Timeout { get; set; }

        public TriggerActionsArgs()
        {
        }
    }

    public sealed class TriggerActionsGetArgs : Pulumi.ResourceArgs
    {
        [Input("arguments")]
        private InputMap<object>? _arguments;

        /// <summary>
        /// Arguments to be passed to the job. You can specify arguments here that your own job-execution script consumes, as well as arguments that AWS Glue itself consumes.
        /// </summary>
        public InputMap<object> Arguments
        {
            get => _arguments ?? (_arguments = new InputMap<object>());
            set => _arguments = value;
        }

        /// <summary>
        /// The name of the job to watch.
        /// </summary>
        [Input("jobName", required: true)]
        public Input<string> JobName { get; set; } = null!;

        /// <summary>
        /// The job run timeout in minutes. It overrides the timeout value of the job.
        /// </summary>
        [Input("timeout")]
        public Input<int>? Timeout { get; set; }

        public TriggerActionsGetArgs()
        {
        }
    }

    public sealed class TriggerPredicateArgs : Pulumi.ResourceArgs
    {
        [Input("conditions", required: true)]
        private InputList<TriggerPredicateConditionsArgs>? _conditions;

        /// <summary>
        /// A list of the conditions that determine when the trigger will fire. Defined below.
        /// </summary>
        public InputList<TriggerPredicateConditionsArgs> Conditions
        {
            get => _conditions ?? (_conditions = new InputList<TriggerPredicateConditionsArgs>());
            set => _conditions = value;
        }

        /// <summary>
        /// How to handle multiple conditions. Defaults to `AND`. Valid values are `AND` or `ANY`.
        /// </summary>
        [Input("logical")]
        public Input<string>? Logical { get; set; }

        public TriggerPredicateArgs()
        {
        }
    }

    public sealed class TriggerPredicateConditionsArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The name of the job to watch.
        /// </summary>
        [Input("jobName", required: true)]
        public Input<string> JobName { get; set; } = null!;

        /// <summary>
        /// A logical operator. Defaults to `EQUALS`.
        /// </summary>
        [Input("logicalOperator")]
        public Input<string>? LogicalOperator { get; set; }

        /// <summary>
        /// The condition state. Currently, the values supported are `SUCCEEDED`, `STOPPED`, `TIMEOUT` and `FAILED`.
        /// </summary>
        [Input("state", required: true)]
        public Input<string> State { get; set; } = null!;

        public TriggerPredicateConditionsArgs()
        {
        }
    }

    public sealed class TriggerPredicateConditionsGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The name of the job to watch.
        /// </summary>
        [Input("jobName", required: true)]
        public Input<string> JobName { get; set; } = null!;

        /// <summary>
        /// A logical operator. Defaults to `EQUALS`.
        /// </summary>
        [Input("logicalOperator")]
        public Input<string>? LogicalOperator { get; set; }

        /// <summary>
        /// The condition state. Currently, the values supported are `SUCCEEDED`, `STOPPED`, `TIMEOUT` and `FAILED`.
        /// </summary>
        [Input("state", required: true)]
        public Input<string> State { get; set; } = null!;

        public TriggerPredicateConditionsGetArgs()
        {
        }
    }

    public sealed class TriggerPredicateGetArgs : Pulumi.ResourceArgs
    {
        [Input("conditions", required: true)]
        private InputList<TriggerPredicateConditionsGetArgs>? _conditions;

        /// <summary>
        /// A list of the conditions that determine when the trigger will fire. Defined below.
        /// </summary>
        public InputList<TriggerPredicateConditionsGetArgs> Conditions
        {
            get => _conditions ?? (_conditions = new InputList<TriggerPredicateConditionsGetArgs>());
            set => _conditions = value;
        }

        /// <summary>
        /// How to handle multiple conditions. Defaults to `AND`. Valid values are `AND` or `ANY`.
        /// </summary>
        [Input("logical")]
        public Input<string>? Logical { get; set; }

        public TriggerPredicateGetArgs()
        {
        }
    }
    }

    namespace Outputs
    {

    [OutputType]
    public sealed class TriggerActions
    {
        /// <summary>
        /// Arguments to be passed to the job. You can specify arguments here that your own job-execution script consumes, as well as arguments that AWS Glue itself consumes.
        /// </summary>
        public readonly ImmutableDictionary<string, object>? Arguments;
        /// <summary>
        /// The name of the job to watch.
        /// </summary>
        public readonly string JobName;
        /// <summary>
        /// The job run timeout in minutes. It overrides the timeout value of the job.
        /// </summary>
        public readonly int? Timeout;

        [OutputConstructor]
        private TriggerActions(
            ImmutableDictionary<string, object>? arguments,
            string jobName,
            int? timeout)
        {
            Arguments = arguments;
            JobName = jobName;
            Timeout = timeout;
        }
    }

    [OutputType]
    public sealed class TriggerPredicate
    {
        /// <summary>
        /// A list of the conditions that determine when the trigger will fire. Defined below.
        /// </summary>
        public readonly ImmutableArray<TriggerPredicateConditions> Conditions;
        /// <summary>
        /// How to handle multiple conditions. Defaults to `AND`. Valid values are `AND` or `ANY`.
        /// </summary>
        public readonly string? Logical;

        [OutputConstructor]
        private TriggerPredicate(
            ImmutableArray<TriggerPredicateConditions> conditions,
            string? logical)
        {
            Conditions = conditions;
            Logical = logical;
        }
    }

    [OutputType]
    public sealed class TriggerPredicateConditions
    {
        /// <summary>
        /// The name of the job to watch.
        /// </summary>
        public readonly string JobName;
        /// <summary>
        /// A logical operator. Defaults to `EQUALS`.
        /// </summary>
        public readonly string? LogicalOperator;
        /// <summary>
        /// The condition state. Currently, the values supported are `SUCCEEDED`, `STOPPED`, `TIMEOUT` and `FAILED`.
        /// </summary>
        public readonly string State;

        [OutputConstructor]
        private TriggerPredicateConditions(
            string jobName,
            string? logicalOperator,
            string state)
        {
            JobName = jobName;
            LogicalOperator = logicalOperator;
            State = state;
        }
    }
    }
}
