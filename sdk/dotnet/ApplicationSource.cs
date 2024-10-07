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
    /// Application Source
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
    ///     var example = new Datarobot.ApplicationSource("example", new()
    ///     {
    ///         BaseEnvironmentId = "6542cd582a9d3d51bf4ac71e",
    ///         Files = new[]
    ///         {
    ///             new[]
    ///             {
    ///                 "start-app.sh",
    ///             },
    ///             new[]
    ///             {
    ///                 "streamlit-app.py",
    ///             },
    ///         },
    ///     });
    /// 
    ///     return new Dictionary&lt;string, object?&gt;
    ///     {
    ///         ["datarobotApplicationSourceId"] = example.Id,
    ///         ["datarobotApplicationSourceVersionId"] = example.VersionId,
    ///     };
    /// });
    /// ```
    /// </summary>
    [DatarobotResourceType("datarobot:index/applicationSource:ApplicationSource")]
    public partial class ApplicationSource : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The ID of the base environment for the Application Source.
        /// </summary>
        [Output("baseEnvironmentId")]
        public Output<string> BaseEnvironmentId { get; private set; } = null!;

        /// <summary>
        /// The ID of the base environment version for the Application Source.
        /// </summary>
        [Output("baseEnvironmentVersionId")]
        public Output<string> BaseEnvironmentVersionId { get; private set; } = null!;

        /// <summary>
        /// The list of tuples, where values in each tuple are the local filesystem path and the path the file should be placed in the Application Source. If list is of strings, then basenames will be used for tuples.
        /// </summary>
        [Output("files")]
        public Output<object?> Files { get; private set; } = null!;

        /// <summary>
        /// The hash of file contents for each file in files.
        /// </summary>
        [Output("filesHashes")]
        public Output<ImmutableArray<string>> FilesHashes { get; private set; } = null!;

        /// <summary>
        /// The path to a folder containing files to build the Application Source. Each file in the folder is uploaded under path relative to a folder path.
        /// </summary>
        [Output("folderPath")]
        public Output<string?> FolderPath { get; private set; } = null!;

        /// <summary>
        /// The hash of the folder path contents.
        /// </summary>
        [Output("folderPathHash")]
        public Output<string> FolderPathHash { get; private set; } = null!;

        /// <summary>
        /// The name of the Application Source.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// The resource settings for the Application Source.
        /// </summary>
        [Output("resourceSettings")]
        public Output<Outputs.ApplicationSourceResourceSettings> ResourceSettings { get; private set; } = null!;

        /// <summary>
        /// The runtime parameter values for the Application Source.
        /// </summary>
        [Output("runtimeParameterValues")]
        public Output<ImmutableArray<Outputs.ApplicationSourceRuntimeParameterValue>> RuntimeParameterValues { get; private set; } = null!;

        /// <summary>
        /// The version ID of the Application Source.
        /// </summary>
        [Output("versionId")]
        public Output<string> VersionId { get; private set; } = null!;


        /// <summary>
        /// Create a ApplicationSource resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public ApplicationSource(string name, ApplicationSourceArgs? args = null, CustomResourceOptions? options = null)
            : base("datarobot:index/applicationSource:ApplicationSource", name, args ?? new ApplicationSourceArgs(), MakeResourceOptions(options, ""))
        {
        }

        private ApplicationSource(string name, Input<string> id, ApplicationSourceState? state = null, CustomResourceOptions? options = null)
            : base("datarobot:index/applicationSource:ApplicationSource", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing ApplicationSource resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static ApplicationSource Get(string name, Input<string> id, ApplicationSourceState? state = null, CustomResourceOptions? options = null)
        {
            return new ApplicationSource(name, id, state, options);
        }
    }

    public sealed class ApplicationSourceArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The ID of the base environment for the Application Source.
        /// </summary>
        [Input("baseEnvironmentId")]
        public Input<string>? BaseEnvironmentId { get; set; }

        /// <summary>
        /// The ID of the base environment version for the Application Source.
        /// </summary>
        [Input("baseEnvironmentVersionId")]
        public Input<string>? BaseEnvironmentVersionId { get; set; }

        /// <summary>
        /// The list of tuples, where values in each tuple are the local filesystem path and the path the file should be placed in the Application Source. If list is of strings, then basenames will be used for tuples.
        /// </summary>
        [Input("files")]
        public Input<object>? Files { get; set; }

        /// <summary>
        /// The path to a folder containing files to build the Application Source. Each file in the folder is uploaded under path relative to a folder path.
        /// </summary>
        [Input("folderPath")]
        public Input<string>? FolderPath { get; set; }

        /// <summary>
        /// The name of the Application Source.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The resource settings for the Application Source.
        /// </summary>
        [Input("resourceSettings")]
        public Input<Inputs.ApplicationSourceResourceSettingsArgs>? ResourceSettings { get; set; }

        [Input("runtimeParameterValues")]
        private InputList<Inputs.ApplicationSourceRuntimeParameterValueArgs>? _runtimeParameterValues;

        /// <summary>
        /// The runtime parameter values for the Application Source.
        /// </summary>
        public InputList<Inputs.ApplicationSourceRuntimeParameterValueArgs> RuntimeParameterValues
        {
            get => _runtimeParameterValues ?? (_runtimeParameterValues = new InputList<Inputs.ApplicationSourceRuntimeParameterValueArgs>());
            set => _runtimeParameterValues = value;
        }

        public ApplicationSourceArgs()
        {
        }
        public static new ApplicationSourceArgs Empty => new ApplicationSourceArgs();
    }

    public sealed class ApplicationSourceState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The ID of the base environment for the Application Source.
        /// </summary>
        [Input("baseEnvironmentId")]
        public Input<string>? BaseEnvironmentId { get; set; }

        /// <summary>
        /// The ID of the base environment version for the Application Source.
        /// </summary>
        [Input("baseEnvironmentVersionId")]
        public Input<string>? BaseEnvironmentVersionId { get; set; }

        /// <summary>
        /// The list of tuples, where values in each tuple are the local filesystem path and the path the file should be placed in the Application Source. If list is of strings, then basenames will be used for tuples.
        /// </summary>
        [Input("files")]
        public Input<object>? Files { get; set; }

        [Input("filesHashes")]
        private InputList<string>? _filesHashes;

        /// <summary>
        /// The hash of file contents for each file in files.
        /// </summary>
        public InputList<string> FilesHashes
        {
            get => _filesHashes ?? (_filesHashes = new InputList<string>());
            set => _filesHashes = value;
        }

        /// <summary>
        /// The path to a folder containing files to build the Application Source. Each file in the folder is uploaded under path relative to a folder path.
        /// </summary>
        [Input("folderPath")]
        public Input<string>? FolderPath { get; set; }

        /// <summary>
        /// The hash of the folder path contents.
        /// </summary>
        [Input("folderPathHash")]
        public Input<string>? FolderPathHash { get; set; }

        /// <summary>
        /// The name of the Application Source.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The resource settings for the Application Source.
        /// </summary>
        [Input("resourceSettings")]
        public Input<Inputs.ApplicationSourceResourceSettingsGetArgs>? ResourceSettings { get; set; }

        [Input("runtimeParameterValues")]
        private InputList<Inputs.ApplicationSourceRuntimeParameterValueGetArgs>? _runtimeParameterValues;

        /// <summary>
        /// The runtime parameter values for the Application Source.
        /// </summary>
        public InputList<Inputs.ApplicationSourceRuntimeParameterValueGetArgs> RuntimeParameterValues
        {
            get => _runtimeParameterValues ?? (_runtimeParameterValues = new InputList<Inputs.ApplicationSourceRuntimeParameterValueGetArgs>());
            set => _runtimeParameterValues = value;
        }

        /// <summary>
        /// The version ID of the Application Source.
        /// </summary>
        [Input("versionId")]
        public Input<string>? VersionId { get; set; }

        public ApplicationSourceState()
        {
        }
        public static new ApplicationSourceState Empty => new ApplicationSourceState();
    }
}
