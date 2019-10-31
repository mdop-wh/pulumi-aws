// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.Wafregional
{
    /// <summary>
    /// Provides a WAF Regional Size Constraint Set Resource for use with Application Load Balancer.
    /// 
    /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/wafregional_size_constraint_set.html.markdown.
    /// </summary>
    public partial class SizeConstraintSet : Pulumi.CustomResource
    {
        /// <summary>
        /// The name or description of the Size Constraint Set.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// Specifies the parts of web requests that you want to inspect the size of.
        /// </summary>
        [Output("sizeConstraints")]
        public Output<ImmutableArray<Outputs.SizeConstraintSetSizeConstraints>> SizeConstraints { get; private set; } = null!;


        /// <summary>
        /// Create a SizeConstraintSet resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public SizeConstraintSet(string name, SizeConstraintSetArgs? args = null, CustomResourceOptions? options = null)
            : base("aws:wafregional/sizeConstraintSet:SizeConstraintSet", name, args, MakeResourceOptions(options, ""))
        {
        }

        private SizeConstraintSet(string name, Input<string> id, SizeConstraintSetState? state = null, CustomResourceOptions? options = null)
            : base("aws:wafregional/sizeConstraintSet:SizeConstraintSet", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing SizeConstraintSet resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static SizeConstraintSet Get(string name, Input<string> id, SizeConstraintSetState? state = null, CustomResourceOptions? options = null)
        {
            return new SizeConstraintSet(name, id, state, options);
        }
    }

    public sealed class SizeConstraintSetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The name or description of the Size Constraint Set.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("sizeConstraints")]
        private InputList<Inputs.SizeConstraintSetSizeConstraintsArgs>? _sizeConstraints;

        /// <summary>
        /// Specifies the parts of web requests that you want to inspect the size of.
        /// </summary>
        public InputList<Inputs.SizeConstraintSetSizeConstraintsArgs> SizeConstraints
        {
            get => _sizeConstraints ?? (_sizeConstraints = new InputList<Inputs.SizeConstraintSetSizeConstraintsArgs>());
            set => _sizeConstraints = value;
        }

        public SizeConstraintSetArgs()
        {
        }
    }

    public sealed class SizeConstraintSetState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The name or description of the Size Constraint Set.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("sizeConstraints")]
        private InputList<Inputs.SizeConstraintSetSizeConstraintsGetArgs>? _sizeConstraints;

        /// <summary>
        /// Specifies the parts of web requests that you want to inspect the size of.
        /// </summary>
        public InputList<Inputs.SizeConstraintSetSizeConstraintsGetArgs> SizeConstraints
        {
            get => _sizeConstraints ?? (_sizeConstraints = new InputList<Inputs.SizeConstraintSetSizeConstraintsGetArgs>());
            set => _sizeConstraints = value;
        }

        public SizeConstraintSetState()
        {
        }
    }

    namespace Inputs
    {

    public sealed class SizeConstraintSetSizeConstraintsArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The type of comparison you want to perform.
        /// e.g. `EQ`, `NE`, `LT`, `GT`.
        /// See [docs](http://docs.aws.amazon.com/waf/latest/APIReference/API_SizeConstraint.html#WAF-Type-SizeConstraint-ComparisonOperator) for all supported values.
        /// </summary>
        [Input("comparisonOperator", required: true)]
        public Input<string> ComparisonOperator { get; set; } = null!;

        /// <summary>
        /// Specifies where in a web request to look for the size constraint.
        /// </summary>
        [Input("fieldToMatch", required: true)]
        public Input<SizeConstraintSetSizeConstraintsFieldToMatchArgs> FieldToMatch { get; set; } = null!;

        /// <summary>
        /// The size in bytes that you want to compare against the size of the specified `field_to_match`.
        /// Valid values are between 0 - 21474836480 bytes (0 - 20 GB).
        /// </summary>
        [Input("size", required: true)]
        public Input<int> Size { get; set; } = null!;

        /// <summary>
        /// Text transformations used to eliminate unusual formatting that attackers use in web requests in an effort to bypass AWS WAF.
        /// If you specify a transformation, AWS WAF performs the transformation on `field_to_match` before inspecting a request for a match.
        /// e.g. `CMD_LINE`, `HTML_ENTITY_DECODE` or `NONE`.
        /// See [docs](http://docs.aws.amazon.com/waf/latest/APIReference/API_SizeConstraint.html#WAF-Type-SizeConstraint-TextTransformation)
        /// for all supported values.
        /// **Note:** if you choose `BODY` as `type`, you must choose `NONE` because CloudFront forwards only the first 8192 bytes for inspection.
        /// </summary>
        [Input("textTransformation", required: true)]
        public Input<string> TextTransformation { get; set; } = null!;

        public SizeConstraintSetSizeConstraintsArgs()
        {
        }
    }

    public sealed class SizeConstraintSetSizeConstraintsFieldToMatchArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// When `type` is `HEADER`, enter the name of the header that you want to search, e.g. `User-Agent` or `Referer`.
        /// If `type` is any other value, omit this field.
        /// </summary>
        [Input("data")]
        public Input<string>? Data { get; set; }

        /// <summary>
        /// The part of the web request that you want AWS WAF to search for a specified string.
        /// e.g. `HEADER`, `METHOD` or `BODY`.
        /// See [docs](http://docs.aws.amazon.com/waf/latest/APIReference/API_FieldToMatch.html)
        /// for all supported values.
        /// </summary>
        [Input("type", required: true)]
        public Input<string> Type { get; set; } = null!;

        public SizeConstraintSetSizeConstraintsFieldToMatchArgs()
        {
        }
    }

    public sealed class SizeConstraintSetSizeConstraintsFieldToMatchGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// When `type` is `HEADER`, enter the name of the header that you want to search, e.g. `User-Agent` or `Referer`.
        /// If `type` is any other value, omit this field.
        /// </summary>
        [Input("data")]
        public Input<string>? Data { get; set; }

        /// <summary>
        /// The part of the web request that you want AWS WAF to search for a specified string.
        /// e.g. `HEADER`, `METHOD` or `BODY`.
        /// See [docs](http://docs.aws.amazon.com/waf/latest/APIReference/API_FieldToMatch.html)
        /// for all supported values.
        /// </summary>
        [Input("type", required: true)]
        public Input<string> Type { get; set; } = null!;

        public SizeConstraintSetSizeConstraintsFieldToMatchGetArgs()
        {
        }
    }

    public sealed class SizeConstraintSetSizeConstraintsGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The type of comparison you want to perform.
        /// e.g. `EQ`, `NE`, `LT`, `GT`.
        /// See [docs](http://docs.aws.amazon.com/waf/latest/APIReference/API_SizeConstraint.html#WAF-Type-SizeConstraint-ComparisonOperator) for all supported values.
        /// </summary>
        [Input("comparisonOperator", required: true)]
        public Input<string> ComparisonOperator { get; set; } = null!;

        /// <summary>
        /// Specifies where in a web request to look for the size constraint.
        /// </summary>
        [Input("fieldToMatch", required: true)]
        public Input<SizeConstraintSetSizeConstraintsFieldToMatchGetArgs> FieldToMatch { get; set; } = null!;

        /// <summary>
        /// The size in bytes that you want to compare against the size of the specified `field_to_match`.
        /// Valid values are between 0 - 21474836480 bytes (0 - 20 GB).
        /// </summary>
        [Input("size", required: true)]
        public Input<int> Size { get; set; } = null!;

        /// <summary>
        /// Text transformations used to eliminate unusual formatting that attackers use in web requests in an effort to bypass AWS WAF.
        /// If you specify a transformation, AWS WAF performs the transformation on `field_to_match` before inspecting a request for a match.
        /// e.g. `CMD_LINE`, `HTML_ENTITY_DECODE` or `NONE`.
        /// See [docs](http://docs.aws.amazon.com/waf/latest/APIReference/API_SizeConstraint.html#WAF-Type-SizeConstraint-TextTransformation)
        /// for all supported values.
        /// **Note:** if you choose `BODY` as `type`, you must choose `NONE` because CloudFront forwards only the first 8192 bytes for inspection.
        /// </summary>
        [Input("textTransformation", required: true)]
        public Input<string> TextTransformation { get; set; } = null!;

        public SizeConstraintSetSizeConstraintsGetArgs()
        {
        }
    }
    }

    namespace Outputs
    {

    [OutputType]
    public sealed class SizeConstraintSetSizeConstraints
    {
        /// <summary>
        /// The type of comparison you want to perform.
        /// e.g. `EQ`, `NE`, `LT`, `GT`.
        /// See [docs](http://docs.aws.amazon.com/waf/latest/APIReference/API_SizeConstraint.html#WAF-Type-SizeConstraint-ComparisonOperator) for all supported values.
        /// </summary>
        public readonly string ComparisonOperator;
        /// <summary>
        /// Specifies where in a web request to look for the size constraint.
        /// </summary>
        public readonly SizeConstraintSetSizeConstraintsFieldToMatch FieldToMatch;
        /// <summary>
        /// The size in bytes that you want to compare against the size of the specified `field_to_match`.
        /// Valid values are between 0 - 21474836480 bytes (0 - 20 GB).
        /// </summary>
        public readonly int Size;
        /// <summary>
        /// Text transformations used to eliminate unusual formatting that attackers use in web requests in an effort to bypass AWS WAF.
        /// If you specify a transformation, AWS WAF performs the transformation on `field_to_match` before inspecting a request for a match.
        /// e.g. `CMD_LINE`, `HTML_ENTITY_DECODE` or `NONE`.
        /// See [docs](http://docs.aws.amazon.com/waf/latest/APIReference/API_SizeConstraint.html#WAF-Type-SizeConstraint-TextTransformation)
        /// for all supported values.
        /// **Note:** if you choose `BODY` as `type`, you must choose `NONE` because CloudFront forwards only the first 8192 bytes for inspection.
        /// </summary>
        public readonly string TextTransformation;

        [OutputConstructor]
        private SizeConstraintSetSizeConstraints(
            string comparisonOperator,
            SizeConstraintSetSizeConstraintsFieldToMatch fieldToMatch,
            int size,
            string textTransformation)
        {
            ComparisonOperator = comparisonOperator;
            FieldToMatch = fieldToMatch;
            Size = size;
            TextTransformation = textTransformation;
        }
    }

    [OutputType]
    public sealed class SizeConstraintSetSizeConstraintsFieldToMatch
    {
        /// <summary>
        /// When `type` is `HEADER`, enter the name of the header that you want to search, e.g. `User-Agent` or `Referer`.
        /// If `type` is any other value, omit this field.
        /// </summary>
        public readonly string? Data;
        /// <summary>
        /// The part of the web request that you want AWS WAF to search for a specified string.
        /// e.g. `HEADER`, `METHOD` or `BODY`.
        /// See [docs](http://docs.aws.amazon.com/waf/latest/APIReference/API_FieldToMatch.html)
        /// for all supported values.
        /// </summary>
        public readonly string Type;

        [OutputConstructor]
        private SizeConstraintSetSizeConstraintsFieldToMatch(
            string? data,
            string type)
        {
            Data = data;
            Type = type;
        }
    }
    }
}
