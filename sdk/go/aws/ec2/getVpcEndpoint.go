// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package ec2

import (
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// The VPC Endpoint data source provides details about
// a specific VPC endpoint.
func LookupVpcEndpoint(ctx *pulumi.Context, args *LookupVpcEndpointArgs, opts ...pulumi.InvokeOption) (*LookupVpcEndpointResult, error) {
	var rv LookupVpcEndpointResult
	err := ctx.Invoke("aws:ec2/getVpcEndpoint:getVpcEndpoint", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getVpcEndpoint.
type LookupVpcEndpointArgs struct {
	// Custom filter block as described below.
	Filters []GetVpcEndpointFilter `pulumi:"filters"`
	// The ID of the specific VPC Endpoint to retrieve.
	Id *string `pulumi:"id"`
	// The service name of the specific VPC Endpoint to retrieve. For AWS services the service name is usually in the form `com.amazonaws.<region>.<service>` (the SageMaker Notebook service is an exception to this rule, the service name is in the form `aws.sagemaker.<region>.notebook`).
	ServiceName *string `pulumi:"serviceName"`
	// The state of the specific VPC Endpoint to retrieve.
	State *string `pulumi:"state"`
	// A mapping of tags, each pair of which must exactly match
	// a pair on the specific VPC Endpoint to retrieve.
	Tags map[string]interface{} `pulumi:"tags"`
	// The ID of the VPC in which the specific VPC Endpoint is used.
	VpcId *string `pulumi:"vpcId"`
}

// A collection of values returned by getVpcEndpoint.
type LookupVpcEndpointResult struct {
	// The list of CIDR blocks for the exposed AWS service. Applicable for endpoints of type `Gateway`.
	CidrBlocks []string `pulumi:"cidrBlocks"`
	// The DNS entries for the VPC Endpoint. Applicable for endpoints of type `Interface`. DNS blocks are documented below.
	DnsEntries []GetVpcEndpointDnsEntry `pulumi:"dnsEntries"`
	Filters    []GetVpcEndpointFilter   `pulumi:"filters"`
	Id         string                   `pulumi:"id"`
	// One or more network interfaces for the VPC Endpoint. Applicable for endpoints of type `Interface`.
	NetworkInterfaceIds []string `pulumi:"networkInterfaceIds"`
	// The ID of the AWS account that owns the VPC endpoint.
	OwnerId string `pulumi:"ownerId"`
	// The policy document associated with the VPC Endpoint. Applicable for endpoints of type `Gateway`.
	Policy string `pulumi:"policy"`
	// The prefix list ID of the exposed AWS service. Applicable for endpoints of type `Gateway`.
	PrefixListId string `pulumi:"prefixListId"`
	// Whether or not the VPC is associated with a private hosted zone - `true` or `false`. Applicable for endpoints of type `Interface`.
	PrivateDnsEnabled bool `pulumi:"privateDnsEnabled"`
	// Whether or not the VPC Endpoint is being managed by its service - `true` or `false`.
	RequesterManaged bool `pulumi:"requesterManaged"`
	// One or more route tables associated with the VPC Endpoint. Applicable for endpoints of type `Gateway`.
	RouteTableIds []string `pulumi:"routeTableIds"`
	// One or more security groups associated with the network interfaces. Applicable for endpoints of type `Interface`.
	SecurityGroupIds []string `pulumi:"securityGroupIds"`
	ServiceName      string   `pulumi:"serviceName"`
	State            string   `pulumi:"state"`
	// One or more subnets in which the VPC Endpoint is located. Applicable for endpoints of type `Interface`.
	SubnetIds []string               `pulumi:"subnetIds"`
	Tags      map[string]interface{} `pulumi:"tags"`
	// The VPC Endpoint type, `Gateway` or `Interface`.
	VpcEndpointType string `pulumi:"vpcEndpointType"`
	VpcId           string `pulumi:"vpcId"`
}
