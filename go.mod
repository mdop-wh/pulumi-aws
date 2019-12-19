module github.com/pulumi/pulumi-aws

require (
	github.com/aws/aws-sdk-go v1.26.5
	github.com/hashicorp/aws-sdk-go-base v0.4.0
	github.com/hashicorp/terraform-plugin-sdk v1.4.1
	github.com/mitchellh/go-homedir v1.1.0
	github.com/pkg/errors v0.8.1
	github.com/pulumi/pulumi v1.6.0
	github.com/pulumi/pulumi-terraform-bridge v1.5.2
	github.com/stretchr/testify v1.4.0
	github.com/terraform-providers/terraform-provider-aws v0.0.0-20191010190908-1261a98537f2
)

replace (
	github.com/Azure/go-autorest => github.com/Azure/go-autorest v12.4.3+incompatible
	github.com/hashicorp/vault => github.com/hashicorp/vault v1.2.0
	github.com/terraform-providers/terraform-provider-aws => github.com/pulumi/terraform-provider-aws v1.38.1-0.20191219215958-ab33ce48bae2
)

go 1.13
