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
    /// Data source
    /// </summary>
    [DatarobotResourceType("datarobot:index/datasource:Datasource")]
    public partial class Datasource : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The user-friendly name of the data source.
        /// </summary>
        [Output("canonicalName")]
        public Output<string> CanonicalName { get; private set; } = null!;

        /// <summary>
        /// The type of data source.
        /// </summary>
        [Output("dataSourceType")]
        public Output<string> DataSourceType { get; private set; } = null!;

        /// <summary>
        /// The data source parameters.
        /// </summary>
        [Output("params")]
        public Output<Outputs.DatasourceParams> Params { get; private set; } = null!;


        /// <summary>
        /// Create a Datasource resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Datasource(string name, DatasourceArgs args, CustomResourceOptions? options = null)
            : base("datarobot:index/datasource:Datasource", name, args ?? new DatasourceArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Datasource(string name, Input<string> id, DatasourceState? state = null, CustomResourceOptions? options = null)
            : base("datarobot:index/datasource:Datasource", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing Datasource resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Datasource Get(string name, Input<string> id, DatasourceState? state = null, CustomResourceOptions? options = null)
        {
            return new Datasource(name, id, state, options);
        }
    }

    public sealed class DatasourceArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The user-friendly name of the data source.
        /// </summary>
        [Input("canonicalName", required: true)]
        public Input<string> CanonicalName { get; set; } = null!;

        /// <summary>
        /// The type of data source.
        /// </summary>
        [Input("dataSourceType", required: true)]
        public Input<string> DataSourceType { get; set; } = null!;

        /// <summary>
        /// The data source parameters.
        /// </summary>
        [Input("params", required: true)]
        public Input<Inputs.DatasourceParamsArgs> Params { get; set; } = null!;

        public DatasourceArgs()
        {
        }
        public static new DatasourceArgs Empty => new DatasourceArgs();
    }

    public sealed class DatasourceState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The user-friendly name of the data source.
        /// </summary>
        [Input("canonicalName")]
        public Input<string>? CanonicalName { get; set; }

        /// <summary>
        /// The type of data source.
        /// </summary>
        [Input("dataSourceType")]
        public Input<string>? DataSourceType { get; set; }

        /// <summary>
        /// The data source parameters.
        /// </summary>
        [Input("params")]
        public Input<Inputs.DatasourceParamsGetArgs>? Params { get; set; }

        public DatasourceState()
        {
        }
        public static new DatasourceState Empty => new DatasourceState();
    }
}
