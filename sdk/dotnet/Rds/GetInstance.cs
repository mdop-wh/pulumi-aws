// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.Rds
{
    public static partial class Invokes
    {
        /// <summary>
        /// Use this data source to get information about an RDS instance
        /// 
        /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/db_instance.html.markdown.
        /// </summary>
        public static Task<GetInstanceResult> GetInstance(GetInstanceArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetInstanceResult>("aws:rds/getInstance:getInstance", args, options.WithVersion());
    }

    public sealed class GetInstanceArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The name of the RDS instance
        /// </summary>
        [Input("dbInstanceIdentifier", required: true)]
        public Input<string> DbInstanceIdentifier { get; set; } = null!;

        public GetInstanceArgs()
        {
        }
    }

    [OutputType]
    public sealed class GetInstanceResult
    {
        /// <summary>
        /// The hostname of the RDS instance. See also `endpoint` and `port`.
        /// </summary>
        public readonly string Address;
        /// <summary>
        /// Specifies the allocated storage size specified in gigabytes.
        /// </summary>
        public readonly int AllocatedStorage;
        /// <summary>
        /// Indicates that minor version patches are applied automatically.
        /// </summary>
        public readonly bool AutoMinorVersionUpgrade;
        /// <summary>
        /// Specifies the name of the Availability Zone the DB instance is located in.
        /// </summary>
        public readonly string AvailabilityZone;
        /// <summary>
        /// Specifies the number of days for which automatic DB snapshots are retained.
        /// </summary>
        public readonly int BackupRetentionPeriod;
        /// <summary>
        /// Specifies the identifier of the CA certificate for the DB instance.
        /// </summary>
        public readonly string CaCertIdentifier;
        /// <summary>
        /// If the DB instance is a member of a DB cluster, contains the name of the DB cluster that the DB instance is a member of.
        /// </summary>
        public readonly string DbClusterIdentifier;
        /// <summary>
        /// The Amazon Resource Name (ARN) for the DB instance.
        /// </summary>
        public readonly string DbInstanceArn;
        /// <summary>
        /// Contains the name of the compute and memory capacity class of the DB instance.
        /// </summary>
        public readonly string DbInstanceClass;
        public readonly string DbInstanceIdentifier;
        /// <summary>
        /// Specifies the port that the DB instance listens on.
        /// </summary>
        public readonly int DbInstancePort;
        /// <summary>
        /// Contains the name of the initial database of this instance that was provided at create time, if one was specified when the DB instance was created. This same name is returned for the life of the DB instance.
        /// </summary>
        public readonly string DbName;
        /// <summary>
        /// Provides the list of DB parameter groups applied to this DB instance.
        /// </summary>
        public readonly ImmutableArray<string> DbParameterGroups;
        /// <summary>
        /// Provides List of DB security groups associated to this DB instance.
        /// </summary>
        public readonly ImmutableArray<string> DbSecurityGroups;
        /// <summary>
        /// Specifies the name of the subnet group associated with the DB instance.
        /// </summary>
        public readonly string DbSubnetGroup;
        /// <summary>
        /// List of log types to export to cloudwatch.
        /// </summary>
        public readonly ImmutableArray<string> EnabledCloudwatchLogsExports;
        /// <summary>
        /// The connection endpoint in `address:port` format.
        /// </summary>
        public readonly string Endpoint;
        /// <summary>
        /// Provides the name of the database engine to be used for this DB instance.
        /// </summary>
        public readonly string Engine;
        /// <summary>
        /// Indicates the database engine version.
        /// </summary>
        public readonly string EngineVersion;
        /// <summary>
        /// The canonical hosted zone ID of the DB instance (to be used in a Route 53 Alias record).
        /// </summary>
        public readonly string HostedZoneId;
        /// <summary>
        /// Specifies the Provisioned IOPS (I/O operations per second) value.
        /// </summary>
        public readonly int Iops;
        /// <summary>
        /// If StorageEncrypted is true, the KMS key identifier for the encrypted DB instance.
        /// </summary>
        public readonly string KmsKeyId;
        /// <summary>
        /// License model information for this DB instance.
        /// </summary>
        public readonly string LicenseModel;
        /// <summary>
        /// Contains the master username for the DB instance.
        /// </summary>
        public readonly string MasterUsername;
        /// <summary>
        /// The interval, in seconds, between points when Enhanced Monitoring metrics are collected for the DB instance.
        /// </summary>
        public readonly int MonitoringInterval;
        /// <summary>
        /// The ARN for the IAM role that permits RDS to send Enhanced Monitoring metrics to CloudWatch Logs.
        /// </summary>
        public readonly string MonitoringRoleArn;
        /// <summary>
        /// Specifies if the DB instance is a Multi-AZ deployment.
        /// </summary>
        public readonly bool MultiAz;
        /// <summary>
        /// Provides the list of option group memberships for this DB instance.
        /// </summary>
        public readonly ImmutableArray<string> OptionGroupMemberships;
        /// <summary>
        /// The database port.
        /// </summary>
        public readonly int Port;
        /// <summary>
        /// Specifies the daily time range during which automated backups are created.
        /// </summary>
        public readonly string PreferredBackupWindow;
        /// <summary>
        /// Specifies the weekly time range during which system maintenance can occur in UTC.
        /// </summary>
        public readonly string PreferredMaintenanceWindow;
        /// <summary>
        /// Specifies the accessibility options for the DB instance.
        /// </summary>
        public readonly bool PubliclyAccessible;
        /// <summary>
        /// The identifier of the source DB that this is a replica of.
        /// </summary>
        public readonly string ReplicateSourceDb;
        /// <summary>
        /// The RDS Resource ID of this instance.
        /// </summary>
        public readonly string ResourceId;
        /// <summary>
        /// Specifies whether the DB instance is encrypted.
        /// </summary>
        public readonly bool StorageEncrypted;
        /// <summary>
        /// Specifies the storage type associated with DB instance.
        /// </summary>
        public readonly string StorageType;
        /// <summary>
        /// The time zone of the DB instance.
        /// </summary>
        public readonly string Timezone;
        /// <summary>
        /// Provides a list of VPC security group elements that the DB instance belongs to.
        /// </summary>
        public readonly ImmutableArray<string> VpcSecurityGroups;
        /// <summary>
        /// id is the provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;

        [OutputConstructor]
        private GetInstanceResult(
            string address,
            int allocatedStorage,
            bool autoMinorVersionUpgrade,
            string availabilityZone,
            int backupRetentionPeriod,
            string caCertIdentifier,
            string dbClusterIdentifier,
            string dbInstanceArn,
            string dbInstanceClass,
            string dbInstanceIdentifier,
            int dbInstancePort,
            string dbName,
            ImmutableArray<string> dbParameterGroups,
            ImmutableArray<string> dbSecurityGroups,
            string dbSubnetGroup,
            ImmutableArray<string> enabledCloudwatchLogsExports,
            string endpoint,
            string engine,
            string engineVersion,
            string hostedZoneId,
            int iops,
            string kmsKeyId,
            string licenseModel,
            string masterUsername,
            int monitoringInterval,
            string monitoringRoleArn,
            bool multiAz,
            ImmutableArray<string> optionGroupMemberships,
            int port,
            string preferredBackupWindow,
            string preferredMaintenanceWindow,
            bool publiclyAccessible,
            string replicateSourceDb,
            string resourceId,
            bool storageEncrypted,
            string storageType,
            string timezone,
            ImmutableArray<string> vpcSecurityGroups,
            string id)
        {
            Address = address;
            AllocatedStorage = allocatedStorage;
            AutoMinorVersionUpgrade = autoMinorVersionUpgrade;
            AvailabilityZone = availabilityZone;
            BackupRetentionPeriod = backupRetentionPeriod;
            CaCertIdentifier = caCertIdentifier;
            DbClusterIdentifier = dbClusterIdentifier;
            DbInstanceArn = dbInstanceArn;
            DbInstanceClass = dbInstanceClass;
            DbInstanceIdentifier = dbInstanceIdentifier;
            DbInstancePort = dbInstancePort;
            DbName = dbName;
            DbParameterGroups = dbParameterGroups;
            DbSecurityGroups = dbSecurityGroups;
            DbSubnetGroup = dbSubnetGroup;
            EnabledCloudwatchLogsExports = enabledCloudwatchLogsExports;
            Endpoint = endpoint;
            Engine = engine;
            EngineVersion = engineVersion;
            HostedZoneId = hostedZoneId;
            Iops = iops;
            KmsKeyId = kmsKeyId;
            LicenseModel = licenseModel;
            MasterUsername = masterUsername;
            MonitoringInterval = monitoringInterval;
            MonitoringRoleArn = monitoringRoleArn;
            MultiAz = multiAz;
            OptionGroupMemberships = optionGroupMemberships;
            Port = port;
            PreferredBackupWindow = preferredBackupWindow;
            PreferredMaintenanceWindow = preferredMaintenanceWindow;
            PubliclyAccessible = publiclyAccessible;
            ReplicateSourceDb = replicateSourceDb;
            ResourceId = resourceId;
            StorageEncrypted = storageEncrypted;
            StorageType = storageType;
            Timezone = timezone;
            VpcSecurityGroups = vpcSecurityGroups;
            Id = id;
        }
    }
}
