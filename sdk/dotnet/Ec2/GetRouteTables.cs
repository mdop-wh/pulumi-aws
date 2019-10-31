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
        /// This resource can be useful for getting back a list of route table ids to be referenced elsewhere.
        /// 
        /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/route_tables.html.markdown.
        /// </summary>
        public static Task<GetRouteTablesResult> GetRouteTables(GetRouteTablesArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetRouteTablesResult>("aws:ec2/getRouteTables:getRouteTables", args, options.WithVersion());
    }

    public sealed class GetRouteTablesArgs : Pulumi.ResourceArgs
    {
        [Input("filters")]
        private InputList<Inputs.GetRouteTablesFiltersArgs>? _filters;

        /// <summary>
        /// Custom filter block as described below.
        /// </summary>
        public InputList<Inputs.GetRouteTablesFiltersArgs> Filters
        {
            get => _filters ?? (_filters = new InputList<Inputs.GetRouteTablesFiltersArgs>());
            set => _filters = value;
        }

        [Input("tags")]
        private InputMap<object>? _tags;

        /// <summary>
        /// A mapping of tags, each pair of which must exactly match
        /// a pair on the desired route tables.
        /// </summary>
        public InputMap<object> Tags
        {
            get => _tags ?? (_tags = new InputMap<object>());
            set => _tags = value;
        }

        /// <summary>
        /// The VPC ID that you want to filter from.
        /// </summary>
        [Input("vpcId")]
        public Input<string>? VpcId { get; set; }

        public GetRouteTablesArgs()
        {
        }
    }

    [OutputType]
    public sealed class GetRouteTablesResult
    {
        public readonly ImmutableArray<Outputs.GetRouteTablesFiltersResult> Filters;
        /// <summary>
        /// A list of all the route table ids found. This data source will fail if none are found.
        /// </summary>
        public readonly ImmutableArray<string> Ids;
        public readonly ImmutableDictionary<string, object> Tags;
        public readonly string? VpcId;
        /// <summary>
        /// id is the provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;

        [OutputConstructor]
        private GetRouteTablesResult(
            ImmutableArray<Outputs.GetRouteTablesFiltersResult> filters,
            ImmutableArray<string> ids,
            ImmutableDictionary<string, object> tags,
            string? vpcId,
            string id)
        {
            Filters = filters;
            Ids = ids;
            Tags = tags;
            VpcId = vpcId;
            Id = id;
        }
    }

    namespace Inputs
    {

    public sealed class GetRouteTablesFiltersArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The name of the field to filter by, as defined by
        /// [the underlying AWS API](http://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeRouteTables.html).
        /// </summary>
        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        [Input("values", required: true)]
        private InputList<string>? _values;

        /// <summary>
        /// Set of values that are accepted for the given field.
        /// A Route Table will be selected if any one of the given values matches.
        /// </summary>
        public InputList<string> Values
        {
            get => _values ?? (_values = new InputList<string>());
            set => _values = value;
        }

        public GetRouteTablesFiltersArgs()
        {
        }
    }
    }

    namespace Outputs
    {

    [OutputType]
    public sealed class GetRouteTablesFiltersResult
    {
        /// <summary>
        /// The name of the field to filter by, as defined by
        /// [the underlying AWS API](http://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeRouteTables.html).
        /// </summary>
        public readonly string Name;
        /// <summary>
        /// Set of values that are accepted for the given field.
        /// A Route Table will be selected if any one of the given values matches.
        /// </summary>
        public readonly ImmutableArray<string> Values;

        [OutputConstructor]
        private GetRouteTablesFiltersResult(
            string name,
            ImmutableArray<string> values)
        {
            Name = name;
            Values = values;
        }
    }
    }
}
