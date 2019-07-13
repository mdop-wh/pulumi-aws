// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

import {RecordType} from "./recordType";

/**
 * > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/route53_record.html.markdown.
 */
export class Record extends pulumi.CustomResource {
    /**
     * Get an existing Record resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: RecordState, opts?: pulumi.CustomResourceOptions): Record {
        return new Record(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws:route53/record:Record';

    /**
     * Returns true if the given object is an instance of Record.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Record {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Record.__pulumiType;
    }

    /**
     * An alias block. Conflicts with `ttl` & `records`.
     * Alias record documented below.
     */
    public readonly aliases!: pulumi.Output<{ evaluateTargetHealth: boolean, name: string, zoneId: string }[] | undefined>;
    public readonly allowOverwrite!: pulumi.Output<boolean>;
    /**
     * A block indicating the routing behavior when associated health check fails. Conflicts with any other routing policy. Documented below.
     */
    public readonly failoverRoutingPolicies!: pulumi.Output<{ type: string }[] | undefined>;
    /**
     * [FQDN](https://en.wikipedia.org/wiki/Fully_qualified_domain_name) built using the zone domain and `name`.
     */
    public /*out*/ readonly fqdn!: pulumi.Output<string>;
    /**
     * A block indicating a routing policy based on the geolocation of the requestor. Conflicts with any other routing policy. Documented below.
     */
    public readonly geolocationRoutingPolicies!: pulumi.Output<{ continent?: string, country?: string, subdivision?: string }[] | undefined>;
    /**
     * The health check the record should be associated with.
     */
    public readonly healthCheckId!: pulumi.Output<string | undefined>;
    /**
     * A block indicating a routing policy based on the latency between the requestor and an AWS region. Conflicts with any other routing policy. Documented below.
     */
    public readonly latencyRoutingPolicies!: pulumi.Output<{ region: string }[] | undefined>;
    /**
     * Set to `true` to indicate a multivalue answer routing policy. Conflicts with any other routing policy.
     */
    public readonly multivalueAnswerRoutingPolicy!: pulumi.Output<boolean | undefined>;
    /**
     * DNS domain name for a CloudFront distribution, S3 bucket, ELB, or another resource record set in this hosted zone.
     */
    public readonly name!: pulumi.Output<string>;
    public readonly records!: pulumi.Output<string[] | undefined>;
    /**
     * Unique identifier to differentiate records with routing policies from one another. Required if using `failover`, `geolocation`, `latency`, or `weighted` routing policies documented below.
     */
    public readonly setIdentifier!: pulumi.Output<string | undefined>;
    /**
     * The TTL of the record.
     */
    public readonly ttl!: pulumi.Output<number | undefined>;
    /**
     * `PRIMARY` or `SECONDARY`. A `PRIMARY` record will be served if its healthcheck is passing, otherwise the `SECONDARY` will be served. See http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-configuring-options.html#dns-failover-failover-rrsets
     */
    public readonly type!: pulumi.Output<string>;
    /**
     * A block indicating a weighted routing policy. Conflicts with any other routing policy. Documented below.
     */
    public readonly weightedRoutingPolicies!: pulumi.Output<{ weight: number }[] | undefined>;
    /**
     * Hosted zone ID for a CloudFront distribution, S3 bucket, ELB, or Route 53 hosted zone. See [`resource_elb.zone_id`](https://www.terraform.io/docs/providers/aws/r/elb.html#zone_id) for example.
     */
    public readonly zoneId!: pulumi.Output<string>;

