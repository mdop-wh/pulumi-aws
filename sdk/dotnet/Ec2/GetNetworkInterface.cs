// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.Ec2
{
    public static partial class Invokes
    {
        /// <summary>
        /// Use this data source to get information about a Network Interface.
        /// 
        /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/network_interface.html.markdown.
        /// </summary>
        public static Task<GetNetworkInterfaceResult> GetNetworkInterface(GetNetworkInterfaceArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetNetworkInterfaceResult>("aws:ec2/getNetworkInterface:getNetworkInterface", args, options.WithVersion());
    }

    public sealed class GetNetworkInterfaceArgs : Pulumi.ResourceArgs
    {
        [Input("filters")]
        private InputList<Inputs.GetNetworkInterfaceFiltersArgs>? _filters;

        /// <summary>
        /// One or more name/value pairs to filter off of. There are several valid keys, for a full reference, check out [describe-network-interfaces](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-network-interfaces.html) in the AWS CLI reference.
        /// </summary>
        public InputList<Inputs.GetNetworkInterfaceFiltersArgs> Filters
        {
            get => _filters ?? (_filters = new InputList<Inputs.GetNetworkInterfaceFiltersArgs>());
            set => _filters = value;
        }

        /// <summary>
        /// The identifier for the network interface.
        /// </summary>
        [Input("id")]
        public Input<string>? Id { get; set; }

        [Input("tags")]
        private InputMap<object>? _tags;
        public InputMap<object> Tags
        {
            get => _tags ?? (_tags = new InputMap<object>());
            set => _tags = value;
        }

        public GetNetworkInterfaceArgs()
        {
        }
    }

    [OutputType]
    public sealed class GetNetworkInterfaceResult
    {
        /// <summary>
        /// The association information for an Elastic IP address (IPv4) associated with the network interface. See supported fields below.
        /// </summary>
        public readonly ImmutableArray<Outputs.GetNetworkInterfaceAssociationsResult> Associations;
        public readonly ImmutableArray<Outputs.GetNetworkInterfaceAttachmentsResult> Attachments;
        /// <summary>
        /// The Availability Zone.
        /// </summary>
        public readonly string AvailabilityZone;
        /// <summary>
        /// Description of the network interface.
        /// </summary>
        public readonly string Description;
        public readonly ImmutableArray<Outputs.GetNetworkInterfaceFiltersResult> Filters;
        public readonly string Id;
        /// <summary>
        /// The type of interface.
        /// </summary>
        public readonly string InterfaceType;
        /// <summary>
        /// List of IPv6 addresses to assign to the ENI.
        /// </summary>
        public readonly ImmutableArray<string> Ipv6Addresses;
        /// <summary>
        /// The MAC address.
        /// </summary>
        public readonly string MacAddress;
        /// <summary>
        /// The AWS account ID of the owner of the network interface.
        /// </summary>
        public readonly string OwnerId;
        /// <summary>
        /// The private DNS name.
        /// </summary>
        public readonly string PrivateDnsName;
        /// <summary>
        /// The private IPv4 address of the network interface within the subnet.
        /// </summary>
        public readonly string PrivateIp;
        /// <summary>
        /// The private IPv4 addresses associated with the network interface.
        /// </summary>
        public readonly ImmutableArray<string> PrivateIps;
        /// <summary>
        /// The ID of the entity that launched the instance on your behalf.
        /// </summary>
        public readonly string RequesterId;
        /// <summary>
        /// The list of security groups for the network interface.
        /// </summary>
        public readonly ImmutableArray<string> SecurityGroups;
        /// <summary>
        /// The ID of the subnet.
        /// </summary>
        public readonly string SubnetId;
        /// <summary>
        /// Any tags assigned to the network interface.
        /// </summary>
        public readonly ImmutableDictionary<string, object> Tags;
        /// <summary>
        /// The ID of the VPC.
        /// </summary>
        public readonly string VpcId;

        [OutputConstructor]
        private GetNetworkInterfaceResult(
            ImmutableArray<Outputs.GetNetworkInterfaceAssociationsResult> associations,
            ImmutableArray<Outputs.GetNetworkInterfaceAttachmentsResult> attachments,
            string availabilityZone,
            string description,
            ImmutableArray<Outputs.GetNetworkInterfaceFiltersResult> filters,
            string id,
            string interfaceType,
            ImmutableArray<string> ipv6Addresses,
            string macAddress,
            string ownerId,
            string privateDnsName,
            string privateIp,
            ImmutableArray<string> privateIps,
            string requesterId,
            ImmutableArray<string> securityGroups,
            string subnetId,
            ImmutableDictionary<string, object> tags,
            string vpcId)
        {
            Associations = associations;
            Attachments = attachments;
            AvailabilityZone = availabilityZone;
            Description = description;
            Filters = filters;
            Id = id;
            InterfaceType = interfaceType;
            Ipv6Addresses = ipv6Addresses;
            MacAddress = macAddress;
            OwnerId = ownerId;
            PrivateDnsName = privateDnsName;
            PrivateIp = privateIp;
            PrivateIps = privateIps;
            RequesterId = requesterId;
            SecurityGroups = securityGroups;
            SubnetId = subnetId;
            Tags = tags;
            VpcId = vpcId;
        }
    }

    namespace Inputs
    {

    public sealed class GetNetworkInterfaceFiltersArgs : Pulumi.ResourceArgs
    {
        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        [Input("values", required: true)]
        private InputList<string>? _values;
        public InputList<string> Values
        {
            get => _values ?? (_values = new InputList<string>());
            set => _values = value;
        }

        public GetNetworkInterfaceFiltersArgs()
        {
        }
    }
    }

    namespace Outputs
    {

    [OutputType]
    public sealed class GetNetworkInterfaceAssociationsResult
    {
        /// <summary>
        /// The allocation ID.
        /// </summary>
        public readonly string AllocationId;
        /// <summary>
        /// The association ID.
        /// </summary>
        public readonly string AssociationId;
        /// <summary>
        /// The ID of the Elastic IP address owner.
        /// </summary>
        public readonly string IpOwnerId;
        /// <summary>
        /// The public DNS name.
        /// </summary>
        public readonly string PublicDnsName;
        /// <summary>
        /// The address of the Elastic IP address bound to the network interface.
        /// </summary>
        public readonly string PublicIp;

        [OutputConstructor]
        private GetNetworkInterfaceAssociationsResult(
            string allocationId,
            string associationId,
            string ipOwnerId,
            string publicDnsName,
            string publicIp)
        {
            AllocationId = allocationId;
            AssociationId = associationId;
            IpOwnerId = ipOwnerId;
            PublicDnsName = publicDnsName;
            PublicIp = publicIp;
        }
    }

    [OutputType]
    public sealed class GetNetworkInterfaceAttachmentsResult
    {
        public readonly string AttachmentId;
        public readonly int DeviceIndex;
        public readonly string InstanceId;
        public readonly string InstanceOwnerId;

        [OutputConstructor]
        private GetNetworkInterfaceAttachmentsResult(
            string attachmentId,
            int deviceIndex,
            string instanceId,
            string instanceOwnerId)
        {
            AttachmentId = attachmentId;
            DeviceIndex = deviceIndex;
            InstanceId = instanceId;
            InstanceOwnerId = instanceOwnerId;
        }
    }

    [OutputType]
    public sealed class GetNetworkInterfaceFiltersResult
    {
        public readonly string Name;
        public readonly ImmutableArray<string> Values;

        [OutputConstructor]
        private GetNetworkInterfaceFiltersResult(
            string name,
            ImmutableArray<string> values)
        {
            Name = name;
            Values = values;
        }
    }
    }
}
