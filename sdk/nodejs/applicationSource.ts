// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

/**
 * Application Source
 */
export class ApplicationSource extends pulumi.CustomResource {
    /**
     * Get an existing ApplicationSource resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ApplicationSourceState, opts?: pulumi.CustomResourceOptions): ApplicationSource {
        return new ApplicationSource(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'datarobot:index/applicationSource:ApplicationSource';

    /**
     * Returns true if the given object is an instance of ApplicationSource.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is ApplicationSource {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === ApplicationSource.__pulumiType;
    }

    /**
     * The ID of the base environment for the Application Source.
     */
    public readonly baseEnvironmentId!: pulumi.Output<string>;
    /**
     * The ID of the base environment version for the Application Source.
     */
    public readonly baseEnvironmentVersionId!: pulumi.Output<string>;
    /**
     * The list of tuples, where values in each tuple are the local filesystem path and the path the file should be placed in the Application Source. If list is of strings, then basenames will be used for tuples.
     */
    public readonly files!: pulumi.Output<any | undefined>;
    /**
     * The hash of file contents for each file in files.
     */
    public /*out*/ readonly filesHashes!: pulumi.Output<string[]>;
    /**
     * The path to a folder containing files to build the Application Source. Each file in the folder is uploaded under path relative to a folder path.
     */
    public readonly folderPath!: pulumi.Output<string | undefined>;
    /**
     * The hash of the folder path contents.
     */
    public /*out*/ readonly folderPathHash!: pulumi.Output<string>;
    /**
     * The name of the Application Source.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * The resources for the Application Source.
     */
    public readonly resources!: pulumi.Output<outputs.ApplicationSourceResources | undefined>;
    /**
     * The runtime parameter values for the Application Source.
     */
    public readonly runtimeParameterValues!: pulumi.Output<outputs.ApplicationSourceRuntimeParameterValue[]>;
    /**
     * The version ID of the Application Source.
     */
    public /*out*/ readonly versionId!: pulumi.Output<string>;

    /**
     * Create a ApplicationSource resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: ApplicationSourceArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: ApplicationSourceArgs | ApplicationSourceState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as ApplicationSourceState | undefined;
            resourceInputs["baseEnvironmentId"] = state ? state.baseEnvironmentId : undefined;
            resourceInputs["baseEnvironmentVersionId"] = state ? state.baseEnvironmentVersionId : undefined;
            resourceInputs["files"] = state ? state.files : undefined;
            resourceInputs["filesHashes"] = state ? state.filesHashes : undefined;
            resourceInputs["folderPath"] = state ? state.folderPath : undefined;
            resourceInputs["folderPathHash"] = state ? state.folderPathHash : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["resources"] = state ? state.resources : undefined;
            resourceInputs["runtimeParameterValues"] = state ? state.runtimeParameterValues : undefined;
            resourceInputs["versionId"] = state ? state.versionId : undefined;
        } else {
            const args = argsOrState as ApplicationSourceArgs | undefined;
            resourceInputs["baseEnvironmentId"] = args ? args.baseEnvironmentId : undefined;
            resourceInputs["baseEnvironmentVersionId"] = args ? args.baseEnvironmentVersionId : undefined;
            resourceInputs["files"] = args ? args.files : undefined;
            resourceInputs["folderPath"] = args ? args.folderPath : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["resources"] = args ? args.resources : undefined;
            resourceInputs["runtimeParameterValues"] = args ? args.runtimeParameterValues : undefined;
            resourceInputs["filesHashes"] = undefined /*out*/;
            resourceInputs["folderPathHash"] = undefined /*out*/;
            resourceInputs["versionId"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(ApplicationSource.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering ApplicationSource resources.
 */
export interface ApplicationSourceState {
    /**
     * The ID of the base environment for the Application Source.
     */
    baseEnvironmentId?: pulumi.Input<string>;
    /**
     * The ID of the base environment version for the Application Source.
     */
    baseEnvironmentVersionId?: pulumi.Input<string>;
    /**
     * The list of tuples, where values in each tuple are the local filesystem path and the path the file should be placed in the Application Source. If list is of strings, then basenames will be used for tuples.
     */
    files?: any;
    /**
     * The hash of file contents for each file in files.
     */
    filesHashes?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The path to a folder containing files to build the Application Source. Each file in the folder is uploaded under path relative to a folder path.
     */
    folderPath?: pulumi.Input<string>;
    /**
     * The hash of the folder path contents.
     */
    folderPathHash?: pulumi.Input<string>;
    /**
     * The name of the Application Source.
     */
    name?: pulumi.Input<string>;
    /**
     * The resources for the Application Source.
     */
    resources?: pulumi.Input<inputs.ApplicationSourceResources>;
    /**
     * The runtime parameter values for the Application Source.
     */
    runtimeParameterValues?: pulumi.Input<pulumi.Input<inputs.ApplicationSourceRuntimeParameterValue>[]>;
    /**
     * The version ID of the Application Source.
     */
    versionId?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a ApplicationSource resource.
 */
export interface ApplicationSourceArgs {
    /**
     * The ID of the base environment for the Application Source.
     */
    baseEnvironmentId?: pulumi.Input<string>;
    /**
     * The ID of the base environment version for the Application Source.
     */
    baseEnvironmentVersionId?: pulumi.Input<string>;
    /**
     * The list of tuples, where values in each tuple are the local filesystem path and the path the file should be placed in the Application Source. If list is of strings, then basenames will be used for tuples.
     */
    files?: any;
    /**
     * The path to a folder containing files to build the Application Source. Each file in the folder is uploaded under path relative to a folder path.
     */
    folderPath?: pulumi.Input<string>;
    /**
     * The name of the Application Source.
     */
    name?: pulumi.Input<string>;
    /**
     * The resources for the Application Source.
     */
    resources?: pulumi.Input<inputs.ApplicationSourceResources>;
    /**
     * The runtime parameter values for the Application Source.
     */
    runtimeParameterValues?: pulumi.Input<pulumi.Input<inputs.ApplicationSourceRuntimeParameterValue>[]>;
}
