// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Manages a Glue Trigger resource.
 * 
 * ## Example Usage
 * 
 * ### Conditional Trigger
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as aws from "@pulumi/aws";
 * 
 * const example = new aws.glue.Trigger("example", {
 *     actions: [{
 *         jobName: aws_glue_job_example1.name,
 *     }],
 *     predicate: {
 *         conditions: [{
 *             jobName: aws_glue_job_example2.name,
 *             state: "SUCCEEDED",
 *         }],
 *     },
 *     type: "CONDITIONAL",
 * });
 * ```
 * 
 * ### On-Demand Trigger
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as aws from "@pulumi/aws";
 * 
 * const example = new aws.glue.Trigger("example", {
 *     actions: [{
 *         jobName: aws_glue_job_example.name,
 *     }],
 *     type: "ON_DEMAND",
 * });
 * ```
 * 
 * ### Scheduled Trigger
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as aws from "@pulumi/aws";
 * 
 * const example = new aws.glue.Trigger("example", {
 *     actions: [{
 *         jobName: aws_glue_job_example.name,
 *     }],
 *     schedule: "cron(15 12 * * ? *)",
 *     type: "SCHEDULED",
 * });
 * ```
 */
export class Trigger extends pulumi.CustomResource {
    /**
     * Get an existing Trigger resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: TriggerState, opts?: pulumi.CustomResourceOptions): Trigger {
        return new Trigger(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws:glue/trigger:Trigger';

    /**
     * Returns true if the given object is an instance of Trigger.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Trigger {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Trigger.__pulumiType;
    }

    /**
     * List of actions initiated by this trigger when it fires. Defined below.
     */
    public readonly actions!: pulumi.Output<{ arguments?: {[key: string]: any}, jobName: string, timeout?: number }[]>;
    /**
     * A description of the new trigger.
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * Start the trigger. Defaults to `true`. Not valid to disable for `ON_DEMAND` type.
     */
    public readonly enabled!: pulumi.Output<boolean | undefined>;
    /**
     * The name of the trigger.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * A predicate to specify when the new trigger should fire. Required when trigger type is `CONDITIONAL`. Defined below.
     */
    public readonly predicate!: pulumi.Output<{ conditions: { jobName: string, logicalOperator?: string, state: string }[], logical?: string } | undefined>;
    /**
     * A cron expression used to specify the schedule. [Time-Based Schedules for Jobs and Crawlers](https://docs.aws.amazon.com/glue/latest/dg/monitor-data-warehouse-schedule.html)
     */
    public readonly schedule!: pulumi.Output<string | undefined>;
    /**
     * The type of trigger. Valid values are `CONDITIONAL`, `ON_DEMAND`, and `SCHEDULED`.
     */
    public readonly type!: pulumi.Output<string>;

    /**
     * Create a Trigger resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: TriggerArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: TriggerArgs | TriggerState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as TriggerState | undefined;
            inputs["actions"] = state ? state.actions : undefined;
            inputs["description"] = state ? state.description : undefined;
            inputs["enabled"] = state ? state.enabled : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["predicate"] = state ? state.predicate : undefined;
            inputs["schedule"] = state ? state.schedule : undefined;
            inputs["type"] = state ? state.type : undefined;
        } else {
            const args = argsOrState as TriggerArgs | undefined;
            if (!args || args.actions === undefined) {
                throw new Error("Missing required property 'actions'");
            }
            if (!args || args.type === undefined) {
                throw new Error("Missing required property 'type'");
            }
            inputs["actions"] = args ? args.actions : undefined;
            inputs["description"] = args ? args.description : undefined;
            inputs["enabled"] = args ? args.enabled : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["predicate"] = args ? args.predicate : undefined;
            inputs["schedule"] = args ? args.schedule : undefined;
            inputs["type"] = args ? args.type : undefined;
        }
        super(Trigger.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Trigger resources.
 */
export interface TriggerState {
    /**
     * List of actions initiated by this trigger when it fires. Defined below.
     */
    readonly actions?: pulumi.Input<pulumi.Input<{ arguments?: pulumi.Input<{[key: string]: any}>, jobName: pulumi.Input<string>, timeout?: pulumi.Input<number> }>[]>;
    /**
     * A description of the new trigger.
     */
    readonly description?: pulumi.Input<string>;
    /**
     * Start the trigger. Defaults to `true`. Not valid to disable for `ON_DEMAND` type.
     */
    readonly enabled?: pulumi.Input<boolean>;
    /**
     * The name of the trigger.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * A predicate to specify when the new trigger should fire. Required when trigger type is `CONDITIONAL`. Defined below.
     */
    readonly predicate?: pulumi.Input<{ conditions: pulumi.Input<pulumi.Input<{ jobName: pulumi.Input<string>, logicalOperator?: pulumi.Input<string>, state: pulumi.Input<string> }>[]>, logical?: pulumi.Input<string> }>;
    /**
     * A cron expression used to specify the schedule. [Time-Based Schedules for Jobs and Crawlers](https://docs.aws.amazon.com/glue/latest/dg/monitor-data-warehouse-schedule.html)
     */
    readonly schedule?: pulumi.Input<string>;
    /**
     * The type of trigger. Valid values are `CONDITIONAL`, `ON_DEMAND`, and `SCHEDULED`.
     */
    readonly type?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a Trigger resource.
 */
export interface TriggerArgs {
    /**
     * List of actions initiated by this trigger when it fires. Defined below.
     */
    readonly actions: pulumi.Input<pulumi.Input<{ arguments?: pulumi.Input<{[key: string]: any}>, jobName: pulumi.Input<string>, timeout?: pulumi.Input<number> }>[]>;
    /**
     * A description of the new trigger.
     */
    readonly description?: pulumi.Input<string>;
    /**
     * Start the trigger. Defaults to `true`. Not valid to disable for `ON_DEMAND` type.
     */
    readonly enabled?: pulumi.Input<boolean>;
    /**
     * The name of the trigger.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * A predicate to specify when the new trigger should fire. Required when trigger type is `CONDITIONAL`. Defined below.
     */
    readonly predicate?: pulumi.Input<{ conditions: pulumi.Input<pulumi.Input<{ jobName: pulumi.Input<string>, logicalOperator?: pulumi.Input<string>, state: pulumi.Input<string> }>[]>, logical?: pulumi.Input<string> }>;
    /**
     * A cron expression used to specify the schedule. [Time-Based Schedules for Jobs and Crawlers](https://docs.aws.amazon.com/glue/latest/dg/monitor-data-warehouse-schedule.html)
     */
    readonly schedule?: pulumi.Input<string>;
    /**
     * The type of trigger. Valid values are `CONDITIONAL`, `ON_DEMAND`, and `SCHEDULED`.
     */
    readonly type: pulumi.Input<string>;
}
