// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package storagegateway

import (
	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/storagegateway_cache.html.markdown.
type Cache struct {
	s *pulumi.ResourceState
}

// NewCache registers a new resource with the given unique name, arguments, and options.
func NewCache(ctx *pulumi.Context,
	name string, args *CacheArgs, opts ...pulumi.ResourceOpt) (*Cache, error) {
	if args == nil || args.DiskId == nil {
		return nil, errors.New("missing required argument 'DiskId'")
	}
	if args == nil || args.GatewayArn == nil {
		return nil, errors.New("missing required argument 'GatewayArn'")
	}
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["diskId"] = nil
		inputs["gatewayArn"] = nil
	} else {
		inputs["diskId"] = args.DiskId
		inputs["gatewayArn"] = args.GatewayArn
	}
	s, err := ctx.RegisterResource("aws:storagegateway/cache:Cache", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &Cache{s: s}, nil
}

// GetCache gets an existing Cache resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetCache(ctx *pulumi.Context,
	name string, id pulumi.ID, state *CacheState, opts ...pulumi.ResourceOpt) (*Cache, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["diskId"] = state.DiskId
		inputs["gatewayArn"] = state.GatewayArn
	}
	s, err := ctx.ReadResource("aws:storagegateway/cache:Cache", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &Cache{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *Cache) URN() *pulumi.URNOutput {
	return r.s.URN()
}

// ID is this resource's unique identifier assigned by its provider.
func (r *Cache) ID() *pulumi.IDOutput {
	return r.s.ID()
}

// Local disk identifier. For example, `pci-0000:03:00.0-scsi-0:0:0:0`.
func (r *Cache) DiskId() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["diskId"])
}

// The Amazon Resource Name (ARN) of the gateway.
func (r *Cache) GatewayArn() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["gatewayArn"])
}

// Input properties used for looking up and filtering Cache resources.
type CacheState struct {
	// Local disk identifier. For example, `pci-0000:03:00.0-scsi-0:0:0:0`.
	DiskId interface{}
	// The Amazon Resource Name (ARN) of the gateway.
	GatewayArn interface{}
}

// The set of arguments for constructing a Cache resource.
type CacheArgs struct {
	// Local disk identifier. For example, `pci-0000:03:00.0-scsi-0:0:0:0`.
	DiskId interface{}
	// The Amazon Resource Name (ARN) of the gateway.
	GatewayArn interface{}
}
