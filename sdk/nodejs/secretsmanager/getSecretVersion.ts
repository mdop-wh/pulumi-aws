// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";

/**
 * Retrieve information about a Secrets Manager secret version includings its secret value. To retrieve secret metadata, see the [`aws_secretsmanager_secret` data source](/docs/providers/aws/d/secretsmanager_secret.html).
 */
export function getSecretVersion(args: GetSecretVersionArgs): Promise<GetSecretVersionResult> {
    return pulumi.runtime.invoke("aws:secretsmanager/getSecretVersion:getSecretVersion", {
        "secretId": args.secretId,
        "versionId": args.versionId,
        "versionStage": args.versionStage,
    });
}

/**
 * A collection of arguments for invoking getSecretVersion.
 */
export interface GetSecretVersionArgs {
    /**
     * Specifies the secret containing the version that you want to retrieve. You can specify either the Amazon Resource Name (ARN) or the friendly name of the secret.
     */
    readonly secretId: pulumi.Input<string>;
    /**
     * Specifies the unique identifier of the version of the secret that you want to retrieve. Overrides `version_stage`.
     */
    readonly versionId?: pulumi.Input<string>;
    /**
     * Specifies the secret version that you want to retrieve by the staging label attached to the version. Defaults to `AWSCURRENT`.
     */
    readonly versionStage?: pulumi.Input<string>;
}

/**
 * A collection of values returned by getSecretVersion.
 */
export interface GetSecretVersionResult {
    /**
     * The decrypted part of the protected secret information that was originally provided as a string.
     */
    readonly secretString: string;
    /**
     * The unique identifier of this version of the secret.
     */
    readonly versionId: string;
    readonly versionStages: string[];
}