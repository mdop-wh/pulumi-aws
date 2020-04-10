// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package iot

import (
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Returns a unique endpoint specific to the AWS account making the call.
func GetEndpoint(ctx *pulumi.Context, args *GetEndpointArgs, opts ...pulumi.InvokeOption) (*GetEndpointResult, error) {
	var rv GetEndpointResult
	err := ctx.Invoke("aws:iot/getEndpoint:getEndpoint", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getEndpoint.
type GetEndpointArgs struct {
	// Endpoint type. Valid values: `iot:CredentialProvider`, `iot:Data`, `iot:Data-ATS`, `iot:Job`.
	EndpointType *string `pulumi:"endpointType"`
}

// A collection of values returned by getEndpoint.
type GetEndpointResult struct {
	// The endpoint based on `endpointType`:
	// * No `endpointType`: Either `iot:Data` or `iot:Data-ATS` [depending on region](https://aws.amazon.com/blogs/iot/aws-iot-core-ats-endpoints/)
	// * `iot:CredentialsProvider`: `IDENTIFIER.credentials.iot.REGION.amazonaws.com`
	// * `iot:Data`: `IDENTIFIER.iot.REGION.amazonaws.com`
	// * `iot:Data-ATS`: `IDENTIFIER-ats.iot.REGION.amazonaws.com`
	// * `iot:Job`: `IDENTIFIER.jobs.iot.REGION.amazonaws.com`
	EndpointAddress string  `pulumi:"endpointAddress"`
	EndpointType    *string `pulumi:"endpointType"`
	// id is the provider-assigned unique ID for this managed resource.
	Id string `pulumi:"id"`
}