    /**
     * Create a Record resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: RecordArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: RecordArgs | RecordState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as RecordState | undefined;
            inputs["aliases"] = state ? state.aliases : undefined;
            inputs["allowOverwrite"] = state ? state.allowOverwrite : undefined;
            inputs["failoverRoutingPolicies"] = state ? state.failoverRoutingPolicies : undefined;
            inputs["fqdn"] = state ? state.fqdn : undefined;
            inputs["geolocationRoutingPolicies"] = state ? state.geolocationRoutingPolicies : undefined;
            inputs["healthCheckId"] = state ? state.healthCheckId : undefined;
            inputs["latencyRoutingPolicies"] = state ? state.latencyRoutingPolicies : undefined;
            inputs["multivalueAnswerRoutingPolicy"] = state ? state.multivalueAnswerRoutingPolicy : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["records"] = state ? state.records : undefined;
            inputs["setIdentifier"] = state ? state.setIdentifier : undefined;
            inputs["ttl"] = state ? state.ttl : undefined;
            inputs["type"] = state ? state.type : undefined;
            inputs["weightedRoutingPolicies"] = state ? state.weightedRoutingPolicies : undefined;
            inputs["zoneId"] = state ? state.zoneId : undefined;
        } else {
            const args = argsOrState as RecordArgs | undefined;
            if (!args || args.type === undefined) {
                throw new Error("Missing required property 'type'");
            }
            if (!args || args.zoneId === undefined) {
                throw new Error("Missing required property 'zoneId'");
            }
            inputs["aliases"] = args ? args.aliases : undefined;
            inputs["allowOverwrite"] = args ? args.allowOverwrite : undefined;
            inputs["failoverRoutingPolicies"] = args ? args.failoverRoutingPolicies : undefined;
            inputs["geolocationRoutingPolicies"] = args ? args.geolocationRoutingPolicies : undefined;
            inputs["healthCheckId"] = args ? args.healthCheckId : undefined;
            inputs["latencyRoutingPolicies"] = args ? args.latencyRoutingPolicies : undefined;
            inputs["multivalueAnswerRoutingPolicy"] = args ? args.multivalueAnswerRoutingPolicy : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["records"] = args ? args.records : undefined;
            inputs["setIdentifier"] = args ? args.setIdentifier : undefined;
            inputs["ttl"] = args ? args.ttl : undefined;
            inputs["type"] = args ? args.type : undefined;
            inputs["weightedRoutingPolicies"] = args ? args.weightedRoutingPolicies : undefined;
            inputs["zoneId"] = args ? args.zoneId : undefined;
            inputs["fqdn"] = undefined /*out*/;
        }
        super(Record.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Record resources.
 */
export interface RecordState {
    /**
     * An alias block. Conflicts with `ttl` & `records`.
     * Alias record documented below.
     */
    readonly aliases?: pulumi.Input<pulumi.Input<{ evaluateTargetHealth: pulumi.Input<boolean>, name: pulumi.Input<string>, zoneId: pulumi.Input<string> }>[]>;
    readonly allowOverwrite?: pulumi.Input<boolean>;
    /**
     * A block indicating the routing behavior when associated health check fails. Conflicts with any other routing policy. Documented below.
     */
    readonly failoverRoutingPolicies?: pulumi.Input<pulumi.Input<{ type: pulumi.Input<string> }>[]>;
    /**
     * [FQDN](https://en.wikipedia.org/wiki/Fully_qualified_domain_name) built using the zone domain and `name`.
     */
    readonly fqdn?: pulumi.Input<string>;
    /**
     * A block indicating a routing policy based on the geolocation of the requestor. Conflicts with any other routing policy. Documented below.
     */
    readonly geolocationRoutingPolicies?: pulumi.Input<pulumi.Input<{ continent?: pulumi.Input<string>, country?: pulumi.Input<string>, subdivision?: pulumi.Input<string> }>[]>;
    /**
     * The health check the record should be associated with.
     */
    readonly healthCheckId?: pulumi.Input<string>;
    /**
     * A block indicating a routing policy based on the latency between the requestor and an AWS region. Conflicts with any other routing policy. Documented below.
     */
    readonly latencyRoutingPolicies?: pulumi.Input<pulumi.Input<{ region: pulumi.Input<string> }>[]>;
    /**
     * Set to `true` to indicate a multivalue answer routing policy. Conflicts with any other routing policy.
     */
    readonly multivalueAnswerRoutingPolicy?: pulumi.Input<boolean>;
    /**
     * DNS domain name for a CloudFront distribution, S3 bucket, ELB, or another resource record set in this hosted zone.
     */
    readonly name?: pulumi.Input<string>;
    readonly records?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Unique identifier to differentiate records with routing policies from one another. Required if using `failover`, `geolocation`, `latency`, or `weighted` routing policies documented below.
     */
    readonly setIdentifier?: pulumi.Input<string>;
    /**
     * The TTL of the record.
     */
    readonly ttl?: pulumi.Input<number>;
    /**
     * `PRIMARY` or `SECONDARY`. A `PRIMARY` record will be served if its healthcheck is passing, otherwise the `SECONDARY` will be served. See http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-configuring-options.html#dns-failover-failover-rrsets
     */
    readonly type?: pulumi.Input<string | RecordType>;
    /**
     * A block indicating a weighted routing policy. Conflicts with any other routing policy. Documented below.
     */
    readonly weightedRoutingPolicies?: pulumi.Input<pulumi.Input<{ weight: pulumi.Input<number> }>[]>;
    /**
     * Hosted zone ID for a CloudFront distribution, S3 bucket, ELB, or Route 53 hosted zone. See [`resource_elb.zone_id`](https://www.terraform.io/docs/providers/aws/r/elb.html#zone_id) for example.
     */
    readonly zoneId?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a Record resource.
 */
export interface RecordArgs {
    /**
     * An alias block. Conflicts with `ttl` & `records`.
     * Alias record documented below.
     */
    readonly aliases?: pulumi.Input<pulumi.Input<{ evaluateTargetHealth: pulumi.Input<boolean>, name: pulumi.Input<string>, zoneId: pulumi.Input<string> }>[]>;
    readonly allowOverwrite?: pulumi.Input<boolean>;
    /**
     * A block indicating the routing behavior when associated health check fails. Conflicts with any other routing policy. Documented below.
     */
    readonly failoverRoutingPolicies?: pulumi.Input<pulumi.Input<{ type: pulumi.Input<string> }>[]>;
    /**
     * A block indicating a routing policy based on the geolocation of the requestor. Conflicts with any other routing policy. Documented below.
     */
    readonly geolocationRoutingPolicies?: pulumi.Input<pulumi.Input<{ continent?: pulumi.Input<string>, country?: pulumi.Input<string>, subdivision?: pulumi.Input<string> }>[]>;
    /**
     * The health check the record should be associated with.
     */
    readonly healthCheckId?: pulumi.Input<string>;
    /**
     * A block indicating a routing policy based on the latency between the requestor and an AWS region. Conflicts with any other routing policy. Documented below.
     */
    readonly latencyRoutingPolicies?: pulumi.Input<pulumi.Input<{ region: pulumi.Input<string> }>[]>;
    /**
     * Set to `true` to indicate a multivalue answer routing policy. Conflicts with any other routing policy.
     */
    readonly multivalueAnswerRoutingPolicy?: pulumi.Input<boolean>;
    /**
     * DNS domain name for a CloudFront distribution, S3 bucket, ELB, or another resource record set in this hosted zone.
     */
    readonly name?: pulumi.Input<string>;
    readonly records?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Unique identifier to differentiate records with routing policies from one another. Required if using `failover`, `geolocation`, `latency`, or `weighted` routing policies documented below.
     */
    readonly setIdentifier?: pulumi.Input<string>;
    /**
     * The TTL of the record.
     */
    readonly ttl?: pulumi.Input<number>;
    /**
     * `PRIMARY` or `SECONDARY`. A `PRIMARY` record will be served if its healthcheck is passing, otherwise the `SECONDARY` will be served. See http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-configuring-options.html#dns-failover-failover-rrsets
     */
    readonly type: pulumi.Input<string | RecordType>;
    /**
     * A block indicating a weighted routing policy. Conflicts with any other routing policy. Documented below.
     */
    readonly weightedRoutingPolicies?: pulumi.Input<pulumi.Input<{ weight: pulumi.Input<number> }>[]>;
    /**
     * Hosted zone ID for a CloudFront distribution, S3 bucket, ELB, or Route 53 hosted zone. See [`resource_elb.zone_id`](https://www.terraform.io/docs/providers/aws/r/elb.html#zone_id) for example.
     */
    readonly zoneId: pulumi.Input<string>;
}
