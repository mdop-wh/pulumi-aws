// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.Batch
{
    /// <summary>
    /// Provides a Batch Job Queue resource.
    /// 
    /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/batch_job_queue.html.markdown.
    /// </summary>
    public partial class JobQueue : Pulumi.CustomResource
    {
        /// <summary>
        /// The Amazon Resource Name of the job queue.
        /// </summary>
        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        /// <summary>
        /// Specifies the set of compute environments
        /// mapped to a job queue and their order.  The position of the compute environments
        /// in the list will dictate the order. You can associate up to 3 compute environments
        /// with a job queue.
        /// </summary>
        [Output("computeEnvironments")]
        public Output<ImmutableArray<string>> ComputeEnvironments { get; private set; } = null!;

        /// <summary>
        /// Specifies the name of the job queue.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// The priority of the job queue. Job queues with a higher priority
        /// are evaluated first when associated with the same compute environment.
        /// </summary>
        [Output("priority")]
        public Output<int> Priority { get; private set; } = null!;

        /// <summary>
        /// The state of the job queue. Must be one of: `ENABLED` or `DISABLED`
        /// </summary>
        [Output("state")]
        public Output<string> State { get; private set; } = null!;


        /// <summary>
        /// Create a JobQueue resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public JobQueue(string name, JobQueueArgs args, CustomResourceOptions? options = null)
            : base("aws:batch/jobQueue:JobQueue", name, args, MakeResourceOptions(options, ""))
        {
        }

        private JobQueue(string name, Input<string> id, JobQueueState? state = null, CustomResourceOptions? options = null)
            : base("aws:batch/jobQueue:JobQueue", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing JobQueue resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static JobQueue Get(string name, Input<string> id, JobQueueState? state = null, CustomResourceOptions? options = null)
        {
            return new JobQueue(name, id, state, options);
        }
    }

    public sealed class JobQueueArgs : Pulumi.ResourceArgs
    {
        [Input("computeEnvironments", required: true)]
        private InputList<string>? _computeEnvironments;

        /// <summary>
        /// Specifies the set of compute environments
        /// mapped to a job queue and their order.  The position of the compute environments
        /// in the list will dictate the order. You can associate up to 3 compute environments
        /// with a job queue.
        /// </summary>
        public InputList<string> ComputeEnvironments
        {
            get => _computeEnvironments ?? (_computeEnvironments = new InputList<string>());
            set => _computeEnvironments = value;
        }

        /// <summary>
        /// Specifies the name of the job queue.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The priority of the job queue. Job queues with a higher priority
        /// are evaluated first when associated with the same compute environment.
        /// </summary>
        [Input("priority", required: true)]
        public Input<int> Priority { get; set; } = null!;

        /// <summary>
        /// The state of the job queue. Must be one of: `ENABLED` or `DISABLED`
        /// </summary>
        [Input("state", required: true)]
        public Input<string> State { get; set; } = null!;

        public JobQueueArgs()
        {
        }
    }

    public sealed class JobQueueState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The Amazon Resource Name of the job queue.
        /// </summary>
        [Input("arn")]
        public Input<string>? Arn { get; set; }

        [Input("computeEnvironments")]
        private InputList<string>? _computeEnvironments;

        /// <summary>
        /// Specifies the set of compute environments
        /// mapped to a job queue and their order.  The position of the compute environments
        /// in the list will dictate the order. You can associate up to 3 compute environments
        /// with a job queue.
        /// </summary>
        public InputList<string> ComputeEnvironments
        {
            get => _computeEnvironments ?? (_computeEnvironments = new InputList<string>());
            set => _computeEnvironments = value;
        }

        /// <summary>
        /// Specifies the name of the job queue.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The priority of the job queue. Job queues with a higher priority
        /// are evaluated first when associated with the same compute environment.
        /// </summary>
        [Input("priority")]
        public Input<int>? Priority { get; set; }

        /// <summary>
        /// The state of the job queue. Must be one of: `ENABLED` or `DISABLED`
        /// </summary>
        [Input("state")]
        public Input<string>? State { get; set; }

        public JobQueueState()
        {
        }
    }
}
