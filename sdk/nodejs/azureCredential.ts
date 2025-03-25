// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * Azure Credential
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as datarobot from "@datarobot/pulumi-datarobot";
 *
 * const example = new datarobot.AzureCredential("example", {
 *     azureConnectionString: "example_connection_string",
 *     description: "Description for the example Azure credential",
 * });
 * ```
 */
export class AzureCredential extends pulumi.CustomResource {
    /**
     * Get an existing AzureCredential resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: AzureCredentialState, opts?: pulumi.CustomResourceOptions): AzureCredential {
        return new AzureCredential(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'datarobot:index/azureCredential:AzureCredential';

    /**
     * Returns true if the given object is an instance of AzureCredential.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is AzureCredential {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === AzureCredential.__pulumiType;
    }

    /**
     * The connection string of the Azure Credential.
     */
    public readonly azureConnectionString!: pulumi.Output<string>;
    /**
     * The description of the Azure Credential.
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * The name of the Azure Credential.
     */
    public readonly name!: pulumi.Output<string>;

    /**
     * Create a AzureCredential resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: AzureCredentialArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: AzureCredentialArgs | AzureCredentialState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as AzureCredentialState | undefined;
            resourceInputs["azureConnectionString"] = state ? state.azureConnectionString : undefined;
            resourceInputs["description"] = state ? state.description : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
        } else {
            const args = argsOrState as AzureCredentialArgs | undefined;
            if ((!args || args.azureConnectionString === undefined) && !opts.urn) {
                throw new Error("Missing required property 'azureConnectionString'");
            }
            resourceInputs["azureConnectionString"] = args?.azureConnectionString ? pulumi.secret(args.azureConnectionString) : undefined;
            resourceInputs["description"] = args ? args.description : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const secretOpts = { additionalSecretOutputs: ["azureConnectionString"] };
        opts = pulumi.mergeOptions(opts, secretOpts);
        super(AzureCredential.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering AzureCredential resources.
 */
export interface AzureCredentialState {
    /**
     * The connection string of the Azure Credential.
     */
    azureConnectionString?: pulumi.Input<string>;
    /**
     * The description of the Azure Credential.
     */
    description?: pulumi.Input<string>;
    /**
     * The name of the Azure Credential.
     */
    name?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a AzureCredential resource.
 */
export interface AzureCredentialArgs {
    /**
     * The connection string of the Azure Credential.
     */
    azureConnectionString: pulumi.Input<string>;
    /**
     * The description of the Azure Credential.
     */
    description?: pulumi.Input<string>;
    /**
     * The name of the Azure Credential.
     */
    name?: pulumi.Input<string>;
}
