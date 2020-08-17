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

__all__ = ['Webhook']


class Webhook(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 authentication: Optional[pulumi.Input[str]] = None,
                 authentication_configuration: Optional[pulumi.Input[pulumi.InputType['WebhookAuthenticationConfigurationArgs']]] = None,
                 filters: Optional[pulumi.Input[List[pulumi.Input[pulumi.InputType['WebhookFilterArgs']]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 target_action: Optional[pulumi.Input[str]] = None,
                 target_pipeline: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides a CodePipeline Webhook.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws
        import pulumi_github as github

        bar_pipeline = aws.codepipeline.Pipeline("barPipeline",
            artifact_store={
                "encryption_key": {
                    "id": data["aws_kms_alias"]["s3kmskey"]["arn"],
                    "type": "KMS",
                },
                "location": aws_s3_bucket["bar"]["bucket"],
                "type": "S3",
            },
            role_arn=aws_iam_role["bar"]["arn"],
            stages=[
                {
                    "actions": [{
                        "category": "Source",
                        "configuration": {
                            "Branch": "master",
                            "Owner": "my-organization",
                            "Repo": "test",
                        },
                        "name": "Source",
                        "outputArtifacts": ["test"],
                        "owner": "ThirdParty",
                        "provider": "GitHub",
                        "version": "1",
                    }],
                    "name": "Source",
                },
                {
                    "actions": [{
                        "category": "Build",
                        "configuration": {
                            "ProjectName": "test",
                        },
                        "inputArtifacts": ["test"],
                        "name": "Build",
                        "owner": "AWS",
                        "provider": "CodeBuild",
                        "version": "1",
                    }],
                    "name": "Build",
                },
            ])
        webhook_secret = "super-secret"
        bar_webhook = aws.codepipeline.Webhook("barWebhook",
            authentication="GITHUB_HMAC",
            authentication_configuration={
                "secretToken": webhook_secret,
            },
            filters=[{
                "jsonPath": "$.ref",
                "matchEquals": "refs/heads/{Branch}",
            }],
            target_action="Source",
            target_pipeline=bar_pipeline.name)
        # Wire the CodePipeline webhook into a GitHub repository.
        bar_repository_webhook = github.RepositoryWebhook("barRepositoryWebhook",
            configuration={
                "contentType": "json",
                "insecureSsl": True,
                "secret": webhook_secret,
                "url": bar_webhook.url,
            },
            events=["push"],
            repository=github_repository["repo"]["name"])
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] authentication: The type of authentication  to use. One of `IP`, `GITHUB_HMAC`, or `UNAUTHENTICATED`.
        :param pulumi.Input[pulumi.InputType['WebhookAuthenticationConfigurationArgs']] authentication_configuration: An `auth` block. Required for `IP` and `GITHUB_HMAC`. Auth blocks are documented below.
        :param pulumi.Input[List[pulumi.Input[pulumi.InputType['WebhookFilterArgs']]]] filters: One or more `filter` blocks. Filter blocks are documented below.
        :param pulumi.Input[str] name: The name of the webhook.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the resource.
        :param pulumi.Input[str] target_action: The name of the action in a pipeline you want to connect to the webhook. The action must be from the source (first) stage of the pipeline.
        :param pulumi.Input[str] target_pipeline: The name of the pipeline.
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

            if authentication is None:
                raise TypeError("Missing required property 'authentication'")
            __props__['authentication'] = authentication
            __props__['authentication_configuration'] = authentication_configuration
            if filters is None:
                raise TypeError("Missing required property 'filters'")
            __props__['filters'] = filters
            __props__['name'] = name
            __props__['tags'] = tags
            if target_action is None:
                raise TypeError("Missing required property 'target_action'")
            __props__['target_action'] = target_action
            if target_pipeline is None:
                raise TypeError("Missing required property 'target_pipeline'")
            __props__['target_pipeline'] = target_pipeline
            __props__['url'] = None
        super(Webhook, __self__).__init__(
            'aws:codepipeline/webhook:Webhook',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: str,
            opts: Optional[pulumi.ResourceOptions] = None,
            authentication: Optional[pulumi.Input[str]] = None,
            authentication_configuration: Optional[pulumi.Input[pulumi.InputType['WebhookAuthenticationConfigurationArgs']]] = None,
            filters: Optional[pulumi.Input[List[pulumi.Input[pulumi.InputType['WebhookFilterArgs']]]]] = None,
            name: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            target_action: Optional[pulumi.Input[str]] = None,
            target_pipeline: Optional[pulumi.Input[str]] = None,
            url: Optional[pulumi.Input[str]] = None) -> 'Webhook':
        """
        Get an existing Webhook resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] authentication: The type of authentication  to use. One of `IP`, `GITHUB_HMAC`, or `UNAUTHENTICATED`.
        :param pulumi.Input[pulumi.InputType['WebhookAuthenticationConfigurationArgs']] authentication_configuration: An `auth` block. Required for `IP` and `GITHUB_HMAC`. Auth blocks are documented below.
        :param pulumi.Input[List[pulumi.Input[pulumi.InputType['WebhookFilterArgs']]]] filters: One or more `filter` blocks. Filter blocks are documented below.
        :param pulumi.Input[str] name: The name of the webhook.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the resource.
        :param pulumi.Input[str] target_action: The name of the action in a pipeline you want to connect to the webhook. The action must be from the source (first) stage of the pipeline.
        :param pulumi.Input[str] target_pipeline: The name of the pipeline.
        :param pulumi.Input[str] url: The CodePipeline webhook's URL. POST events to this endpoint to trigger the target.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["authentication"] = authentication
        __props__["authentication_configuration"] = authentication_configuration
        __props__["filters"] = filters
        __props__["name"] = name
        __props__["tags"] = tags
        __props__["target_action"] = target_action
        __props__["target_pipeline"] = target_pipeline
        __props__["url"] = url
        return Webhook(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def authentication(self) -> str:
        """
        The type of authentication  to use. One of `IP`, `GITHUB_HMAC`, or `UNAUTHENTICATED`.
        """
        ...

    @property
    @pulumi.getter(name="authenticationConfiguration")
    def authentication_configuration(self) -> Optional['outputs.WebhookAuthenticationConfiguration']:
        """
        An `auth` block. Required for `IP` and `GITHUB_HMAC`. Auth blocks are documented below.
        """
        ...

    @property
    @pulumi.getter
    def filters(self) -> List['outputs.WebhookFilter']:
        """
        One or more `filter` blocks. Filter blocks are documented below.
        """
        ...

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the webhook.
        """
        ...

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        A map of tags to assign to the resource.
        """
        ...

    @property
    @pulumi.getter(name="targetAction")
    def target_action(self) -> str:
        """
        The name of the action in a pipeline you want to connect to the webhook. The action must be from the source (first) stage of the pipeline.
        """
        ...

    @property
    @pulumi.getter(name="targetPipeline")
    def target_pipeline(self) -> str:
        """
        The name of the pipeline.
        """
        ...

    @property
    @pulumi.getter
    def url(self) -> str:
        """
        The CodePipeline webhook's URL. POST events to this endpoint to trigger the target.
        """
        ...

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

