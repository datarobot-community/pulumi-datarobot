// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * Api Token Credential
 */
export class GoogleCloudCredential extends pulumi.CustomResource {
    /**
     * Get an existing GoogleCloudCredential resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: GoogleCloudCredentialState, opts?: pulumi.CustomResourceOptions): GoogleCloudCredential {
        return new GoogleCloudCredential(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'datarobot:index/googleCloudCredential:GoogleCloudCredential';

    /**
     * Returns true if the given object is an instance of GoogleCloudCredential.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is GoogleCloudCredential {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === GoogleCloudCredential.__pulumiType;
    }

    /**
     * The GCP key in JSON format.
     */
    public readonly gcpKey!: pulumi.Output<string | undefined>;
    /**
     * The file that has the GCP key. Cannot be used with `gcpKey`.
     */
    public readonly gcpKeyFile!: pulumi.Output<string | undefined>;
    /**
     * The hash of the GCP key file contents.
     */
    public /*out*/ readonly gcpKeyFileHash!: pulumi.Output<string>;
    /**
     * The name of the Google Cloud Credential.
     */
    public readonly name!: pulumi.Output<string>;

    /**
     * Create a GoogleCloudCredential resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: GoogleCloudCredentialArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: GoogleCloudCredentialArgs | GoogleCloudCredentialState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as GoogleCloudCredentialState | undefined;
            resourceInputs["gcpKey"] = state ? state.gcpKey : undefined;
            resourceInputs["gcpKeyFile"] = state ? state.gcpKeyFile : undefined;
            resourceInputs["gcpKeyFileHash"] = state ? state.gcpKeyFileHash : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
        } else {
            const args = argsOrState as GoogleCloudCredentialArgs | undefined;
            resourceInputs["gcpKey"] = args?.gcpKey ? pulumi.secret(args.gcpKey) : undefined;
            resourceInputs["gcpKeyFile"] = args ? args.gcpKeyFile : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["gcpKeyFileHash"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const secretOpts = { additionalSecretOutputs: ["gcpKey"] };
        opts = pulumi.mergeOptions(opts, secretOpts);
        super(GoogleCloudCredential.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering GoogleCloudCredential resources.
 */
export interface GoogleCloudCredentialState {
    /**
     * The GCP key in JSON format.
     */
    gcpKey?: pulumi.Input<string>;
    /**
     * The file that has the GCP key. Cannot be used with `gcpKey`.
     */
    gcpKeyFile?: pulumi.Input<string>;
    /**
     * The hash of the GCP key file contents.
     */
    gcpKeyFileHash?: pulumi.Input<string>;
    /**
     * The name of the Google Cloud Credential.
     */
    name?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a GoogleCloudCredential resource.
 */
export interface GoogleCloudCredentialArgs {
    /**
     * The GCP key in JSON format.
     */
    gcpKey?: pulumi.Input<string>;
    /**
     * The file that has the GCP key. Cannot be used with `gcpKey`.
     */
    gcpKeyFile?: pulumi.Input<string>;
    /**
     * The name of the Google Cloud Credential.
     */
    name?: pulumi.Input<string>;
}
