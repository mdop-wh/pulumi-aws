# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class GetOrganizationResult:
    """
    A collection of values returned by getOrganization.
    """
    def __init__(__self__, accounts=None, arn=None, aws_service_access_principals=None, enabled_policy_types=None, feature_set=None, id=None, master_account_arn=None, master_account_email=None, master_account_id=None, non_master_accounts=None, roots=None):
        if accounts and not isinstance(accounts, list):
            raise TypeError("Expected argument 'accounts' to be a list")
        __self__.accounts = accounts
        """
        List of organization accounts including the master account. For a list excluding the master account, see the `non_master_accounts` attribute. All elements have these attributes:
        """
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        __self__.arn = arn
        """
        ARN of the root
        """
        if aws_service_access_principals and not isinstance(aws_service_access_principals, list):
            raise TypeError("Expected argument 'aws_service_access_principals' to be a list")
        __self__.aws_service_access_principals = aws_service_access_principals
        """
        A list of AWS service principal names that have integration enabled with your organization. Organization must have `feature_set` set to `ALL`. For additional information, see the [AWS Organizations User Guide](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services.html).
        """
        if enabled_policy_types and not isinstance(enabled_policy_types, list):
            raise TypeError("Expected argument 'enabled_policy_types' to be a list")
        __self__.enabled_policy_types = enabled_policy_types
        """
        A list of Organizations policy types that are enabled in the Organization Root. Organization must have `feature_set` set to `ALL`. For additional information about valid policy types (e.g. `SERVICE_CONTROL_POLICY`), see the [AWS Organizations API Reference](https://docs.aws.amazon.com/organizations/latest/APIReference/API_EnablePolicyType.html).
        """
        if feature_set and not isinstance(feature_set, str):
            raise TypeError("Expected argument 'feature_set' to be a str")
        __self__.feature_set = feature_set
        """
        The FeatureSet of the organization.
        """
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        """
        id is the provider-assigned unique ID for this managed resource.
        """
        if master_account_arn and not isinstance(master_account_arn, str):
            raise TypeError("Expected argument 'master_account_arn' to be a str")
        __self__.master_account_arn = master_account_arn
        """
        The Amazon Resource Name (ARN) of the account that is designated as the master account for the organization.
        """
        if master_account_email and not isinstance(master_account_email, str):
            raise TypeError("Expected argument 'master_account_email' to be a str")
        __self__.master_account_email = master_account_email
        """
        The email address that is associated with the AWS account that is designated as the master account for the organization.
        """
        if master_account_id and not isinstance(master_account_id, str):
            raise TypeError("Expected argument 'master_account_id' to be a str")
        __self__.master_account_id = master_account_id
        """
        The unique identifier (ID) of the master account of an organization.
        """
        if non_master_accounts and not isinstance(non_master_accounts, list):
            raise TypeError("Expected argument 'non_master_accounts' to be a list")
        __self__.non_master_accounts = non_master_accounts
        """
        List of organization accounts excluding the master account. For a list including the master account, see the `accounts` attribute. All elements have these attributes:
        """
        if roots and not isinstance(roots, list):
            raise TypeError("Expected argument 'roots' to be a list")
        __self__.roots = roots
        """
        List of organization roots. All elements have these attributes:
        """
class AwaitableGetOrganizationResult(GetOrganizationResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetOrganizationResult(
            accounts=self.accounts,
            arn=self.arn,
            aws_service_access_principals=self.aws_service_access_principals,
            enabled_policy_types=self.enabled_policy_types,
            feature_set=self.feature_set,
            id=self.id,
            master_account_arn=self.master_account_arn,
            master_account_email=self.master_account_email,
            master_account_id=self.master_account_id,
            non_master_accounts=self.non_master_accounts,
            roots=self.roots)

def get_organization(opts=None):
    """
    Get information about the organization that the user's account belongs to
    """
    __args__ = dict()


    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws:organizations/getOrganization:getOrganization', __args__, opts=opts).value

    return AwaitableGetOrganizationResult(
        accounts=__ret__.get('accounts'),
        arn=__ret__.get('arn'),
        aws_service_access_principals=__ret__.get('awsServiceAccessPrincipals'),
        enabled_policy_types=__ret__.get('enabledPolicyTypes'),
        feature_set=__ret__.get('featureSet'),
        id=__ret__.get('id'),
        master_account_arn=__ret__.get('masterAccountArn'),
        master_account_email=__ret__.get('masterAccountEmail'),
        master_account_id=__ret__.get('masterAccountId'),
        non_master_accounts=__ret__.get('nonMasterAccounts'),
        roots=__ret__.get('roots'))
