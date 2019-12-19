// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.Lambda
{
    /// <summary>
    /// Manages an asynchronous invocation configuration for a Lambda Function or Alias. More information about asynchronous invocations and the configurable values can be found in the [Lambda Developer Guide](https://docs.aws.amazon.com/lambda/latest/dg/invocation-async.html).
    /// 
    /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/lambda_function_event_invoke_config.html.markdown.
    /// </summary>
    public partial class FunctionEventInvokeConfig : Pulumi.CustomResource
    {
        /// <summary>
        /// Configuration block with destination configuration. See below for details.
        /// </summary>
        [Output("destinationConfig")]
        public Output<Outputs.FunctionEventInvokeConfigDestinationConfig?> DestinationConfig { get; private set; } = null!;

        /// <summary>
        /// Name or Amazon Resource Name (ARN) of the Lambda Function, omitting any version or alias qualifier.
        /// </summary>
        [Output("functionName")]
        public Output<string> FunctionName { get; private set; } = null!;

        /// <summary>
        /// Maximum age of a request that Lambda sends to a function for processing in seconds. Valid values between 60 and 21600.
        /// </summary>
        [Output("maximumEventAgeInSeconds")]
        public Output<int?> MaximumEventAgeInSeconds { get; private set; } = null!;

        /// <summary>
        /// Maximum number of times to retry when the function returns an error. Valid values between 0 and 2. Defaults to 2.
        /// </summary>
        [Output("maximumRetryAttempts")]
        public Output<int?> MaximumRetryAttempts { get; private set; } = null!;

        /// <summary>
        /// Lambda Function published version, `$LATEST`, or Lambda Alias name.
        /// </summary>
        [Output("qualifier")]
        public Output<string?> Qualifier { get; private set; } = null!;


        /// <summary>
        /// Create a FunctionEventInvokeConfig resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public FunctionEventInvokeConfig(string name, FunctionEventInvokeConfigArgs args, CustomResourceOptions? options = null)
            : base("aws:lambda/functionEventInvokeConfig:FunctionEventInvokeConfig", name, args ?? ResourceArgs.Empty, MakeResourceOptions(options, ""))
        {
        }

        private FunctionEventInvokeConfig(string name, Input<string> id, FunctionEventInvokeConfigState? state = null, CustomResourceOptions? options = null)
            : base("aws:lambda/functionEventInvokeConfig:FunctionEventInvokeConfig", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing FunctionEventInvokeConfig resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static FunctionEventInvokeConfig Get(string name, Input<string> id, FunctionEventInvokeConfigState? state = null, CustomResourceOptions? options = null)
        {
            return new FunctionEventInvokeConfig(name, id, state, options);
        }
    }

    public sealed class FunctionEventInvokeConfigArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Configuration block with destination configuration. See below for details.
        /// </summary>
        [Input("destinationConfig")]
        public Input<Inputs.FunctionEventInvokeConfigDestinationConfigArgs>? DestinationConfig { get; set; }

        /// <summary>
        /// Name or Amazon Resource Name (ARN) of the Lambda Function, omitting any version or alias qualifier.
        /// </summary>
        [Input("functionName", required: true)]
        public Input<string> FunctionName { get; set; } = null!;

        /// <summary>
        /// Maximum age of a request that Lambda sends to a function for processing in seconds. Valid values between 60 and 21600.
        /// </summary>
        [Input("maximumEventAgeInSeconds")]
        public Input<int>? MaximumEventAgeInSeconds { get; set; }

        /// <summary>
        /// Maximum number of times to retry when the function returns an error. Valid values between 0 and 2. Defaults to 2.
        /// </summary>
        [Input("maximumRetryAttempts")]
        public Input<int>? MaximumRetryAttempts { get; set; }

        /// <summary>
        /// Lambda Function published version, `$LATEST`, or Lambda Alias name.
        /// </summary>
        [Input("qualifier")]
        public Input<string>? Qualifier { get; set; }

        public FunctionEventInvokeConfigArgs()
        {
        }
    }

    public sealed class FunctionEventInvokeConfigState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Configuration block with destination configuration. See below for details.
        /// </summary>
        [Input("destinationConfig")]
        public Input<Inputs.FunctionEventInvokeConfigDestinationConfigGetArgs>? DestinationConfig { get; set; }

        /// <summary>
        /// Name or Amazon Resource Name (ARN) of the Lambda Function, omitting any version or alias qualifier.
        /// </summary>
        [Input("functionName")]
        public Input<string>? FunctionName { get; set; }

        /// <summary>
        /// Maximum age of a request that Lambda sends to a function for processing in seconds. Valid values between 60 and 21600.
        /// </summary>
        [Input("maximumEventAgeInSeconds")]
        public Input<int>? MaximumEventAgeInSeconds { get; set; }

        /// <summary>
        /// Maximum number of times to retry when the function returns an error. Valid values between 0 and 2. Defaults to 2.
        /// </summary>
        [Input("maximumRetryAttempts")]
        public Input<int>? MaximumRetryAttempts { get; set; }

        /// <summary>
        /// Lambda Function published version, `$LATEST`, or Lambda Alias name.
        /// </summary>
        [Input("qualifier")]
        public Input<string>? Qualifier { get; set; }

        public FunctionEventInvokeConfigState()
        {
        }
    }

    namespace Inputs
    {

    public sealed class FunctionEventInvokeConfigDestinationConfigArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Configuration block with destination configuration for failed asynchronous invocations. See below for details.
        /// </summary>
        [Input("onFailure")]
        public Input<FunctionEventInvokeConfigDestinationConfigOnFailureArgs>? OnFailure { get; set; }

        /// <summary>
        /// Configuration block with destination configuration for successful asynchronous invocations. See below for details.
        /// </summary>
        [Input("onSuccess")]
        public Input<FunctionEventInvokeConfigDestinationConfigOnSuccessArgs>? OnSuccess { get; set; }

        public FunctionEventInvokeConfigDestinationConfigArgs()
        {
        }
    }

    public sealed class FunctionEventInvokeConfigDestinationConfigGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Configuration block with destination configuration for failed asynchronous invocations. See below for details.
        /// </summary>
        [Input("onFailure")]
        public Input<FunctionEventInvokeConfigDestinationConfigOnFailureGetArgs>? OnFailure { get; set; }

        /// <summary>
        /// Configuration block with destination configuration for successful asynchronous invocations. See below for details.
        /// </summary>
        [Input("onSuccess")]
        public Input<FunctionEventInvokeConfigDestinationConfigOnSuccessGetArgs>? OnSuccess { get; set; }

        public FunctionEventInvokeConfigDestinationConfigGetArgs()
        {
        }
    }

    public sealed class FunctionEventInvokeConfigDestinationConfigOnFailureArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Amazon Resource Name (ARN) of the destination resource. See the [Lambda Developer Guide](https://docs.aws.amazon.com/lambda/latest/dg/invocation-async.html#invocation-async-destinations) for acceptable resource types and associated IAM permissions.
        /// </summary>
        [Input("destination", required: true)]
        public Input<string> Destination { get; set; } = null!;

        public FunctionEventInvokeConfigDestinationConfigOnFailureArgs()
        {
        }
    }

    public sealed class FunctionEventInvokeConfigDestinationConfigOnFailureGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Amazon Resource Name (ARN) of the destination resource. See the [Lambda Developer Guide](https://docs.aws.amazon.com/lambda/latest/dg/invocation-async.html#invocation-async-destinations) for acceptable resource types and associated IAM permissions.
        /// </summary>
        [Input("destination", required: true)]
        public Input<string> Destination { get; set; } = null!;

        public FunctionEventInvokeConfigDestinationConfigOnFailureGetArgs()
        {
        }
    }

    public sealed class FunctionEventInvokeConfigDestinationConfigOnSuccessArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Amazon Resource Name (ARN) of the destination resource. See the [Lambda Developer Guide](https://docs.aws.amazon.com/lambda/latest/dg/invocation-async.html#invocation-async-destinations) for acceptable resource types and associated IAM permissions.
        /// </summary>
        [Input("destination", required: true)]
        public Input<string> Destination { get; set; } = null!;

        public FunctionEventInvokeConfigDestinationConfigOnSuccessArgs()
        {
        }
    }

    public sealed class FunctionEventInvokeConfigDestinationConfigOnSuccessGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Amazon Resource Name (ARN) of the destination resource. See the [Lambda Developer Guide](https://docs.aws.amazon.com/lambda/latest/dg/invocation-async.html#invocation-async-destinations) for acceptable resource types and associated IAM permissions.
        /// </summary>
        [Input("destination", required: true)]
        public Input<string> Destination { get; set; } = null!;

        public FunctionEventInvokeConfigDestinationConfigOnSuccessGetArgs()
        {
        }
    }
    }

    namespace Outputs
    {

    [OutputType]
    public sealed class FunctionEventInvokeConfigDestinationConfig
    {
        /// <summary>
        /// Configuration block with destination configuration for failed asynchronous invocations. See below for details.
        /// </summary>
        public readonly FunctionEventInvokeConfigDestinationConfigOnFailure? OnFailure;
        /// <summary>
        /// Configuration block with destination configuration for successful asynchronous invocations. See below for details.
        /// </summary>
        public readonly FunctionEventInvokeConfigDestinationConfigOnSuccess? OnSuccess;

        [OutputConstructor]
        private FunctionEventInvokeConfigDestinationConfig(
            FunctionEventInvokeConfigDestinationConfigOnFailure? onFailure,
            FunctionEventInvokeConfigDestinationConfigOnSuccess? onSuccess)
        {
            OnFailure = onFailure;
            OnSuccess = onSuccess;
        }
    }

    [OutputType]
    public sealed class FunctionEventInvokeConfigDestinationConfigOnFailure
    {
        /// <summary>
        /// Amazon Resource Name (ARN) of the destination resource. See the [Lambda Developer Guide](https://docs.aws.amazon.com/lambda/latest/dg/invocation-async.html#invocation-async-destinations) for acceptable resource types and associated IAM permissions.
        /// </summary>
        public readonly string Destination;

        [OutputConstructor]
        private FunctionEventInvokeConfigDestinationConfigOnFailure(string destination)
        {
            Destination = destination;
        }
    }

    [OutputType]
    public sealed class FunctionEventInvokeConfigDestinationConfigOnSuccess
    {
        /// <summary>
        /// Amazon Resource Name (ARN) of the destination resource. See the [Lambda Developer Guide](https://docs.aws.amazon.com/lambda/latest/dg/invocation-async.html#invocation-async-destinations) for acceptable resource types and associated IAM permissions.
        /// </summary>
        public readonly string Destination;

        [OutputConstructor]
        private FunctionEventInvokeConfigDestinationConfigOnSuccess(string destination)
        {
            Destination = destination;
        }
    }
    }
}
