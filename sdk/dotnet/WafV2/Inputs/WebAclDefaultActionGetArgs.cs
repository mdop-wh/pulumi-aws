// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.WafV2.Inputs
{

    public sealed class WebAclDefaultActionGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Specifies that AWS WAF should allow requests by default.
        /// </summary>
        [Input("allow")]
        public Input<Inputs.WebAclDefaultActionAllowGetArgs>? Allow { get; set; }

        /// <summary>
        /// Specifies that AWS WAF should block requests by default.
        /// </summary>
        [Input("block")]
        public Input<Inputs.WebAclDefaultActionBlockGetArgs>? Block { get; set; }

        public WebAclDefaultActionGetArgs()
        {
        }
    }
}