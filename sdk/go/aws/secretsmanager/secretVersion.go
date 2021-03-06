// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package secretsmanager

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Provides a resource to manage AWS Secrets Manager secret version including its secret value. To manage secret metadata, see the `secretsmanager.Secret` resource.
//
// > **NOTE:** If the `AWSCURRENT` staging label is present on this version during resource deletion, that label cannot be removed and will be skipped to prevent errors when fully deleting the secret. That label will leave this secret version active even after the resource is deleted from this provider unless the secret itself is deleted. Move the `AWSCURRENT` staging label before or after deleting this resource from this provider to fully trigger version deprecation if necessary.
//
// ## Example Usage
// ### Simple String Value
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-aws/sdk/v3/go/aws/secretsmanager"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		_, err := secretsmanager.NewSecretVersion(ctx, "example", &secretsmanager.SecretVersionArgs{
// 			SecretId:     pulumi.Any(aws_secretsmanager_secret.Example.Id),
// 			SecretString: pulumi.String("example-string-to-protect"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
// ### Key-Value Pairs
//
// Secrets Manager also accepts key-value pairs in JSON.
//
// ```go
// package main
//
// import (
// 	"encoding/json"
//
// 	"github.com/pulumi/pulumi-aws/sdk/v3/go/aws/secretsmanager"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		tmpJSON0, err := json.Marshal(example)
// 		if err != nil {
// 			return err
// 		}
// 		json0 := string(tmpJSON0)
// 		_, err := secretsmanager.NewSecretVersion(ctx, "exampleSecretVersion", &secretsmanager.SecretVersionArgs{
// 			SecretId:     pulumi.Any(aws_secretsmanager_secret.Example.Id),
// 			SecretString: pulumi.String(json0),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
type SecretVersion struct {
	pulumi.CustomResourceState

	// The ARN of the secret.
	Arn pulumi.StringOutput `pulumi:"arn"`
	// Specifies binary data that you want to encrypt and store in this version of the secret. This is required if secretString is not set. Needs to be encoded to base64.
	SecretBinary pulumi.StringPtrOutput `pulumi:"secretBinary"`
	// Specifies the secret to which you want to add a new version. You can specify either the Amazon Resource Name (ARN) or the friendly name of the secret. The secret must already exist.
	SecretId pulumi.StringOutput `pulumi:"secretId"`
	// Specifies text data that you want to encrypt and store in this version of the secret. This is required if secretBinary is not set.
	SecretString pulumi.StringPtrOutput `pulumi:"secretString"`
	// The unique identifier of the version of the secret.
	VersionId pulumi.StringOutput `pulumi:"versionId"`
	// Specifies a list of staging labels that are attached to this version of the secret. A staging label must be unique to a single version of the secret. If you specify a staging label that's already associated with a different version of the same secret then that staging label is automatically removed from the other version and attached to this version. If you do not specify a value, then AWS Secrets Manager automatically moves the staging label `AWSCURRENT` to this new version on creation.
	VersionStages pulumi.StringArrayOutput `pulumi:"versionStages"`
}

