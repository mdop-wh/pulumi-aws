// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.Waf
{
    /// <summary>
    /// Provides a WAF Regex Match Set Resource
    /// 
    /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/waf_regex_match_set.html.markdown.
    /// </summary>
    public partial class RegexMatchSet : Pulumi.CustomResource
    {
        /// <summary>
        /// The name or description of the Regex Match Set.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// The regular expression pattern that you want AWS WAF to search for in web requests,
        /// the location in requests that you want AWS WAF to search, and other settings. See below.
        /// </summary>
        [Output("regexMatchTuples")]
        public Output<ImmutableArray<Outputs.RegexMatchSetRegexMatchTuples>> RegexMatchTuples { get; private set; } = null!;


        /// <summary>
        /// Create a RegexMatchSet resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public RegexMatchSet(string name, RegexMatchSetArgs? args = null, CustomResourceOptions? options = null)
            : base("aws:waf/regexMatchSet:RegexMatchSet", name, args, MakeResourceOptions(options, ""))
        {
        }

        private RegexMatchSet(string name, Input<string> id, RegexMatchSetState? state = null, CustomResourceOptions? options = null)
            : base("aws:waf/regexMatchSet:RegexMatchSet", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing RegexMatchSet resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static RegexMatchSet Get(string name, Input<string> id, RegexMatchSetState? state = null, CustomResourceOptions? options = null)
        {
            return new RegexMatchSet(name, id, state, options);
        }
    }

    public sealed class RegexMatchSetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The name or description of the Regex Match Set.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("regexMatchTuples")]
        private InputList<Inputs.RegexMatchSetRegexMatchTuplesArgs>? _regexMatchTuples;

        /// <summary>
        /// The regular expression pattern that you want AWS WAF to search for in web requests,
        /// the location in requests that you want AWS WAF to search, and other settings. See below.
        /// </summary>
        public InputList<Inputs.RegexMatchSetRegexMatchTuplesArgs> RegexMatchTuples
        {
            get => _regexMatchTuples ?? (_regexMatchTuples = new InputList<Inputs.RegexMatchSetRegexMatchTuplesArgs>());
            set => _regexMatchTuples = value;
        }

        public RegexMatchSetArgs()
        {
        }
    }

    public sealed class RegexMatchSetState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The name or description of the Regex Match Set.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("regexMatchTuples")]
        private InputList<Inputs.RegexMatchSetRegexMatchTuplesGetArgs>? _regexMatchTuples;

        /// <summary>
        /// The regular expression pattern that you want AWS WAF to search for in web requests,
        /// the location in requests that you want AWS WAF to search, and other settings. See below.
        /// </summary>
        public InputList<Inputs.RegexMatchSetRegexMatchTuplesGetArgs> RegexMatchTuples
        {
            get => _regexMatchTuples ?? (_regexMatchTuples = new InputList<Inputs.RegexMatchSetRegexMatchTuplesGetArgs>());
            set => _regexMatchTuples = value;
        }

        public RegexMatchSetState()
        {
        }
    }

    namespace Inputs
    {

    public sealed class RegexMatchSetRegexMatchTuplesArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The part of a web request that you want to search, such as a specified header or a query string.
        /// </summary>
        [Input("fieldToMatch", required: true)]
        public Input<RegexMatchSetRegexMatchTuplesFieldToMatchArgs> FieldToMatch { get; set; } = null!;

        /// <summary>
        /// The ID of a [Regex Pattern Set](https://www.terraform.io/docs/providers/aws/r/waf_regex_pattern_set.html).
        /// </summary>
        [Input("regexPatternSetId", required: true)]
        public Input<string> RegexPatternSetId { get; set; } = null!;

        /// <summary>
        /// Text transformations used to eliminate unusual formatting that attackers use in web requests in an effort to bypass AWS WAF.
        /// e.g. `CMD_LINE`, `HTML_ENTITY_DECODE` or `NONE`.
        /// See [docs](http://docs.aws.amazon.com/waf/latest/APIReference/API_ByteMatchTuple.html#WAF-Type-ByteMatchTuple-TextTransformation)
        /// for all supported values.
        /// </summary>
        [Input("textTransformation", required: true)]
        public Input<string> TextTransformation { get; set; } = null!;

        public RegexMatchSetRegexMatchTuplesArgs()
        {
        }
    }

    public sealed class RegexMatchSetRegexMatchTuplesFieldToMatchArgs : Pulumi.ResourceArgs
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

        public RegexMatchSetRegexMatchTuplesFieldToMatchArgs()
        {
        }
    }

    public sealed class RegexMatchSetRegexMatchTuplesFieldToMatchGetArgs : Pulumi.ResourceArgs
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

        public RegexMatchSetRegexMatchTuplesFieldToMatchGetArgs()
        {
        }
    }

    public sealed class RegexMatchSetRegexMatchTuplesGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The part of a web request that you want to search, such as a specified header or a query string.
        /// </summary>
        [Input("fieldToMatch", required: true)]
        public Input<RegexMatchSetRegexMatchTuplesFieldToMatchGetArgs> FieldToMatch { get; set; } = null!;

        /// <summary>
        /// The ID of a [Regex Pattern Set](https://www.terraform.io/docs/providers/aws/r/waf_regex_pattern_set.html).
        /// </summary>
        [Input("regexPatternSetId", required: true)]
        public Input<string> RegexPatternSetId { get; set; } = null!;

        /// <summary>
        /// Text transformations used to eliminate unusual formatting that attackers use in web requests in an effort to bypass AWS WAF.
        /// e.g. `CMD_LINE`, `HTML_ENTITY_DECODE` or `NONE`.
        /// See [docs](http://docs.aws.amazon.com/waf/latest/APIReference/API_ByteMatchTuple.html#WAF-Type-ByteMatchTuple-TextTransformation)
        /// for all supported values.
        /// </summary>
        [Input("textTransformation", required: true)]
        public Input<string> TextTransformation { get; set; } = null!;

        public RegexMatchSetRegexMatchTuplesGetArgs()
        {
        }
    }
    }

    namespace Outputs
    {

    [OutputType]
    public sealed class RegexMatchSetRegexMatchTuples
    {
        /// <summary>
        /// The part of a web request that you want to search, such as a specified header or a query string.
        /// </summary>
        public readonly RegexMatchSetRegexMatchTuplesFieldToMatch FieldToMatch;
        /// <summary>
        /// The ID of a [Regex Pattern Set](https://www.terraform.io/docs/providers/aws/r/waf_regex_pattern_set.html).
        /// </summary>
        public readonly string RegexPatternSetId;
        /// <summary>
        /// Text transformations used to eliminate unusual formatting that attackers use in web requests in an effort to bypass AWS WAF.
        /// e.g. `CMD_LINE`, `HTML_ENTITY_DECODE` or `NONE`.
        /// See [docs](http://docs.aws.amazon.com/waf/latest/APIReference/API_ByteMatchTuple.html#WAF-Type-ByteMatchTuple-TextTransformation)
        /// for all supported values.
        /// </summary>
        public readonly string TextTransformation;

        [OutputConstructor]
        private RegexMatchSetRegexMatchTuples(
            RegexMatchSetRegexMatchTuplesFieldToMatch fieldToMatch,
            string regexPatternSetId,
            string textTransformation)
        {
            FieldToMatch = fieldToMatch;
            RegexPatternSetId = regexPatternSetId;
            TextTransformation = textTransformation;
        }
    }

    [OutputType]
    public sealed class RegexMatchSetRegexMatchTuplesFieldToMatch
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
        private RegexMatchSetRegexMatchTuplesFieldToMatch(
            string? data,
            string type)
        {
            Data = data;
            Type = type;
        }
    }
    }
}
