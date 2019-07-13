// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package appmesh

import (
	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/appmesh_virtual_node.html.markdown.
type VirtualNode struct {
	s *pulumi.ResourceState
}

// NewVirtualNode registers a new resource with the given unique name, arguments, and options.
func NewVirtualNode(ctx *pulumi.Context,
	name string, args *VirtualNodeArgs, opts ...pulumi.ResourceOpt) (*VirtualNode, error) {
	if args == nil || args.MeshName == nil {
		return nil, errors.New("missing required argument 'MeshName'")
	}
	if args == nil || args.Spec == nil {
		return nil, errors.New("missing required argument 'Spec'")
	}
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["meshName"] = nil
		inputs["name"] = nil
		inputs["spec"] = nil
		inputs["tags"] = nil
	} else {
		inputs["meshName"] = args.MeshName
		inputs["name"] = args.Name
		inputs["spec"] = args.Spec
		inputs["tags"] = args.Tags
	}
	inputs["arn"] = nil
	inputs["createdDate"] = nil
	inputs["lastUpdatedDate"] = nil
	s, err := ctx.RegisterResource("aws:appmesh/virtualNode:VirtualNode", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &VirtualNode{s: s}, nil
}

// GetVirtualNode gets an existing VirtualNode resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetVirtualNode(ctx *pulumi.Context,
	name string, id pulumi.ID, state *VirtualNodeState, opts ...pulumi.ResourceOpt) (*VirtualNode, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["arn"] = state.Arn
		inputs["createdDate"] = state.CreatedDate
		inputs["lastUpdatedDate"] = state.LastUpdatedDate
		inputs["meshName"] = state.MeshName
		inputs["name"] = state.Name
		inputs["spec"] = state.Spec
		inputs["tags"] = state.Tags
	}
	s, err := ctx.ReadResource("aws:appmesh/virtualNode:VirtualNode", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &VirtualNode{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *VirtualNode) URN() *pulumi.URNOutput {
	return r.s.URN()
}

// ID is this resource's unique identifier assigned by its provider.
func (r *VirtualNode) ID() *pulumi.IDOutput {
	return r.s.ID()
}

// The ARN of the virtual node.
func (r *VirtualNode) Arn() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["arn"])
}

// The creation date of the virtual node.
func (r *VirtualNode) CreatedDate() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["createdDate"])
}

// The last update date of the virtual node.
func (r *VirtualNode) LastUpdatedDate() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["lastUpdatedDate"])
}

// The name of the service mesh in which to create the virtual node.
func (r *VirtualNode) MeshName() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["meshName"])
}

// The name to use for the virtual node.
func (r *VirtualNode) Name() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["name"])
}

// The virtual node specification to apply.
func (r *VirtualNode) Spec() *pulumi.Output {
	return r.s.State["spec"]
}

// A mapping of tags to assign to the resource.
func (r *VirtualNode) Tags() *pulumi.MapOutput {
	return (*pulumi.MapOutput)(r.s.State["tags"])
}

// Input properties used for looking up and filtering VirtualNode resources.
type VirtualNodeState struct {
	// The ARN of the virtual node.
	Arn interface{}
	// The creation date of the virtual node.
	CreatedDate interface{}
	// The last update date of the virtual node.
	LastUpdatedDate interface{}
	// The name of the service mesh in which to create the virtual node.
	MeshName interface{}
	// The name to use for the virtual node.
	Name interface{}
	// The virtual node specification to apply.
	Spec interface{}
	// A mapping of tags to assign to the resource.
	Tags interface{}
}

// The set of arguments for constructing a VirtualNode resource.
type VirtualNodeArgs struct {
	// The name of the service mesh in which to create the virtual node.
	MeshName interface{}
	// The name to use for the virtual node.
	Name interface{}
	// The virtual node specification to apply.
	Spec interface{}
	// A mapping of tags to assign to the resource.
	Tags interface{}
}
