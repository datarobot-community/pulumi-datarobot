// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * Data store
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as datarobot from "@datarobot/pulumi-datarobot";
 *
 * const exampleConnector = new datarobot.Datastore("exampleConnector", {
 *     canonicalName: "Example Connector Datastore",
 *     dataStoreType: "dr-connector-v1",
 *     connectorId: "65538041dde6a1d664d0b2ec",
 *     fields: [{
 *         id: "fs.defaultFS",
 *         name: "Bucket Name",
 *         value: "my-bucket",
 *     }],
 * });
 * const exampleJdbc = new datarobot.Datastore("exampleJdbc", {
 *     canonicalName: "Example JDBC Datastore",
 *     dataStoreType: "jdbc",
 *     driverId: "5b4752844bf542000175dbea",
 *     fields: [
 *         {
 *             name: "address",
 *             value: "my-address",
 *         },
 *         {
 *             name: "database",
 *             value: "my-database",
 *         },
 *     ],
 * });
 * const exampleDatabase = new datarobot.Datastore("exampleDatabase", {
 *     canonicalName: "Example Database Datastore",
 *     dataStoreType: "dr-database-v1",
 *     driverId: "64a288a50636598d75df7f82",
 *     fields: [{
 *         id: "bq.project_id",
 *         name: "Project Id",
 *         value: "project-id",
 *     }],
 * });
 * export const exampleConnectorId = exampleConnector.id;
 * ```
 */
export class Datastore extends pulumi.CustomResource {
    /**
     * Get an existing Datastore resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: DatastoreState, opts?: pulumi.CustomResourceOptions): Datastore {
        return new Datastore(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'datarobot:index/datastore:Datastore';

    /**
     * Returns true if the given object is an instance of Datastore.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Datastore {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Datastore.__pulumiType;
    }

    /**
     * The user-friendly name of the data store.
     */
    public readonly canonicalName!: pulumi.Output<string>;
    /**
     * The identifier of the Connector if data*store*type is DR*CONNECTOR*V1
     */
    public readonly connectorId!: pulumi.Output<string | undefined>;
    /**
     * The type of data store.
     */
    public readonly dataStoreType!: pulumi.Output<string>;
    /**
     * The identifier of the DataDriver if data*store*type is JDBC or DR*DATABASE*V1
     */
    public readonly driverId!: pulumi.Output<string | undefined>;
    /**
     * If the type is dr-database-v1, then the fields specify the configuration.
     */
    public readonly fields!: pulumi.Output<{[key: string]: string}[] | undefined>;
    /**
     * The full JDBC URL (for example: jdbc:postgresql://my.dbaddress.org:5432/my_db).
     */
    public readonly jdbcUrl!: pulumi.Output<string | undefined>;

    /**
     * Create a Datastore resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: DatastoreArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: DatastoreArgs | DatastoreState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as DatastoreState | undefined;
            resourceInputs["canonicalName"] = state ? state.canonicalName : undefined;
            resourceInputs["connectorId"] = state ? state.connectorId : undefined;
            resourceInputs["dataStoreType"] = state ? state.dataStoreType : undefined;
            resourceInputs["driverId"] = state ? state.driverId : undefined;
            resourceInputs["fields"] = state ? state.fields : undefined;
            resourceInputs["jdbcUrl"] = state ? state.jdbcUrl : undefined;
        } else {
            const args = argsOrState as DatastoreArgs | undefined;
            if ((!args || args.canonicalName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'canonicalName'");
            }
            if ((!args || args.dataStoreType === undefined) && !opts.urn) {
                throw new Error("Missing required property 'dataStoreType'");
            }
            resourceInputs["canonicalName"] = args ? args.canonicalName : undefined;
            resourceInputs["connectorId"] = args ? args.connectorId : undefined;
            resourceInputs["dataStoreType"] = args ? args.dataStoreType : undefined;
            resourceInputs["driverId"] = args ? args.driverId : undefined;
            resourceInputs["fields"] = args ? args.fields : undefined;
            resourceInputs["jdbcUrl"] = args ? args.jdbcUrl : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(Datastore.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Datastore resources.
 */
export interface DatastoreState {
    /**
     * The user-friendly name of the data store.
     */
    canonicalName?: pulumi.Input<string>;
    /**
     * The identifier of the Connector if data*store*type is DR*CONNECTOR*V1
     */
    connectorId?: pulumi.Input<string>;
    /**
     * The type of data store.
     */
    dataStoreType?: pulumi.Input<string>;
    /**
     * The identifier of the DataDriver if data*store*type is JDBC or DR*DATABASE*V1
     */
    driverId?: pulumi.Input<string>;
    /**
     * If the type is dr-database-v1, then the fields specify the configuration.
     */
    fields?: pulumi.Input<pulumi.Input<{[key: string]: pulumi.Input<string>}>[]>;
    /**
     * The full JDBC URL (for example: jdbc:postgresql://my.dbaddress.org:5432/my_db).
     */
    jdbcUrl?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a Datastore resource.
 */
export interface DatastoreArgs {
    /**
     * The user-friendly name of the data store.
     */
    canonicalName: pulumi.Input<string>;
    /**
     * The identifier of the Connector if data*store*type is DR*CONNECTOR*V1
     */
    connectorId?: pulumi.Input<string>;
    /**
     * The type of data store.
     */
    dataStoreType: pulumi.Input<string>;
    /**
     * The identifier of the DataDriver if data*store*type is JDBC or DR*DATABASE*V1
     */
    driverId?: pulumi.Input<string>;
    /**
     * If the type is dr-database-v1, then the fields specify the configuration.
     */
    fields?: pulumi.Input<pulumi.Input<{[key: string]: pulumi.Input<string>}>[]>;
    /**
     * The full JDBC URL (for example: jdbc:postgresql://my.dbaddress.org:5432/my_db).
     */
    jdbcUrl?: pulumi.Input<string>;
}