// Copyright 2016-2017, Pulumi Corporation.  All rights reserved.

import * as crypto from "crypto";
import * as pulumi from "@pulumi/pulumi";
import { Role, RolePolicyAttachment } from "../iam";
import * as lambda from "../lambda";
import { ARN } from "../arn";

/**
 * Context is the shape of the context object passed to a Function callback.
 */
export interface Context {
    callbackWaitsForEmptyEventLoop: boolean;
    readonly functionName: string;
    readonly functionVersion: string;
    readonly invokedFunctionArn: string;
    readonly memoryLimitInMB: string;
    readonly awsRequestId: string;
    readonly logGroupName: string;
    readonly logStreamName: string;
    readonly identity: any;
    readonly clientContext: any;
    getRemainingTimeInMillis(): string;
}

/**
 * Handler is the signature for a serverless function.
 */
export type Handler = (event: any, context: Context, callback: (error: any, result: any) => void) => any;

export interface FunctionOptions {
    policies: ARN[];
    timeout?: number;
    memorySize?: number;
    runtime?: lambda.Runtime;
    deadLetterConfig?: { targetArn: pulumi.Input<string>; };
    vpcConfig?: {
        securityGroupIds: pulumi.Input<string[]>,
        subnetIds: pulumi.Input<string[]>,
    };
}

/**
 * Function is a higher-level API for creating and managing AWS Lambda Function resources implemented
 * by a Lumi lambda expression and with a set of attached policies.
 */
export class Function extends pulumi.ComponentResource {
    public readonly options: FunctionOptions;
    public readonly lambda: lambda.Function;
    public readonly role: Role;
    public readonly policies: RolePolicyAttachment[];

    constructor(name: string,
                options: FunctionOptions,
                func: Handler,
                opts?: pulumi.ResourceOptions,
                serialize?: (obj: any) => boolean) {
        if (!name) {
            throw new Error("Missing required resource name");
        }
        if (!func) {
            throw new Error("Missing required function callback");
        }

        super("aws:serverless:Function", name, { options: options }, opts);

        // Attach a role and then, if there are policies, attach those too.
        this.role = new Role(name, {
            assumeRolePolicy: JSON.stringify(lambdaRolePolicy),
        }, { parent: this });

        this.policies = [];
        for (let policy of options.policies) {
            // RolePolicyAttachment objects don't have a phyiscal identity, and create/deletes are processed
            // structurally based on the `role` and `policyArn`.  So we need to make sure our Pulumi name matches the
            // structural identity by using a name that includes the role name and policyArn.
            let attachment = new RolePolicyAttachment(`${name}-${sha1hash(policy)}`, {
                role: this.role,
                policyArn: policy,
            }, { parent: this });
            this.policies.push(attachment);
        }

        // Now compile the function text into an asset we can use to create the lambda. Note: to
        // prevent a circularity/deadlock, we list this Function object as something that the
        // serialized closure cannot reference.
        serialize = serialize || (_ => true);
        const finalSerialize = (o: any) => {
            return serialize(o) && o !== this;
        }

        let closure = pulumi.runtime.serializeFunctionAsync(func, finalSerialize);
        if (!closure) {
            throw new Error("Failed to serialize function closure");
        }

        // console.log("Making function: " + name);
        this.lambda = new lambda.Function(name, {
            code: new pulumi.asset.AssetArchive({
                // TODO[pulumi/pulumi-aws#35] We may want to allow users to control what gets uploaded. Currently, we
                //     upload the entire folder as there may be dependencies on any files here.
                ".": new pulumi.asset.FileArchive("."),
                "__index.js": new pulumi.asset.StringAsset(closure),
            }),
            handler: "__index.handler",
            runtime: options.runtime || lambda.NodeJS8d10Runtime,
            role: this.role.arn,
            timeout: options.timeout === undefined ? 180 : options.timeout,
            memorySize: options.memorySize,
            deadLetterConfig: options.deadLetterConfig,
            vpcConfig: options.vpcConfig,
        }, { parent: this });
    }
}

const lambdaRolePolicy = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Action": "sts:AssumeRole",
            "Principal": {
                "Service": "lambda.amazonaws.com",
            },
            "Effect": "Allow",
            "Sid": "",
        },
    ],
};

// sha1hash returns a partial SHA1 hash of the input string.
function sha1hash(s: string): string {
    const shasum: crypto.Hash = crypto.createHash("sha1");
    shasum.update(s);
    return shasum.digest("hex").substring(0, 8);
}