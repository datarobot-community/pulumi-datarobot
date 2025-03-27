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
    /// </summary>
    [DatarobotResourceType("datarobot:index/applicationSourceFromTemplate:ApplicationSourceFromTemplate")]
    public partial class ApplicationSourceFromTemplate : global::Pulumi.CustomResource
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
        /// The resources for the Application Source.
        /// </summary>
        [Output("resources")]
        public Output<Outputs.ApplicationSourceFromTemplateResources?> Resources { get; private set; } = null!;

        /// <summary>
        /// The runtime parameter values for the Application Source.
        /// </summary>
        [Output("runtimeParameterValues")]
        public Output<ImmutableArray<Outputs.ApplicationSourceFromTemplateRuntimeParameterValue>> RuntimeParameterValues { get; private set; } = null!;

        /// <summary>
        /// The ID of the template used to create the Application Source.
        /// </summary>
        [Output("templateId")]
        public Output<string> TemplateId { get; private set; } = null!;

        /// <summary>
        /// The version ID of the Application Source.
        /// </summary>
        [Output("versionId")]
        public Output<string> VersionId { get; private set; } = null!;


        /// <summary>
        /// Create a ApplicationSourceFromTemplate resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public ApplicationSourceFromTemplate(string name, ApplicationSourceFromTemplateArgs args, CustomResourceOptions? options = null)
            : base("datarobot:index/applicationSourceFromTemplate:ApplicationSourceFromTemplate", name, args ?? new ApplicationSourceFromTemplateArgs(), MakeResourceOptions(options, ""))
        {
        }

        private ApplicationSourceFromTemplate(string name, Input<string> id, ApplicationSourceFromTemplateState? state = null, CustomResourceOptions? options = null)
            : base("datarobot:index/applicationSourceFromTemplate:ApplicationSourceFromTemplate", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing ApplicationSourceFromTemplate resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static ApplicationSourceFromTemplate Get(string name, Input<string> id, ApplicationSourceFromTemplateState? state = null, CustomResourceOptions? options = null)
        {
            return new ApplicationSourceFromTemplate(name, id, state, options);
        }
    }

    public sealed class ApplicationSourceFromTemplateArgs : global::Pulumi.ResourceArgs
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
        /// The resources for the Application Source.
        /// </summary>
        [Input("resources")]
        public Input<Inputs.ApplicationSourceFromTemplateResourcesArgs>? Resources { get; set; }

        [Input("runtimeParameterValues")]
        private InputList<Inputs.ApplicationSourceFromTemplateRuntimeParameterValueArgs>? _runtimeParameterValues;

        /// <summary>
        /// The runtime parameter values for the Application Source.
        /// </summary>
        public InputList<Inputs.ApplicationSourceFromTemplateRuntimeParameterValueArgs> RuntimeParameterValues
        {
            get => _runtimeParameterValues ?? (_runtimeParameterValues = new InputList<Inputs.ApplicationSourceFromTemplateRuntimeParameterValueArgs>());
            set => _runtimeParameterValues = value;
        }

        /// <summary>
        /// The ID of the template used to create the Application Source.
        /// </summary>
        [Input("templateId", required: true)]
        public Input<string> TemplateId { get; set; } = null!;

        public ApplicationSourceFromTemplateArgs()
        {
        }
        public static new ApplicationSourceFromTemplateArgs Empty => new ApplicationSourceFromTemplateArgs();
    }

    public sealed class ApplicationSourceFromTemplateState : global::Pulumi.ResourceArgs
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
        /// The resources for the Application Source.
        /// </summary>
        [Input("resources")]
        public Input<Inputs.ApplicationSourceFromTemplateResourcesGetArgs>? Resources { get; set; }

        [Input("runtimeParameterValues")]
        private InputList<Inputs.ApplicationSourceFromTemplateRuntimeParameterValueGetArgs>? _runtimeParameterValues;

        /// <summary>
        /// The runtime parameter values for the Application Source.
        /// </summary>
        public InputList<Inputs.ApplicationSourceFromTemplateRuntimeParameterValueGetArgs> RuntimeParameterValues
        {
            get => _runtimeParameterValues ?? (_runtimeParameterValues = new InputList<Inputs.ApplicationSourceFromTemplateRuntimeParameterValueGetArgs>());
            set => _runtimeParameterValues = value;
        }

        /// <summary>
        /// The ID of the template used to create the Application Source.
        /// </summary>
        [Input("templateId")]
        public Input<string>? TemplateId { get; set; }

        /// <summary>
        /// The version ID of the Application Source.
        /// </summary>
        [Input("versionId")]
        public Input<string>? VersionId { get; set; }

        public ApplicationSourceFromTemplateState()
        {
        }
        public static new ApplicationSourceFromTemplateState Empty => new ApplicationSourceFromTemplateState();
    }
}
