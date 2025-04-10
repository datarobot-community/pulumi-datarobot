// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

/**
 * Custom Job
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as datarobot from "@datarobot/pulumi-datarobot";
 *
 * const example = new datarobot.CustomMetricJob("example", {
 *     files: [
 *         "file1.py",
 *         "file2.py",
 *     ],
 *     environmentId: "65f9b27eab986d30d4c64268",
 *     description: "Example Custom Metric Job Description",
 *     runtimeParameterValues: [{
 *         key: "EXAMPLE_PARAM",
 *         type: "string",
 *         value: "val",
 *     }],
 *     egressNetworkPolicy: "none",
 *     resourceBundleId: "cpu.micro",
 *     units: "count",
 *     directionality: "lowerIsBetter",
 *     type: "sum",
 *     isModelSpecific: false,
 * });
 * export const exampleId = example.id;
 * ```
 */
export class CustomMetricJob extends pulumi.CustomResource {
    /**
     * Get an existing CustomMetricJob resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: CustomMetricJobState, opts?: pulumi.CustomResourceOptions): CustomMetricJob {
        return new CustomMetricJob(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'datarobot:index/customMetricJob:CustomMetricJob';

    /**
     * Returns true if the given object is an instance of CustomMetricJob.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is CustomMetricJob {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === CustomMetricJob.__pulumiType;
    }

    /**
     * The description of the Custom Metric Job.
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * The directionality of the Custom Metric.
     */
    public readonly directionality!: pulumi.Output<string>;
    /**
     * The egress network policy for the Job.
     */
    public readonly egressNetworkPolicy!: pulumi.Output<string>;
    /**
     * The ID of the environment to use with the Job.
     */
    public readonly environmentId!: pulumi.Output<string>;
    /**
     * The ID of the environment version to use with the Job.
     */
    public readonly environmentVersionId!: pulumi.Output<string>;
    /**
     * The list of tuples, where values in each tuple are the local filesystem path and the path the file should be placed in the Job. If list is of strings, then basenames will be used for tuples.
     */
    public readonly files!: pulumi.Output<any | undefined>;
    /**
     * The hash of file contents for each file in files.
     */
    public /*out*/ readonly filesHashes!: pulumi.Output<string[]>;
    /**
     * The path to a folder containing files to be uploaded. Each file in the folder is uploaded under path relative to a folder path.
     */
    public readonly folderPath!: pulumi.Output<string | undefined>;
    /**
     * The hash of the folder path contents.
     */
    public /*out*/ readonly folderPathHash!: pulumi.Output<string>;
    /**
     * Determines whether the metric is related to the model or deployment.
     */
    public readonly isModelSpecific!: pulumi.Output<boolean>;
    /**
     * The name of the Custom Metric Job.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * A single identifier that represents a bundle of resources: Memory, CPU, GPU, etc.
     */
    public readonly resourceBundleId!: pulumi.Output<string | undefined>;
    /**
     * Additional parameters to be injected into a Job at runtime.
     */
    public readonly runtimeParameterValues!: pulumi.Output<outputs.CustomMetricJobRuntimeParameterValue[]>;
    /**
     * Custom metric time bucket size.
     */
    public readonly timeStep!: pulumi.Output<string>;
    /**
     * The aggregation type of the custom metric.
     */
    public readonly type!: pulumi.Output<string>;
    /**
     * The units, or the y-axis label, of the given custom metric.
     */
    public readonly units!: pulumi.Output<string>;

