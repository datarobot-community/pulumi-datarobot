// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace DataRobotPulumi.Datarobot.Outputs
{

    [OutputType]
    public sealed class DatasourceParams
    {
        /// <summary>
        /// The Catalog name in the database if supported.
        /// </summary>
        public readonly string? Catalog;
        /// <summary>
        /// The id of the DataStore.
        /// </summary>
        public readonly string DataStoreId;
        /// <summary>
        /// A user specified fetch size in the range [1, 20000]. By default a fetchSize will be assigned to balance throughput and memory usage.
        /// </summary>
        public readonly int? FetchSize;
        /// <summary>
        /// The name of the partition column.
        /// </summary>
        public readonly string? PartitionColumn;
        /// <summary>
        /// The user-specified path for BLOB storage.
        /// </summary>
        public readonly string? Path;
        /// <summary>
        /// The user specified SQL query.
        /// </summary>
        public readonly string? Query;
        /// <summary>
        /// The name of the schema associated with the table.
        /// </summary>
        public readonly string? Schema;
        /// <summary>
        /// The name of specified database table.
        /// </summary>
        public readonly string? Table;

        [OutputConstructor]
        private DatasourceParams(
            string? catalog,

            string dataStoreId,

            int? fetchSize,

            string? partitionColumn,

            string? path,

            string? query,

            string? schema,

            string? table)
        {
            Catalog = catalog;
            DataStoreId = dataStoreId;
            FetchSize = fetchSize;
            PartitionColumn = partitionColumn;
            Path = path;
            Query = query;
            Schema = schema;
            Table = table;
        }
    }
}