// NewSecretVersion registers a new resource with the given unique name, arguments, and options.
func NewSecretVersion(ctx *pulumi.Context,
	name string, args *SecretVersionArgs, opts ...pulumi.ResourceOption) (*SecretVersion, error) {
	if args == nil || args.SecretId == nil {
		return nil, errors.New("missing required argument 'SecretId'")
	}
	if args == nil {
		args = &SecretVersionArgs{}
	}
	var resource SecretVersion
	err := ctx.RegisterResource("aws:secretsmanager/secretVersion:SecretVersion", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetSecretVersion gets an existing SecretVersion resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetSecretVersion(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *SecretVersionState, opts ...pulumi.ResourceOption) (*SecretVersion, error) {
	var resource SecretVersion
	err := ctx.ReadResource("aws:secretsmanager/secretVersion:SecretVersion", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering SecretVersion resources.
type secretVersionState struct {
	// The ARN of the secret.
	Arn *string `pulumi:"arn"`
	// Specifies binary data that you want to encrypt and store in this version of the secret. This is required if secretString is not set. Needs to be encoded to base64.
	SecretBinary *string `pulumi:"secretBinary"`
	// Specifies the secret to which you want to add a new version. You can specify either the Amazon Resource Name (ARN) or the friendly name of the secret. The secret must already exist.
	SecretId *string `pulumi:"secretId"`
	// Specifies text data that you want to encrypt and store in this version of the secret. This is required if secretBinary is not set.
	SecretString *string `pulumi:"secretString"`
	// The unique identifier of the version of the secret.
	VersionId *string `pulumi:"versionId"`
	// Specifies a list of staging labels that are attached to this version of the secret. A staging label must be unique to a single version of the secret. If you specify a staging label that's already associated with a different version of the same secret then that staging label is automatically removed from the other version and attached to this version. If you do not specify a value, then AWS Secrets Manager automatically moves the staging label `AWSCURRENT` to this new version on creation.
	VersionStages []string `pulumi:"versionStages"`
}

type SecretVersionState struct {
	// The ARN of the secret.
	Arn pulumi.StringPtrInput
	// Specifies binary data that you want to encrypt and store in this version of the secret. This is required if secretString is not set. Needs to be encoded to base64.
	SecretBinary pulumi.StringPtrInput
	// Specifies the secret to which you want to add a new version. You can specify either the Amazon Resource Name (ARN) or the friendly name of the secret. The secret must already exist.
	SecretId pulumi.StringPtrInput
	// Specifies text data that you want to encrypt and store in this version of the secret. This is required if secretBinary is not set.
	SecretString pulumi.StringPtrInput
	// The unique identifier of the version of the secret.
	VersionId pulumi.StringPtrInput
	// Specifies a list of staging labels that are attached to this version of the secret. A staging label must be unique to a single version of the secret. If you specify a staging label that's already associated with a different version of the same secret then that staging label is automatically removed from the other version and attached to this version. If you do not specify a value, then AWS Secrets Manager automatically moves the staging label `AWSCURRENT` to this new version on creation.
	VersionStages pulumi.StringArrayInput
}

func (SecretVersionState) ElementType() reflect.Type {
	return reflect.TypeOf((*secretVersionState)(nil)).Elem()
}

type secretVersionArgs struct {
	// Specifies binary data that you want to encrypt and store in this version of the secret. This is required if secretString is not set. Needs to be encoded to base64.
	SecretBinary *string `pulumi:"secretBinary"`
	// Specifies the secret to which you want to add a new version. You can specify either the Amazon Resource Name (ARN) or the friendly name of the secret. The secret must already exist.
	SecretId string `pulumi:"secretId"`
	// Specifies text data that you want to encrypt and store in this version of the secret. This is required if secretBinary is not set.
	SecretString *string `pulumi:"secretString"`
	// Specifies a list of staging labels that are attached to this version of the secret. A staging label must be unique to a single version of the secret. If you specify a staging label that's already associated with a different version of the same secret then that staging label is automatically removed from the other version and attached to this version. If you do not specify a value, then AWS Secrets Manager automatically moves the staging label `AWSCURRENT` to this new version on creation.
	VersionStages []string `pulumi:"versionStages"`
}

// The set of arguments for constructing a SecretVersion resource.
type SecretVersionArgs struct {
	// Specifies binary data that you want to encrypt and store in this version of the secret. This is required if secretString is not set. Needs to be encoded to base64.
	SecretBinary pulumi.StringPtrInput
	// Specifies the secret to which you want to add a new version. You can specify either the Amazon Resource Name (ARN) or the friendly name of the secret. The secret must already exist.
	SecretId pulumi.StringInput
	// Specifies text data that you want to encrypt and store in this version of the secret. This is required if secretBinary is not set.
	SecretString pulumi.StringPtrInput
	// Specifies a list of staging labels that are attached to this version of the secret. A staging label must be unique to a single version of the secret. If you specify a staging label that's already associated with a different version of the same secret then that staging label is automatically removed from the other version and attached to this version. If you do not specify a value, then AWS Secrets Manager automatically moves the staging label `AWSCURRENT` to this new version on creation.
	VersionStages pulumi.StringArrayInput
}

func (SecretVersionArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*secretVersionArgs)(nil)).Elem()
}
