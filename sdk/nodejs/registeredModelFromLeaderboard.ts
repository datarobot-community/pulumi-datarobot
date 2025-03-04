// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * registered model from leaderboard
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as datarobot from "@datarobot/pulumi-datarobot";
 *
 * const example = new datarobot.RegisteredModelFromLeaderboard("example", {
 *     modelId: "111111111111",
 *     description: "example description",
 *     versionName: "example version name",
 *     predictionThreshold: 0.5,
 *     computeAllTsIntervals: true,
 *     distributionPredictionModelId: "222222222222",
 *     useCaseIds: [datarobot_use_case.example.id],
 * });
 * export const datarobotRegisteredModelFromLeaderboardId = example.id;
 * export const datarobotRegisteredModelFromLeaderboardVersionId = example.versionId;
 * ```
 */
export class RegisteredModelFromLeaderboard extends pulumi.CustomResource {
    /**
     * Get an existing RegisteredModelFromLeaderboard resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: RegisteredModelFromLeaderboardState, opts?: pulumi.CustomResourceOptions): RegisteredModelFromLeaderboard {
        return new RegisteredModelFromLeaderboard(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'datarobot:index/registeredModelFromLeaderboard:RegisteredModelFromLeaderboard';

    /**
     * Returns true if the given object is an instance of RegisteredModelFromLeaderboard.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is RegisteredModelFromLeaderboard {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === RegisteredModelFromLeaderboard.__pulumiType;
    }

    /**
     * Whether to compute all time series intervals (1-100 percentiles).
     */
    public readonly computeAllTsIntervals!: pulumi.Output<boolean | undefined>;
    /**
     * The description of the Registered Model.
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * The ID of the DataRobot distribution prediction model trained on predictions from the DataRobot model.
     */
    public readonly distributionPredictionModelId!: pulumi.Output<string | undefined>;
    /**
     * The ID of the DataRobot model for this Registered Model.
     */
    public readonly modelId!: pulumi.Output<string>;
    /**
     * The name of the Registered Model.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * The prediction threshold for the model.
     */
    public readonly predictionThreshold!: pulumi.Output<number | undefined>;
    /**
     * The list of Use Case IDs to add the Registered Model version to.
     */
    public readonly useCaseIds!: pulumi.Output<string[] | undefined>;
    /**
     * The ID of the Registered Model Version.
     */
    public /*out*/ readonly versionId!: pulumi.Output<string>;
    /**
     * The name of the Registered Model Version.
     */
    public readonly versionName!: pulumi.Output<string>;

    /**
     * Create a RegisteredModelFromLeaderboard resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: RegisteredModelFromLeaderboardArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: RegisteredModelFromLeaderboardArgs | RegisteredModelFromLeaderboardState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as RegisteredModelFromLeaderboardState | undefined;
            resourceInputs["computeAllTsIntervals"] = state ? state.computeAllTsIntervals : undefined;
            resourceInputs["description"] = state ? state.description : undefined;
            resourceInputs["distributionPredictionModelId"] = state ? state.distributionPredictionModelId : undefined;
            resourceInputs["modelId"] = state ? state.modelId : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["predictionThreshold"] = state ? state.predictionThreshold : undefined;
            resourceInputs["useCaseIds"] = state ? state.useCaseIds : undefined;
            resourceInputs["versionId"] = state ? state.versionId : undefined;
            resourceInputs["versionName"] = state ? state.versionName : undefined;
        } else {
            const args = argsOrState as RegisteredModelFromLeaderboardArgs | undefined;
            if ((!args || args.modelId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'modelId'");
            }
            resourceInputs["computeAllTsIntervals"] = args ? args.computeAllTsIntervals : undefined;
            resourceInputs["description"] = args ? args.description : undefined;
            resourceInputs["distributionPredictionModelId"] = args ? args.distributionPredictionModelId : undefined;
            resourceInputs["modelId"] = args ? args.modelId : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["predictionThreshold"] = args ? args.predictionThreshold : undefined;
            resourceInputs["useCaseIds"] = args ? args.useCaseIds : undefined;
            resourceInputs["versionName"] = args ? args.versionName : undefined;
            resourceInputs["versionId"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(RegisteredModelFromLeaderboard.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering RegisteredModelFromLeaderboard resources.
 */
export interface RegisteredModelFromLeaderboardState {
    /**
     * Whether to compute all time series intervals (1-100 percentiles).
     */
    computeAllTsIntervals?: pulumi.Input<boolean>;
    /**
     * The description of the Registered Model.
     */
    description?: pulumi.Input<string>;
    /**
     * The ID of the DataRobot distribution prediction model trained on predictions from the DataRobot model.
     */
    distributionPredictionModelId?: pulumi.Input<string>;
    /**
     * The ID of the DataRobot model for this Registered Model.
     */
    modelId?: pulumi.Input<string>;
    /**
     * The name of the Registered Model.
     */
    name?: pulumi.Input<string>;
    /**
     * The prediction threshold for the model.
     */
    predictionThreshold?: pulumi.Input<number>;
    /**
     * The list of Use Case IDs to add the Registered Model version to.
     */
    useCaseIds?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The ID of the Registered Model Version.
     */
    versionId?: pulumi.Input<string>;
    /**
     * The name of the Registered Model Version.
     */
    versionName?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a RegisteredModelFromLeaderboard resource.
 */
export interface RegisteredModelFromLeaderboardArgs {
    /**
     * Whether to compute all time series intervals (1-100 percentiles).
     */
    computeAllTsIntervals?: pulumi.Input<boolean>;
    /**
     * The description of the Registered Model.
     */
    description?: pulumi.Input<string>;
    /**
     * The ID of the DataRobot distribution prediction model trained on predictions from the DataRobot model.
     */
    distributionPredictionModelId?: pulumi.Input<string>;
    /**
     * The ID of the DataRobot model for this Registered Model.
     */
    modelId: pulumi.Input<string>;
    /**
     * The name of the Registered Model.
     */
    name?: pulumi.Input<string>;
    /**
     * The prediction threshold for the model.
     */
    predictionThreshold?: pulumi.Input<number>;
    /**
     * The list of Use Case IDs to add the Registered Model version to.
     */
    useCaseIds?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The name of the Registered Model Version.
     */
    versionName?: pulumi.Input<string>;
}
