// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package ec2

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Provides an Elastic network interface (ENI) resource.
type NetworkInterface struct {
	pulumi.CustomResourceState

	// Block to define the attachment of the ENI. Documented below.
	Attachments NetworkInterfaceAttachmentTypeArrayOutput `pulumi:"attachments"`
	// A description for the network interface.
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// The MAC address of the network interface.
	MacAddress pulumi.StringOutput `pulumi:"macAddress"`
	// The private DNS name of the network interface (IPv4).
	PrivateDnsName pulumi.StringOutput `pulumi:"privateDnsName"`
	PrivateIp      pulumi.StringOutput `pulumi:"privateIp"`
	// List of private IPs to assign to the ENI.
	PrivateIps pulumi.StringArrayOutput `pulumi:"privateIps"`
	// Number of secondary private IPs to assign to the ENI. The total number of private IPs will be 1 + private_ips_count, as a primary private IP will be assiged to an ENI by default.
	PrivateIpsCount pulumi.IntOutput `pulumi:"privateIpsCount"`
	// List of security group IDs to assign to the ENI.
	SecurityGroups pulumi.StringArrayOutput `pulumi:"securityGroups"`
	// Whether to enable source destination checking for the ENI. Default true.
	SourceDestCheck pulumi.BoolPtrOutput `pulumi:"sourceDestCheck"`
	// Subnet ID to create the ENI in.
	SubnetId pulumi.StringOutput `pulumi:"subnetId"`
	// A mapping of tags to assign to the resource.
	Tags pulumi.MapOutput `pulumi:"tags"`
}

// NewNetworkInterface registers a new resource with the given unique name, arguments, and options.
func NewNetworkInterface(ctx *pulumi.Context,
	name string, args *NetworkInterfaceArgs, opts ...pulumi.ResourceOption) (*NetworkInterface, error) {
	if args == nil || args.SubnetId == nil {
		return nil, errors.New("missing required argument 'SubnetId'")
	}
	if args == nil {
		args = &NetworkInterfaceArgs{}
	}
	var resource NetworkInterface
	err := ctx.RegisterResource("aws:ec2/networkInterface:NetworkInterface", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetNetworkInterface gets an existing NetworkInterface resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetNetworkInterface(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *NetworkInterfaceState, opts ...pulumi.ResourceOption) (*NetworkInterface, error) {
	var resource NetworkInterface
	err := ctx.ReadResource("aws:ec2/networkInterface:NetworkInterface", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering NetworkInterface resources.
type networkInterfaceState struct {
	// Block to define the attachment of the ENI. Documented below.
	Attachments []NetworkInterfaceAttachmentType `pulumi:"attachments"`
	// A description for the network interface.
	Description *string `pulumi:"description"`
	// The MAC address of the network interface.
	MacAddress *string `pulumi:"macAddress"`
	// The private DNS name of the network interface (IPv4).
	PrivateDnsName *string `pulumi:"privateDnsName"`
	PrivateIp      *string `pulumi:"privateIp"`
	// List of private IPs to assign to the ENI.
	PrivateIps []string `pulumi:"privateIps"`
	// Number of secondary private IPs to assign to the ENI. The total number of private IPs will be 1 + private_ips_count, as a primary private IP will be assiged to an ENI by default.
	PrivateIpsCount *int `pulumi:"privateIpsCount"`
	// List of security group IDs to assign to the ENI.
	SecurityGroups []string `pulumi:"securityGroups"`
	// Whether to enable source destination checking for the ENI. Default true.
	SourceDestCheck *bool `pulumi:"sourceDestCheck"`
	// Subnet ID to create the ENI in.
	SubnetId *string `pulumi:"subnetId"`
	// A mapping of tags to assign to the resource.
	Tags map[string]interface{} `pulumi:"tags"`
}

type NetworkInterfaceState struct {
	// Block to define the attachment of the ENI. Documented below.
	Attachments NetworkInterfaceAttachmentTypeArrayInput
	// A description for the network interface.
	Description pulumi.StringPtrInput
	// The MAC address of the network interface.
	MacAddress pulumi.StringPtrInput
	// The private DNS name of the network interface (IPv4).
	PrivateDnsName pulumi.StringPtrInput
	PrivateIp      pulumi.StringPtrInput
	// List of private IPs to assign to the ENI.
	PrivateIps pulumi.StringArrayInput
	// Number of secondary private IPs to assign to the ENI. The total number of private IPs will be 1 + private_ips_count, as a primary private IP will be assiged to an ENI by default.
	PrivateIpsCount pulumi.IntPtrInput
	// List of security group IDs to assign to the ENI.
	SecurityGroups pulumi.StringArrayInput
	// Whether to enable source destination checking for the ENI. Default true.
	SourceDestCheck pulumi.BoolPtrInput
	// Subnet ID to create the ENI in.
	SubnetId pulumi.StringPtrInput
	// A mapping of tags to assign to the resource.
	Tags pulumi.MapInput
}

func (NetworkInterfaceState) ElementType() reflect.Type {
	return reflect.TypeOf((*networkInterfaceState)(nil)).Elem()
}

type networkInterfaceArgs struct {
	// Block to define the attachment of the ENI. Documented below.
	Attachments []NetworkInterfaceAttachmentType `pulumi:"attachments"`
	// A description for the network interface.
	Description *string `pulumi:"description"`
	PrivateIp   *string `pulumi:"privateIp"`
	// List of private IPs to assign to the ENI.
	PrivateIps []string `pulumi:"privateIps"`
	// Number of secondary private IPs to assign to the ENI. The total number of private IPs will be 1 + private_ips_count, as a primary private IP will be assiged to an ENI by default.
	PrivateIpsCount *int `pulumi:"privateIpsCount"`
	// List of security group IDs to assign to the ENI.
	SecurityGroups []string `pulumi:"securityGroups"`
	// Whether to enable source destination checking for the ENI. Default true.
	SourceDestCheck *bool `pulumi:"sourceDestCheck"`
	// Subnet ID to create the ENI in.
	SubnetId string `pulumi:"subnetId"`
	// A mapping of tags to assign to the resource.
	Tags map[string]interface{} `pulumi:"tags"`
}

// The set of arguments for constructing a NetworkInterface resource.
type NetworkInterfaceArgs struct {
	// Block to define the attachment of the ENI. Documented below.
	Attachments NetworkInterfaceAttachmentTypeArrayInput
	// A description for the network interface.
	Description pulumi.StringPtrInput
	PrivateIp   pulumi.StringPtrInput
	// List of private IPs to assign to the ENI.
	PrivateIps pulumi.StringArrayInput
	// Number of secondary private IPs to assign to the ENI. The total number of private IPs will be 1 + private_ips_count, as a primary private IP will be assiged to an ENI by default.
	PrivateIpsCount pulumi.IntPtrInput
	// List of security group IDs to assign to the ENI.
	SecurityGroups pulumi.StringArrayInput
	// Whether to enable source destination checking for the ENI. Default true.
	SourceDestCheck pulumi.BoolPtrInput
	// Subnet ID to create the ENI in.
	SubnetId pulumi.StringInput
	// A mapping of tags to assign to the resource.
	Tags pulumi.MapInput
}

func (NetworkInterfaceArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*networkInterfaceArgs)(nil)).Elem()
}
