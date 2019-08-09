// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package cloudformation

import (
	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Manages a CloudFormation Stack Set. Stack Sets allow CloudFormation templates to be easily deployed across multiple accounts and regions via Stack Set Instances ([`cloudformation.StackSetInstance` resource](https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set_instance.html)). Additional information about Stack Sets can be found in the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/what-is-cfnstacksets.html).
// 
// > **NOTE:** All template parameters, including those with a `Default`, must be configured or ignored with the `lifecycle` configuration block `ignoreChanges` argument.
// 
// > **NOTE:** All `NoEcho` template parameters must be ignored with the `lifecycle` configuration block `ignoreChanges` argument.
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/cloudformation_stack_set.html.markdown.
type StackSet struct {
	s *pulumi.ResourceState
}

// NewStackSet registers a new resource with the given unique name, arguments, and options.
func NewStackSet(ctx *pulumi.Context,
	name string, args *StackSetArgs, opts ...pulumi.ResourceOpt) (*StackSet, error) {
	if args == nil || args.AdministrationRoleArn == nil {
		return nil, errors.New("missing required argument 'AdministrationRoleArn'")
	}
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["administrationRoleArn"] = nil
		inputs["capabilities"] = nil
		inputs["description"] = nil
		inputs["executionRoleName"] = nil
		inputs["name"] = nil
		inputs["parameters"] = nil
		inputs["tags"] = nil
		inputs["templateBody"] = nil
		inputs["templateUrl"] = nil
	} else {
		inputs["administrationRoleArn"] = args.AdministrationRoleArn
		inputs["capabilities"] = args.Capabilities
		inputs["description"] = args.Description
		inputs["executionRoleName"] = args.ExecutionRoleName
		inputs["name"] = args.Name
		inputs["parameters"] = args.Parameters
		inputs["tags"] = args.Tags
		inputs["templateBody"] = args.TemplateBody
		inputs["templateUrl"] = args.TemplateUrl
	}
	inputs["arn"] = nil
	inputs["stackSetId"] = nil
	s, err := ctx.RegisterResource("aws:cloudformation/stackSet:StackSet", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &StackSet{s: s}, nil
}

// GetStackSet gets an existing StackSet resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetStackSet(ctx *pulumi.Context,
	name string, id pulumi.ID, state *StackSetState, opts ...pulumi.ResourceOpt) (*StackSet, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["administrationRoleArn"] = state.AdministrationRoleArn
		inputs["arn"] = state.Arn
		inputs["capabilities"] = state.Capabilities
		inputs["description"] = state.Description
		inputs["executionRoleName"] = state.ExecutionRoleName
		inputs["name"] = state.Name
		inputs["parameters"] = state.Parameters
		inputs["stackSetId"] = state.StackSetId
		inputs["tags"] = state.Tags
		inputs["templateBody"] = state.TemplateBody
		inputs["templateUrl"] = state.TemplateUrl
	}
	s, err := ctx.ReadResource("aws:cloudformation/stackSet:StackSet", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &StackSet{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *StackSet) URN() *pulumi.URNOutput {
	return r.s.URN()
}

// ID is this resource's unique identifier assigned by its provider.
func (r *StackSet) ID() *pulumi.IDOutput {
	return r.s.ID()
}

// Amazon Resource Number (ARN) of the IAM Role in the administrator account.
func (r *StackSet) AdministrationRoleArn() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["administrationRoleArn"])
}

// Amazon Resource Name (ARN) of the Stack Set.
func (r *StackSet) Arn() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["arn"])
}

// A list of capabilities. Valid values: `CAPABILITY_IAM`, `CAPABILITY_NAMED_IAM`, `CAPABILITY_AUTO_EXPAND`.
func (r *StackSet) Capabilities() *pulumi.ArrayOutput {
	return (*pulumi.ArrayOutput)(r.s.State["capabilities"])
}

// Description of the Stack Set.
func (r *StackSet) Description() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["description"])
}

// Name of the IAM Role in all target accounts for Stack Set operations. Defaults to `AWSCloudFormationStackSetExecutionRole`.
func (r *StackSet) ExecutionRoleName() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["executionRoleName"])
}

// Name of the Stack Set. The name must be unique in the region where you create your Stack Set. The name can contain only alphanumeric characters (case-sensitive) and hyphens. It must start with an alphabetic character and cannot be longer than 128 characters.
func (r *StackSet) Name() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["name"])
}

// Key-value map of input parameters for the Stack Set template. All template parameters, including those with a `Default`, must be configured or ignored with `lifecycle` configuration block `ignoreChanges` argument. All `NoEcho` template parameters must be ignored with the `lifecycle` configuration block `ignoreChanges` argument.
func (r *StackSet) Parameters() *pulumi.MapOutput {
	return (*pulumi.MapOutput)(r.s.State["parameters"])
}

