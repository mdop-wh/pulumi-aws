// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Use this data source to get information about a DB Snapshot for use when provisioning DB instances
 * 
 * > **NOTE:** This data source does not apply to snapshots created on Aurora DB clusters.
 * See the [`aws_db_cluster_snapshot` data source](https://www.terraform.io/docs/providers/aws/d/db_cluster_snapshot.html) for DB Cluster snapshots.
 * 
 * ## Example Usage
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as aws from "@pulumi/aws";
 * 
 * const prod = new aws.rds.Instance("prod", {
 *     allocatedStorage: 10,
 *     dbSubnetGroupName: "my_database_subnet_group",
 *     engine: "mysql",
 *     engineVersion: "5.6.17",
 *     instanceClass: "db.t2.micro",
 *     name: "mydb",
 *     parameterGroupName: "default.mysql5.6",
 *     password: "bar",
 *     username: "foo",
 * });
 * const latestProdSnapshot = prod.id.apply(id => aws.rds.getSnapshot({
 *     dbInstanceIdentifier: id,
 *     mostRecent: true,
 * }));
 * // Use the latest production snapshot to create a dev instance.
 * const dev = new aws.rds.Instance("dev", {
 *     instanceClass: "db.t2.micro",
 *     name: "mydbdev",
 *     snapshotIdentifier: latestProdSnapshot.apply(latestProdSnapshot => latestProdSnapshot.id),
 * });
 * ```
 */
export function getSnapshot(args?: GetSnapshotArgs, opts?: pulumi.InvokeOptions): Promise<GetSnapshotResult> {
    args = args || {};
    return pulumi.runtime.invoke("aws:rds/getSnapshot:getSnapshot", {
        "dbInstanceIdentifier": args.dbInstanceIdentifier,
        "dbSnapshotIdentifier": args.dbSnapshotIdentifier,
        "includePublic": args.includePublic,
        "includeShared": args.includeShared,
        "mostRecent": args.mostRecent,
        "snapshotType": args.snapshotType,
    }, opts);
}

/**
 * A collection of arguments for invoking getSnapshot.
 */
export interface GetSnapshotArgs {
    /**
     * Returns the list of snapshots created by the specific db_instance
     */
    readonly dbInstanceIdentifier?: string;
    /**
     * Returns information on a specific snapshot_id.
     */
    readonly dbSnapshotIdentifier?: string;
    /**
     * Set this value to true to include manual DB snapshots that are public and can be
     * copied or restored by any AWS account, otherwise set this value to false. The default is `false`.
     */
    readonly includePublic?: boolean;
    /**
     * Set this value to true to include shared manual DB snapshots from other
     * AWS accounts that this AWS account has been given permission to copy or restore, otherwise set this value to false.
     * The default is `false`.
     */
    readonly includeShared?: boolean;
    /**
     * If more than one result is returned, use the most
     * recent Snapshot.
     */
    readonly mostRecent?: boolean;
    /**
     * The type of snapshots to be returned. If you don't specify a SnapshotType
     * value, then both automated and manual snapshots are returned. Shared and public DB snapshots are not
     * included in the returned results by default. Possible values are, `automated`, `manual`, `shared` and `public`.
     */
    readonly snapshotType?: string;
}

/**
 * A collection of values returned by getSnapshot.
 */
export interface GetSnapshotResult {
    /**
     * Specifies the allocated storage size in gigabytes (GB).
     */
    readonly allocatedStorage: number;
    /**
     * Specifies the name of the Availability Zone the DB instance was located in at the time of the DB snapshot.
     */
    readonly availabilityZone: string;
    /**
     * The Amazon Resource Name (ARN) for the DB snapshot.
     */
    readonly dbSnapshotArn: string;
    /**
     * Specifies whether the DB snapshot is encrypted.
     */
    readonly encrypted: boolean;
    /**
     * Specifies the name of the database engine.
     */
    readonly engine: string;
    /**
     * Specifies the version of the database engine.
     */
    readonly engineVersion: string;
    /**
     * Specifies the Provisioned IOPS (I/O operations per second) value of the DB instance at the time of the snapshot.
     */
    readonly iops: number;
    /**
     * The ARN for the KMS encryption key.
     */
    readonly kmsKeyId: string;
    /**
     * License model information for the restored DB instance.
     */
    readonly licenseModel: string;
    /**
     * Provides the option group name for the DB snapshot.
     */
    readonly optionGroupName: string;
    readonly port: number;
    /**
     * Provides the time when the snapshot was taken, in Universal Coordinated Time (UTC).
     */
    readonly snapshotCreateTime: string;
    /**
     * The DB snapshot Arn that the DB snapshot was copied from. It only has value in case of cross customer or cross region copy.
     */
    readonly sourceDbSnapshotIdentifier: string;
    /**
     * The region that the DB snapshot was created in or copied from.
     */
    readonly sourceRegion: string;
    /**
     * Specifies the status of this DB snapshot.
     */
    readonly status: string;
    /**
     * Specifies the storage type associated with DB snapshot.
     */
    readonly storageType: string;
    /**
     * Specifies the ID of the VPC associated with the DB snapshot.
     */
    readonly vpcId: string;
    /**
     * id is the provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
}
