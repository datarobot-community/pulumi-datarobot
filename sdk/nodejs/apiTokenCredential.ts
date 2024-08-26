// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * Api Token Credential
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as datarobot from "@pulumi/datarobot";
 *
 * const example = new datarobot.ApiTokenCredential("example", {apiToken: "[the API Key value here]"});
 * ```
 */
export class ApiTokenCredential extends pulumi.CustomResource {
    /**
     * Get an existing ApiTokenCredential resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ApiTokenCredentialState, opts?: pulumi.CustomResourceOptions): ApiTokenCredential {
        return new ApiTokenCredential(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'datarobot:index/apiTokenCredential:ApiTokenCredential';

    /**
     * Returns true if the given object is an instance of ApiTokenCredential.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is ApiTokenCredential {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === ApiTokenCredential.__pulumiType;
    }

    /**
     * The description of the Api Token Credential.
     */
    public readonly apiToken!: pulumi.Output<string>;
    /**
     * The description of the Api Token Credential.
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * The name of the Api Token Credential.
     */
    public readonly name!: pulumi.Output<string>;

    /**
     * Create a ApiTokenCredential resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ApiTokenCredentialArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: ApiTokenCredentialArgs | ApiTokenCredentialState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as ApiTokenCredentialState | undefined;
            resourceInputs["apiToken"] = state ? state.apiToken : undefined;
            resourceInputs["description"] = state ? state.description : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
        } else {
            const args = argsOrState as ApiTokenCredentialArgs | undefined;
            if ((!args || args.apiToken === undefined) && !opts.urn) {
                throw new Error("Missing required property 'apiToken'");
            }
            resourceInputs["apiToken"] = args?.apiToken ? pulumi.secret(args.apiToken) : undefined;
            resourceInputs["description"] = args ? args.description : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const secretOpts = { additionalSecretOutputs: ["apiToken"] };
        opts = pulumi.mergeOptions(opts, secretOpts);
        super(ApiTokenCredential.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering ApiTokenCredential resources.
 */
export interface ApiTokenCredentialState {
    /**
     * The description of the Api Token Credential.
     */
    apiToken?: pulumi.Input<string>;
    /**
     * The description of the Api Token Credential.
     */
    description?: pulumi.Input<string>;
    /**
     * The name of the Api Token Credential.
     */
    name?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a ApiTokenCredential resource.
 */
export interface ApiTokenCredentialArgs {
    /**
     * The description of the Api Token Credential.
     */
    apiToken: pulumi.Input<string>;
    /**
     * The description of the Api Token Credential.
     */
    description?: pulumi.Input<string>;
    /**
     * The name of the Api Token Credential.
     */
    name?: pulumi.Input<string>;
}
