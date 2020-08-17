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

__all__ = ['Repository']


class Repository(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 image_scanning_configuration: Optional[pulumi.Input[pulumi.InputType['RepositoryImageScanningConfigurationArgs']]] = None,
                 image_tag_mutability: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides an Elastic Container Registry Repository.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        foo = aws.ecr.Repository("foo",
            image_scanning_configuration={
                "scanOnPush": True,
            },
            image_tag_mutability="MUTABLE")
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['RepositoryImageScanningConfigurationArgs']] image_scanning_configuration: Configuration block that defines image scanning configuration for the repository. By default, image scanning must be manually triggered. See the [ECR User Guide](https://docs.aws.amazon.com/AmazonECR/latest/userguide/image-scanning.html) for more information about image scanning.
        :param pulumi.Input[str] image_tag_mutability: The tag mutability setting for the repository. Must be one of: `MUTABLE` or `IMMUTABLE`. Defaults to `MUTABLE`.
        :param pulumi.Input[str] name: Name of the repository.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the resource.
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

            __props__['image_scanning_configuration'] = image_scanning_configuration
            __props__['image_tag_mutability'] = image_tag_mutability
            __props__['name'] = name
            __props__['tags'] = tags
            __props__['arn'] = None
            __props__['registry_id'] = None
            __props__['repository_url'] = None
        super(Repository, __self__).__init__(
            'aws:ecr/repository:Repository',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: str,
            opts: Optional[pulumi.ResourceOptions] = None,
            arn: Optional[pulumi.Input[str]] = None,
            image_scanning_configuration: Optional[pulumi.Input[pulumi.InputType['RepositoryImageScanningConfigurationArgs']]] = None,
            image_tag_mutability: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            registry_id: Optional[pulumi.Input[str]] = None,
            repository_url: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None) -> 'Repository':
        """
        Get an existing Repository resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] arn: Full ARN of the repository.
        :param pulumi.Input[pulumi.InputType['RepositoryImageScanningConfigurationArgs']] image_scanning_configuration: Configuration block that defines image scanning configuration for the repository. By default, image scanning must be manually triggered. See the [ECR User Guide](https://docs.aws.amazon.com/AmazonECR/latest/userguide/image-scanning.html) for more information about image scanning.
        :param pulumi.Input[str] image_tag_mutability: The tag mutability setting for the repository. Must be one of: `MUTABLE` or `IMMUTABLE`. Defaults to `MUTABLE`.
        :param pulumi.Input[str] name: Name of the repository.
        :param pulumi.Input[str] registry_id: The registry ID where the repository was created.
        :param pulumi.Input[str] repository_url: The URL of the repository (in the form `aws_account_id.dkr.ecr.region.amazonaws.com/repositoryName`).
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["arn"] = arn
        __props__["image_scanning_configuration"] = image_scanning_configuration
        __props__["image_tag_mutability"] = image_tag_mutability
        __props__["name"] = name
        __props__["registry_id"] = registry_id
        __props__["repository_url"] = repository_url
        __props__["tags"] = tags
        return Repository(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> str:
        """
        Full ARN of the repository.
        """
        ...

    @property
    @pulumi.getter(name="imageScanningConfiguration")
    def image_scanning_configuration(self) -> Optional['outputs.RepositoryImageScanningConfiguration']:
        """
        Configuration block that defines image scanning configuration for the repository. By default, image scanning must be manually triggered. See the [ECR User Guide](https://docs.aws.amazon.com/AmazonECR/latest/userguide/image-scanning.html) for more information about image scanning.
        """
        ...

    @property
    @pulumi.getter(name="imageTagMutability")
    def image_tag_mutability(self) -> Optional[str]:
        """
        The tag mutability setting for the repository. Must be one of: `MUTABLE` or `IMMUTABLE`. Defaults to `MUTABLE`.
        """
        ...

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of the repository.
        """
        ...

    @property
    @pulumi.getter(name="registryId")
    def registry_id(self) -> str:
        """
        The registry ID where the repository was created.
        """
        ...

    @property
    @pulumi.getter(name="repositoryUrl")
    def repository_url(self) -> str:
        """
        The URL of the repository (in the form `aws_account_id.dkr.ecr.region.amazonaws.com/repositoryName`).
        """
        ...

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        A map of tags to assign to the resource.
        """
        ...

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

