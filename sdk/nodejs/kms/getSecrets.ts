// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/kms_secrets.html.markdown.
 */
export function getSecrets(args: GetSecretsArgs, opts?: pulumi.InvokeOptions): Promise<GetSecretsResult> {
    return pulumi.runtime.invoke("aws:kms/getSecrets:getSecrets", {
        "secrets": args.secrets,
    }, opts);
}

/**
 * A collection of arguments for invoking getSecrets.
 */
export interface GetSecretsArgs {
    /**
     * One or more encrypted payload definitions from the KMS service. See the Secret Definitions below.
     */
    readonly secrets: { context?: {[key: string]: string}, grantTokens?: string[], name: string, payload: string }[];
}

/**
 * A collection of values returned by getSecrets.
 */
export interface GetSecretsResult {
    /**
     * Map containing each `secret` `name` as the key with its decrypted plaintext value
     */
    readonly plaintext: {[key: string]: string};
    readonly secrets: { context?: {[key: string]: string}, grantTokens?: string[], name: string, payload: string }[];
    /**
     * id is the provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
}
