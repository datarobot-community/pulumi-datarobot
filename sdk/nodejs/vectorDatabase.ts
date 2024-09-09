// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

/**
 * Vector database
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as datarobot from "@datarobot/pulumi-datarobot";
 *
 * const exampleUseCase = new datarobot.UseCase("exampleUseCase", {description: "Description for the example use case"});
 * const exampleDatasetFromFile = new datarobot.DatasetFromFile("exampleDatasetFromFile", {
 *     sourceFile: "[Path to file to upload]",
 *     useCaseId: exampleUseCase.id,
 * });
 * const exampleVectorDatabase = new datarobot.VectorDatabase("exampleVectorDatabase", {
 *     useCaseId: exampleUseCase.id,
 *     datasetId: exampleDatasetFromFile.id,
 * });
 * // Optional
 * // chunking_parameters = {
 * //   chunk_overlap_percentage = 0
 * //   chunk_size               = 512
 * //   chunking_method          = "recursive"
 * //   embedding_model          = "jinaai/jina-embedding-t-en-v1"
 * //   separators               = ["\n", " "]
 * // }
 * export const exampleId = exampleVectorDatabase.id;
 * ```
 */
export class VectorDatabase extends pulumi.CustomResource {
    /**
     * Get an existing VectorDatabase resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: VectorDatabaseState, opts?: pulumi.CustomResourceOptions): VectorDatabase {
        return new VectorDatabase(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'datarobot:index/vectorDatabase:VectorDatabase';

    /**
     * Returns true if the given object is an instance of VectorDatabase.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is VectorDatabase {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === VectorDatabase.__pulumiType;
    }

    /**
     * The chunking parameters for the Model.
     */
    public readonly chunkingParameters!: pulumi.Output<outputs.VectorDatabaseChunkingParameters>;
    /**
     * The id of the Vector Database.
     */
    public readonly datasetId!: pulumi.Output<string>;
    /**
     * The name of the VectorDatabase.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * The id of the Use Case.
     */
    public readonly useCaseId!: pulumi.Output<string>;

    /**
     * Create a VectorDatabase resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: VectorDatabaseArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: VectorDatabaseArgs | VectorDatabaseState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as VectorDatabaseState | undefined;
            resourceInputs["chunkingParameters"] = state ? state.chunkingParameters : undefined;
            resourceInputs["datasetId"] = state ? state.datasetId : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["useCaseId"] = state ? state.useCaseId : undefined;
        } else {
            const args = argsOrState as VectorDatabaseArgs | undefined;
            if ((!args || args.datasetId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'datasetId'");
            }
            if ((!args || args.useCaseId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'useCaseId'");
            }
            resourceInputs["chunkingParameters"] = args ? args.chunkingParameters : undefined;
            resourceInputs["datasetId"] = args ? args.datasetId : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["useCaseId"] = args ? args.useCaseId : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(VectorDatabase.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering VectorDatabase resources.
 */
export interface VectorDatabaseState {
    /**
     * The chunking parameters for the Model.
     */
    chunkingParameters?: pulumi.Input<inputs.VectorDatabaseChunkingParameters>;
    /**
     * The id of the Vector Database.
     */
    datasetId?: pulumi.Input<string>;
    /**
     * The name of the VectorDatabase.
     */
    name?: pulumi.Input<string>;
    /**
     * The id of the Use Case.
     */
    useCaseId?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a VectorDatabase resource.
 */
export interface VectorDatabaseArgs {
    /**
     * The chunking parameters for the Model.
     */
    chunkingParameters?: pulumi.Input<inputs.VectorDatabaseChunkingParameters>;
    /**
     * The id of the Vector Database.
     */
    datasetId: pulumi.Input<string>;
    /**
     * The name of the VectorDatabase.
     */
    name?: pulumi.Input<string>;
    /**
     * The id of the Use Case.
     */
    useCaseId: pulumi.Input<string>;
}
