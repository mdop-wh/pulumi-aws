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

__all__ = ['OptionGroup']


class OptionGroup(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 engine_name: Optional[pulumi.Input[str]] = None,
                 major_engine_version: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 name_prefix: Optional[pulumi.Input[str]] = None,
                 option_group_description: Optional[pulumi.Input[str]] = None,
                 options: Optional[pulumi.Input[List[pulumi.Input[pulumi.InputType['OptionGroupOptionArgs']]]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides an RDS DB option group resource. Documentation of the available options for various RDS engines can be found at:

        * [MariaDB Options](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.MariaDB.Options.html)
        * [Microsoft SQL Server Options](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.SQLServer.Options.html)
        * [MySQL Options](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.MySQL.Options.html)
        * [Oracle Options](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.Options.html)

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.rds.OptionGroup("example",
            engine_name="sqlserver-ee",
            major_engine_version="11.00",
            options=[
                {
                    "optionName": "Timezone",
                    "optionSettings": [{
                        "name": "TIME_ZONE",
                        "value": "UTC",
                    }],
                },
                {
                    "optionName": "SQLSERVER_BACKUP_RESTORE",
                    "optionSettings": [{
                        "name": "IAM_ROLE_ARN",
                        "value": aws_iam_role["example"]["arn"],
                    }],
                },
                {
                    "optionName": "TDE",
                },
            ],
            option_group_description="Option Group")
        ```

        > **Note**: Any modifications to the `db_option_group` are set to happen immediately as we default to applying immediately.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] engine_name: Specifies the name of the engine that this option group should be associated with.
        :param pulumi.Input[str] major_engine_version: Specifies the major version of the engine that this option group should be associated with.
        :param pulumi.Input[str] name: The Name of the setting.
        :param pulumi.Input[str] name_prefix: Creates a unique name beginning with the specified prefix. Conflicts with `name`. Must be lowercase, to match as it is stored in AWS.
        :param pulumi.Input[str] option_group_description: The description of the option group. Defaults to "Managed by Pulumi".
        :param pulumi.Input[List[pulumi.Input[pulumi.InputType['OptionGroupOptionArgs']]]] options: A list of Options to apply.
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

            if engine_name is None:
                raise TypeError("Missing required property 'engine_name'")
            __props__['engine_name'] = engine_name
            if major_engine_version is None:
                raise TypeError("Missing required property 'major_engine_version'")
            __props__['major_engine_version'] = major_engine_version
            __props__['name'] = name
            __props__['name_prefix'] = name_prefix
            if option_group_description is None:
                option_group_description = 'Managed by Pulumi'
            __props__['option_group_description'] = option_group_description
            __props__['options'] = options
            __props__['tags'] = tags
            __props__['arn'] = None
        super(OptionGroup, __self__).__init__(
            'aws:rds/optionGroup:OptionGroup',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: str,
            opts: Optional[pulumi.ResourceOptions] = None,
            arn: Optional[pulumi.Input[str]] = None,
            engine_name: Optional[pulumi.Input[str]] = None,
            major_engine_version: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            name_prefix: Optional[pulumi.Input[str]] = None,
            option_group_description: Optional[pulumi.Input[str]] = None,
            options: Optional[pulumi.Input[List[pulumi.Input[pulumi.InputType['OptionGroupOptionArgs']]]]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None) -> 'OptionGroup':
        """
        Get an existing OptionGroup resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] arn: The ARN of the db option group.
        :param pulumi.Input[str] engine_name: Specifies the name of the engine that this option group should be associated with.
        :param pulumi.Input[str] major_engine_version: Specifies the major version of the engine that this option group should be associated with.
        :param pulumi.Input[str] name: The Name of the setting.
        :param pulumi.Input[str] name_prefix: Creates a unique name beginning with the specified prefix. Conflicts with `name`. Must be lowercase, to match as it is stored in AWS.
        :param pulumi.Input[str] option_group_description: The description of the option group. Defaults to "Managed by Pulumi".
        :param pulumi.Input[List[pulumi.Input[pulumi.InputType['OptionGroupOptionArgs']]]] options: A list of Options to apply.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["arn"] = arn
        __props__["engine_name"] = engine_name
        __props__["major_engine_version"] = major_engine_version
        __props__["name"] = name
        __props__["name_prefix"] = name_prefix
        __props__["option_group_description"] = option_group_description
        __props__["options"] = options
        __props__["tags"] = tags
        return OptionGroup(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> str:
        """
        The ARN of the db option group.
        """
        ...

    @property
    @pulumi.getter(name="engineName")
    def engine_name(self) -> str:
        """
        Specifies the name of the engine that this option group should be associated with.
        """
        ...

    @property
    @pulumi.getter(name="majorEngineVersion")
    def major_engine_version(self) -> str:
        """
        Specifies the major version of the engine that this option group should be associated with.
        """
        ...

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The Name of the setting.
        """
        ...

    @property
    @pulumi.getter(name="namePrefix")
    def name_prefix(self) -> str:
        """
        Creates a unique name beginning with the specified prefix. Conflicts with `name`. Must be lowercase, to match as it is stored in AWS.
        """
        ...

    @property
    @pulumi.getter(name="optionGroupDescription")
    def option_group_description(self) -> str:
        """
        The description of the option group. Defaults to "Managed by Pulumi".
        """
        ...

    @property
    @pulumi.getter
    def options(self) -> Optional[List['outputs.OptionGroupOption']]:
        """
        A list of Options to apply.
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

