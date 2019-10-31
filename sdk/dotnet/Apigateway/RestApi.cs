// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.Apigateway
{
    /// <summary>
    /// Provides an API Gateway REST API.
    /// 
    /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/api_gateway_rest_api.html.markdown.
    /// </summary>
    public partial class RestApi : Pulumi.CustomResource
    {
        /// <summary>
        /// The source of the API key for requests. Valid values are HEADER (default) and AUTHORIZER.
        /// </summary>
        [Output("apiKeySource")]
        public Output<string?> ApiKeySource { get; private set; } = null!;

        /// <summary>
        /// The list of binary media types supported by the RestApi. By default, the RestApi supports only UTF-8-encoded text payloads.
        /// </summary>
        [Output("binaryMediaTypes")]
        public Output<ImmutableArray<string>> BinaryMediaTypes { get; private set; } = null!;

        /// <summary>
        /// An OpenAPI specification that defines the set of routes and integrations to create as part of the REST API.
        /// </summary>
        [Output("body")]
        public Output<string?> Body { get; private set; } = null!;

        /// <summary>
        /// The creation date of the REST API
        /// </summary>
        [Output("createdDate")]
        public Output<string> CreatedDate { get; private set; } = null!;

        /// <summary>
        /// The description of the REST API
        /// </summary>
        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        /// <summary>
        /// Nested argument defining API endpoint configuration including endpoint type. Defined below.
        /// </summary>
        [Output("endpointConfiguration")]
        public Output<Outputs.RestApiEndpointConfiguration> EndpointConfiguration { get; private set; } = null!;

        /// <summary>
        /// The execution ARN part to be used in [`lambda_permission`](https://www.terraform.io/docs/providers/aws/r/lambda_permission.html)'s `source_arn`
        /// when allowing API Gateway to invoke a Lambda function,
        /// e.g. `arn:aws:execute-api:eu-west-2:123456789012:z4675bid1j`, which can be concatenated with allowed stage, method and resource path.
        /// </summary>
        [Output("executionArn")]
        public Output<string> ExecutionArn { get; private set; } = null!;

        /// <summary>
        /// Minimum response size to compress for the REST API. Integer between -1 and 10485760 (10MB). Setting a value greater than -1 will enable compression, -1 disables compression (default).
        /// </summary>
        [Output("minimumCompressionSize")]
        public Output<int?> MinimumCompressionSize { get; private set; } = null!;

        /// <summary>
        /// The name of the REST API
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// JSON formatted policy document that controls access to the API Gateway.
        /// </summary>
        [Output("policy")]
        public Output<string?> Policy { get; private set; } = null!;

        /// <summary>
        /// The resource ID of the REST API's root
        /// </summary>
        [Output("rootResourceId")]
        public Output<string> RootResourceId { get; private set; } = null!;


        /// <summary>
        /// Create a RestApi resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public RestApi(string name, RestApiArgs? args = null, CustomResourceOptions? options = null)
            : base("aws:apigateway/restApi:RestApi", name, args, MakeResourceOptions(options, ""))
        {
        }

        private RestApi(string name, Input<string> id, RestApiState? state = null, CustomResourceOptions? options = null)
            : base("aws:apigateway/restApi:RestApi", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing RestApi resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static RestApi Get(string name, Input<string> id, RestApiState? state = null, CustomResourceOptions? options = null)
        {
            return new RestApi(name, id, state, options);
        }
    }

    public sealed class RestApiArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The source of the API key for requests. Valid values are HEADER (default) and AUTHORIZER.
        /// </summary>
        [Input("apiKeySource")]
        public Input<string>? ApiKeySource { get; set; }

        [Input("binaryMediaTypes")]
        private InputList<string>? _binaryMediaTypes;

        /// <summary>
        /// The list of binary media types supported by the RestApi. By default, the RestApi supports only UTF-8-encoded text payloads.
        /// </summary>
        public InputList<string> BinaryMediaTypes
        {
            get => _binaryMediaTypes ?? (_binaryMediaTypes = new InputList<string>());
            set => _binaryMediaTypes = value;
        }

        /// <summary>
        /// An OpenAPI specification that defines the set of routes and integrations to create as part of the REST API.
        /// </summary>
        [Input("body")]
        public Input<string>? Body { get; set; }

        /// <summary>
        /// The description of the REST API
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// Nested argument defining API endpoint configuration including endpoint type. Defined below.
        /// </summary>
        [Input("endpointConfiguration")]
        public Input<Inputs.RestApiEndpointConfigurationArgs>? EndpointConfiguration { get; set; }

        /// <summary>
        /// Minimum response size to compress for the REST API. Integer between -1 and 10485760 (10MB). Setting a value greater than -1 will enable compression, -1 disables compression (default).
        /// </summary>
        [Input("minimumCompressionSize")]
        public Input<int>? MinimumCompressionSize { get; set; }

        /// <summary>
        /// The name of the REST API
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// JSON formatted policy document that controls access to the API Gateway.
        /// </summary>
        [Input("policy")]
        public Input<string>? Policy { get; set; }

        public RestApiArgs()
        {
        }
    }

    public sealed class RestApiState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The source of the API key for requests. Valid values are HEADER (default) and AUTHORIZER.
        /// </summary>
        [Input("apiKeySource")]
        public Input<string>? ApiKeySource { get; set; }

        [Input("binaryMediaTypes")]
        private InputList<string>? _binaryMediaTypes;

        /// <summary>
        /// The list of binary media types supported by the RestApi. By default, the RestApi supports only UTF-8-encoded text payloads.
        /// </summary>
        public InputList<string> BinaryMediaTypes
        {
            get => _binaryMediaTypes ?? (_binaryMediaTypes = new InputList<string>());
            set => _binaryMediaTypes = value;
        }

        /// <summary>
        /// An OpenAPI specification that defines the set of routes and integrations to create as part of the REST API.
        /// </summary>
        [Input("body")]
        public Input<string>? Body { get; set; }

        /// <summary>
        /// The creation date of the REST API
        /// </summary>
        [Input("createdDate")]
        public Input<string>? CreatedDate { get; set; }

        /// <summary>
        /// The description of the REST API
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// Nested argument defining API endpoint configuration including endpoint type. Defined below.
        /// </summary>
        [Input("endpointConfiguration")]
        public Input<Inputs.RestApiEndpointConfigurationGetArgs>? EndpointConfiguration { get; set; }

        /// <summary>
        /// The execution ARN part to be used in [`lambda_permission`](https://www.terraform.io/docs/providers/aws/r/lambda_permission.html)'s `source_arn`
        /// when allowing API Gateway to invoke a Lambda function,
        /// e.g. `arn:aws:execute-api:eu-west-2:123456789012:z4675bid1j`, which can be concatenated with allowed stage, method and resource path.
        /// </summary>
        [Input("executionArn")]
        public Input<string>? ExecutionArn { get; set; }

        /// <summary>
        /// Minimum response size to compress for the REST API. Integer between -1 and 10485760 (10MB). Setting a value greater than -1 will enable compression, -1 disables compression (default).
        /// </summary>
        [Input("minimumCompressionSize")]
        public Input<int>? MinimumCompressionSize { get; set; }

        /// <summary>
        /// The name of the REST API
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// JSON formatted policy document that controls access to the API Gateway.
        /// </summary>
        [Input("policy")]
        public Input<string>? Policy { get; set; }

        /// <summary>
        /// The resource ID of the REST API's root
        /// </summary>
        [Input("rootResourceId")]
        public Input<string>? RootResourceId { get; set; }

        public RestApiState()
        {
        }
    }

    namespace Inputs
    {

    public sealed class RestApiEndpointConfigurationArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// A list of endpoint types. This resource currently only supports managing a single value. Valid values: `EDGE`, `REGIONAL` or `PRIVATE`. If unspecified, defaults to `EDGE`. Must be declared as `REGIONAL` in non-Commercial partitions. Refer to the [documentation](https://docs.aws.amazon.com/apigateway/latest/developerguide/create-regional-api.html) for more information on the difference between edge-optimized and regional APIs.
        /// </summary>
        [Input("types", required: true)]
        public Input<string> Types { get; set; } = null!;

        public RestApiEndpointConfigurationArgs()
        {
        }
    }

    public sealed class RestApiEndpointConfigurationGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// A list of endpoint types. This resource currently only supports managing a single value. Valid values: `EDGE`, `REGIONAL` or `PRIVATE`. If unspecified, defaults to `EDGE`. Must be declared as `REGIONAL` in non-Commercial partitions. Refer to the [documentation](https://docs.aws.amazon.com/apigateway/latest/developerguide/create-regional-api.html) for more information on the difference between edge-optimized and regional APIs.
        /// </summary>
        [Input("types", required: true)]
        public Input<string> Types { get; set; } = null!;

        public RestApiEndpointConfigurationGetArgs()
        {
        }
    }
    }

    namespace Outputs
    {

    [OutputType]
    public sealed class RestApiEndpointConfiguration
    {
        /// <summary>
        /// A list of endpoint types. This resource currently only supports managing a single value. Valid values: `EDGE`, `REGIONAL` or `PRIVATE`. If unspecified, defaults to `EDGE`. Must be declared as `REGIONAL` in non-Commercial partitions. Refer to the [documentation](https://docs.aws.amazon.com/apigateway/latest/developerguide/create-regional-api.html) for more information on the difference between edge-optimized and regional APIs.
        /// </summary>
        public readonly string Types;

        [OutputConstructor]
        private RestApiEndpointConfiguration(string types)
        {
            Types = types;
        }
    }
    }
}
