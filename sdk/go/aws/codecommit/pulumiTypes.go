// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package codecommit

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

type TriggerTrigger struct {
	// The branches that will be included in the trigger configuration. If no branches are specified, the trigger will apply to all branches.
	Branches []string `pulumi:"branches"`
	// Any custom data associated with the trigger that will be included in the information sent to the target of the trigger.
	CustomData *string `pulumi:"customData"`
	// The ARN of the resource that is the target for a trigger. For example, the ARN of a topic in Amazon Simple Notification Service (SNS).
	DestinationArn string `pulumi:"destinationArn"`
	// The repository events that will cause the trigger to run actions in another service, such as sending a notification through Amazon Simple Notification Service (SNS). If no events are specified, the trigger will run for all repository events. Event types include: `all`, `updateReference`, `createReference`, `deleteReference`.
	Events []string `pulumi:"events"`
	// The name of the trigger.
	Name string `pulumi:"name"`
}

// TriggerTriggerInput is an input type that accepts TriggerTriggerArgs and TriggerTriggerOutput values.
// You can construct a concrete instance of `TriggerTriggerInput` via:
//
// 		 TriggerTriggerArgs{...}
//
type TriggerTriggerInput interface {
	pulumi.Input

	ToTriggerTriggerOutput() TriggerTriggerOutput
	ToTriggerTriggerOutputWithContext(context.Context) TriggerTriggerOutput
}

type TriggerTriggerArgs struct {
	// The branches that will be included in the trigger configuration. If no branches are specified, the trigger will apply to all branches.
	Branches pulumi.StringArrayInput `pulumi:"branches"`
	// Any custom data associated with the trigger that will be included in the information sent to the target of the trigger.
	CustomData pulumi.StringPtrInput `pulumi:"customData"`
	// The ARN of the resource that is the target for a trigger. For example, the ARN of a topic in Amazon Simple Notification Service (SNS).
	DestinationArn pulumi.StringInput `pulumi:"destinationArn"`
	// The repository events that will cause the trigger to run actions in another service, such as sending a notification through Amazon Simple Notification Service (SNS). If no events are specified, the trigger will run for all repository events. Event types include: `all`, `updateReference`, `createReference`, `deleteReference`.
	Events pulumi.StringArrayInput `pulumi:"events"`
	// The name of the trigger.
	Name pulumi.StringInput `pulumi:"name"`
}

func (TriggerTriggerArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*TriggerTrigger)(nil)).Elem()
}

func (i TriggerTriggerArgs) ToTriggerTriggerOutput() TriggerTriggerOutput {
	return i.ToTriggerTriggerOutputWithContext(context.Background())
}

func (i TriggerTriggerArgs) ToTriggerTriggerOutputWithContext(ctx context.Context) TriggerTriggerOutput {
	return pulumi.ToOutputWithContext(ctx, i).(TriggerTriggerOutput)
}

// TriggerTriggerArrayInput is an input type that accepts TriggerTriggerArray and TriggerTriggerArrayOutput values.
// You can construct a concrete instance of `TriggerTriggerArrayInput` via:
//
// 		 TriggerTriggerArray{ TriggerTriggerArgs{...} }
//
type TriggerTriggerArrayInput interface {
	pulumi.Input

	ToTriggerTriggerArrayOutput() TriggerTriggerArrayOutput
	ToTriggerTriggerArrayOutputWithContext(context.Context) TriggerTriggerArrayOutput
}

type TriggerTriggerArray []TriggerTriggerInput

func (TriggerTriggerArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]TriggerTrigger)(nil)).Elem()
}

func (i TriggerTriggerArray) ToTriggerTriggerArrayOutput() TriggerTriggerArrayOutput {
	return i.ToTriggerTriggerArrayOutputWithContext(context.Background())
}

func (i TriggerTriggerArray) ToTriggerTriggerArrayOutputWithContext(ctx context.Context) TriggerTriggerArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(TriggerTriggerArrayOutput)
}

type TriggerTriggerOutput struct{ *pulumi.OutputState }

func (TriggerTriggerOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*TriggerTrigger)(nil)).Elem()
}

func (o TriggerTriggerOutput) ToTriggerTriggerOutput() TriggerTriggerOutput {
	return o
}

func (o TriggerTriggerOutput) ToTriggerTriggerOutputWithContext(ctx context.Context) TriggerTriggerOutput {
	return o
}

// The branches that will be included in the trigger configuration. If no branches are specified, the trigger will apply to all branches.
func (o TriggerTriggerOutput) Branches() pulumi.StringArrayOutput {
	return o.ApplyT(func(v TriggerTrigger) []string { return v.Branches }).(pulumi.StringArrayOutput)
}

// Any custom data associated with the trigger that will be included in the information sent to the target of the trigger.
func (o TriggerTriggerOutput) CustomData() pulumi.StringPtrOutput {
	return o.ApplyT(func(v TriggerTrigger) *string { return v.CustomData }).(pulumi.StringPtrOutput)
}

// The ARN of the resource that is the target for a trigger. For example, the ARN of a topic in Amazon Simple Notification Service (SNS).
func (o TriggerTriggerOutput) DestinationArn() pulumi.StringOutput {
	return o.ApplyT(func(v TriggerTrigger) string { return v.DestinationArn }).(pulumi.StringOutput)
}

// The repository events that will cause the trigger to run actions in another service, such as sending a notification through Amazon Simple Notification Service (SNS). If no events are specified, the trigger will run for all repository events. Event types include: `all`, `updateReference`, `createReference`, `deleteReference`.
func (o TriggerTriggerOutput) Events() pulumi.StringArrayOutput {
	return o.ApplyT(func(v TriggerTrigger) []string { return v.Events }).(pulumi.StringArrayOutput)
}

// The name of the trigger.
func (o TriggerTriggerOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v TriggerTrigger) string { return v.Name }).(pulumi.StringOutput)
}

type TriggerTriggerArrayOutput struct{ *pulumi.OutputState }

func (TriggerTriggerArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]TriggerTrigger)(nil)).Elem()
}

func (o TriggerTriggerArrayOutput) ToTriggerTriggerArrayOutput() TriggerTriggerArrayOutput {
	return o
}

func (o TriggerTriggerArrayOutput) ToTriggerTriggerArrayOutputWithContext(ctx context.Context) TriggerTriggerArrayOutput {
	return o
}

func (o TriggerTriggerArrayOutput) Index(i pulumi.IntInput) TriggerTriggerOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) TriggerTrigger {
		return vs[0].([]TriggerTrigger)[vs[1].(int)]
	}).(TriggerTriggerOutput)
}

func init() {
	pulumi.RegisterOutputType(TriggerTriggerOutput{})
	pulumi.RegisterOutputType(TriggerTriggerArrayOutput{})
}
