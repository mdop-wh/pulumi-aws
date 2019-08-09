// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package applicationloadbalancing

import (
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// > **Note:** `alb.LoadBalancer` is known as `lb.LoadBalancer`. The functionality is identical.
// 
// Provides information about a Load Balancer.
// 
// This data source can prove useful when a module accepts an LB as an input
// variable and needs to, for example, determine the security groups associated
// with it, etc.
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/alb_legacy.html.markdown.
func LookupLoadBalancer(ctx *pulumi.Context, args *GetLoadBalancerArgs) (*GetLoadBalancerResult, error) {
	inputs := make(map[string]interface{})
	if args != nil {
		inputs["arn"] = args.Arn
		inputs["name"] = args.Name
		inputs["tags"] = args.Tags
	}
	outputs, err := ctx.Invoke("aws:applicationloadbalancing/getLoadBalancer:getLoadBalancer", inputs)
	if err != nil {
		return nil, err
	}
	return &GetLoadBalancerResult{
		AccessLogs: outputs["accessLogs"],
		Arn: outputs["arn"],
		ArnSuffix: outputs["arnSuffix"],
		DnsName: outputs["dnsName"],
		EnableDeletionProtection: outputs["enableDeletionProtection"],
		IdleTimeout: outputs["idleTimeout"],
		Internal: outputs["internal"],
		LoadBalancerType: outputs["loadBalancerType"],
		Name: outputs["name"],
		SecurityGroups: outputs["securityGroups"],
		SubnetMappings: outputs["subnetMappings"],
		Subnets: outputs["subnets"],
		Tags: outputs["tags"],
		VpcId: outputs["vpcId"],
		ZoneId: outputs["zoneId"],
		Id: outputs["id"],
	}, nil
}

// A collection of arguments for invoking getLoadBalancer.
type GetLoadBalancerArgs struct {
	// The full ARN of the load balancer.
	Arn interface{}
	// The unique name of the load balancer.
	Name interface{}
	Tags interface{}
}

// A collection of values returned by getLoadBalancer.
type GetLoadBalancerResult struct {
	AccessLogs interface{}
	Arn interface{}
	ArnSuffix interface{}
	DnsName interface{}
	EnableDeletionProtection interface{}
	IdleTimeout interface{}
	Internal interface{}
	LoadBalancerType interface{}
	Name interface{}
	SecurityGroups interface{}
	SubnetMappings interface{}
	Subnets interface{}
	Tags interface{}
	VpcId interface{}
	ZoneId interface{}
	// id is the provider-assigned unique ID for this managed resource.
	Id interface{}
}
