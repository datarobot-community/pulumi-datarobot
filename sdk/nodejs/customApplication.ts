// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * Custom Application
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as datarobot from "@datarobot/pulumi-datarobot";
 *
 * const exampleApplicationSource = new datarobot.ApplicationSource("exampleApplicationSource", {files: [
 *     ["start-app.sh"],
 *     ["streamlit-app.py"],
 * ]});
 * const exampleCustomApplication = new datarobot.CustomApplication("exampleCustomApplication", {
 *     sourceVersionId: exampleApplicationSource.versionId,
 *     externalAccessEnabled: true,
 *     externalAccessRecipients: ["recipient@example.com"],
 * });
 * export const datarobotCustomApplicationId = exampleCustomApplication.id;
 * export const datarobotCustomApplicationSourceId = exampleCustomApplication.sourceId;
 * export const datarobotCustomApplicationSourceVersionId = exampleCustomApplication.sourceVersionId;
 * export const datarobotCustomApplicationUrl = exampleCustomApplication.applicationUrl;
 * ```
 */
export class CustomApplication extends pulumi.CustomResource {
    /**
     * Get an existing CustomApplication resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: CustomApplicationState, opts?: pulumi.CustomResourceOptions): CustomApplication {
        return new CustomApplication(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'datarobot:index/customApplication:CustomApplication';

    /**
     * Returns true if the given object is an instance of CustomApplication.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is CustomApplication {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === CustomApplication.__pulumiType;
    }

    /**
     * The URL of the Custom Application.
     */
    public /*out*/ readonly applicationUrl!: pulumi.Output<string>;
    /**
     * Whether external access is enabled for the Custom Application.
     */
    public readonly externalAccessEnabled!: pulumi.Output<boolean>;
    /**
     * The list of external email addresses that have access to the Custom Application.
     */
    public readonly externalAccessRecipients!: pulumi.Output<string[] | undefined>;
    /**
     * The name of the Custom Application.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * The ID of the Custom Application Source.
     */
    public /*out*/ readonly sourceId!: pulumi.Output<string>;
    /**
     * The version ID of the Custom Application Source.
     */
    public readonly sourceVersionId!: pulumi.Output<string>;

    /**
     * Create a CustomApplication resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: CustomApplicationArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: CustomApplicationArgs | CustomApplicationState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as CustomApplicationState | undefined;
            resourceInputs["applicationUrl"] = state ? state.applicationUrl : undefined;
            resourceInputs["externalAccessEnabled"] = state ? state.externalAccessEnabled : undefined;
            resourceInputs["externalAccessRecipients"] = state ? state.externalAccessRecipients : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["sourceId"] = state ? state.sourceId : undefined;
            resourceInputs["sourceVersionId"] = state ? state.sourceVersionId : undefined;
        } else {
            const args = argsOrState as CustomApplicationArgs | undefined;
            if ((!args || args.sourceVersionId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'sourceVersionId'");
            }
            resourceInputs["externalAccessEnabled"] = args ? args.externalAccessEnabled : undefined;
            resourceInputs["externalAccessRecipients"] = args ? args.externalAccessRecipients : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["sourceVersionId"] = args ? args.sourceVersionId : undefined;
            resourceInputs["applicationUrl"] = undefined /*out*/;
            resourceInputs["sourceId"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(CustomApplication.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering CustomApplication resources.
 */
export interface CustomApplicationState {
    /**
     * The URL of the Custom Application.
     */
    applicationUrl?: pulumi.Input<string>;
    /**
     * Whether external access is enabled for the Custom Application.
     */
    externalAccessEnabled?: pulumi.Input<boolean>;
    /**
     * The list of external email addresses that have access to the Custom Application.
     */
    externalAccessRecipients?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The name of the Custom Application.
     */
    name?: pulumi.Input<string>;
    /**
     * The ID of the Custom Application Source.
     */
    sourceId?: pulumi.Input<string>;
    /**
     * The version ID of the Custom Application Source.
     */
    sourceVersionId?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a CustomApplication resource.
 */
export interface CustomApplicationArgs {
    /**
     * Whether external access is enabled for the Custom Application.
     */
    externalAccessEnabled?: pulumi.Input<boolean>;
    /**
     * The list of external email addresses that have access to the Custom Application.
     */
    externalAccessRecipients?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The name of the Custom Application.
     */
    name?: pulumi.Input<string>;
    /**
     * The version ID of the Custom Application Source.
     */
    sourceVersionId: pulumi.Input<string>;
}
