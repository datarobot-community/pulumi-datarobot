// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * Global Model
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as datarobot from "@pulumi/datarobot";
 *
 * const dummyBinaryClassification = datarobot.getGlobalModel({
 *     name: "[DataRobot] Dummy Binary Classification",
 * });
 * ```
 */
export function getGlobalModel(args: GetGlobalModelArgs, opts?: pulumi.InvokeOptions): Promise<GetGlobalModelResult> {
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("datarobot:index/getGlobalModel:getGlobalModel", {
        "name": args.name,
    }, opts);
}

/**
 * A collection of arguments for invoking getGlobalModel.
 */
export interface GetGlobalModelArgs {
    /**
     * The name of the Registered Model.
     */
    name: string;
}

/**
 * A collection of values returned by getGlobalModel.
 */
export interface GetGlobalModelResult {
    /**
     * The ID of the Global Model.
     */
    readonly id: string;
    /**
     * The name of the Registered Model.
     */
    readonly name: string;
    /**
     * The ID of the Global Model Version.
     */
    readonly versionId: string;
}
/**
 * Global Model
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as datarobot from "@pulumi/datarobot";
 *
 * const dummyBinaryClassification = datarobot.getGlobalModel({
 *     name: "[DataRobot] Dummy Binary Classification",
 * });
 * ```
 */
export function getGlobalModelOutput(args: GetGlobalModelOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetGlobalModelResult> {
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invokeOutput("datarobot:index/getGlobalModel:getGlobalModel", {
        "name": args.name,
    }, opts);
}

/**
 * A collection of arguments for invoking getGlobalModel.
 */
export interface GetGlobalModelOutputArgs {
    /**
     * The name of the Registered Model.
     */
    name: pulumi.Input<string>;
}
