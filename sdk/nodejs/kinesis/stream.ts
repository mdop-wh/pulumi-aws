// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Provides a Kinesis Stream resource. Amazon Kinesis is a managed service that
 * scales elastically for real-time processing of streaming big data.
 * 
 * For more details, see the [Amazon Kinesis Documentation][1].
 * 
 * ## Example Usage
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as aws from "@pulumi/aws";
 * 
 * const testStream = new aws.kinesis.Stream("test_stream", {
 *     retentionPeriod: 48,
 *     shardCount: 1,
 *     shardLevelMetrics: [
 *         "IncomingBytes",
 *         "OutgoingBytes",
 *     ],
 *     tags: {
 *         Environment: "test",
 *     },
 * });
 * ```
 */
export class Stream extends pulumi.CustomResource {
    /**
     * Get an existing Stream resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: StreamState, opts?: pulumi.CustomResourceOptions): Stream {
        return new Stream(name, <any>state, { ...opts, id: id });
    }

    /**
     * The Amazon Resource Name (ARN) specifying the Stream (same as `id`)
     */
    public readonly arn!: pulumi.Output<string>;
    /**
     * The encryption type to use. The only acceptable values are `NONE` or `KMS`. The default value is `NONE`.
     */
    public readonly encryptionType!: pulumi.Output<string | undefined>;
    /**
     * A boolean that indicates all registered consumers should be deregistered from the stream so that the stream can be destroyed without error. The default value is `false`.
     */
    public readonly enforceConsumerDeletion!: pulumi.Output<boolean | undefined>;
    /**
     * The GUID for the customer-managed KMS key to use for encryption. You can also use a Kinesis-owned master key by specifying the alias `alias/aws/kinesis`.
     */
    public readonly kmsKeyId!: pulumi.Output<string | undefined>;
    /**
     * A name to identify the stream. This is unique to the
     * AWS account and region the Stream is created in.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * Length of time data records are accessible after they are added to the stream. The maximum value of a stream's retention period is 168 hours. Minimum value is 24. Default is 24.
     */
    public readonly retentionPeriod!: pulumi.Output<number | undefined>;
    /**
     * The number of shards that the stream will use.
     * Amazon has guidlines for specifying the Stream size that should be referenced
     * when creating a Kinesis stream. See [Amazon Kinesis Streams][2] for more.
     */
    public readonly shardCount!: pulumi.Output<number>;
    /**
     * A list of shard-level CloudWatch metrics which can be enabled for the stream. See [Monitoring with CloudWatch][3] for more. Note that the value ALL should not be used; instead you should provide an explicit list of metrics you wish to enable.
     */
    public readonly shardLevelMetrics!: pulumi.Output<string[] | undefined>;
    /**
     * A mapping of tags to assign to the resource.
     */
    public readonly tags!: pulumi.Output<{[key: string]: any} | undefined>;

    /**
     * Create a Stream resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: StreamArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: StreamArgs | StreamState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as StreamState | undefined;
            inputs["arn"] = state ? state.arn : undefined;
            inputs["encryptionType"] = state ? state.encryptionType : undefined;
            inputs["enforceConsumerDeletion"] = state ? state.enforceConsumerDeletion : undefined;
            inputs["kmsKeyId"] = state ? state.kmsKeyId : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["retentionPeriod"] = state ? state.retentionPeriod : undefined;
            inputs["shardCount"] = state ? state.shardCount : undefined;
            inputs["shardLevelMetrics"] = state ? state.shardLevelMetrics : undefined;
            inputs["tags"] = state ? state.tags : undefined;
        } else {
            const args = argsOrState as StreamArgs | undefined;
            if (!args || args.shardCount === undefined) {
                throw new Error("Missing required property 'shardCount'");
            }
            inputs["arn"] = args ? args.arn : undefined;
            inputs["encryptionType"] = args ? args.encryptionType : undefined;
            inputs["enforceConsumerDeletion"] = args ? args.enforceConsumerDeletion : undefined;
            inputs["kmsKeyId"] = args ? args.kmsKeyId : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["retentionPeriod"] = args ? args.retentionPeriod : undefined;
            inputs["shardCount"] = args ? args.shardCount : undefined;
            inputs["shardLevelMetrics"] = args ? args.shardLevelMetrics : undefined;
            inputs["tags"] = args ? args.tags : undefined;
        }
        super("aws:kinesis/stream:Stream", name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Stream resources.
 */
export interface StreamState {
    /**
     * The Amazon Resource Name (ARN) specifying the Stream (same as `id`)
     */
    readonly arn?: pulumi.Input<string>;
    /**
     * The encryption type to use. The only acceptable values are `NONE` or `KMS`. The default value is `NONE`.
     */
    readonly encryptionType?: pulumi.Input<string>;
    /**
     * A boolean that indicates all registered consumers should be deregistered from the stream so that the stream can be destroyed without error. The default value is `false`.
     */
    readonly enforceConsumerDeletion?: pulumi.Input<boolean>;
    /**
     * The GUID for the customer-managed KMS key to use for encryption. You can also use a Kinesis-owned master key by specifying the alias `alias/aws/kinesis`.
     */
    readonly kmsKeyId?: pulumi.Input<string>;
    /**
     * A name to identify the stream. This is unique to the
     * AWS account and region the Stream is created in.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * Length of time data records are accessible after they are added to the stream. The maximum value of a stream's retention period is 168 hours. Minimum value is 24. Default is 24.
     */
    readonly retentionPeriod?: pulumi.Input<number>;
    /**
     * The number of shards that the stream will use.
     * Amazon has guidlines for specifying the Stream size that should be referenced
     * when creating a Kinesis stream. See [Amazon Kinesis Streams][2] for more.
     */
    readonly shardCount?: pulumi.Input<number>;
    /**
     * A list of shard-level CloudWatch metrics which can be enabled for the stream. See [Monitoring with CloudWatch][3] for more. Note that the value ALL should not be used; instead you should provide an explicit list of metrics you wish to enable.
     */
    readonly shardLevelMetrics?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * A mapping of tags to assign to the resource.
     */
    readonly tags?: pulumi.Input<{[key: string]: any}>;
}

/**
 * The set of arguments for constructing a Stream resource.
 */
export interface StreamArgs {
    /**
     * The Amazon Resource Name (ARN) specifying the Stream (same as `id`)
     */
    readonly arn?: pulumi.Input<string>;
    /**
     * The encryption type to use. The only acceptable values are `NONE` or `KMS`. The default value is `NONE`.
     */
    readonly encryptionType?: pulumi.Input<string>;
    /**
     * A boolean that indicates all registered consumers should be deregistered from the stream so that the stream can be destroyed without error. The default value is `false`.
     */
    readonly enforceConsumerDeletion?: pulumi.Input<boolean>;
    /**
     * The GUID for the customer-managed KMS key to use for encryption. You can also use a Kinesis-owned master key by specifying the alias `alias/aws/kinesis`.
     */
    readonly kmsKeyId?: pulumi.Input<string>;
    /**
     * A name to identify the stream. This is unique to the
     * AWS account and region the Stream is created in.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * Length of time data records are accessible after they are added to the stream. The maximum value of a stream's retention period is 168 hours. Minimum value is 24. Default is 24.
     */
    readonly retentionPeriod?: pulumi.Input<number>;
    /**
     * The number of shards that the stream will use.
     * Amazon has guidlines for specifying the Stream size that should be referenced
     * when creating a Kinesis stream. See [Amazon Kinesis Streams][2] for more.
     */
    readonly shardCount: pulumi.Input<number>;
    /**
     * A list of shard-level CloudWatch metrics which can be enabled for the stream. See [Monitoring with CloudWatch][3] for more. Note that the value ALL should not be used; instead you should provide an explicit list of metrics you wish to enable.
     */
    readonly shardLevelMetrics?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * A mapping of tags to assign to the resource.
     */
    readonly tags?: pulumi.Input<{[key: string]: any}>;
}
