// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package ec2

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Provides a resource to create a VPC routing table.
//
// > **NOTE on Route Tables and Routes:** This provider currently
// provides both a standalone Route resource and a Route Table resource with routes
// defined in-line. At this time you cannot use a Route Table with in-line routes
// in conjunction with any Route resources. Doing so will cause
// a conflict of rule settings and will overwrite rules.
//
// > **NOTE on `gatewayId` and `natGatewayId`:** The AWS API is very forgiving with these two
// attributes and the `ec2.RouteTable` resource can be created with a NAT ID specified as a Gateway ID attribute.
// This _will_ lead to a permanent diff between your configuration and statefile, as the API returns the correct
// parameters in the returned route table. If you're experiencing constant diffs in your `ec2.RouteTable` resources,
// the first thing to check is whether or not you're specifying a NAT ID instead of a Gateway ID, or vice-versa.
//
// > **NOTE on `propagatingVgws` and the `ec2.VpnGatewayRoutePropagation` resource:**
// If the `propagatingVgws` argument is present, it's not supported to _also_
// define route propagations using `ec2.VpnGatewayRoutePropagation`, since
// this resource will delete any propagating gateways not explicitly listed in
// `propagatingVgws`. Omit this argument when defining route propagation using
// the separate resource.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-aws/sdk/v2/go/aws/ec2"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		_, err := ec2.NewRouteTable(ctx, "routeTable", &ec2.RouteTableArgs{
// 			VpcId: pulumi.Any(aws_vpc.Default.Id),
// 			Routes: ec2.RouteTableRouteArray{
// 				&ec2.RouteTableRouteArgs{
// 					CidrBlock: pulumi.String("10.0.1.0/24"),
// 					GatewayId: pulumi.Any(aws_internet_gateway.Main.Id),
// 				},
// 				&ec2.RouteTableRouteArgs{
// 					Ipv6CidrBlock:       pulumi.String("::/0"),
// 					EgressOnlyGatewayId: pulumi.Any(aws_egress_only_internet_gateway.Foo.Id),
// 				},
// 			},
// 			Tags: pulumi.StringMap{
// 				"Name": pulumi.String("main"),
// 			},
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
type RouteTable struct {
	pulumi.CustomResourceState

	// The ID of the AWS account that owns the route table.
	OwnerId pulumi.StringOutput `pulumi:"ownerId"`
	// A list of virtual gateways for propagation.
	PropagatingVgws pulumi.StringArrayOutput `pulumi:"propagatingVgws"`
	// A list of route objects. Their keys are documented below.
	Routes RouteTableRouteArrayOutput `pulumi:"routes"`
	// A mapping of tags to assign to the resource.
	Tags pulumi.StringMapOutput `pulumi:"tags"`
	// The VPC ID.
	VpcId pulumi.StringOutput `pulumi:"vpcId"`
}

// NewRouteTable registers a new resource with the given unique name, arguments, and options.
func NewRouteTable(ctx *pulumi.Context,
	name string, args *RouteTableArgs, opts ...pulumi.ResourceOption) (*RouteTable, error) {
	if args == nil || args.VpcId == nil {
		return nil, errors.New("missing required argument 'VpcId'")
	}
	if args == nil {
		args = &RouteTableArgs{}
	}
	var resource RouteTable
	err := ctx.RegisterResource("aws:ec2/routeTable:RouteTable", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetRouteTable gets an existing RouteTable resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetRouteTable(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *RouteTableState, opts ...pulumi.ResourceOption) (*RouteTable, error) {
	var resource RouteTable
	err := ctx.ReadResource("aws:ec2/routeTable:RouteTable", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering RouteTable resources.
type routeTableState struct {
	// The ID of the AWS account that owns the route table.
	OwnerId *string `pulumi:"ownerId"`
	// A list of virtual gateways for propagation.
	PropagatingVgws []string `pulumi:"propagatingVgws"`
	// A list of route objects. Their keys are documented below.
	Routes []RouteTableRoute `pulumi:"routes"`
	// A mapping of tags to assign to the resource.
	Tags map[string]string `pulumi:"tags"`
	// The VPC ID.
	VpcId *string `pulumi:"vpcId"`
}

type RouteTableState struct {
	// The ID of the AWS account that owns the route table.
	OwnerId pulumi.StringPtrInput
	// A list of virtual gateways for propagation.
	PropagatingVgws pulumi.StringArrayInput
	// A list of route objects. Their keys are documented below.
	Routes RouteTableRouteArrayInput
	// A mapping of tags to assign to the resource.
	Tags pulumi.StringMapInput
	// The VPC ID.
	VpcId pulumi.StringPtrInput
}

func (RouteTableState) ElementType() reflect.Type {
	return reflect.TypeOf((*routeTableState)(nil)).Elem()
}

type routeTableArgs struct {
	// A list of virtual gateways for propagation.
	PropagatingVgws []string `pulumi:"propagatingVgws"`
	// A list of route objects. Their keys are documented below.
	Routes []RouteTableRoute `pulumi:"routes"`
	// A mapping of tags to assign to the resource.
	Tags map[string]string `pulumi:"tags"`
	// The VPC ID.
	VpcId string `pulumi:"vpcId"`
}

// The set of arguments for constructing a RouteTable resource.
type RouteTableArgs struct {
	// A list of virtual gateways for propagation.
	PropagatingVgws pulumi.StringArrayInput
	// A list of route objects. Their keys are documented below.
	Routes RouteTableRouteArrayInput
	// A mapping of tags to assign to the resource.
	Tags pulumi.StringMapInput
	// The VPC ID.
	VpcId pulumi.StringInput
}

func (RouteTableArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*routeTableArgs)(nil)).Elem()
}
