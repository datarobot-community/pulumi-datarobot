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
    /// Data set from file
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
    ///     var example = new Datarobot.DatasetFromFile("example", new()
    ///     {
    ///         FilePath = "[Path to file to upload]",
    ///         UseCaseIds = new[]
    ///         {
    ///             datarobot_use_case.Example.Id,
    ///         },
    ///     });
    /// 
    ///     return new Dictionary&lt;string, object?&gt;
    ///     {
    ///         ["exampleId"] = example.Id,
    ///     };
    /// });
    /// ```
    /// </summary>
    [DatarobotResourceType("datarobot:index/datasetFromFile:DatasetFromFile")]
    public partial class DatasetFromFile : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The path to the file to upload.
        /// </summary>
        [Output("filePath")]
        public Output<string> FilePath { get; private set; } = null!;

        /// <summary>
        /// The name of the Dataset. Defaults to the file name.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// The list of Use Case IDs to add the Dataset to.
        /// </summary>
        [Output("useCaseIds")]
        public Output<ImmutableArray<string>> UseCaseIds { get; private set; } = null!;


        /// <summary>
        /// Create a DatasetFromFile resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public DatasetFromFile(string name, DatasetFromFileArgs args, CustomResourceOptions? options = null)
            : base("datarobot:index/datasetFromFile:DatasetFromFile", name, args ?? new DatasetFromFileArgs(), MakeResourceOptions(options, ""))
        {
        }

        private DatasetFromFile(string name, Input<string> id, DatasetFromFileState? state = null, CustomResourceOptions? options = null)
            : base("datarobot:index/datasetFromFile:DatasetFromFile", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing DatasetFromFile resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static DatasetFromFile Get(string name, Input<string> id, DatasetFromFileState? state = null, CustomResourceOptions? options = null)
        {
            return new DatasetFromFile(name, id, state, options);
        }
    }

    public sealed class DatasetFromFileArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The path to the file to upload.
        /// </summary>
        [Input("filePath", required: true)]
        public Input<string> FilePath { get; set; } = null!;

        /// <summary>
        /// The name of the Dataset. Defaults to the file name.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("useCaseIds")]
        private InputList<string>? _useCaseIds;

        /// <summary>
        /// The list of Use Case IDs to add the Dataset to.
        /// </summary>
        public InputList<string> UseCaseIds
        {
            get => _useCaseIds ?? (_useCaseIds = new InputList<string>());
            set => _useCaseIds = value;
        }

        public DatasetFromFileArgs()
        {
        }
        public static new DatasetFromFileArgs Empty => new DatasetFromFileArgs();
    }

    public sealed class DatasetFromFileState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The path to the file to upload.
        /// </summary>
        [Input("filePath")]
        public Input<string>? FilePath { get; set; }

        /// <summary>
        /// The name of the Dataset. Defaults to the file name.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("useCaseIds")]
        private InputList<string>? _useCaseIds;

        /// <summary>
        /// The list of Use Case IDs to add the Dataset to.
        /// </summary>
        public InputList<string> UseCaseIds
        {
            get => _useCaseIds ?? (_useCaseIds = new InputList<string>());
            set => _useCaseIds = value;
        }

        public DatasetFromFileState()
        {
        }
        public static new DatasetFromFileState Empty => new DatasetFromFileState();
    }
}
