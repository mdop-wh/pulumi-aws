// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package backup

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Manages selection conditions for AWS Backup plan resources.
//
// ## Example Usage
// ### IAM Role
//
// > For more information about creating and managing IAM Roles for backups and restores, see the [AWS Backup Developer Guide](https://docs.aws.amazon.com/aws-backup/latest/devguide/iam-service-roles.html).
//
// The below example creates an IAM role with the default managed IAM Policy for allowing AWS Backup to create backups.
//
// ```go
// package main
//
// import (
// 	"fmt"
//
// 	"github.com/pulumi/pulumi-aws/sdk/v3/go/aws/backup"
// 	"github.com/pulumi/pulumi-aws/sdk/v3/go/aws/iam"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		exampleRole, err := iam.NewRole(ctx, "exampleRole", &iam.RoleArgs{
// 			AssumeRolePolicy: pulumi.String(fmt.Sprintf("%v%v%v%v%v%v%v%v%v%v%v%v", "{\n", "  \"Version\": \"2012-10-17\",\n", "  \"Statement\": [\n", "    {\n", "      \"Action\": [\"sts:AssumeRole\"],\n", "      \"Effect\": \"allow\",\n", "      \"Principal\": {\n", "        \"Service\": [\"backup.amazonaws.com\"]\n", "      }\n", "    }\n", "  ]\n", "}\n")),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		_, err = iam.NewRolePolicyAttachment(ctx, "exampleRolePolicyAttachment", &iam.RolePolicyAttachmentArgs{
// 			PolicyArn: pulumi.String("arn:aws:iam::aws:policy/service-role/AWSBackupServiceRolePolicyForBackup"),
// 			Role:      exampleRole.Name,
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		_, err = backup.NewSelection(ctx, "exampleSelection", &backup.SelectionArgs{
// 			IamRoleArn: exampleRole.Arn,
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
// ### Selecting Backups By Tag
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-aws/sdk/v3/go/aws/backup"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		_, err := backup.NewSelection(ctx, "example", &backup.SelectionArgs{
// 			IamRoleArn: pulumi.Any(aws_iam_role.Example.Arn),
// 			PlanId:     pulumi.Any(aws_backup_plan.Example.Id),
// 			SelectionTags: backup.SelectionSelectionTagArray{
// 				&backup.SelectionSelectionTagArgs{
// 					Type:  pulumi.String("STRINGEQUALS"),
// 					Key:   pulumi.String("foo"),
// 					Value: pulumi.String("bar"),
// 				},
// 			},
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
type Selection struct {
	pulumi.CustomResourceState

	// The ARN of the IAM role that AWS Backup uses to authenticate when restoring and backing up the target resource. See the [AWS Backup Developer Guide](https://docs.aws.amazon.com/aws-backup/latest/devguide/access-control.html#managed-policies) for additional information about using AWS managed policies or creating custom policies attached to the IAM role.
	IamRoleArn pulumi.StringOutput `pulumi:"iamRoleArn"`
	// The display name of a resource selection document.
	Name pulumi.StringOutput `pulumi:"name"`
	// The backup plan ID to be associated with the selection of resources.
	PlanId pulumi.StringOutput `pulumi:"planId"`
	// An array of strings that either contain Amazon Resource Names (ARNs) or match patterns of resources to assign to a backup plan..
	Resources pulumi.StringArrayOutput `pulumi:"resources"`
	// Tag-based conditions used to specify a set of resources to assign to a backup plan.
	SelectionTags SelectionSelectionTagArrayOutput `pulumi:"selectionTags"`
}

// NewSelection registers a new resource with the given unique name, arguments, and options.
func NewSelection(ctx *pulumi.Context,
	name string, args *SelectionArgs, opts ...pulumi.ResourceOption) (*Selection, error) {
	if args == nil || args.IamRoleArn == nil {
		return nil, errors.New("missing required argument 'IamRoleArn'")
	}
	if args == nil || args.PlanId == nil {
		return nil, errors.New("missing required argument 'PlanId'")
	}
	if args == nil {
		args = &SelectionArgs{}
	}
	var resource Selection
	err := ctx.RegisterResource("aws:backup/selection:Selection", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetSelection gets an existing Selection resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetSelection(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *SelectionState, opts ...pulumi.ResourceOption) (*Selection, error) {
	var resource Selection
	err := ctx.ReadResource("aws:backup/selection:Selection", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Selection resources.
type selectionState struct {
	// The ARN of the IAM role that AWS Backup uses to authenticate when restoring and backing up the target resource. See the [AWS Backup Developer Guide](https://docs.aws.amazon.com/aws-backup/latest/devguide/access-control.html#managed-policies) for additional information about using AWS managed policies or creating custom policies attached to the IAM role.
	IamRoleArn *string `pulumi:"iamRoleArn"`
	// The display name of a resource selection document.
	Name *string `pulumi:"name"`
	// The backup plan ID to be associated with the selection of resources.
	PlanId *string `pulumi:"planId"`
	// An array of strings that either contain Amazon Resource Names (ARNs) or match patterns of resources to assign to a backup plan..
	Resources []string `pulumi:"resources"`
	// Tag-based conditions used to specify a set of resources to assign to a backup plan.
	SelectionTags []SelectionSelectionTag `pulumi:"selectionTags"`
}

type SelectionState struct {
	// The ARN of the IAM role that AWS Backup uses to authenticate when restoring and backing up the target resource. See the [AWS Backup Developer Guide](https://docs.aws.amazon.com/aws-backup/latest/devguide/access-control.html#managed-policies) for additional information about using AWS managed policies or creating custom policies attached to the IAM role.
	IamRoleArn pulumi.StringPtrInput
	// The display name of a resource selection document.
	Name pulumi.StringPtrInput
	// The backup plan ID to be associated with the selection of resources.
	PlanId pulumi.StringPtrInput
	// An array of strings that either contain Amazon Resource Names (ARNs) or match patterns of resources to assign to a backup plan..
	Resources pulumi.StringArrayInput
	// Tag-based conditions used to specify a set of resources to assign to a backup plan.
	SelectionTags SelectionSelectionTagArrayInput
}

func (SelectionState) ElementType() reflect.Type {
	return reflect.TypeOf((*selectionState)(nil)).Elem()
}

type selectionArgs struct {
	// The ARN of the IAM role that AWS Backup uses to authenticate when restoring and backing up the target resource. See the [AWS Backup Developer Guide](https://docs.aws.amazon.com/aws-backup/latest/devguide/access-control.html#managed-policies) for additional information about using AWS managed policies or creating custom policies attached to the IAM role.
	IamRoleArn string `pulumi:"iamRoleArn"`
	// The display name of a resource selection document.
	Name *string `pulumi:"name"`
	// The backup plan ID to be associated with the selection of resources.
	PlanId string `pulumi:"planId"`
	// An array of strings that either contain Amazon Resource Names (ARNs) or match patterns of resources to assign to a backup plan..
	Resources []string `pulumi:"resources"`
	// Tag-based conditions used to specify a set of resources to assign to a backup plan.
	SelectionTags []SelectionSelectionTag `pulumi:"selectionTags"`
}

// The set of arguments for constructing a Selection resource.
type SelectionArgs struct {
	// The ARN of the IAM role that AWS Backup uses to authenticate when restoring and backing up the target resource. See the [AWS Backup Developer Guide](https://docs.aws.amazon.com/aws-backup/latest/devguide/access-control.html#managed-policies) for additional information about using AWS managed policies or creating custom policies attached to the IAM role.
	IamRoleArn pulumi.StringInput
	// The display name of a resource selection document.
	Name pulumi.StringPtrInput
	// The backup plan ID to be associated with the selection of resources.
	PlanId pulumi.StringInput
	// An array of strings that either contain Amazon Resource Names (ARNs) or match patterns of resources to assign to a backup plan..
	Resources pulumi.StringArrayInput
	// Tag-based conditions used to specify a set of resources to assign to a backup plan.
	SelectionTags SelectionSelectionTagArrayInput
}

func (SelectionArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*selectionArgs)(nil)).Elem()
}
