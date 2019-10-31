// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.Appsync
{
    /// <summary>
    /// Provides an AppSync DataSource.
    /// 
    /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/appsync_datasource.html.markdown.
    /// </summary>
    public partial class DataSource : Pulumi.CustomResource
    {
        /// <summary>
        /// The API ID for the GraphQL API for the DataSource.
        /// </summary>
        [Output("apiId")]
        public Output<string> ApiId { get; private set; } = null!;

        /// <summary>
        /// The ARN
        /// </summary>
        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        /// <summary>
        /// A description of the DataSource.
        /// </summary>
        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        /// <summary>
        /// DynamoDB settings. See below
        /// </summary>
        [Output("dynamodbConfig")]
        public Output<Outputs.DataSourceDynamodbConfig?> DynamodbConfig { get; private set; } = null!;

        /// <summary>
        /// Amazon Elasticsearch settings. See below
        /// </summary>
        [Output("elasticsearchConfig")]
        public Output<Outputs.DataSourceElasticsearchConfig?> ElasticsearchConfig { get; private set; } = null!;

        /// <summary>
        /// HTTP settings. See below
        /// </summary>
        [Output("httpConfig")]
        public Output<Outputs.DataSourceHttpConfig?> HttpConfig { get; private set; } = null!;

        /// <summary>
        /// AWS Lambda settings. See below
        /// </summary>
        [Output("lambdaConfig")]
        public Output<Outputs.DataSourceLambdaConfig?> LambdaConfig { get; private set; } = null!;

        /// <summary>
        /// A user-supplied name for the DataSource.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// The IAM service role ARN for the data source.
        /// </summary>
        [Output("serviceRoleArn")]
        public Output<string?> ServiceRoleArn { get; private set; } = null!;

        /// <summary>
        /// The type of the DataSource. Valid values: `AWS_LAMBDA`, `AMAZON_DYNAMODB`, `AMAZON_ELASTICSEARCH`, `HTTP`, `NONE`.
        /// </summary>
        [Output("type")]
        public Output<string> Type { get; private set; } = null!;


        /// <summary>
        /// Create a DataSource resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public DataSource(string name, DataSourceArgs args, CustomResourceOptions? options = null)
            : base("aws:appsync/dataSource:DataSource", name, args, MakeResourceOptions(options, ""))
        {
        }

        private DataSource(string name, Input<string> id, DataSourceState? state = null, CustomResourceOptions? options = null)
            : base("aws:appsync/dataSource:DataSource", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing DataSource resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static DataSource Get(string name, Input<string> id, DataSourceState? state = null, CustomResourceOptions? options = null)
        {
            return new DataSource(name, id, state, options);
        }
    }

    public sealed class DataSourceArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The API ID for the GraphQL API for the DataSource.
        /// </summary>
        [Input("apiId", required: true)]
        public Input<string> ApiId { get; set; } = null!;

        /// <summary>
        /// A description of the DataSource.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// DynamoDB settings. See below
        /// </summary>
        [Input("dynamodbConfig")]
        public Input<Inputs.DataSourceDynamodbConfigArgs>? DynamodbConfig { get; set; }

        /// <summary>
        /// Amazon Elasticsearch settings. See below
        /// </summary>
        [Input("elasticsearchConfig")]
        public Input<Inputs.DataSourceElasticsearchConfigArgs>? ElasticsearchConfig { get; set; }

        /// <summary>
        /// HTTP settings. See below
        /// </summary>
        [Input("httpConfig")]
        public Input<Inputs.DataSourceHttpConfigArgs>? HttpConfig { get; set; }

        /// <summary>
        /// AWS Lambda settings. See below
        /// </summary>
        [Input("lambdaConfig")]
        public Input<Inputs.DataSourceLambdaConfigArgs>? LambdaConfig { get; set; }

        /// <summary>
        /// A user-supplied name for the DataSource.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The IAM service role ARN for the data source.
        /// </summary>
        [Input("serviceRoleArn")]
        public Input<string>? ServiceRoleArn { get; set; }

        /// <summary>
        /// The type of the DataSource. Valid values: `AWS_LAMBDA`, `AMAZON_DYNAMODB`, `AMAZON_ELASTICSEARCH`, `HTTP`, `NONE`.
        /// </summary>
        [Input("type", required: true)]
        public Input<string> Type { get; set; } = null!;

        public DataSourceArgs()
        {
        }
    }

    public sealed class DataSourceState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The API ID for the GraphQL API for the DataSource.
        /// </summary>
        [Input("apiId")]
        public Input<string>? ApiId { get; set; }

        /// <summary>
        /// The ARN
        /// </summary>
        [Input("arn")]
        public Input<string>? Arn { get; set; }

        /// <summary>
        /// A description of the DataSource.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// DynamoDB settings. See below
        /// </summary>
        [Input("dynamodbConfig")]
        public Input<Inputs.DataSourceDynamodbConfigGetArgs>? DynamodbConfig { get; set; }

        /// <summary>
        /// Amazon Elasticsearch settings. See below
        /// </summary>
        [Input("elasticsearchConfig")]
        public Input<Inputs.DataSourceElasticsearchConfigGetArgs>? ElasticsearchConfig { get; set; }

        /// <summary>
        /// HTTP settings. See below
        /// </summary>
        [Input("httpConfig")]
        public Input<Inputs.DataSourceHttpConfigGetArgs>? HttpConfig { get; set; }

        /// <summary>
        /// AWS Lambda settings. See below
        /// </summary>
        [Input("lambdaConfig")]
        public Input<Inputs.DataSourceLambdaConfigGetArgs>? LambdaConfig { get; set; }

        /// <summary>
        /// A user-supplied name for the DataSource.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The IAM service role ARN for the data source.
        /// </summary>
        [Input("serviceRoleArn")]
        public Input<string>? ServiceRoleArn { get; set; }

        /// <summary>
        /// The type of the DataSource. Valid values: `AWS_LAMBDA`, `AMAZON_DYNAMODB`, `AMAZON_ELASTICSEARCH`, `HTTP`, `NONE`.
        /// </summary>
        [Input("type")]
        public Input<string>? Type { get; set; }

        public DataSourceState()
        {
        }
    }

    namespace Inputs
    {

    public sealed class DataSourceDynamodbConfigArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// AWS region of Elasticsearch domain. Defaults to current region.
        /// </summary>
        [Input("region")]
        public Input<string>? Region { get; set; }

        /// <summary>
        /// Name of the DynamoDB table.
        /// </summary>
        [Input("tableName", required: true)]
        public Input<string> TableName { get; set; } = null!;

        /// <summary>
        /// Set to `true` to use Amazon Cognito credentials with this data source.
        /// </summary>
        [Input("useCallerCredentials")]
        public Input<bool>? UseCallerCredentials { get; set; }

        public DataSourceDynamodbConfigArgs()
        {
        }
    }

    public sealed class DataSourceDynamodbConfigGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// AWS region of Elasticsearch domain. Defaults to current region.
        /// </summary>
        [Input("region")]
        public Input<string>? Region { get; set; }

        /// <summary>
        /// Name of the DynamoDB table.
        /// </summary>
        [Input("tableName", required: true)]
        public Input<string> TableName { get; set; } = null!;

        /// <summary>
        /// Set to `true` to use Amazon Cognito credentials with this data source.
        /// </summary>
        [Input("useCallerCredentials")]
        public Input<bool>? UseCallerCredentials { get; set; }

        public DataSourceDynamodbConfigGetArgs()
        {
        }
    }

    public sealed class DataSourceElasticsearchConfigArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// HTTP URL.
        /// </summary>
        [Input("endpoint", required: true)]
        public Input<string> Endpoint { get; set; } = null!;

        /// <summary>
        /// AWS region of Elasticsearch domain. Defaults to current region.
        /// </summary>
        [Input("region")]
        public Input<string>? Region { get; set; }

        public DataSourceElasticsearchConfigArgs()
        {
        }
    }

    public sealed class DataSourceElasticsearchConfigGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// HTTP URL.
        /// </summary>
        [Input("endpoint", required: true)]
        public Input<string> Endpoint { get; set; } = null!;

        /// <summary>
        /// AWS region of Elasticsearch domain. Defaults to current region.
        /// </summary>
        [Input("region")]
        public Input<string>? Region { get; set; }

        public DataSourceElasticsearchConfigGetArgs()
        {
        }
    }

    public sealed class DataSourceHttpConfigArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// HTTP URL.
        /// </summary>
        [Input("endpoint", required: true)]
        public Input<string> Endpoint { get; set; } = null!;

        public DataSourceHttpConfigArgs()
        {
        }
    }

    public sealed class DataSourceHttpConfigGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// HTTP URL.
        /// </summary>
        [Input("endpoint", required: true)]
        public Input<string> Endpoint { get; set; } = null!;

        public DataSourceHttpConfigGetArgs()
        {
        }
    }

    public sealed class DataSourceLambdaConfigArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The ARN for the Lambda function.
        /// </summary>
        [Input("functionArn", required: true)]
        public Input<string> FunctionArn { get; set; } = null!;

        public DataSourceLambdaConfigArgs()
        {
        }
    }

    public sealed class DataSourceLambdaConfigGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The ARN for the Lambda function.
        /// </summary>
        [Input("functionArn", required: true)]
        public Input<string> FunctionArn { get; set; } = null!;

        public DataSourceLambdaConfigGetArgs()
        {
        }
    }
    }

    namespace Outputs
    {

    [OutputType]
    public sealed class DataSourceDynamodbConfig
    {
        /// <summary>
        /// AWS region of Elasticsearch domain. Defaults to current region.
        /// </summary>
        public readonly string Region;
        /// <summary>
        /// Name of the DynamoDB table.
        /// </summary>
        public readonly string TableName;
        /// <summary>
        /// Set to `true` to use Amazon Cognito credentials with this data source.
        /// </summary>
        public readonly bool? UseCallerCredentials;

        [OutputConstructor]
        private DataSourceDynamodbConfig(
            string region,
            string tableName,
            bool? useCallerCredentials)
        {
            Region = region;
            TableName = tableName;
            UseCallerCredentials = useCallerCredentials;
        }
    }

    [OutputType]
    public sealed class DataSourceElasticsearchConfig
    {
        /// <summary>
        /// HTTP URL.
        /// </summary>
        public readonly string Endpoint;
        /// <summary>
        /// AWS region of Elasticsearch domain. Defaults to current region.
        /// </summary>
        public readonly string Region;

        [OutputConstructor]
        private DataSourceElasticsearchConfig(
            string endpoint,
            string region)
        {
            Endpoint = endpoint;
            Region = region;
        }
    }

    [OutputType]
    public sealed class DataSourceHttpConfig
    {
        /// <summary>
        /// HTTP URL.
        /// </summary>
        public readonly string Endpoint;

        [OutputConstructor]
        private DataSourceHttpConfig(string endpoint)
        {
            Endpoint = endpoint;
        }
    }

    [OutputType]
    public sealed class DataSourceLambdaConfig
    {
        /// <summary>
        /// The ARN for the Lambda function.
        /// </summary>
        public readonly string FunctionArn;

        [OutputConstructor]
        private DataSourceLambdaConfig(string functionArn)
        {
            FunctionArn = functionArn;
        }
    }
    }
}
