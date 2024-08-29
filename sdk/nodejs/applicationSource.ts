// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
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
     * The list of local file paths used to build the Application Source.
     */
    public readonly localFiles!: pulumi.Output<string[]>;
    /**
     * The name of the Application Source.
     */
    public readonly name!: pulumi.Output<string>;
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
    constructor(name: string, args: ApplicationSourceArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: ApplicationSourceArgs | ApplicationSourceState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as ApplicationSourceState | undefined;
            resourceInputs["localFiles"] = state ? state.localFiles : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["versionId"] = state ? state.versionId : undefined;
        } else {
            const args = argsOrState as ApplicationSourceArgs | undefined;
            if ((!args || args.localFiles === undefined) && !opts.urn) {
                throw new Error("Missing required property 'localFiles'");
            }
            resourceInputs["localFiles"] = args ? args.localFiles : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
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
     * The list of local file paths used to build the Application Source.
     */
    localFiles?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The name of the Application Source.
     */
    name?: pulumi.Input<string>;
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
     * The list of local file paths used to build the Application Source.
     */
    localFiles: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The name of the Application Source.
     */
    name?: pulumi.Input<string>;
}