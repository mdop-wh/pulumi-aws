// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

import {Bucket} from "../s3/bucket";
import {Application} from "./application";

/**
 * Provides an Elastic Beanstalk Application Version Resource. Elastic Beanstalk allows
 * you to deploy and manage applications in the AWS cloud without worrying about
 * the infrastructure that runs those applications.
 * 
 * This resource creates a Beanstalk Application Version that can be deployed to a Beanstalk
 * Environment.
 * 
 * > **NOTE on Application Version Resource:**  When using the Application Version resource with multiple 
 * Elastic Beanstalk Environments it is possible that an error may be returned
 * when attempting to delete an Application Version while it is still in use by a different environment.
 * To work around this you can:
 * <ol>
 * <li>Create each environment in a separate AWS account</li>
 * <li>Create your `aws.elasticbeanstalk.ApplicationVersion` resources with a unique names in your 
 * Elastic Beanstalk Application. For example &lt;revision&gt;-&lt;environment&gt;.</li>
 * </ol>
 * 
 * ## Example Usage
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as aws from "@pulumi/aws";
 * 
 * const defaultApplication = new aws.elasticbeanstalk.Application("default", {
 *     description: "tf-test-desc",
 * });
 * const defaultBucket = new aws.s3.Bucket("default", {});
 * const defaultBucketObject = new aws.s3.BucketObject("default", {
 *     bucket: defaultBucket.id,
 *     key: "beanstalk/go-v1.zip",
 *     source: new pulumi.asset.FileAsset("go-v1.zip"),
 * });
 * const defaultApplicationVersion = new aws.elasticbeanstalk.ApplicationVersion("default", {
 *     application: "tf-test-name",
 *     bucket: defaultBucket.id,
 *     description: "application version",
 *     key: defaultBucketObject.id,
 * });
 * ```
 *
 * > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/elastic_beanstalk_application_version.html.markdown.
 */
export class ApplicationVersion extends pulumi.CustomResource {
    /**
     * Get an existing ApplicationVersion resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ApplicationVersionState, opts?: pulumi.CustomResourceOptions): ApplicationVersion {
        return new ApplicationVersion(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws:elasticbeanstalk/applicationVersion:ApplicationVersion';

    /**
     * Returns true if the given object is an instance of ApplicationVersion.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is ApplicationVersion {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === ApplicationVersion.__pulumiType;
    }

    /**
     * Name of the Beanstalk Application the version is associated with.
     */
    public readonly application!: pulumi.Output<Application>;
    /**
     * The ARN assigned by AWS for this Elastic Beanstalk Application.
     */
    public /*out*/ readonly arn!: pulumi.Output<string>;
    /**
     * S3 bucket that contains the Application Version source bundle.
     */
    public readonly bucket!: pulumi.Output<string>;
    /**
     * Short description of the Application Version.
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * On delete, force an Application Version to be deleted when it may be in use
     * by multiple Elastic Beanstalk Environments.
     */
    public readonly forceDelete!: pulumi.Output<boolean | undefined>;
    /**
     * S3 object that is the Application Version source bundle.
     */
    public readonly key!: pulumi.Output<string>;
    /**
     * A unique name for the this Application Version.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * Key-value mapping of tags for the Elastic Beanstalk Application Version.
     */
    public readonly tags!: pulumi.Output<{[key: string]: any} | undefined>;

    /**
     * Create a ApplicationVersion resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ApplicationVersionArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: ApplicationVersionArgs | ApplicationVersionState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as ApplicationVersionState | undefined;
            inputs["application"] = state ? state.application : undefined;
            inputs["arn"] = state ? state.arn : undefined;
            inputs["bucket"] = state ? state.bucket : undefined;
            inputs["description"] = state ? state.description : undefined;
            inputs["forceDelete"] = state ? state.forceDelete : undefined;
            inputs["key"] = state ? state.key : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["tags"] = state ? state.tags : undefined;
        } else {
            const args = argsOrState as ApplicationVersionArgs | undefined;
            if (!args || args.application === undefined) {
                throw new Error("Missing required property 'application'");
            }
            if (!args || args.bucket === undefined) {
                throw new Error("Missing required property 'bucket'");
            }
            if (!args || args.key === undefined) {
                throw new Error("Missing required property 'key'");
            }
            inputs["application"] = args ? args.application : undefined;
            inputs["bucket"] = args ? args.bucket : undefined;
            inputs["description"] = args ? args.description : undefined;
            inputs["forceDelete"] = args ? args.forceDelete : undefined;
            inputs["key"] = args ? args.key : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["arn"] = undefined /*out*/;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(ApplicationVersion.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering ApplicationVersion resources.
 */
export interface ApplicationVersionState {
    /**
     * Name of the Beanstalk Application the version is associated with.
     */
    readonly application?: pulumi.Input<Application>;
    /**
     * The ARN assigned by AWS for this Elastic Beanstalk Application.
     */
    readonly arn?: pulumi.Input<string>;
    /**
     * S3 bucket that contains the Application Version source bundle.
     */
    readonly bucket?: pulumi.Input<string | Bucket>;
    /**
     * Short description of the Application Version.
     */
    readonly description?: pulumi.Input<string>;
    /**
     * On delete, force an Application Version to be deleted when it may be in use
     * by multiple Elastic Beanstalk Environments.
     */
    readonly forceDelete?: pulumi.Input<boolean>;
    /**
     * S3 object that is the Application Version source bundle.
     */
    readonly key?: pulumi.Input<string>;
    /**
     * A unique name for the this Application Version.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * Key-value mapping of tags for the Elastic Beanstalk Application Version.
     */
    readonly tags?: pulumi.Input<{[key: string]: any}>;
}

/**
 * The set of arguments for constructing a ApplicationVersion resource.
 */
export interface ApplicationVersionArgs {
    /**
     * Name of the Beanstalk Application the version is associated with.
     */
    readonly application: pulumi.Input<Application>;
    /**
     * S3 bucket that contains the Application Version source bundle.
     */
    readonly bucket: pulumi.Input<string | Bucket>;
    /**
     * Short description of the Application Version.
     */
    readonly description?: pulumi.Input<string>;
    /**
     * On delete, force an Application Version to be deleted when it may be in use
     * by multiple Elastic Beanstalk Environments.
     */
    readonly forceDelete?: pulumi.Input<boolean>;
    /**
     * S3 object that is the Application Version source bundle.
     */
    readonly key: pulumi.Input<string>;
    /**
     * A unique name for the this Application Version.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * Key-value mapping of tags for the Elastic Beanstalk Application Version.
     */
    readonly tags?: pulumi.Input<{[key: string]: any}>;
}
