// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace DataRobotPulumi.Datarobot
{
    /// <summary>
    /// Data store
    /// 
    /// ## Example Usage
    /// 
    /// ```csharp
    /// using System.Collections.Generic;
    /// using System.Linq;
    /// using Pulumi;
    /// using Datarobot = DataRobotPulumi.Datarobot;
    /// 
    /// return await Deployment.RunAsync(() =&gt; 
    /// {
    ///     var exampleConnector = new Datarobot.Datastore("exampleConnector", new()
    ///     {
    ///         CanonicalName = "Example Connector Datastore",
    ///         DataStoreType = "dr-connector-v1",
    ///         ConnectorId = "65538041dde6a1d664d0b2ec",
    ///         Fields = new[]
    ///         {
    ///             
    ///             {
    ///                 { "id", "fs.defaultFS" },
    ///                 { "name", "Bucket Name" },
    ///                 { "value", "my-bucket" },
    ///             },
    ///         },
    ///     });
    /// 
    ///     var exampleJdbc = new Datarobot.Datastore("exampleJdbc", new()
    ///     {
    ///         CanonicalName = "Example JDBC Datastore",
    ///         DataStoreType = "jdbc",
    ///         DriverId = "5b4752844bf542000175dbea",
    ///         Fields = new[]
    ///         {
    ///             
    ///             {
    ///                 { "name", "address" },
    ///                 { "value", "my-address" },
    ///             },
    ///             
    ///             {
    ///                 { "name", "database" },
    ///                 { "value", "my-database" },
    ///             },
    ///         },
    ///     });
    /// 
    ///     var exampleDatabase = new Datarobot.Datastore("exampleDatabase", new()
    ///     {
    ///         CanonicalName = "Example Database Datastore",
    ///         DataStoreType = "dr-database-v1",
    ///         DriverId = "64a288a50636598d75df7f82",
    ///         Fields = new[]
    ///         {
    ///             
    ///             {
    ///                 { "id", "bq.project_id" },
    ///                 { "name", "Project Id" },
    ///                 { "value", "project-id" },
    ///             },
    ///         },
    ///     });
    /// 
    ///     return new Dictionary&lt;string, object?&gt;
    ///     {
    ///         ["exampleConnectorId"] = exampleConnector.Id,
    ///     };
    /// });
    /// ```
    /// </summary>
    [DatarobotResourceType("datarobot:index/datastore:Datastore")]
    public partial class Datastore : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The user-friendly name of the data store.
        /// </summary>
        [Output("canonicalName")]
        public Output<string> CanonicalName { get; private set; } = null!;

        /// <summary>
        /// The identifier of the Connector if data*store*type is DR*CONNECTOR*V1
        /// </summary>
        [Output("connectorId")]
        public Output<string?> ConnectorId { get; private set; } = null!;

        /// <summary>
        /// The type of data store.
        /// </summary>
        [Output("dataStoreType")]
        public Output<string> DataStoreType { get; private set; } = null!;

        /// <summary>
        /// The identifier of the DataDriver if data*store*type is JDBC or DR*DATABASE*V1
        /// </summary>
        [Output("driverId")]
        public Output<string?> DriverId { get; private set; } = null!;

        /// <summary>
        /// If the type is dr-database-v1, then the fields specify the configuration.
        /// </summary>
        [Output("fields")]
        public Output<ImmutableArray<ImmutableDictionary<string, string>>> Fields { get; private set; } = null!;

        /// <summary>
        /// The full JDBC URL (for example: jdbc:postgresql://my.dbaddress.org:5432/my_db).
        /// </summary>
        [Output("jdbcUrl")]
        public Output<string?> JdbcUrl { get; private set; } = null!;


        /// <summary>
        /// Create a Datastore resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Datastore(string name, DatastoreArgs args, CustomResourceOptions? options = null)
            : base("datarobot:index/datastore:Datastore", name, args ?? new DatastoreArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Datastore(string name, Input<string> id, DatastoreState? state = null, CustomResourceOptions? options = null)
            : base("datarobot:index/datastore:Datastore", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                PluginDownloadURL = "github://api.github.com/datarobot-community/pulumi-datarobot",
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Datastore resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Datastore Get(string name, Input<string> id, DatastoreState? state = null, CustomResourceOptions? options = null)
        {
            return new Datastore(name, id, state, options);
        }
    }

    public sealed class DatastoreArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The user-friendly name of the data store.
        /// </summary>
        [Input("canonicalName", required: true)]
        public Input<string> CanonicalName { get; set; } = null!;

        /// <summary>
        /// The identifier of the Connector if data*store*type is DR*CONNECTOR*V1
        /// </summary>
        [Input("connectorId")]
        public Input<string>? ConnectorId { get; set; }

        /// <summary>
        /// The type of data store.
        /// </summary>
        [Input("dataStoreType", required: true)]
        public Input<string> DataStoreType { get; set; } = null!;

        /// <summary>
        /// The identifier of the DataDriver if data*store*type is JDBC or DR*DATABASE*V1
        /// </summary>
        [Input("driverId")]
        public Input<string>? DriverId { get; set; }

        [Input("fields")]
        private InputList<ImmutableDictionary<string, string>>? _fields;

        /// <summary>
        /// If the type is dr-database-v1, then the fields specify the configuration.
        /// </summary>
        public InputList<ImmutableDictionary<string, string>> Fields
        {
            get => _fields ?? (_fields = new InputList<ImmutableDictionary<string, string>>());
            set => _fields = value;
        }

        /// <summary>
        /// The full JDBC URL (for example: jdbc:postgresql://my.dbaddress.org:5432/my_db).
        /// </summary>
        [Input("jdbcUrl")]
        public Input<string>? JdbcUrl { get; set; }

        public DatastoreArgs()
        {
        }
        public static new DatastoreArgs Empty => new DatastoreArgs();
    }

    public sealed class DatastoreState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The user-friendly name of the data store.
        /// </summary>
        [Input("canonicalName")]
        public Input<string>? CanonicalName { get; set; }

        /// <summary>
        /// The identifier of the Connector if data*store*type is DR*CONNECTOR*V1
        /// </summary>
        [Input("connectorId")]
        public Input<string>? ConnectorId { get; set; }

        /// <summary>
        /// The type of data store.
        /// </summary>
        [Input("dataStoreType")]
        public Input<string>? DataStoreType { get; set; }

        /// <summary>
        /// The identifier of the DataDriver if data*store*type is JDBC or DR*DATABASE*V1
        /// </summary>
        [Input("driverId")]
        public Input<string>? DriverId { get; set; }

        [Input("fields")]
        private InputList<ImmutableDictionary<string, string>>? _fields;

        /// <summary>
        /// If the type is dr-database-v1, then the fields specify the configuration.
        /// </summary>
        public InputList<ImmutableDictionary<string, string>> Fields
        {
            get => _fields ?? (_fields = new InputList<ImmutableDictionary<string, string>>());
            set => _fields = value;
        }

        /// <summary>
        /// The full JDBC URL (for example: jdbc:postgresql://my.dbaddress.org:5432/my_db).
        /// </summary>
        [Input("jdbcUrl")]
        public Input<string>? JdbcUrl { get; set; }

        public DatastoreState()
        {
        }
        public static new DatastoreState Empty => new DatastoreState();
    }
}
