// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.Ec2
{
    public static partial class Invokes
    {
        /// <summary>
        /// Use this data source to get IDs and VPC membership of Security Groups that are created
        /// outside of this provider.
        /// 
        /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/security_groups.html.markdown.
        /// </summary>
        public static Task<GetSecurityGroupsResult> GetSecurityGroups(GetSecurityGroupsArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetSecurityGroupsResult>("aws:ec2/getSecurityGroups:getSecurityGroups", args, options.WithVersion());
    }

    public sealed class GetSecurityGroupsArgs : Pulumi.ResourceArgs
    {
        [Input("filters")]
        private InputList<Inputs.GetSecurityGroupsFiltersArgs>? _filters;

        /// <summary>
        /// One or more name/value pairs to use as filters. There are
        /// several valid keys, for a full reference, check out
        /// [describe-security-groups in the AWS CLI reference][1].
        /// </summary>
        public InputList<Inputs.GetSecurityGroupsFiltersArgs> Filters
        {
            get => _filters ?? (_filters = new InputList<Inputs.GetSecurityGroupsFiltersArgs>());
            set => _filters = value;
        }

        [Input("tags")]
        private InputMap<object>? _tags;

        /// <summary>
        /// A mapping of tags, each pair of which must exactly match for
        /// desired security groups.
        /// </summary>
        public InputMap<object> Tags
        {
            get => _tags ?? (_tags = new InputMap<object>());
            set => _tags = value;
        }

        public GetSecurityGroupsArgs()
        {
        }
    }

    [OutputType]
    public sealed class GetSecurityGroupsResult
    {
        public readonly ImmutableArray<Outputs.GetSecurityGroupsFiltersResult> Filters;
        /// <summary>
        /// IDs of the matches security groups.
        /// </summary>
        public readonly ImmutableArray<string> Ids;
        public readonly ImmutableDictionary<string, object> Tags;
        /// <summary>
        /// The VPC IDs of the matched security groups. The data source's tag or filter *will span VPCs*
        /// unless the `vpc-id` filter is also used.
        /// </summary>
        public readonly ImmutableArray<string> VpcIds;
        /// <summary>
        /// id is the provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;

        [OutputConstructor]
        private GetSecurityGroupsResult(
            ImmutableArray<Outputs.GetSecurityGroupsFiltersResult> filters,
            ImmutableArray<string> ids,
            ImmutableDictionary<string, object> tags,
            ImmutableArray<string> vpcIds,
            string id)
        {
            Filters = filters;
            Ids = ids;
            Tags = tags;
            VpcIds = vpcIds;
            Id = id;
        }
    }

    namespace Inputs
    {

    public sealed class GetSecurityGroupsFiltersArgs : Pulumi.ResourceArgs
    {
        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        [Input("values", required: true)]
        private InputList<string>? _values;
        public InputList<string> Values
        {
            get => _values ?? (_values = new InputList<string>());
            set => _values = value;
        }

        public GetSecurityGroupsFiltersArgs()
        {
        }
    }
    }

    namespace Outputs
    {

    [OutputType]
    public sealed class GetSecurityGroupsFiltersResult
    {
        public readonly string Name;
        public readonly ImmutableArray<string> Values;

        [OutputConstructor]
        private GetSecurityGroupsFiltersResult(
            string name,
            ImmutableArray<string> values)
        {
            Name = name;
            Values = values;
        }
    }
    }
}
