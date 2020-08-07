// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * Provides details about an Outposts Site.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as aws from "@pulumi/aws";
 *
 * const example = pulumi.output(aws.outposts.getSite({
 *     name: "example",
 * }, { async: true }));
 * ```
 */
export function getSite(args?: GetSiteArgs, opts?: pulumi.InvokeOptions): Promise<GetSiteResult> {
    args = args || {};
    if (!opts) {
        opts = {}
    }

    if (!opts.version) {
        opts.version = utilities.getVersion();
    }
    return pulumi.runtime.invoke("aws:outposts/getSite:getSite", {
        "id": args.id,
        "name": args.name,
    }, opts);
}

/**
 * A collection of arguments for invoking getSite.
 */
export interface GetSiteArgs {
    /**
     * Identifier of the Site.
     */
    readonly id?: string;
    /**
     * Name of the Site.
     */
    readonly name?: string;
}

/**
 * A collection of values returned by getSite.
 */
export interface GetSiteResult {
    /**
     * AWS Account identifier.
     */
    readonly accountId: string;
    /**
     * Description.
     */
    readonly description: string;
    readonly id: string;
    readonly name: string;
}