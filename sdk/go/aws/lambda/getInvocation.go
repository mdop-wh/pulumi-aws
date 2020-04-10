// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package lambda

import (
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Use this data source to invoke custom lambda functions as data source.
// The lambda function is invoked with [RequestResponse](https://docs.aws.amazon.com/lambda/latest/dg/API_Invoke.html#API_Invoke_RequestSyntax)
// invocation type.
func GetInvocation(ctx *pulumi.Context, args *GetInvocationArgs, opts ...pulumi.InvokeOption) (*GetInvocationResult, error) {
	var rv GetInvocationResult
	err := ctx.Invoke("aws:lambda/getInvocation:getInvocation", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getInvocation.
type GetInvocationArgs struct {
	// The name of the lambda function.
	FunctionName string `pulumi:"functionName"`
	// A string in JSON format that is passed as payload to the lambda function.
	Input string `pulumi:"input"`
	// The qualifier (a.k.a version) of the lambda function. Defaults
	// to `$LATEST`.
	Qualifier *string `pulumi:"qualifier"`
}

// A collection of values returned by getInvocation.
type GetInvocationResult struct {
	FunctionName string `pulumi:"functionName"`
	// id is the provider-assigned unique ID for this managed resource.
	Id        string  `pulumi:"id"`
	Input     string  `pulumi:"input"`
	Qualifier *string `pulumi:"qualifier"`
	// String result of the lambda function invocation.
	Result string `pulumi:"result"`
	// This field is set only if result is a map of primitive types, where the map is string keys and string values.
	ResultMap map[string]string `pulumi:"resultMap"`
}
