// *** WARNING: this file was generated by the Lumi Terraform Bridge (TFGEN) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as lumi from "@lumi/lumi";
import * as lumirt from "@lumi/lumirt";

export class ActiveReceiptRuleSet extends lumi.NamedResource implements ActiveReceiptRuleSetArgs {
    public readonly ruleSetName: string;

    constructor(name: string, args: ActiveReceiptRuleSetArgs) {
        super(name);
        if (lumirt.defaultIfComputed(args.ruleSetName, "") === undefined) {
            throw new Error("Property argument 'ruleSetName' is required, but was missing");
        }
        this.ruleSetName = args.ruleSetName;
    }
}

export interface ActiveReceiptRuleSetArgs {
    readonly ruleSetName: string;
}
