// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package apigateway

import (
	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Connects a custom domain name registered via `apigateway.DomainName`
// with a deployed API so that its methods can be called via the
// custom domain name.
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/api_gateway_base_path_mapping.html.markdown.
type BasePathMapping struct {
	s *pulumi.ResourceState
}

// NewBasePathMapping registers a new resource with the given unique name, arguments, and options.
func NewBasePathMapping(ctx *pulumi.Context,
	name string, args *BasePathMappingArgs, opts ...pulumi.ResourceOpt) (*BasePathMapping, error) {
	if args == nil || args.RestApi == nil {
		return nil, errors.New("missing required argument 'RestApi'")
	}
	if args == nil || args.DomainName == nil {
		return nil, errors.New("missing required argument 'DomainName'")
	}
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["restApi"] = nil
		inputs["basePath"] = nil
		inputs["domainName"] = nil
		inputs["stageName"] = nil
	} else {
		inputs["restApi"] = args.RestApi
		inputs["basePath"] = args.BasePath
		inputs["domainName"] = args.DomainName
		inputs["stageName"] = args.StageName
	}
	s, err := ctx.RegisterResource("aws:apigateway/basePathMapping:BasePathMapping", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &BasePathMapping{s: s}, nil
}

// GetBasePathMapping gets an existing BasePathMapping resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetBasePathMapping(ctx *pulumi.Context,
	name string, id pulumi.ID, state *BasePathMappingState, opts ...pulumi.ResourceOpt) (*BasePathMapping, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["restApi"] = state.RestApi
		inputs["basePath"] = state.BasePath
		inputs["domainName"] = state.DomainName
		inputs["stageName"] = state.StageName
	}
	s, err := ctx.ReadResource("aws:apigateway/basePathMapping:BasePathMapping", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &BasePathMapping{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *BasePathMapping) URN() *pulumi.URNOutput {
	return r.s.URN()
}

// ID is this resource's unique identifier assigned by its provider.
func (r *BasePathMapping) ID() *pulumi.IDOutput {
	return r.s.ID()
}

// The id of the API to connect.
func (r *BasePathMapping) RestApi() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["restApi"])
}

// Path segment that must be prepended to the path when accessing the API via this mapping. If omitted, the API is exposed at the root of the given domain.
func (r *BasePathMapping) BasePath() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["basePath"])
}

// The already-registered domain name to connect the API to.
func (r *BasePathMapping) DomainName() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["domainName"])
}

// The name of a specific deployment stage to expose at the given path. If omitted, callers may select any stage by including its name as a path element after the base path.
func (r *BasePathMapping) StageName() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["stageName"])
}

// Input properties used for looking up and filtering BasePathMapping resources.
type BasePathMappingState struct {
	// The id of the API to connect.
	RestApi interface{}
	// Path segment that must be prepended to the path when accessing the API via this mapping. If omitted, the API is exposed at the root of the given domain.
	BasePath interface{}
	// The already-registered domain name to connect the API to.
	DomainName interface{}
	// The name of a specific deployment stage to expose at the given path. If omitted, callers may select any stage by including its name as a path element after the base path.
	StageName interface{}
}

// The set of arguments for constructing a BasePathMapping resource.
type BasePathMappingArgs struct {
	// The id of the API to connect.
	RestApi interface{}
	// Path segment that must be prepended to the path when accessing the API via this mapping. If omitted, the API is exposed at the root of the given domain.
	BasePath interface{}
	// The already-registered domain name to connect the API to.
	DomainName interface{}
	// The name of a specific deployment stage to expose at the given path. If omitted, callers may select any stage by including its name as a path element after the base path.
	StageName interface{}
}