// Unique identifier of the Stack Set.
func (r *StackSet) StackSetId() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["stackSetId"])
}

// Key-value map of tags to associate with this Stack Set and the Stacks created from it. AWS CloudFormation also propagates these tags to supported resources that are created in the Stacks. A maximum number of 50 tags can be specified.
func (r *StackSet) Tags() *pulumi.MapOutput {
	return (*pulumi.MapOutput)(r.s.State["tags"])
}

// String containing the CloudFormation template body. Maximum size: 51,200 bytes. Conflicts with `templateUrl`.
func (r *StackSet) TemplateBody() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["templateBody"])
}

// String containing the location of a file containing the CloudFormation template body. The URL must point to a template that is located in an Amazon S3 bucket. Maximum location file size: 460,800 bytes. Conflicts with `templateBody`.
func (r *StackSet) TemplateUrl() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["templateUrl"])
}

// Input properties used for looking up and filtering StackSet resources.
type StackSetState struct {
	// Amazon Resource Number (ARN) of the IAM Role in the administrator account.
	AdministrationRoleArn interface{}
	// Amazon Resource Name (ARN) of the Stack Set.
	Arn interface{}
	// A list of capabilities. Valid values: `CAPABILITY_IAM`, `CAPABILITY_NAMED_IAM`, `CAPABILITY_AUTO_EXPAND`.
	Capabilities interface{}
	// Description of the Stack Set.
	Description interface{}
	// Name of the IAM Role in all target accounts for Stack Set operations. Defaults to `AWSCloudFormationStackSetExecutionRole`.
	ExecutionRoleName interface{}
	// Name of the Stack Set. The name must be unique in the region where you create your Stack Set. The name can contain only alphanumeric characters (case-sensitive) and hyphens. It must start with an alphabetic character and cannot be longer than 128 characters.
	Name interface{}
	// Key-value map of input parameters for the Stack Set template. All template parameters, including those with a `Default`, must be configured or ignored with `lifecycle` configuration block `ignoreChanges` argument. All `NoEcho` template parameters must be ignored with the `lifecycle` configuration block `ignoreChanges` argument.
	Parameters interface{}
	// Unique identifier of the Stack Set.
	StackSetId interface{}
	// Key-value map of tags to associate with this Stack Set and the Stacks created from it. AWS CloudFormation also propagates these tags to supported resources that are created in the Stacks. A maximum number of 50 tags can be specified.
	Tags interface{}
	// String containing the CloudFormation template body. Maximum size: 51,200 bytes. Conflicts with `templateUrl`.
	TemplateBody interface{}
	// String containing the location of a file containing the CloudFormation template body. The URL must point to a template that is located in an Amazon S3 bucket. Maximum location file size: 460,800 bytes. Conflicts with `templateBody`.
	TemplateUrl interface{}
}

// The set of arguments for constructing a StackSet resource.
type StackSetArgs struct {
	// Amazon Resource Number (ARN) of the IAM Role in the administrator account.
	AdministrationRoleArn interface{}
	// A list of capabilities. Valid values: `CAPABILITY_IAM`, `CAPABILITY_NAMED_IAM`, `CAPABILITY_AUTO_EXPAND`.
	Capabilities interface{}
	// Description of the Stack Set.
	Description interface{}
	// Name of the IAM Role in all target accounts for Stack Set operations. Defaults to `AWSCloudFormationStackSetExecutionRole`.
	ExecutionRoleName interface{}
	// Name of the Stack Set. The name must be unique in the region where you create your Stack Set. The name can contain only alphanumeric characters (case-sensitive) and hyphens. It must start with an alphabetic character and cannot be longer than 128 characters.
	Name interface{}
	// Key-value map of input parameters for the Stack Set template. All template parameters, including those with a `Default`, must be configured or ignored with `lifecycle` configuration block `ignoreChanges` argument. All `NoEcho` template parameters must be ignored with the `lifecycle` configuration block `ignoreChanges` argument.
	Parameters interface{}
	// Key-value map of tags to associate with this Stack Set and the Stacks created from it. AWS CloudFormation also propagates these tags to supported resources that are created in the Stacks. A maximum number of 50 tags can be specified.
	Tags interface{}
	// String containing the CloudFormation template body. Maximum size: 51,200 bytes. Conflicts with `templateUrl`.
	TemplateBody interface{}
	// String containing the location of a file containing the CloudFormation template body. The URL must point to a template that is located in an Amazon S3 bucket. Maximum location file size: 460,800 bytes. Conflicts with `templateBody`.
	TemplateUrl interface{}
}
