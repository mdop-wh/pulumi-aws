// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.Elasticloadbalancing
{
    /// <summary>
    /// Attaches an EC2 instance to an Elastic Load Balancer (ELB). For attaching resources with Application Load Balancer (ALB) or Network Load Balancer (NLB), see the [`aws.lb.TargetGroupAttachment` resource](https://www.terraform.io/docs/providers/aws/r/lb_target_group_attachment.html).
    /// 
    /// &gt; **NOTE on ELB Instances and ELB Attachments:** This provider currently provides
    /// both a standalone ELB Attachment resource (describing an instance attached to
    /// an ELB), and an Elastic Load Balancer resource with
    /// `instances` defined in-line. At this time you cannot use an ELB with in-line
    /// instances in conjunction with an ELB Attachment resource. Doing so will cause a
    /// conflict and will overwrite attachments.
    /// 
    /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/elb_attachment_legacy.html.markdown.
    /// </summary>
    public partial class Attachment : Pulumi.CustomResource
    {
        /// <summary>
        /// The name of the ELB.
        /// </summary>
        [Output("elb")]
        public Output<string> Elb { get; private set; } = null!;

        /// <summary>
        /// Instance ID to place in the ELB pool.
        /// </summary>
        [Output("instance")]
        public Output<string> Instance { get; private set; } = null!;


        /// <summary>
        /// Create a Attachment resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Attachment(string name, AttachmentArgs args, CustomResourceOptions? options = null)
            : base("aws:elasticloadbalancing/attachment:Attachment", name, args, MakeResourceOptions(options, ""))
        {
        }

        private Attachment(string name, Input<string> id, AttachmentState? state = null, CustomResourceOptions? options = null)
            : base("aws:elasticloadbalancing/attachment:Attachment", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing Attachment resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Attachment Get(string name, Input<string> id, AttachmentState? state = null, CustomResourceOptions? options = null)
        {
            return new Attachment(name, id, state, options);
        }
    }

    public sealed class AttachmentArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The name of the ELB.
        /// </summary>
        [Input("elb", required: true)]
        public Input<string> Elb { get; set; } = null!;

        /// <summary>
        /// Instance ID to place in the ELB pool.
        /// </summary>
        [Input("instance", required: true)]
        public Input<string> Instance { get; set; } = null!;

        public AttachmentArgs()
        {
        }
    }

    public sealed class AttachmentState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The name of the ELB.
        /// </summary>
        [Input("elb")]
        public Input<string>? Elb { get; set; }

        /// <summary>
        /// Instance ID to place in the ELB pool.
        /// </summary>
        [Input("instance")]
        public Input<string>? Instance { get; set; }

        public AttachmentState()
        {
        }
    }
}
