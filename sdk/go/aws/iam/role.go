// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package iam

import (
	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Provides an IAM role.
// 
// > *NOTE:* If policies are attached to the role via the [`aws_iam_policy_attachment` resource](https://www.terraform.io/docs/providers/aws/r/iam_policy_attachment.html) and you are modifying the role `name` or `path`, the `force_detach_policies` argument must be set to `true` and applied before attempting the operation otherwise you will encounter a `DeleteConflict` error. The [`aws_iam_role_policy_attachment` resource (recommended)](https://www.terraform.io/docs/providers/aws/r/iam_role_policy_attachment.html) does not have this requirement.
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_role.html.markdown.
type Role struct {
	s *pulumi.ResourceState
}

// NewRole registers a new resource with the given unique name, arguments, and options.
func NewRole(ctx *pulumi.Context,
	name string, args *RoleArgs, opts ...pulumi.ResourceOpt) (*Role, error) {
	if args == nil || args.AssumeRolePolicy == nil {
		return nil, errors.New("missing required argument 'AssumeRolePolicy'")
	}
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["assumeRolePolicy"] = nil
		inputs["description"] = nil
		inputs["forceDetachPolicies"] = nil
		inputs["maxSessionDuration"] = nil
		inputs["name"] = nil
		inputs["namePrefix"] = nil
		inputs["path"] = nil
		inputs["permissionsBoundary"] = nil
		inputs["tags"] = nil
	} else {
		inputs["assumeRolePolicy"] = args.AssumeRolePolicy
		inputs["description"] = args.Description
		inputs["forceDetachPolicies"] = args.ForceDetachPolicies
		inputs["maxSessionDuration"] = args.MaxSessionDuration
		inputs["name"] = args.Name
		inputs["namePrefix"] = args.NamePrefix
		inputs["path"] = args.Path
		inputs["permissionsBoundary"] = args.PermissionsBoundary
		inputs["tags"] = args.Tags
	}
	inputs["arn"] = nil
	inputs["createDate"] = nil
	inputs["uniqueId"] = nil
	s, err := ctx.RegisterResource("aws:iam/role:Role", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &Role{s: s}, nil
}

// GetRole gets an existing Role resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetRole(ctx *pulumi.Context,
	name string, id pulumi.ID, state *RoleState, opts ...pulumi.ResourceOpt) (*Role, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["arn"] = state.Arn
		inputs["assumeRolePolicy"] = state.AssumeRolePolicy
		inputs["createDate"] = state.CreateDate
		inputs["description"] = state.Description
		inputs["forceDetachPolicies"] = state.ForceDetachPolicies
		inputs["maxSessionDuration"] = state.MaxSessionDuration
		inputs["name"] = state.Name
		inputs["namePrefix"] = state.NamePrefix
		inputs["path"] = state.Path
		inputs["permissionsBoundary"] = state.PermissionsBoundary
		inputs["tags"] = state.Tags
		inputs["uniqueId"] = state.UniqueId
	}
	s, err := ctx.ReadResource("aws:iam/role:Role", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &Role{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *Role) URN() *pulumi.URNOutput {
	return r.s.URN()
}

// ID is this resource's unique identifier assigned by its provider.
func (r *Role) ID() *pulumi.IDOutput {
	return r.s.ID()
}

// The Amazon Resource Name (ARN) specifying the role.
func (r *Role) Arn() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["arn"])
}

// The policy that grants an entity permission to assume the role.
func (r *Role) AssumeRolePolicy() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["assumeRolePolicy"])
}

// The creation date of the IAM role.
func (r *Role) CreateDate() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["createDate"])
}

// The description of the role.
func (r *Role) Description() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["description"])
}

// Specifies to force detaching any policies the role has before destroying it. Defaults to `false`.
func (r *Role) ForceDetachPolicies() *pulumi.BoolOutput {
	return (*pulumi.BoolOutput)(r.s.State["forceDetachPolicies"])
}

// The maximum session duration (in seconds) that you want to set for the specified role. If you do not specify a value for this setting, the default maximum of one hour is applied. This setting can have a value from 1 hour to 12 hours.
func (r *Role) MaxSessionDuration() *pulumi.IntOutput {
	return (*pulumi.IntOutput)(r.s.State["maxSessionDuration"])
}

func (r *Role) Name() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["name"])
}

// Creates a unique name beginning with the specified prefix. Conflicts with `name`.
func (r *Role) NamePrefix() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["namePrefix"])
}

// The path to the role.
// See [IAM Identifiers](https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html) for more information.
func (r *Role) Path() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["path"])
}

// The ARN of the policy that is used to set the permissions boundary for the role.
func (r *Role) PermissionsBoundary() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["permissionsBoundary"])
}

// Key-value mapping of tags for the IAM role
func (r *Role) Tags() *pulumi.MapOutput {
	return (*pulumi.MapOutput)(r.s.State["tags"])
}

// The stable and unique string identifying the role.
func (r *Role) UniqueId() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["uniqueId"])
}

// Input properties used for looking up and filtering Role resources.
type RoleState struct {
	// The Amazon Resource Name (ARN) specifying the role.
	Arn interface{}
	// The policy that grants an entity permission to assume the role.
	AssumeRolePolicy interface{}
	// The creation date of the IAM role.
	CreateDate interface{}
	// The description of the role.
	Description interface{}
	// Specifies to force detaching any policies the role has before destroying it. Defaults to `false`.
	ForceDetachPolicies interface{}
	// The maximum session duration (in seconds) that you want to set for the specified role. If you do not specify a value for this setting, the default maximum of one hour is applied. This setting can have a value from 1 hour to 12 hours.
	MaxSessionDuration interface{}
	Name interface{}
	// Creates a unique name beginning with the specified prefix. Conflicts with `name`.
	NamePrefix interface{}
	// The path to the role.
	// See [IAM Identifiers](https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html) for more information.
	Path interface{}
	// The ARN of the policy that is used to set the permissions boundary for the role.
	PermissionsBoundary interface{}
	// Key-value mapping of tags for the IAM role
	Tags interface{}
	// The stable and unique string identifying the role.
	UniqueId interface{}
}

// The set of arguments for constructing a Role resource.
type RoleArgs struct {
	// The policy that grants an entity permission to assume the role.
	AssumeRolePolicy interface{}
	// The description of the role.
	Description interface{}
	// Specifies to force detaching any policies the role has before destroying it. Defaults to `false`.
	ForceDetachPolicies interface{}
	// The maximum session duration (in seconds) that you want to set for the specified role. If you do not specify a value for this setting, the default maximum of one hour is applied. This setting can have a value from 1 hour to 12 hours.
	MaxSessionDuration interface{}
	Name interface{}
	// Creates a unique name beginning with the specified prefix. Conflicts with `name`.
	NamePrefix interface{}
	// The path to the role.
	// See [IAM Identifiers](https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html) for more information.
	Path interface{}
	// The ARN of the policy that is used to set the permissions boundary for the role.
	PermissionsBoundary interface{}
	// Key-value mapping of tags for the IAM role
	Tags interface{}
}
