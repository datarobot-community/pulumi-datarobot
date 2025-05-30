// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * Custom Model LLM Validation
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as datarobot from "@datarobot/pulumi-datarobot";
 *
 * const example = new datarobot.CustomModelLlmValidation("example", {
 *     deploymentId: datarobot_deployment.example.id,
 *     promptColumnName: "promptText",
 *     targetColumnName: "resultText",
 *     chatModelId: "111111111111",
 *     predictionTimeout: 100,
 *     useCaseId: datarobot.use_case.example.id,
 * });
 * export const exampleId = example.id;
 * ```
 */
export class CustomModelLlmValidation extends pulumi.CustomResource {
    /**
     * Get an existing CustomModelLlmValidation resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: CustomModelLlmValidationState, opts?: pulumi.CustomResourceOptions): CustomModelLlmValidation {
        return new CustomModelLlmValidation(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'datarobot:index/customModelLlmValidation:CustomModelLlmValidation';

    /**
     * Returns true if the given object is an instance of CustomModelLlmValidation.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is CustomModelLlmValidation {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === CustomModelLlmValidation.__pulumiType;
    }

    /**
     * The ID of the chat model to use for the custom model LLM validation.
     */
    public readonly chatModelId!: pulumi.Output<string | undefined>;
    /**
     * The ID of the custom model deployment.
     */
    public readonly deploymentId!: pulumi.Output<string>;
    /**
     * The ID of the model used in the deployment.
     */
    public readonly modelId!: pulumi.Output<string>;
    /**
     * The name to use for the validated custom model.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * The timeout in seconds for the prediction when validating a custom model. Defaults to 300.
     */
    public readonly predictionTimeout!: pulumi.Output<number>;
    /**
     * The name of the column the custom model uses for prompt text input.
     */
    public readonly promptColumnName!: pulumi.Output<string | undefined>;
    /**
     * The name of the column the custom model uses for prediction output.
     */
    public readonly targetColumnName!: pulumi.Output<string | undefined>;
    /**
     * The ID of the use case to associate with the validated custom model.
     */
    public readonly useCaseId!: pulumi.Output<string | undefined>;

    /**
     * Create a CustomModelLlmValidation resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: CustomModelLlmValidationArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: CustomModelLlmValidationArgs | CustomModelLlmValidationState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as CustomModelLlmValidationState | undefined;
            resourceInputs["chatModelId"] = state ? state.chatModelId : undefined;
            resourceInputs["deploymentId"] = state ? state.deploymentId : undefined;
            resourceInputs["modelId"] = state ? state.modelId : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["predictionTimeout"] = state ? state.predictionTimeout : undefined;
            resourceInputs["promptColumnName"] = state ? state.promptColumnName : undefined;
            resourceInputs["targetColumnName"] = state ? state.targetColumnName : undefined;
            resourceInputs["useCaseId"] = state ? state.useCaseId : undefined;
        } else {
            const args = argsOrState as CustomModelLlmValidationArgs | undefined;
            if ((!args || args.deploymentId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'deploymentId'");
            }
            resourceInputs["chatModelId"] = args ? args.chatModelId : undefined;
            resourceInputs["deploymentId"] = args ? args.deploymentId : undefined;
            resourceInputs["modelId"] = args ? args.modelId : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["predictionTimeout"] = args ? args.predictionTimeout : undefined;
            resourceInputs["promptColumnName"] = args ? args.promptColumnName : undefined;
            resourceInputs["targetColumnName"] = args ? args.targetColumnName : undefined;
            resourceInputs["useCaseId"] = args ? args.useCaseId : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(CustomModelLlmValidation.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering CustomModelLlmValidation resources.
 */
export interface CustomModelLlmValidationState {
    /**
     * The ID of the chat model to use for the custom model LLM validation.
     */
    chatModelId?: pulumi.Input<string>;
    /**
     * The ID of the custom model deployment.
     */
    deploymentId?: pulumi.Input<string>;
    /**
     * The ID of the model used in the deployment.
     */
    modelId?: pulumi.Input<string>;
    /**
     * The name to use for the validated custom model.
     */
    name?: pulumi.Input<string>;
    /**
     * The timeout in seconds for the prediction when validating a custom model. Defaults to 300.
     */
    predictionTimeout?: pulumi.Input<number>;
    /**
     * The name of the column the custom model uses for prompt text input.
     */
    promptColumnName?: pulumi.Input<string>;
    /**
     * The name of the column the custom model uses for prediction output.
     */
    targetColumnName?: pulumi.Input<string>;
    /**
     * The ID of the use case to associate with the validated custom model.
     */
    useCaseId?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a CustomModelLlmValidation resource.
 */
export interface CustomModelLlmValidationArgs {
    /**
     * The ID of the chat model to use for the custom model LLM validation.
     */
    chatModelId?: pulumi.Input<string>;
    /**
     * The ID of the custom model deployment.
     */
    deploymentId: pulumi.Input<string>;
    /**
     * The ID of the model used in the deployment.
     */
    modelId?: pulumi.Input<string>;
    /**
     * The name to use for the validated custom model.
     */
    name?: pulumi.Input<string>;
    /**
     * The timeout in seconds for the prediction when validating a custom model. Defaults to 300.
     */
    predictionTimeout?: pulumi.Input<number>;
    /**
     * The name of the column the custom model uses for prompt text input.
     */
    promptColumnName?: pulumi.Input<string>;
    /**
     * The name of the column the custom model uses for prediction output.
     */
    targetColumnName?: pulumi.Input<string>;
    /**
     * The ID of the use case to associate with the validated custom model.
     */
    useCaseId?: pulumi.Input<string>;
}
