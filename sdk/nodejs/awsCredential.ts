// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * AWS Credential
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as datarobot from "@datarobot/pulumi-datarobot";
 *
 * const example = new datarobot.AwsCredential("example", {
 *     awsAccessKeyId: "example_access_key_id",
 *     awsSecretAccessKey: "example_secret_access_key",
 *     awsSessionToken: "example_session_token",
 *     description: "Description for the example AWS credential",
 * });
 * ```
 */
export class AwsCredential extends pulumi.CustomResource {
    /**
     * Get an existing AwsCredential resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: AwsCredentialState, opts?: pulumi.CustomResourceOptions): AwsCredential {
        return new AwsCredential(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'datarobot:index/awsCredential:AwsCredential';

    /**
     * Returns true if the given object is an instance of AwsCredential.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is AwsCredential {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === AwsCredential.__pulumiType;
    }

    /**
     * The AWS Access Key ID.
     */
    public readonly awsAccessKeyId!: pulumi.Output<string | undefined>;
    /**
     * The AWS Secret Access Key.
     */
    public readonly awsSecretAccessKey!: pulumi.Output<string | undefined>;
    /**
     * The AWS Session Token.
     */
    public readonly awsSessionToken!: pulumi.Output<string | undefined>;
    /**
     * The ID of the saved shared secure configuration. If specified, cannot include awsAccessKeyId, awsSecretAccessKey or awsSessionToken.
     */
    public readonly configId!: pulumi.Output<string | undefined>;
    /**
     * The description of the AWS Credential.
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * The name of the AWS Credential.
     */
    public readonly name!: pulumi.Output<string>;

    /**
     * Create a AwsCredential resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: AwsCredentialArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: AwsCredentialArgs | AwsCredentialState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as AwsCredentialState | undefined;
            resourceInputs["awsAccessKeyId"] = state ? state.awsAccessKeyId : undefined;
            resourceInputs["awsSecretAccessKey"] = state ? state.awsSecretAccessKey : undefined;
            resourceInputs["awsSessionToken"] = state ? state.awsSessionToken : undefined;
            resourceInputs["configId"] = state ? state.configId : undefined;
            resourceInputs["description"] = state ? state.description : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
        } else {
            const args = argsOrState as AwsCredentialArgs | undefined;
            resourceInputs["awsAccessKeyId"] = args ? args.awsAccessKeyId : undefined;
            resourceInputs["awsSecretAccessKey"] = args?.awsSecretAccessKey ? pulumi.secret(args.awsSecretAccessKey) : undefined;
            resourceInputs["awsSessionToken"] = args?.awsSessionToken ? pulumi.secret(args.awsSessionToken) : undefined;
            resourceInputs["configId"] = args ? args.configId : undefined;
            resourceInputs["description"] = args ? args.description : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const secretOpts = { additionalSecretOutputs: ["awsSecretAccessKey", "awsSessionToken"] };
        opts = pulumi.mergeOptions(opts, secretOpts);
        super(AwsCredential.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering AwsCredential resources.
 */
export interface AwsCredentialState {
    /**
     * The AWS Access Key ID.
     */
    awsAccessKeyId?: pulumi.Input<string>;
    /**
     * The AWS Secret Access Key.
     */
    awsSecretAccessKey?: pulumi.Input<string>;
    /**
     * The AWS Session Token.
     */
    awsSessionToken?: pulumi.Input<string>;
    /**
     * The ID of the saved shared secure configuration. If specified, cannot include awsAccessKeyId, awsSecretAccessKey or awsSessionToken.
     */
    configId?: pulumi.Input<string>;
    /**
     * The description of the AWS Credential.
     */
    description?: pulumi.Input<string>;
    /**
     * The name of the AWS Credential.
     */
    name?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a AwsCredential resource.
 */
export interface AwsCredentialArgs {
    /**
     * The AWS Access Key ID.
     */
    awsAccessKeyId?: pulumi.Input<string>;
    /**
     * The AWS Secret Access Key.
     */
    awsSecretAccessKey?: pulumi.Input<string>;
    /**
     * The AWS Session Token.
     */
    awsSessionToken?: pulumi.Input<string>;
    /**
     * The ID of the saved shared secure configuration. If specified, cannot include awsAccessKeyId, awsSecretAccessKey or awsSessionToken.
     */
    configId?: pulumi.Input<string>;
    /**
     * The description of the AWS Credential.
     */
    description?: pulumi.Input<string>;
    /**
     * The name of the AWS Credential.
     */
    name?: pulumi.Input<string>;
}