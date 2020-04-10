// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package sfn

import (
	"reflect"

	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Provides a Step Function Activity resource
type Activity struct {
	pulumi.CustomResourceState

	// The date the activity was created.
	CreationDate pulumi.StringOutput `pulumi:"creationDate"`
	// The name of the activity to create.
	Name pulumi.StringOutput `pulumi:"name"`
	// Key-value mapping of resource tags
	Tags pulumi.MapOutput `pulumi:"tags"`
}

// NewActivity registers a new resource with the given unique name, arguments, and options.
func NewActivity(ctx *pulumi.Context,
	name string, args *ActivityArgs, opts ...pulumi.ResourceOption) (*Activity, error) {
	if args == nil {
		args = &ActivityArgs{}
	}
	var resource Activity
	err := ctx.RegisterResource("aws:sfn/activity:Activity", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetActivity gets an existing Activity resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetActivity(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ActivityState, opts ...pulumi.ResourceOption) (*Activity, error) {
	var resource Activity
	err := ctx.ReadResource("aws:sfn/activity:Activity", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Activity resources.
type activityState struct {
	// The date the activity was created.
	CreationDate *string `pulumi:"creationDate"`
	// The name of the activity to create.
	Name *string `pulumi:"name"`
	// Key-value mapping of resource tags
	Tags map[string]interface{} `pulumi:"tags"`
}

type ActivityState struct {
	// The date the activity was created.
	CreationDate pulumi.StringPtrInput
	// The name of the activity to create.
	Name pulumi.StringPtrInput
	// Key-value mapping of resource tags
	Tags pulumi.MapInput
}

func (ActivityState) ElementType() reflect.Type {
	return reflect.TypeOf((*activityState)(nil)).Elem()
}

type activityArgs struct {
	// The name of the activity to create.
	Name *string `pulumi:"name"`
	// Key-value mapping of resource tags
	Tags map[string]interface{} `pulumi:"tags"`
}

// The set of arguments for constructing a Activity resource.
type ActivityArgs struct {
	// The name of the activity to create.
	Name pulumi.StringPtrInput
	// Key-value mapping of resource tags
	Tags pulumi.MapInput
}

func (ActivityArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*activityArgs)(nil)).Elem()
}
