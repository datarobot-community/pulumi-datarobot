// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * Q&A Application
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as datarobot from "@pulumi/datarobot";
 *
 * const exampleCustomModel = new datarobot.CustomModel("exampleCustomModel", {
 *     description: "Description for the example custom model",
 *     targetType: "Binary",
 *     targetName: "my_label",
 *     baseEnvironmentName: "[GenAI] Python 3.11 with Moderations",
 *     files: ["example.py"],
 * });
 * const exampleRegisteredModel = new datarobot.RegisteredModel("exampleRegisteredModel", {
 *     customModelVersionId: exampleCustomModel.versionId,
 *     description: "Description for the example registered model",
 * });
 * const examplePredictionEnvironment = new datarobot.PredictionEnvironment("examplePredictionEnvironment", {
 *     description: "Description for the example prediction environment",
 *     platform: "datarobotServerless",
 * });
 * const exampleDeployment = new datarobot.Deployment("exampleDeployment", {
 *     label: "An example deployment",
 *     predictionEnvironmentId: examplePredictionEnvironment.id,
 *     registeredModelVersionId: exampleRegisteredModel.versionId,
 * });
 * const exampleQaApplication = new datarobot.QaApplication("exampleQaApplication", {
 *     deploymentId: exampleDeployment.id,
 *     externalAccessEnabled: true,
 *     externalAccessRecipients: ["recipient@example.com"],
 * });
 * export const datarobotQaApplicationId = exampleQaApplication.id;
 * export const datarobotQaApplicationSourceId = exampleQaApplication.sourceId;
 * export const datarobotQaApplicationSourceVersionId = exampleQaApplication.sourceVersionId;
 * export const datarobotQaApplicationUrl = exampleQaApplication.applicationUrl;
 * ```
 */
export class QaApplication extends pulumi.CustomResource {
    /**
     * Get an existing QaApplication resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: QaApplicationState, opts?: pulumi.CustomResourceOptions): QaApplication {
        return new QaApplication(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'datarobot:index/qaApplication:QaApplication';

    /**
     * Returns true if the given object is an instance of QaApplication.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is QaApplication {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === QaApplication.__pulumiType;
    }

    /**
     * The URL of the Q&A Application.
     */
    public /*out*/ readonly applicationUrl!: pulumi.Output<string>;
    /**
     * The deployment ID of the Q&A Application.
     */
    public readonly deploymentId!: pulumi.Output<string>;
    /**
     * Whether external access is enabled for the Q&A Application.
     */
    public readonly externalAccessEnabled!: pulumi.Output<boolean>;
    /**
     * The list of external email addresses that have access to the Q&A Application.
     */
    public readonly externalAccessRecipients!: pulumi.Output<string[] | undefined>;
    /**
     * The name of the Q&A Application.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * The ID of the Q&A Application Source.
     */
    public /*out*/ readonly sourceId!: pulumi.Output<string>;
    /**
     * The version ID of the Q&A Application Source.
     */
    public /*out*/ readonly sourceVersionId!: pulumi.Output<string>;

    /**
     * Create a QaApplication resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: QaApplicationArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: QaApplicationArgs | QaApplicationState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as QaApplicationState | undefined;
            resourceInputs["applicationUrl"] = state ? state.applicationUrl : undefined;
            resourceInputs["deploymentId"] = state ? state.deploymentId : undefined;
            resourceInputs["externalAccessEnabled"] = state ? state.externalAccessEnabled : undefined;
            resourceInputs["externalAccessRecipients"] = state ? state.externalAccessRecipients : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["sourceId"] = state ? state.sourceId : undefined;
            resourceInputs["sourceVersionId"] = state ? state.sourceVersionId : undefined;
        } else {
            const args = argsOrState as QaApplicationArgs | undefined;
            if ((!args || args.deploymentId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'deploymentId'");
            }
            resourceInputs["deploymentId"] = args ? args.deploymentId : undefined;
            resourceInputs["externalAccessEnabled"] = args ? args.externalAccessEnabled : undefined;
            resourceInputs["externalAccessRecipients"] = args ? args.externalAccessRecipients : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["applicationUrl"] = undefined /*out*/;
            resourceInputs["sourceId"] = undefined /*out*/;
            resourceInputs["sourceVersionId"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(QaApplication.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering QaApplication resources.
 */
export interface QaApplicationState {
    /**
     * The URL of the Q&A Application.
     */
    applicationUrl?: pulumi.Input<string>;
    /**
     * The deployment ID of the Q&A Application.
     */
    deploymentId?: pulumi.Input<string>;
    /**
     * Whether external access is enabled for the Q&A Application.
     */
    externalAccessEnabled?: pulumi.Input<boolean>;
    /**
     * The list of external email addresses that have access to the Q&A Application.
     */
    externalAccessRecipients?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The name of the Q&A Application.
     */
    name?: pulumi.Input<string>;
    /**
     * The ID of the Q&A Application Source.
     */
    sourceId?: pulumi.Input<string>;
    /**
     * The version ID of the Q&A Application Source.
     */
    sourceVersionId?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a QaApplication resource.
 */
export interface QaApplicationArgs {
    /**
     * The deployment ID of the Q&A Application.
     */
    deploymentId: pulumi.Input<string>;
    /**
     * Whether external access is enabled for the Q&A Application.
     */
    externalAccessEnabled?: pulumi.Input<boolean>;
    /**
     * The list of external email addresses that have access to the Q&A Application.
     */
    externalAccessRecipients?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The name of the Q&A Application.
     */
    name?: pulumi.Input<string>;
}
