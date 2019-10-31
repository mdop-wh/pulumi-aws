// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.Elasticloadbalancing
{
    /// <summary>
    /// Provides an Elastic Load Balancer resource, also known as a "Classic
    /// Load Balancer" after the release of
    /// [Application/Network Load Balancers](https://www.terraform.io/docs/providers/aws/r/lb.html).
    /// 
    /// &gt; **NOTE on ELB Instances and ELB Attachments:** This provider currently
    /// provides both a standalone ELB Attachment resource
    /// (describing an instance attached to an ELB), and an ELB resource with
    /// `instances` defined in-line. At this time you cannot use an ELB with in-line
    /// instances in conjunction with a ELB Attachment resources. Doing so will cause a
    /// conflict and will overwrite attachments.
    /// 
    /// ## Note on ECDSA Key Algorithm
    /// 
    /// If the ARN of the `ssl_certificate_id` that is pointed to references a
    /// certificate that was signed by an ECDSA key, note that ELB only supports the
    /// P256 and P384 curves.  Using a certificate signed by a key using a different
    /// curve could produce the error `ERR_SSL_VERSION_OR_CIPHER_MISMATCH` in your
    /// browser.
    /// 
    /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/elb_legacy.html.markdown.
    /// </summary>
    public partial class LoadBalancer : Pulumi.CustomResource
    {
        /// <summary>
        /// An Access Logs block. Access Logs documented below.
        /// </summary>
        [Output("accessLogs")]
        public Output<Outputs.LoadBalancerAccessLogs?> AccessLogs { get; private set; } = null!;

        /// <summary>
        /// The ARN of the ELB
        /// </summary>
        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        /// <summary>
        /// The AZ's to serve traffic in.
        /// </summary>
        [Output("availabilityZones")]
        public Output<ImmutableArray<string>> AvailabilityZones { get; private set; } = null!;

        /// <summary>
        /// Boolean to enable connection draining. Default: `false`
        /// </summary>
        [Output("connectionDraining")]
        public Output<bool?> ConnectionDraining { get; private set; } = null!;

        /// <summary>
        /// The time in seconds to allow for connections to drain. Default: `300`
        /// </summary>
        [Output("connectionDrainingTimeout")]
        public Output<int?> ConnectionDrainingTimeout { get; private set; } = null!;

        /// <summary>
        /// Enable cross-zone load balancing. Default: `true`
        /// </summary>
        [Output("crossZoneLoadBalancing")]
        public Output<bool?> CrossZoneLoadBalancing { get; private set; } = null!;

        /// <summary>
        /// The DNS name of the ELB
        /// </summary>
        [Output("dnsName")]
        public Output<string> DnsName { get; private set; } = null!;

        /// <summary>
        /// A health_check block. Health Check documented below.
        /// </summary>
        [Output("healthCheck")]
        public Output<Outputs.LoadBalancerHealthCheck> HealthCheck { get; private set; } = null!;

        /// <summary>
        /// The time in seconds that the connection is allowed to be idle. Default: `60`
        /// </summary>
        [Output("idleTimeout")]
        public Output<int?> IdleTimeout { get; private set; } = null!;

        /// <summary>
        /// A list of instance ids to place in the ELB pool.
        /// </summary>
        [Output("instances")]
        public Output<ImmutableArray<string>> Instances { get; private set; } = null!;

        /// <summary>
        /// If true, ELB will be an internal ELB.
        /// </summary>
        [Output("internal")]
        public Output<bool> Internal { get; private set; } = null!;

        /// <summary>
        /// A list of listener blocks. Listeners documented below.
        /// </summary>
        [Output("listeners")]
        public Output<ImmutableArray<Outputs.LoadBalancerListeners>> Listeners { get; private set; } = null!;

        /// <summary>
        /// The name of the ELB. By default generated by this provider.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// Creates a unique name beginning with the specified
        /// prefix. Conflicts with `name`.
        /// </summary>
        [Output("namePrefix")]
        public Output<string?> NamePrefix { get; private set; } = null!;

        /// <summary>
        /// A list of security group IDs to assign to the ELB.
        /// Only valid if creating an ELB within a VPC
        /// </summary>
        [Output("securityGroups")]
        public Output<ImmutableArray<string>> SecurityGroups { get; private set; } = null!;

        /// <summary>
        /// The name of the security group that you can use as
        /// part of your inbound rules for your load balancer's back-end application
        /// instances. Use this for Classic or Default VPC only.
        /// </summary>
        [Output("sourceSecurityGroup")]
        public Output<string> SourceSecurityGroup { get; private set; } = null!;

        /// <summary>
        /// The ID of the security group that you can use as
        /// part of your inbound rules for your load balancer's back-end application
        /// instances. Only available on ELBs launched in a VPC.
        /// </summary>
        [Output("sourceSecurityGroupId")]
        public Output<string> SourceSecurityGroupId { get; private set; } = null!;

        /// <summary>
        /// A list of subnet IDs to attach to the ELB.
        /// </summary>
        [Output("subnets")]
        public Output<ImmutableArray<string>> Subnets { get; private set; } = null!;

        /// <summary>
        /// A mapping of tags to assign to the resource.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableDictionary<string, object>?> Tags { get; private set; } = null!;

        /// <summary>
        /// The canonical hosted zone ID of the ELB (to be used in a Route 53 Alias record)
        /// </summary>
        [Output("zoneId")]
        public Output<string> ZoneId { get; private set; } = null!;


        /// <summary>
        /// Create a LoadBalancer resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public LoadBalancer(string name, LoadBalancerArgs args, CustomResourceOptions? options = null)
            : base("aws:elasticloadbalancing/loadBalancer:LoadBalancer", name, args, MakeResourceOptions(options, ""))
        {
        }

        private LoadBalancer(string name, Input<string> id, LoadBalancerState? state = null, CustomResourceOptions? options = null)
            : base("aws:elasticloadbalancing/loadBalancer:LoadBalancer", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing LoadBalancer resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static LoadBalancer Get(string name, Input<string> id, LoadBalancerState? state = null, CustomResourceOptions? options = null)
        {
            return new LoadBalancer(name, id, state, options);
        }
    }

    public sealed class LoadBalancerArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// An Access Logs block. Access Logs documented below.
        /// </summary>
        [Input("accessLogs")]
        public Input<Inputs.LoadBalancerAccessLogsArgs>? AccessLogs { get; set; }

        [Input("availabilityZones")]
        private InputList<string>? _availabilityZones;

        /// <summary>
        /// The AZ's to serve traffic in.
        /// </summary>
        public InputList<string> AvailabilityZones
        {
            get => _availabilityZones ?? (_availabilityZones = new InputList<string>());
            set => _availabilityZones = value;
        }

        /// <summary>
        /// Boolean to enable connection draining. Default: `false`
        /// </summary>
        [Input("connectionDraining")]
        public Input<bool>? ConnectionDraining { get; set; }

        /// <summary>
        /// The time in seconds to allow for connections to drain. Default: `300`
        /// </summary>
        [Input("connectionDrainingTimeout")]
        public Input<int>? ConnectionDrainingTimeout { get; set; }

        /// <summary>
        /// Enable cross-zone load balancing. Default: `true`
        /// </summary>
        [Input("crossZoneLoadBalancing")]
        public Input<bool>? CrossZoneLoadBalancing { get; set; }

        /// <summary>
        /// A health_check block. Health Check documented below.
        /// </summary>
        [Input("healthCheck")]
        public Input<Inputs.LoadBalancerHealthCheckArgs>? HealthCheck { get; set; }

        /// <summary>
        /// The time in seconds that the connection is allowed to be idle. Default: `60`
        /// </summary>
        [Input("idleTimeout")]
        public Input<int>? IdleTimeout { get; set; }

        [Input("instances")]
        private InputList<string>? _instances;

        /// <summary>
        /// A list of instance ids to place in the ELB pool.
        /// </summary>
        public InputList<string> Instances
        {
            get => _instances ?? (_instances = new InputList<string>());
            set => _instances = value;
        }

        /// <summary>
        /// If true, ELB will be an internal ELB.
        /// </summary>
        [Input("internal")]
        public Input<bool>? Internal { get; set; }

        [Input("listeners", required: true)]
        private InputList<Inputs.LoadBalancerListenersArgs>? _listeners;

        /// <summary>
        /// A list of listener blocks. Listeners documented below.
        /// </summary>
        public InputList<Inputs.LoadBalancerListenersArgs> Listeners
        {
            get => _listeners ?? (_listeners = new InputList<Inputs.LoadBalancerListenersArgs>());
            set => _listeners = value;
        }

        /// <summary>
        /// The name of the ELB. By default generated by this provider.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// Creates a unique name beginning with the specified
        /// prefix. Conflicts with `name`.
        /// </summary>
        [Input("namePrefix")]
        public Input<string>? NamePrefix { get; set; }

        [Input("securityGroups")]
        private InputList<string>? _securityGroups;

        /// <summary>
        /// A list of security group IDs to assign to the ELB.
        /// Only valid if creating an ELB within a VPC
        /// </summary>
        public InputList<string> SecurityGroups
        {
            get => _securityGroups ?? (_securityGroups = new InputList<string>());
            set => _securityGroups = value;
        }

        /// <summary>
        /// The name of the security group that you can use as
        /// part of your inbound rules for your load balancer's back-end application
        /// instances. Use this for Classic or Default VPC only.
        /// </summary>
        [Input("sourceSecurityGroup")]
        public Input<string>? SourceSecurityGroup { get; set; }

        [Input("subnets")]
        private InputList<string>? _subnets;

        /// <summary>
        /// A list of subnet IDs to attach to the ELB.
        /// </summary>
        public InputList<string> Subnets
        {
            get => _subnets ?? (_subnets = new InputList<string>());
            set => _subnets = value;
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

        public LoadBalancerArgs()
        {
        }
    }

    public sealed class LoadBalancerState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// An Access Logs block. Access Logs documented below.
        /// </summary>
        [Input("accessLogs")]
        public Input<Inputs.LoadBalancerAccessLogsGetArgs>? AccessLogs { get; set; }

        /// <summary>
        /// The ARN of the ELB
        /// </summary>
        [Input("arn")]
        public Input<string>? Arn { get; set; }

        [Input("availabilityZones")]
        private InputList<string>? _availabilityZones;

        /// <summary>
        /// The AZ's to serve traffic in.
        /// </summary>
        public InputList<string> AvailabilityZones
        {
            get => _availabilityZones ?? (_availabilityZones = new InputList<string>());
            set => _availabilityZones = value;
        }

        /// <summary>
        /// Boolean to enable connection draining. Default: `false`
        /// </summary>
        [Input("connectionDraining")]
        public Input<bool>? ConnectionDraining { get; set; }

        /// <summary>
        /// The time in seconds to allow for connections to drain. Default: `300`
        /// </summary>
        [Input("connectionDrainingTimeout")]
        public Input<int>? ConnectionDrainingTimeout { get; set; }

        /// <summary>
        /// Enable cross-zone load balancing. Default: `true`
        /// </summary>
        [Input("crossZoneLoadBalancing")]
        public Input<bool>? CrossZoneLoadBalancing { get; set; }

        /// <summary>
        /// The DNS name of the ELB
        /// </summary>
        [Input("dnsName")]
        public Input<string>? DnsName { get; set; }

        /// <summary>
        /// A health_check block. Health Check documented below.
        /// </summary>
        [Input("healthCheck")]
        public Input<Inputs.LoadBalancerHealthCheckGetArgs>? HealthCheck { get; set; }

        /// <summary>
        /// The time in seconds that the connection is allowed to be idle. Default: `60`
        /// </summary>
        [Input("idleTimeout")]
        public Input<int>? IdleTimeout { get; set; }

        [Input("instances")]
        private InputList<string>? _instances;

        /// <summary>
        /// A list of instance ids to place in the ELB pool.
        /// </summary>
        public InputList<string> Instances
        {
            get => _instances ?? (_instances = new InputList<string>());
            set => _instances = value;
        }

        /// <summary>
        /// If true, ELB will be an internal ELB.
        /// </summary>
        [Input("internal")]
        public Input<bool>? Internal { get; set; }

        [Input("listeners")]
        private InputList<Inputs.LoadBalancerListenersGetArgs>? _listeners;

        /// <summary>
        /// A list of listener blocks. Listeners documented below.
        /// </summary>
        public InputList<Inputs.LoadBalancerListenersGetArgs> Listeners
        {
            get => _listeners ?? (_listeners = new InputList<Inputs.LoadBalancerListenersGetArgs>());
            set => _listeners = value;
        }

        /// <summary>
        /// The name of the ELB. By default generated by this provider.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// Creates a unique name beginning with the specified
        /// prefix. Conflicts with `name`.
        /// </summary>
        [Input("namePrefix")]
        public Input<string>? NamePrefix { get; set; }

        [Input("securityGroups")]
        private InputList<string>? _securityGroups;

        /// <summary>
        /// A list of security group IDs to assign to the ELB.
        /// Only valid if creating an ELB within a VPC
        /// </summary>
        public InputList<string> SecurityGroups
        {
            get => _securityGroups ?? (_securityGroups = new InputList<string>());
            set => _securityGroups = value;
        }

        /// <summary>
        /// The name of the security group that you can use as
        /// part of your inbound rules for your load balancer's back-end application
        /// instances. Use this for Classic or Default VPC only.
        /// </summary>
        [Input("sourceSecurityGroup")]
        public Input<string>? SourceSecurityGroup { get; set; }

        /// <summary>
        /// The ID of the security group that you can use as
        /// part of your inbound rules for your load balancer's back-end application
        /// instances. Only available on ELBs launched in a VPC.
        /// </summary>
        [Input("sourceSecurityGroupId")]
        public Input<string>? SourceSecurityGroupId { get; set; }

        [Input("subnets")]
        private InputList<string>? _subnets;

        /// <summary>
        /// A list of subnet IDs to attach to the ELB.
        /// </summary>
        public InputList<string> Subnets
        {
            get => _subnets ?? (_subnets = new InputList<string>());
            set => _subnets = value;
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
        /// The canonical hosted zone ID of the ELB (to be used in a Route 53 Alias record)
        /// </summary>
        [Input("zoneId")]
        public Input<string>? ZoneId { get; set; }

        public LoadBalancerState()
        {
        }
    }

    namespace Inputs
    {

    public sealed class LoadBalancerAccessLogsArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The S3 bucket name to store the logs in.
        /// </summary>
        [Input("bucket", required: true)]
        public Input<string> Bucket { get; set; } = null!;

        /// <summary>
        /// The S3 bucket prefix. Logs are stored in the root if not configured.
        /// </summary>
        [Input("bucketPrefix")]
        public Input<string>? BucketPrefix { get; set; }

        /// <summary>
        /// Boolean to enable / disable `access_logs`. Default is `true`
        /// </summary>
        [Input("enabled")]
        public Input<bool>? Enabled { get; set; }

        /// <summary>
        /// The interval between checks.
        /// </summary>
        [Input("interval")]
        public Input<int>? Interval { get; set; }

        public LoadBalancerAccessLogsArgs()
        {
        }
    }

    public sealed class LoadBalancerAccessLogsGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The S3 bucket name to store the logs in.
        /// </summary>
        [Input("bucket", required: true)]
        public Input<string> Bucket { get; set; } = null!;

        /// <summary>
        /// The S3 bucket prefix. Logs are stored in the root if not configured.
        /// </summary>
        [Input("bucketPrefix")]
        public Input<string>? BucketPrefix { get; set; }

        /// <summary>
        /// Boolean to enable / disable `access_logs`. Default is `true`
        /// </summary>
        [Input("enabled")]
        public Input<bool>? Enabled { get; set; }

        /// <summary>
        /// The interval between checks.
        /// </summary>
        [Input("interval")]
        public Input<int>? Interval { get; set; }

        public LoadBalancerAccessLogsGetArgs()
        {
        }
    }

    public sealed class LoadBalancerHealthCheckArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The number of checks before the instance is declared healthy.
        /// </summary>
        [Input("healthyThreshold", required: true)]
        public Input<int> HealthyThreshold { get; set; } = null!;

        /// <summary>
        /// The interval between checks.
        /// </summary>
        [Input("interval", required: true)]
        public Input<int> Interval { get; set; } = null!;

        /// <summary>
        /// The target of the check. Valid pattern is "${PROTOCOL}:${PORT}${PATH}", where PROTOCOL
        /// values are:
        /// * `HTTP`, `HTTPS` - PORT and PATH are required
        /// * `TCP`, `SSL` - PORT is required, PATH is not supported
        /// </summary>
        [Input("target", required: true)]
        public Input<string> Target { get; set; } = null!;

        /// <summary>
        /// The length of time before the check times out.
        /// </summary>
        [Input("timeout", required: true)]
        public Input<int> Timeout { get; set; } = null!;

        /// <summary>
        /// The number of checks before the instance is declared unhealthy.
        /// </summary>
        [Input("unhealthyThreshold", required: true)]
        public Input<int> UnhealthyThreshold { get; set; } = null!;

        public LoadBalancerHealthCheckArgs()
        {
        }
    }

    public sealed class LoadBalancerHealthCheckGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The number of checks before the instance is declared healthy.
        /// </summary>
        [Input("healthyThreshold", required: true)]
        public Input<int> HealthyThreshold { get; set; } = null!;

        /// <summary>
        /// The interval between checks.
        /// </summary>
        [Input("interval", required: true)]
        public Input<int> Interval { get; set; } = null!;

        /// <summary>
        /// The target of the check. Valid pattern is "${PROTOCOL}:${PORT}${PATH}", where PROTOCOL
        /// values are:
        /// * `HTTP`, `HTTPS` - PORT and PATH are required
        /// * `TCP`, `SSL` - PORT is required, PATH is not supported
        /// </summary>
        [Input("target", required: true)]
        public Input<string> Target { get; set; } = null!;

        /// <summary>
        /// The length of time before the check times out.
        /// </summary>
        [Input("timeout", required: true)]
        public Input<int> Timeout { get; set; } = null!;

        /// <summary>
        /// The number of checks before the instance is declared unhealthy.
        /// </summary>
        [Input("unhealthyThreshold", required: true)]
        public Input<int> UnhealthyThreshold { get; set; } = null!;

        public LoadBalancerHealthCheckGetArgs()
        {
        }
    }

    public sealed class LoadBalancerListenersArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The port on the instance to route to
        /// </summary>
        [Input("instancePort", required: true)]
        public Input<int> InstancePort { get; set; } = null!;

        /// <summary>
        /// The protocol to use to the instance. Valid
        /// values are `HTTP`, `HTTPS`, `TCP`, or `SSL`
        /// </summary>
        [Input("instanceProtocol", required: true)]
        public Input<string> InstanceProtocol { get; set; } = null!;

        /// <summary>
        /// The port to listen on for the load balancer
        /// </summary>
        [Input("lbPort", required: true)]
        public Input<int> LbPort { get; set; } = null!;

        /// <summary>
        /// The protocol to listen on. Valid values are `HTTP`,
        /// `HTTPS`, `TCP`, or `SSL`
        /// </summary>
        [Input("lbProtocol", required: true)]
        public Input<string> LbProtocol { get; set; } = null!;

        /// <summary>
        /// The ARN of an SSL certificate you have
        /// uploaded to AWS IAM. **Note ECDSA-specific restrictions below.  Only valid when `lb_protocol` is either HTTPS or SSL**
        /// </summary>
        [Input("sslCertificateId")]
        public Input<string>? SslCertificateId { get; set; }

        public LoadBalancerListenersArgs()
        {
        }
    }

    public sealed class LoadBalancerListenersGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The port on the instance to route to
        /// </summary>
        [Input("instancePort", required: true)]
        public Input<int> InstancePort { get; set; } = null!;

        /// <summary>
        /// The protocol to use to the instance. Valid
        /// values are `HTTP`, `HTTPS`, `TCP`, or `SSL`
        /// </summary>
        [Input("instanceProtocol", required: true)]
        public Input<string> InstanceProtocol { get; set; } = null!;

        /// <summary>
        /// The port to listen on for the load balancer
        /// </summary>
        [Input("lbPort", required: true)]
        public Input<int> LbPort { get; set; } = null!;

        /// <summary>
        /// The protocol to listen on. Valid values are `HTTP`,
        /// `HTTPS`, `TCP`, or `SSL`
        /// </summary>
        [Input("lbProtocol", required: true)]
        public Input<string> LbProtocol { get; set; } = null!;

        /// <summary>
        /// The ARN of an SSL certificate you have
        /// uploaded to AWS IAM. **Note ECDSA-specific restrictions below.  Only valid when `lb_protocol` is either HTTPS or SSL**
        /// </summary>
        [Input("sslCertificateId")]
        public Input<string>? SslCertificateId { get; set; }

        public LoadBalancerListenersGetArgs()
        {
        }
    }
    }

    namespace Outputs
    {

    [OutputType]
    public sealed class LoadBalancerAccessLogs
    {
        /// <summary>
        /// The S3 bucket name to store the logs in.
        /// </summary>
        public readonly string Bucket;
        /// <summary>
        /// The S3 bucket prefix. Logs are stored in the root if not configured.
        /// </summary>
        public readonly string? BucketPrefix;
        /// <summary>
        /// Boolean to enable / disable `access_logs`. Default is `true`
        /// </summary>
        public readonly bool? Enabled;
        /// <summary>
        /// The interval between checks.
        /// </summary>
        public readonly int? Interval;

        [OutputConstructor]
        private LoadBalancerAccessLogs(
            string bucket,
            string? bucketPrefix,
            bool? enabled,
            int? interval)
        {
            Bucket = bucket;
            BucketPrefix = bucketPrefix;
            Enabled = enabled;
            Interval = interval;
        }
    }

    [OutputType]
    public sealed class LoadBalancerHealthCheck
    {
        /// <summary>
        /// The number of checks before the instance is declared healthy.
        /// </summary>
        public readonly int HealthyThreshold;
        /// <summary>
        /// The interval between checks.
        /// </summary>
        public readonly int Interval;
        /// <summary>
        /// The target of the check. Valid pattern is "${PROTOCOL}:${PORT}${PATH}", where PROTOCOL
        /// values are:
        /// * `HTTP`, `HTTPS` - PORT and PATH are required
        /// * `TCP`, `SSL` - PORT is required, PATH is not supported
        /// </summary>
        public readonly string Target;
        /// <summary>
        /// The length of time before the check times out.
        /// </summary>
        public readonly int Timeout;
        /// <summary>
        /// The number of checks before the instance is declared unhealthy.
        /// </summary>
        public readonly int UnhealthyThreshold;

        [OutputConstructor]
        private LoadBalancerHealthCheck(
            int healthyThreshold,
            int interval,
            string target,
            int timeout,
            int unhealthyThreshold)
        {
            HealthyThreshold = healthyThreshold;
            Interval = interval;
            Target = target;
            Timeout = timeout;
            UnhealthyThreshold = unhealthyThreshold;
        }
    }

    [OutputType]
    public sealed class LoadBalancerListeners
    {
        /// <summary>
        /// The port on the instance to route to
        /// </summary>
        public readonly int InstancePort;
        /// <summary>
        /// The protocol to use to the instance. Valid
        /// values are `HTTP`, `HTTPS`, `TCP`, or `SSL`
        /// </summary>
        public readonly string InstanceProtocol;
        /// <summary>
        /// The port to listen on for the load balancer
        /// </summary>
        public readonly int LbPort;
        /// <summary>
        /// The protocol to listen on. Valid values are `HTTP`,
        /// `HTTPS`, `TCP`, or `SSL`
        /// </summary>
        public readonly string LbProtocol;
        /// <summary>
        /// The ARN of an SSL certificate you have
        /// uploaded to AWS IAM. **Note ECDSA-specific restrictions below.  Only valid when `lb_protocol` is either HTTPS or SSL**
        /// </summary>
        public readonly string? SslCertificateId;

        [OutputConstructor]
        private LoadBalancerListeners(
            int instancePort,
            string instanceProtocol,
            int lbPort,
            string lbProtocol,
            string? sslCertificateId)
        {
            InstancePort = instancePort;
            InstanceProtocol = instanceProtocol;
            LbPort = lbPort;
            LbProtocol = lbProtocol;
            SslCertificateId = sslCertificateId;
        }
    }
    }
}