    /**
     * Create a CustomMetricJob resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: CustomMetricJobArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: CustomMetricJobArgs | CustomMetricJobState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as CustomMetricJobState | undefined;
            resourceInputs["description"] = state ? state.description : undefined;
            resourceInputs["directionality"] = state ? state.directionality : undefined;
            resourceInputs["egressNetworkPolicy"] = state ? state.egressNetworkPolicy : undefined;
            resourceInputs["environmentId"] = state ? state.environmentId : undefined;
            resourceInputs["environmentVersionId"] = state ? state.environmentVersionId : undefined;
            resourceInputs["files"] = state ? state.files : undefined;
            resourceInputs["filesHashes"] = state ? state.filesHashes : undefined;
            resourceInputs["folderPath"] = state ? state.folderPath : undefined;
            resourceInputs["folderPathHash"] = state ? state.folderPathHash : undefined;
            resourceInputs["isModelSpecific"] = state ? state.isModelSpecific : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["resourceBundleId"] = state ? state.resourceBundleId : undefined;
            resourceInputs["runtimeParameterValues"] = state ? state.runtimeParameterValues : undefined;
            resourceInputs["timeStep"] = state ? state.timeStep : undefined;
            resourceInputs["type"] = state ? state.type : undefined;
            resourceInputs["units"] = state ? state.units : undefined;
        } else {
            const args = argsOrState as CustomMetricJobArgs | undefined;
            resourceInputs["description"] = args ? args.description : undefined;
            resourceInputs["directionality"] = args ? args.directionality : undefined;
            resourceInputs["egressNetworkPolicy"] = args ? args.egressNetworkPolicy : undefined;
            resourceInputs["environmentId"] = args ? args.environmentId : undefined;
            resourceInputs["environmentVersionId"] = args ? args.environmentVersionId : undefined;
            resourceInputs["files"] = args ? args.files : undefined;
            resourceInputs["folderPath"] = args ? args.folderPath : undefined;
            resourceInputs["isModelSpecific"] = args ? args.isModelSpecific : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["resourceBundleId"] = args ? args.resourceBundleId : undefined;
            resourceInputs["runtimeParameterValues"] = args ? args.runtimeParameterValues : undefined;
            resourceInputs["timeStep"] = args ? args.timeStep : undefined;
            resourceInputs["type"] = args ? args.type : undefined;
            resourceInputs["units"] = args ? args.units : undefined;
            resourceInputs["filesHashes"] = undefined /*out*/;
            resourceInputs["folderPathHash"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(CustomMetricJob.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering CustomMetricJob resources.
 */
export interface CustomMetricJobState {
    /**
     * The description of the Custom Metric Job.
     */
    description?: pulumi.Input<string>;
    /**
     * The directionality of the Custom Metric.
     */
    directionality?: pulumi.Input<string>;
    /**
     * The egress network policy for the Job.
     */
    egressNetworkPolicy?: pulumi.Input<string>;
    /**
     * The ID of the environment to use with the Job.
     */
    environmentId?: pulumi.Input<string>;
    /**
     * The ID of the environment version to use with the Job.
     */
    environmentVersionId?: pulumi.Input<string>;
    /**
     * The list of tuples, where values in each tuple are the local filesystem path and the path the file should be placed in the Job. If list is of strings, then basenames will be used for tuples.
     */
    files?: any;
    /**
     * The hash of file contents for each file in files.
     */
    filesHashes?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The path to a folder containing files to be uploaded. Each file in the folder is uploaded under path relative to a folder path.
     */
    folderPath?: pulumi.Input<string>;
    /**
     * The hash of the folder path contents.
     */
    folderPathHash?: pulumi.Input<string>;
    /**
     * Determines whether the metric is related to the model or deployment.
     */
    isModelSpecific?: pulumi.Input<boolean>;
    /**
     * The name of the Custom Metric Job.
     */
    name?: pulumi.Input<string>;
    /**
     * A single identifier that represents a bundle of resources: Memory, CPU, GPU, etc.
     */
    resourceBundleId?: pulumi.Input<string>;
    /**
     * Additional parameters to be injected into a Job at runtime.
     */
    runtimeParameterValues?: pulumi.Input<pulumi.Input<inputs.CustomMetricJobRuntimeParameterValue>[]>;
    /**
     * Custom metric time bucket size.
     */
    timeStep?: pulumi.Input<string>;
    /**
     * The aggregation type of the custom metric.
     */
    type?: pulumi.Input<string>;
    /**
     * The units, or the y-axis label, of the given custom metric.
     */
    units?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a CustomMetricJob resource.
 */
export interface CustomMetricJobArgs {
    /**
     * The description of the Custom Metric Job.
     */
    description?: pulumi.Input<string>;
    /**
     * The directionality of the Custom Metric.
     */
    directionality?: pulumi.Input<string>;
    /**
     * The egress network policy for the Job.
     */
    egressNetworkPolicy?: pulumi.Input<string>;
    /**
     * The ID of the environment to use with the Job.
     */
    environmentId?: pulumi.Input<string>;
    /**
     * The ID of the environment version to use with the Job.
     */
    environmentVersionId?: pulumi.Input<string>;
    /**
     * The list of tuples, where values in each tuple are the local filesystem path and the path the file should be placed in the Job. If list is of strings, then basenames will be used for tuples.
     */
    files?: any;
    /**
     * The path to a folder containing files to be uploaded. Each file in the folder is uploaded under path relative to a folder path.
     */
    folderPath?: pulumi.Input<string>;
    /**
     * Determines whether the metric is related to the model or deployment.
     */
    isModelSpecific?: pulumi.Input<boolean>;
    /**
     * The name of the Custom Metric Job.
     */
    name?: pulumi.Input<string>;
    /**
     * A single identifier that represents a bundle of resources: Memory, CPU, GPU, etc.
     */
    resourceBundleId?: pulumi.Input<string>;
    /**
     * Additional parameters to be injected into a Job at runtime.
     */
    runtimeParameterValues?: pulumi.Input<pulumi.Input<inputs.CustomMetricJobRuntimeParameterValue>[]>;
    /**
     * Custom metric time bucket size.
     */
    timeStep?: pulumi.Input<string>;
    /**
     * The aggregation type of the custom metric.
     */
    type?: pulumi.Input<string>;
    /**
     * The units, or the y-axis label, of the given custom metric.
     */
    units?: pulumi.Input<string>;
}
