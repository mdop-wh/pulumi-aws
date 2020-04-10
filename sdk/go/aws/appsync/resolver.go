// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package appsync

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Provides an AppSync Resolver.
type Resolver struct {
	pulumi.CustomResourceState

	// The API ID for the GraphQL API.
	ApiId pulumi.StringOutput `pulumi:"apiId"`
	// The ARN
	Arn pulumi.StringOutput `pulumi:"arn"`
	// The DataSource name.
	DataSource pulumi.StringPtrOutput `pulumi:"dataSource"`
	// The field name from the schema defined in the GraphQL API.
	Field pulumi.StringOutput `pulumi:"field"`
	// The resolver type. Valid values are `UNIT` and `PIPELINE`.
	Kind pulumi.StringPtrOutput `pulumi:"kind"`
	// The PipelineConfig. A `pipelineConfig` block is documented below.
	PipelineConfig ResolverPipelineConfigPtrOutput `pulumi:"pipelineConfig"`
	// The request mapping template for UNIT resolver or 'before mapping template' for PIPELINE resolver.
	RequestTemplate pulumi.StringOutput `pulumi:"requestTemplate"`
	// The response mapping template for UNIT resolver or 'after mapping template' for PIPELINE resolver.
	ResponseTemplate pulumi.StringOutput `pulumi:"responseTemplate"`
	// The type name from the schema defined in the GraphQL API.
	Type pulumi.StringOutput `pulumi:"type"`
}

// NewResolver registers a new resource with the given unique name, arguments, and options.
func NewResolver(ctx *pulumi.Context,
	name string, args *ResolverArgs, opts ...pulumi.ResourceOption) (*Resolver, error) {
	if args == nil || args.ApiId == nil {
		return nil, errors.New("missing required argument 'ApiId'")
	}
	if args == nil || args.Field == nil {
		return nil, errors.New("missing required argument 'Field'")
	}
	if args == nil || args.RequestTemplate == nil {
		return nil, errors.New("missing required argument 'RequestTemplate'")
	}
	if args == nil || args.ResponseTemplate == nil {
		return nil, errors.New("missing required argument 'ResponseTemplate'")
	}
	if args == nil || args.Type == nil {
		return nil, errors.New("missing required argument 'Type'")
	}
	if args == nil {
		args = &ResolverArgs{}
	}
	var resource Resolver
	err := ctx.RegisterResource("aws:appsync/resolver:Resolver", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetResolver gets an existing Resolver resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetResolver(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ResolverState, opts ...pulumi.ResourceOption) (*Resolver, error) {
	var resource Resolver
	err := ctx.ReadResource("aws:appsync/resolver:Resolver", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Resolver resources.
type resolverState struct {
	// The API ID for the GraphQL API.
	ApiId *string `pulumi:"apiId"`
	// The ARN
	Arn *string `pulumi:"arn"`
	// The DataSource name.
	DataSource *string `pulumi:"dataSource"`
	// The field name from the schema defined in the GraphQL API.
	Field *string `pulumi:"field"`
	// The resolver type. Valid values are `UNIT` and `PIPELINE`.
	Kind *string `pulumi:"kind"`
	// The PipelineConfig. A `pipelineConfig` block is documented below.
	PipelineConfig *ResolverPipelineConfig `pulumi:"pipelineConfig"`
	// The request mapping template for UNIT resolver or 'before mapping template' for PIPELINE resolver.
	RequestTemplate *string `pulumi:"requestTemplate"`
	// The response mapping template for UNIT resolver or 'after mapping template' for PIPELINE resolver.
	ResponseTemplate *string `pulumi:"responseTemplate"`
	// The type name from the schema defined in the GraphQL API.
	Type *string `pulumi:"type"`
}

type ResolverState struct {
	// The API ID for the GraphQL API.
	ApiId pulumi.StringPtrInput
	// The ARN
	Arn pulumi.StringPtrInput
	// The DataSource name.
	DataSource pulumi.StringPtrInput
	// The field name from the schema defined in the GraphQL API.
	Field pulumi.StringPtrInput
	// The resolver type. Valid values are `UNIT` and `PIPELINE`.
	Kind pulumi.StringPtrInput
	// The PipelineConfig. A `pipelineConfig` block is documented below.
	PipelineConfig ResolverPipelineConfigPtrInput
	// The request mapping template for UNIT resolver or 'before mapping template' for PIPELINE resolver.
	RequestTemplate pulumi.StringPtrInput
	// The response mapping template for UNIT resolver or 'after mapping template' for PIPELINE resolver.
	ResponseTemplate pulumi.StringPtrInput
	// The type name from the schema defined in the GraphQL API.
	Type pulumi.StringPtrInput
}

func (ResolverState) ElementType() reflect.Type {
	return reflect.TypeOf((*resolverState)(nil)).Elem()
}

type resolverArgs struct {
	// The API ID for the GraphQL API.
	ApiId string `pulumi:"apiId"`
	// The DataSource name.
	DataSource *string `pulumi:"dataSource"`
	// The field name from the schema defined in the GraphQL API.
	Field string `pulumi:"field"`
	// The resolver type. Valid values are `UNIT` and `PIPELINE`.
	Kind *string `pulumi:"kind"`
	// The PipelineConfig. A `pipelineConfig` block is documented below.
	PipelineConfig *ResolverPipelineConfig `pulumi:"pipelineConfig"`
	// The request mapping template for UNIT resolver or 'before mapping template' for PIPELINE resolver.
	RequestTemplate string `pulumi:"requestTemplate"`
	// The response mapping template for UNIT resolver or 'after mapping template' for PIPELINE resolver.
	ResponseTemplate string `pulumi:"responseTemplate"`
	// The type name from the schema defined in the GraphQL API.
	Type string `pulumi:"type"`
}

// The set of arguments for constructing a Resolver resource.
type ResolverArgs struct {
	// The API ID for the GraphQL API.
	ApiId pulumi.StringInput
	// The DataSource name.
	DataSource pulumi.StringPtrInput
	// The field name from the schema defined in the GraphQL API.
	Field pulumi.StringInput
	// The resolver type. Valid values are `UNIT` and `PIPELINE`.
	Kind pulumi.StringPtrInput
	// The PipelineConfig. A `pipelineConfig` block is documented below.
	PipelineConfig ResolverPipelineConfigPtrInput
	// The request mapping template for UNIT resolver or 'before mapping template' for PIPELINE resolver.
	RequestTemplate pulumi.StringInput
	// The response mapping template for UNIT resolver or 'after mapping template' for PIPELINE resolver.
	ResponseTemplate pulumi.StringInput
	// The type name from the schema defined in the GraphQL API.
	Type pulumi.StringInput
}

func (ResolverArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*resolverArgs)(nil)).Elem()
}
