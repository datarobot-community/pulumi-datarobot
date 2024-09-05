// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

/**
 * Deployment
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
 *     localFiles: ["example.py"],
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
 * // Optional settings
 * // settings = {
 * //   prediction_row_storage = true
 * // }
 * export const datarobotDeploymentId = exampleDeployment.id;
 * ```
 */
export class Deployment extends pulumi.CustomResource {
    /**
     * Get an existing Deployment resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: DeploymentState, opts?: pulumi.CustomResourceOptions): Deployment {
        return new Deployment(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'datarobot:index/deployment:Deployment';

    /**
     * Returns true if the given object is an instance of Deployment.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Deployment {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Deployment.__pulumiType;
    }

    /**
     * The label of the Deployment.
     */
    public readonly label!: pulumi.Output<string>;
    /**
     * The ID of the predication environment for this Deployment.
     */
    public readonly predictionEnvironmentId!: pulumi.Output<string>;
    /**
     * The ID of the registered model version for this Deployment.
     */
    public readonly registeredModelVersionId!: pulumi.Output<string>;
    /**
     * The settings for the Deployment.
     */
    public readonly settings!: pulumi.Output<outputs.DeploymentSettings | undefined>;

    /**
     * Create a Deployment resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: DeploymentArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: DeploymentArgs | DeploymentState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as DeploymentState | undefined;
            resourceInputs["label"] = state ? state.label : undefined;
            resourceInputs["predictionEnvironmentId"] = state ? state.predictionEnvironmentId : undefined;
            resourceInputs["registeredModelVersionId"] = state ? state.registeredModelVersionId : undefined;
            resourceInputs["settings"] = state ? state.settings : undefined;
        } else {
            const args = argsOrState as DeploymentArgs | undefined;
            if ((!args || args.label === undefined) && !opts.urn) {
                throw new Error("Missing required property 'label'");
            }
            if ((!args || args.predictionEnvironmentId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'predictionEnvironmentId'");
            }
            if ((!args || args.registeredModelVersionId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'registeredModelVersionId'");
            }
            resourceInputs["label"] = args ? args.label : undefined;
            resourceInputs["predictionEnvironmentId"] = args ? args.predictionEnvironmentId : undefined;
            resourceInputs["registeredModelVersionId"] = args ? args.registeredModelVersionId : undefined;
            resourceInputs["settings"] = args ? args.settings : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(Deployment.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Deployment resources.
 */
export interface DeploymentState {
    /**
     * The label of the Deployment.
     */
    label?: pulumi.Input<string>;
    /**
     * The ID of the predication environment for this Deployment.
     */
    predictionEnvironmentId?: pulumi.Input<string>;
    /**
     * The ID of the registered model version for this Deployment.
     */
    registeredModelVersionId?: pulumi.Input<string>;
    /**
     * The settings for the Deployment.
     */
    settings?: pulumi.Input<inputs.DeploymentSettings>;
}

/**
 * The set of arguments for constructing a Deployment resource.
 */
export interface DeploymentArgs {
    /**
     * The label of the Deployment.
     */
    label: pulumi.Input<string>;
    /**
     * The ID of the predication environment for this Deployment.
     */
    predictionEnvironmentId: pulumi.Input<string>;
    /**
     * The ID of the registered model version for this Deployment.
     */
    registeredModelVersionId: pulumi.Input<string>;
    /**
     * The settings for the Deployment.
     */
    settings?: pulumi.Input<inputs.DeploymentSettings>;
}
