# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from .. import _utilities, _tables
from . import outputs
from ._inputs import *

__all__ = ['Domain']


class Domain(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 access_policies: Optional[pulumi.Input[str]] = None,
                 advanced_options: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 advanced_security_options: Optional[pulumi.Input[pulumi.InputType['DomainAdvancedSecurityOptionsArgs']]] = None,
                 cluster_config: Optional[pulumi.Input[pulumi.InputType['DomainClusterConfigArgs']]] = None,
                 cognito_options: Optional[pulumi.Input[pulumi.InputType['DomainCognitoOptionsArgs']]] = None,
                 domain_endpoint_options: Optional[pulumi.Input[pulumi.InputType['DomainDomainEndpointOptionsArgs']]] = None,
                 domain_name: Optional[pulumi.Input[str]] = None,
                 ebs_options: Optional[pulumi.Input[pulumi.InputType['DomainEbsOptionsArgs']]] = None,
                 elasticsearch_version: Optional[pulumi.Input[str]] = None,
                 encrypt_at_rest: Optional[pulumi.Input[pulumi.InputType['DomainEncryptAtRestArgs']]] = None,
                 log_publishing_options: Optional[pulumi.Input[List[pulumi.Input[pulumi.InputType['DomainLogPublishingOptionArgs']]]]] = None,
                 node_to_node_encryption: Optional[pulumi.Input[pulumi.InputType['DomainNodeToNodeEncryptionArgs']]] = None,
                 snapshot_options: Optional[pulumi.Input[pulumi.InputType['DomainSnapshotOptionsArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 vpc_options: Optional[pulumi.Input[pulumi.InputType['DomainVpcOptionsArgs']]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Manages an AWS Elasticsearch Domain.

        ## Example Usage
        ### Basic Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.elasticsearch.Domain("example",
            cluster_config={
                "instance_type": "r4.large.elasticsearch",
            },
            elasticsearch_version="1.5",
            snapshot_options={
                "automatedSnapshotStartHour": 23,
            },
            tags={
                "Domain": "TestDomain",
            })
        ```
        ### Access Policy

        > See also: `elasticsearch.DomainPolicy` resource

        ```python
        import pulumi
        import pulumi_aws as aws

        config = pulumi.Config()
        domain = config.get("domain")
        if domain is None:
            domain = "tf-test"
        current_region = aws.get_region()
        current_caller_identity = aws.get_caller_identity()
        example = aws.elasticsearch.Domain("example", access_policies=f\"\"\"{{
          "Version": "2012-10-17",
          "Statement": [
            {{
              "Action": "es:*",
              "Principal": "*",
              "Effect": "Allow",
              "Resource": "arn:aws:es:{current_region.name}:{current_caller_identity.account_id}:domain/{domain}/*",
              "Condition": {{
                "IpAddress": {{"aws:SourceIp": ["66.193.100.22/32"]}}
              }}
            }}
          ]
        }}

        \"\"\")
        ```
        ### Log Publishing to CloudWatch Logs

        ```python
        import pulumi
        import pulumi_aws as aws

        example_log_group = aws.cloudwatch.LogGroup("exampleLogGroup")
        example_log_resource_policy = aws.cloudwatch.LogResourcePolicy("exampleLogResourcePolicy",
            policy_document=\"\"\"{
          "Version": "2012-10-17",
          "Statement": [
            {
              "Effect": "Allow",
              "Principal": {
                "Service": "es.amazonaws.com"
              },
              "Action": [
                "logs:PutLogEvents",
                "logs:PutLogEventsBatch",
                "logs:CreateLogStream"
              ],
              "Resource": "arn:aws:logs:*"
            }
          ]
        }

        \"\"\",
            policy_name="example")
        example_domain = aws.elasticsearch.Domain("exampleDomain", log_publishing_options=[{
            "cloudwatch_log_group_arn": example_log_group.arn,
            "logType": "INDEX_SLOW_LOGS",
        }])
        ```
        ### VPC based ES

        ```python
        import pulumi
        import pulumi_aws as aws

        config = pulumi.Config()
        vpc = config.require_object("vpc")
        domain = config.get("domain")
        if domain is None:
            domain = "tf-test"
        selected_vpc = aws.ec2.get_vpc(tags={
            "Name": vpc,
        })
        selected_subnet_ids = aws.ec2.get_subnet_ids(tags={
                "Tier": "private",
            },
            vpc_id=selected_vpc.id)
        current_region = aws.get_region()
        current_caller_identity = aws.get_caller_identity()
        es_security_group = aws.ec2.SecurityGroup("esSecurityGroup",
            description="Managed by Pulumi",
            ingress=[{
                "cidr_blocks": [selected_vpc.cidr_block],
                "from_port": 443,
                "protocol": "tcp",
                "to_port": 443,
            }],
            vpc_id=selected_vpc.id)
        es_service_linked_role = aws.iam.ServiceLinkedRole("esServiceLinkedRole", aws_service_name="es.amazonaws.com")
        es_domain = aws.elasticsearch.Domain("esDomain",
            access_policies=f\"\"\"{{
        	"Version": "2012-10-17",
        	"Statement": [
        		{{
        			"Action": "es:*",
        			"Principal": "*",
        			"Effect": "Allow",
        			"Resource": "arn:aws:es:{current_region.name}:{current_caller_identity.account_id}:domain/{domain}/*"
        		}}
        	]
        }}

        \"\"\",
            advanced_options={
                "rest.action.multi.allow_explicit_index": "true",
            },
            cluster_config={
                "instance_type": "m4.large.elasticsearch",
            },
            elasticsearch_version="6.3",
            snapshot_options={
                "automatedSnapshotStartHour": 23,
            },
            tags={
                "Domain": "TestDomain",
            },
            vpc_options={
                "security_group_ids": [es_security_group.id],
                "subnet_ids": [
                    selected_subnet_ids.ids[0],
                    selected_subnet_ids.ids[1],
                ],
            },
            opts=ResourceOptions(depends_on=["aws_iam_service_linked_role.es"]))
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] access_policies: IAM policy document specifying the access policies for the domain
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] advanced_options: Key-value string pairs to specify advanced configuration options.
               Note that the values for these configuration options must be strings (wrapped in quotes) or they
               may be wrong and cause a perpetual diff, causing this provider to want to recreate your Elasticsearch
               domain on every apply.
        :param pulumi.Input[pulumi.InputType['DomainAdvancedSecurityOptionsArgs']] advanced_security_options: Options for [fine-grained access control](https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/fgac.html). See below for more details.
        :param pulumi.Input[pulumi.InputType['DomainClusterConfigArgs']] cluster_config: Cluster configuration of the domain, see below.
        :param pulumi.Input[pulumi.InputType['DomainDomainEndpointOptionsArgs']] domain_endpoint_options: Domain endpoint HTTP(S) related options. See below.
        :param pulumi.Input[str] domain_name: Name of the domain.
        :param pulumi.Input[pulumi.InputType['DomainEbsOptionsArgs']] ebs_options: EBS related options, may be required based on chosen [instance size](https://aws.amazon.com/elasticsearch-service/pricing/). See below.
        :param pulumi.Input[str] elasticsearch_version: The version of Elasticsearch to deploy. Defaults to `1.5`
        :param pulumi.Input[pulumi.InputType['DomainEncryptAtRestArgs']] encrypt_at_rest: Encrypt at rest options. Only available for [certain instance types](http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/aes-supported-instance-types.html). See below.
        :param pulumi.Input[List[pulumi.Input[pulumi.InputType['DomainLogPublishingOptionArgs']]]] log_publishing_options: Options for publishing slow logs to CloudWatch Logs.
        :param pulumi.Input[pulumi.InputType['DomainNodeToNodeEncryptionArgs']] node_to_node_encryption: Node-to-node encryption options. See below.
        :param pulumi.Input[pulumi.InputType['DomainSnapshotOptionsArgs']] snapshot_options: Snapshot related options, see below.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the resource
        :param pulumi.Input[pulumi.InputType['DomainVpcOptionsArgs']] vpc_options: VPC related options, see below. Adding or removing this configuration forces a new resource ([documentation](https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-vpc.html#es-vpc-limitations)).
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            __props__['access_policies'] = access_policies
            __props__['advanced_options'] = advanced_options
            __props__['advanced_security_options'] = advanced_security_options
            __props__['cluster_config'] = cluster_config
            __props__['cognito_options'] = cognito_options
            __props__['domain_endpoint_options'] = domain_endpoint_options
            __props__['domain_name'] = domain_name
            __props__['ebs_options'] = ebs_options
            __props__['elasticsearch_version'] = elasticsearch_version
            __props__['encrypt_at_rest'] = encrypt_at_rest
            __props__['log_publishing_options'] = log_publishing_options
            __props__['node_to_node_encryption'] = node_to_node_encryption
            __props__['snapshot_options'] = snapshot_options
            __props__['tags'] = tags
            __props__['vpc_options'] = vpc_options
            __props__['arn'] = None
            __props__['domain_id'] = None
            __props__['endpoint'] = None
            __props__['kibana_endpoint'] = None
        super(Domain, __self__).__init__(
            'aws:elasticsearch/domain:Domain',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: str,
            opts: Optional[pulumi.ResourceOptions] = None,
            access_policies: Optional[pulumi.Input[str]] = None,
            advanced_options: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            advanced_security_options: Optional[pulumi.Input[pulumi.InputType['DomainAdvancedSecurityOptionsArgs']]] = None,
            arn: Optional[pulumi.Input[str]] = None,
            cluster_config: Optional[pulumi.Input[pulumi.InputType['DomainClusterConfigArgs']]] = None,
            cognito_options: Optional[pulumi.Input[pulumi.InputType['DomainCognitoOptionsArgs']]] = None,
            domain_endpoint_options: Optional[pulumi.Input[pulumi.InputType['DomainDomainEndpointOptionsArgs']]] = None,
            domain_id: Optional[pulumi.Input[str]] = None,
            domain_name: Optional[pulumi.Input[str]] = None,
            ebs_options: Optional[pulumi.Input[pulumi.InputType['DomainEbsOptionsArgs']]] = None,
            elasticsearch_version: Optional[pulumi.Input[str]] = None,
            encrypt_at_rest: Optional[pulumi.Input[pulumi.InputType['DomainEncryptAtRestArgs']]] = None,
            endpoint: Optional[pulumi.Input[str]] = None,
            kibana_endpoint: Optional[pulumi.Input[str]] = None,
            log_publishing_options: Optional[pulumi.Input[List[pulumi.Input[pulumi.InputType['DomainLogPublishingOptionArgs']]]]] = None,
            node_to_node_encryption: Optional[pulumi.Input[pulumi.InputType['DomainNodeToNodeEncryptionArgs']]] = None,
            snapshot_options: Optional[pulumi.Input[pulumi.InputType['DomainSnapshotOptionsArgs']]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            vpc_options: Optional[pulumi.Input[pulumi.InputType['DomainVpcOptionsArgs']]] = None) -> 'Domain':
        """
        Get an existing Domain resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] access_policies: IAM policy document specifying the access policies for the domain
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] advanced_options: Key-value string pairs to specify advanced configuration options.
               Note that the values for these configuration options must be strings (wrapped in quotes) or they
               may be wrong and cause a perpetual diff, causing this provider to want to recreate your Elasticsearch
               domain on every apply.
        :param pulumi.Input[pulumi.InputType['DomainAdvancedSecurityOptionsArgs']] advanced_security_options: Options for [fine-grained access control](https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/fgac.html). See below for more details.
        :param pulumi.Input[str] arn: Amazon Resource Name (ARN) of the domain.
        :param pulumi.Input[pulumi.InputType['DomainClusterConfigArgs']] cluster_config: Cluster configuration of the domain, see below.
        :param pulumi.Input[pulumi.InputType['DomainDomainEndpointOptionsArgs']] domain_endpoint_options: Domain endpoint HTTP(S) related options. See below.
        :param pulumi.Input[str] domain_id: Unique identifier for the domain.
        :param pulumi.Input[str] domain_name: Name of the domain.
        :param pulumi.Input[pulumi.InputType['DomainEbsOptionsArgs']] ebs_options: EBS related options, may be required based on chosen [instance size](https://aws.amazon.com/elasticsearch-service/pricing/). See below.
        :param pulumi.Input[str] elasticsearch_version: The version of Elasticsearch to deploy. Defaults to `1.5`
        :param pulumi.Input[pulumi.InputType['DomainEncryptAtRestArgs']] encrypt_at_rest: Encrypt at rest options. Only available for [certain instance types](http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/aes-supported-instance-types.html). See below.
        :param pulumi.Input[str] endpoint: Domain-specific endpoint used to submit index, search, and data upload requests.
        :param pulumi.Input[str] kibana_endpoint: Domain-specific endpoint for kibana without https scheme.
               * `vpc_options.0.availability_zones` - If the domain was created inside a VPC, the names of the availability zones the configured `subnet_ids` were created inside.
               * `vpc_options.0.vpc_id` - If the domain was created inside a VPC, the ID of the VPC.
        :param pulumi.Input[List[pulumi.Input[pulumi.InputType['DomainLogPublishingOptionArgs']]]] log_publishing_options: Options for publishing slow logs to CloudWatch Logs.
        :param pulumi.Input[pulumi.InputType['DomainNodeToNodeEncryptionArgs']] node_to_node_encryption: Node-to-node encryption options. See below.
        :param pulumi.Input[pulumi.InputType['DomainSnapshotOptionsArgs']] snapshot_options: Snapshot related options, see below.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the resource
        :param pulumi.Input[pulumi.InputType['DomainVpcOptionsArgs']] vpc_options: VPC related options, see below. Adding or removing this configuration forces a new resource ([documentation](https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-vpc.html#es-vpc-limitations)).
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["access_policies"] = access_policies
        __props__["advanced_options"] = advanced_options
        __props__["advanced_security_options"] = advanced_security_options
        __props__["arn"] = arn
        __props__["cluster_config"] = cluster_config
        __props__["cognito_options"] = cognito_options
        __props__["domain_endpoint_options"] = domain_endpoint_options
        __props__["domain_id"] = domain_id
        __props__["domain_name"] = domain_name
        __props__["ebs_options"] = ebs_options
        __props__["elasticsearch_version"] = elasticsearch_version
        __props__["encrypt_at_rest"] = encrypt_at_rest
        __props__["endpoint"] = endpoint
        __props__["kibana_endpoint"] = kibana_endpoint
        __props__["log_publishing_options"] = log_publishing_options
        __props__["node_to_node_encryption"] = node_to_node_encryption
        __props__["snapshot_options"] = snapshot_options
        __props__["tags"] = tags
        __props__["vpc_options"] = vpc_options
        return Domain(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accessPolicies")
    def access_policies(self) -> str:
        """
        IAM policy document specifying the access policies for the domain
        """
        ...

    @property
    @pulumi.getter(name="advancedOptions")
    def advanced_options(self) -> Mapping[str, str]:
        """
        Key-value string pairs to specify advanced configuration options.
        Note that the values for these configuration options must be strings (wrapped in quotes) or they
        may be wrong and cause a perpetual diff, causing this provider to want to recreate your Elasticsearch
        domain on every apply.
        """
        ...

    @property
    @pulumi.getter(name="advancedSecurityOptions")
    def advanced_security_options(self) -> 'outputs.DomainAdvancedSecurityOptions':
        """
        Options for [fine-grained access control](https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/fgac.html). See below for more details.
        """
        ...

    @property
    @pulumi.getter
    def arn(self) -> str:
        """
        Amazon Resource Name (ARN) of the domain.
        """
        ...

    @property
    @pulumi.getter(name="clusterConfig")
    def cluster_config(self) -> 'outputs.DomainClusterConfig':
        """
        Cluster configuration of the domain, see below.
        """
        ...

    @property
    @pulumi.getter(name="cognitoOptions")
    def cognito_options(self) -> Optional['outputs.DomainCognitoOptions']:
        ...

    @property
    @pulumi.getter(name="domainEndpointOptions")
    def domain_endpoint_options(self) -> 'outputs.DomainDomainEndpointOptions':
        """
        Domain endpoint HTTP(S) related options. See below.
        """
        ...

    @property
    @pulumi.getter(name="domainId")
    def domain_id(self) -> str:
        """
        Unique identifier for the domain.
        """
        ...

    @property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> str:
        """
        Name of the domain.
        """
        ...

    @property
    @pulumi.getter(name="ebsOptions")
    def ebs_options(self) -> 'outputs.DomainEbsOptions':
        """
        EBS related options, may be required based on chosen [instance size](https://aws.amazon.com/elasticsearch-service/pricing/). See below.
        """
        ...

    @property
    @pulumi.getter(name="elasticsearchVersion")
    def elasticsearch_version(self) -> Optional[str]:
        """
        The version of Elasticsearch to deploy. Defaults to `1.5`
        """
        ...

    @property
    @pulumi.getter(name="encryptAtRest")
    def encrypt_at_rest(self) -> 'outputs.DomainEncryptAtRest':
        """
        Encrypt at rest options. Only available for [certain instance types](http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/aes-supported-instance-types.html). See below.
        """
        ...

    @property
    @pulumi.getter
    def endpoint(self) -> str:
        """
        Domain-specific endpoint used to submit index, search, and data upload requests.
        """
        ...

    @property
    @pulumi.getter(name="kibanaEndpoint")
    def kibana_endpoint(self) -> str:
        """
        Domain-specific endpoint for kibana without https scheme.
        * `vpc_options.0.availability_zones` - If the domain was created inside a VPC, the names of the availability zones the configured `subnet_ids` were created inside.
        * `vpc_options.0.vpc_id` - If the domain was created inside a VPC, the ID of the VPC.
        """
        ...

    @property
    @pulumi.getter(name="logPublishingOptions")
    def log_publishing_options(self) -> Optional[List['outputs.DomainLogPublishingOption']]:
        """
        Options for publishing slow logs to CloudWatch Logs.
        """
        ...

    @property
    @pulumi.getter(name="nodeToNodeEncryption")
    def node_to_node_encryption(self) -> 'outputs.DomainNodeToNodeEncryption':
        """
        Node-to-node encryption options. See below.
        """
        ...

    @property
    @pulumi.getter(name="snapshotOptions")
    def snapshot_options(self) -> Optional['outputs.DomainSnapshotOptions']:
        """
        Snapshot related options, see below.
        """
        ...

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        A map of tags to assign to the resource
        """
        ...

    @property
    @pulumi.getter(name="vpcOptions")
    def vpc_options(self) -> Optional['outputs.DomainVpcOptions']:
        """
        VPC related options, see below. Adding or removing this configuration forces a new resource ([documentation](https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-vpc.html#es-vpc-limitations)).
        """
        ...

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

