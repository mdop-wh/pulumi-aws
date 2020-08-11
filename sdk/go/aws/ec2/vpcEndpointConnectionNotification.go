// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package ec2

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Provides a VPC Endpoint connection notification resource.
// Connection notifications notify subscribers of VPC Endpoint events.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"fmt"
//
// 	"github.com/pulumi/pulumi-aws/sdk/v2/go/aws/ec2"
// 	"github.com/pulumi/pulumi-aws/sdk/v2/go/aws/sns"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		topic, err := sns.NewTopic(ctx, "topic", &sns.TopicArgs{
// 			Policy: pulumi.String(fmt.Sprintf("%v%v%v%v%v%v%v%v%v%v%v", "{\n", "    \"Version\":\"2012-10-17\",\n", "    \"Statement\":[{\n", "        \"Effect\": \"Allow\",\n", "        \"Principal\": {\n", "            \"Service\": \"vpce.amazonaws.com\"\n", "        },\n", "        \"Action\": \"SNS:Publish\",\n", "        \"Resource\": \"arn:aws:sns:*:*:vpce-notification-topic\"\n", "    }]\n", "}\n")),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		fooVpcEndpointService, err := ec2.NewVpcEndpointService(ctx, "fooVpcEndpointService", &ec2.VpcEndpointServiceArgs{
// 			AcceptanceRequired: pulumi.Bool(false),
// 			NetworkLoadBalancerArns: pulumi.StringArray{
// 				pulumi.Any(aws_lb.Test.Arn),
// 			},
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		_, err = ec2.NewVpcEndpointConnectionNotification(ctx, "fooVpcEndpointConnectionNotification", &ec2.VpcEndpointConnectionNotificationArgs{
// 			VpcEndpointServiceId:      fooVpcEndpointService.ID(),
// 			ConnectionNotificationArn: topic.Arn,
// 			ConnectionEvents: pulumi.StringArray{
// 				pulumi.String("Accept"),
// 				pulumi.String("Reject"),
// 			},
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
type VpcEndpointConnectionNotification struct {
	pulumi.CustomResourceState

	// One or more endpoint [events](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateVpcEndpointConnectionNotification.html#API_CreateVpcEndpointConnectionNotification_RequestParameters) for which to receive notifications.
	ConnectionEvents pulumi.StringArrayOutput `pulumi:"connectionEvents"`
	// The ARN of the SNS topic for the notifications.
	ConnectionNotificationArn pulumi.StringOutput `pulumi:"connectionNotificationArn"`
	// The type of notification.
	NotificationType pulumi.StringOutput `pulumi:"notificationType"`
	// The state of the notification.
	State pulumi.StringOutput `pulumi:"state"`
	// The ID of the VPC Endpoint to receive notifications for.
	VpcEndpointId pulumi.StringPtrOutput `pulumi:"vpcEndpointId"`
	// The ID of the VPC Endpoint Service to receive notifications for.
	VpcEndpointServiceId pulumi.StringPtrOutput `pulumi:"vpcEndpointServiceId"`
}

// NewVpcEndpointConnectionNotification registers a new resource with the given unique name, arguments, and options.
func NewVpcEndpointConnectionNotification(ctx *pulumi.Context,
	name string, args *VpcEndpointConnectionNotificationArgs, opts ...pulumi.ResourceOption) (*VpcEndpointConnectionNotification, error) {
	if args == nil || args.ConnectionEvents == nil {
		return nil, errors.New("missing required argument 'ConnectionEvents'")
	}
	if args == nil || args.ConnectionNotificationArn == nil {
		return nil, errors.New("missing required argument 'ConnectionNotificationArn'")
	}
	if args == nil {
		args = &VpcEndpointConnectionNotificationArgs{}
	}
	var resource VpcEndpointConnectionNotification
	err := ctx.RegisterResource("aws:ec2/vpcEndpointConnectionNotification:VpcEndpointConnectionNotification", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetVpcEndpointConnectionNotification gets an existing VpcEndpointConnectionNotification resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetVpcEndpointConnectionNotification(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *VpcEndpointConnectionNotificationState, opts ...pulumi.ResourceOption) (*VpcEndpointConnectionNotification, error) {
	var resource VpcEndpointConnectionNotification
	err := ctx.ReadResource("aws:ec2/vpcEndpointConnectionNotification:VpcEndpointConnectionNotification", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering VpcEndpointConnectionNotification resources.
type vpcEndpointConnectionNotificationState struct {
	// One or more endpoint [events](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateVpcEndpointConnectionNotification.html#API_CreateVpcEndpointConnectionNotification_RequestParameters) for which to receive notifications.
	ConnectionEvents []string `pulumi:"connectionEvents"`
	// The ARN of the SNS topic for the notifications.
	ConnectionNotificationArn *string `pulumi:"connectionNotificationArn"`
	// The type of notification.
	NotificationType *string `pulumi:"notificationType"`
	// The state of the notification.
	State *string `pulumi:"state"`
	// The ID of the VPC Endpoint to receive notifications for.
	VpcEndpointId *string `pulumi:"vpcEndpointId"`
	// The ID of the VPC Endpoint Service to receive notifications for.
	VpcEndpointServiceId *string `pulumi:"vpcEndpointServiceId"`
}

type VpcEndpointConnectionNotificationState struct {
	// One or more endpoint [events](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateVpcEndpointConnectionNotification.html#API_CreateVpcEndpointConnectionNotification_RequestParameters) for which to receive notifications.
	ConnectionEvents pulumi.StringArrayInput
	// The ARN of the SNS topic for the notifications.
	ConnectionNotificationArn pulumi.StringPtrInput
	// The type of notification.
	NotificationType pulumi.StringPtrInput
	// The state of the notification.
	State pulumi.StringPtrInput
	// The ID of the VPC Endpoint to receive notifications for.
	VpcEndpointId pulumi.StringPtrInput
	// The ID of the VPC Endpoint Service to receive notifications for.
	VpcEndpointServiceId pulumi.StringPtrInput
}

func (VpcEndpointConnectionNotificationState) ElementType() reflect.Type {
	return reflect.TypeOf((*vpcEndpointConnectionNotificationState)(nil)).Elem()
}

type vpcEndpointConnectionNotificationArgs struct {
	// One or more endpoint [events](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateVpcEndpointConnectionNotification.html#API_CreateVpcEndpointConnectionNotification_RequestParameters) for which to receive notifications.
	ConnectionEvents []string `pulumi:"connectionEvents"`
	// The ARN of the SNS topic for the notifications.
	ConnectionNotificationArn string `pulumi:"connectionNotificationArn"`
	// The ID of the VPC Endpoint to receive notifications for.
	VpcEndpointId *string `pulumi:"vpcEndpointId"`
	// The ID of the VPC Endpoint Service to receive notifications for.
	VpcEndpointServiceId *string `pulumi:"vpcEndpointServiceId"`
}

// The set of arguments for constructing a VpcEndpointConnectionNotification resource.
type VpcEndpointConnectionNotificationArgs struct {
	// One or more endpoint [events](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateVpcEndpointConnectionNotification.html#API_CreateVpcEndpointConnectionNotification_RequestParameters) for which to receive notifications.
	ConnectionEvents pulumi.StringArrayInput
	// The ARN of the SNS topic for the notifications.
	ConnectionNotificationArn pulumi.StringInput
	// The ID of the VPC Endpoint to receive notifications for.
	VpcEndpointId pulumi.StringPtrInput
	// The ID of the VPC Endpoint Service to receive notifications for.
	VpcEndpointServiceId pulumi.StringPtrInput
}

func (VpcEndpointConnectionNotificationArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*vpcEndpointConnectionNotificationArgs)(nil)).Elem()
}
