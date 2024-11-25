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
    /// Custom Model
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
    ///     var exampleRemoteRepository = new Datarobot.RemoteRepository("exampleRemoteRepository", new()
    ///     {
    ///         Description = "GitHub repository with Datarobot user models",
    ///         Location = "https://github.com/datarobot/datarobot-user-models",
    ///         SourceType = "github",
    ///     });
    /// 
    ///     // set the credential id for private repositories
    ///     // credential_id = datarobot_api_token_credential.example.id
    ///     var exampleCustomModel = new Datarobot.CustomModel("exampleCustomModel", new()
    ///     {
    ///         Description = "An example custom model from GitHub repository",
    ///         Files = new[]
    ///         {
    ///             "file1.py",
    ///             "file2.py",
    ///         },
    ///         TargetType = "Binary",
    ///         TargetName = "my_label",
    ///         BaseEnvironmentId = "65f9b27eab986d30d4c64268",
    ///     });
    /// 
    ///     // Optional
    ///     // source_remote_repositories = [
    ///     //   {
    ///     //     id  = datarobot_remote_repository.example.id
    ///     //     ref = "master"
    ///     //     source_paths = [
    ///     //       "model_templates/python3_dummy_binary",
    ///     //     ]
    ///     //   }
    ///     // ]
    ///     // guard_configurations = [
    ///     //   {
    ///     //     template_name = "Rouge 1"
    ///     //     name          = "Rouge 1 response"
    ///     //     stages        = ["response"]
    ///     //     intervention = {
    ///     //       action  = "block"
    ///     //       message = "response has been blocked by Rogue 1 guard"
    ///     //       condition = jsonencode({
    ///     //         "comparand": 0.5, 
    ///     //         "comparator": "greaterThan"
    ///     //       })
    ///     //     }
    ///     //   },
    ///     // ]
    ///     // overall_moderation_configuration = {
    ///     //   timeout_sec    = 120
    ///     //   timeout_action = "score"
    ///     // }
    ///     // memory_mb      = 512
    ///     // replicas       = 2
    ///     // network_access = "NONE"
    ///     return new Dictionary&lt;string, object?&gt;
    ///     {
    ///         ["exampleId"] = exampleCustomModel.Id,
    ///     };
    /// });
    /// ```
    /// </summary>
    [DatarobotResourceType("datarobot:index/customModel:CustomModel")]
    public partial class CustomModel : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The ID of the base environment for the Custom Model.
        /// </summary>
        [Output("baseEnvironmentId")]
        public Output<string> BaseEnvironmentId { get; private set; } = null!;

        /// <summary>
        /// The ID of the base environment version for the Custom Model.
        /// </summary>
        [Output("baseEnvironmentVersionId")]
        public Output<string> BaseEnvironmentVersionId { get; private set; } = null!;

        /// <summary>
        /// Class labels for multiclass classification. Cannot be used with class*labels*file.
        /// </summary>
        [Output("classLabels")]
        public Output<ImmutableArray<string>> ClassLabels { get; private set; } = null!;

        /// <summary>
        /// Path to file containing newline separated class labels for multiclass classification. Cannot be used with class_labels.
        /// </summary>
        [Output("classLabelsFile")]
        public Output<string?> ClassLabelsFile { get; private set; } = null!;

        /// <summary>
        /// The number of deployments for the Custom Model.
        /// </summary>
        [Output("deploymentsCount")]
        public Output<int> DeploymentsCount { get; private set; } = null!;

        /// <summary>
        /// The description of the Custom Model.
        /// </summary>
        [Output("description")]
        public Output<string> Description { get; private set; } = null!;

        /// <summary>
        /// The list of tuples, where values in each tuple are the local filesystem path and the path the file should be placed in the Custom Model. If list is of strings, then basenames will be used for tuples.
        /// </summary>
        [Output("files")]
        public Output<object?> Files { get; private set; } = null!;

        /// <summary>
        /// The hash of file contents for each file in files.
        /// </summary>
        [Output("filesHashes")]
        public Output<ImmutableArray<string>> FilesHashes { get; private set; } = null!;

        /// <summary>
        /// The path to a folder containing files to build the Custom Model. Each file in the folder is uploaded under path relative to a folder path.
        /// </summary>
        [Output("folderPath")]
        public Output<string?> FolderPath { get; private set; } = null!;

        /// <summary>
        /// The hash of the folder path contents.
        /// </summary>
        [Output("folderPathHash")]
        public Output<string> FolderPathHash { get; private set; } = null!;

        /// <summary>
        /// The guard configurations for the Custom Model.
        /// </summary>
        [Output("guardConfigurations")]
        public Output<ImmutableArray<Outputs.CustomModelGuardConfiguration>> GuardConfigurations { get; private set; } = null!;

        /// <summary>
        /// Flag indicating if the Custom Model is a proxy model.
        /// </summary>
        [Output("isProxy")]
        public Output<bool> IsProxy { get; private set; } = null!;

        /// <summary>
        /// The language used to build the Custom Model.
        /// </summary>
        [Output("language")]
        public Output<string?> Language { get; private set; } = null!;

        /// <summary>
        /// The memory in MB for the Custom Model.
        /// </summary>
        [Output("memoryMb")]
        public Output<int> MemoryMb { get; private set; } = null!;

        /// <summary>
        /// The name of the Custom Model.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// The negative class label of the Custom Model.
        /// </summary>
        [Output("negativeClassLabel")]
        public Output<string> NegativeClassLabel { get; private set; } = null!;

        /// <summary>
        /// The network access for the Custom Model.
        /// </summary>
        [Output("networkAccess")]
        public Output<string> NetworkAccess { get; private set; } = null!;

        /// <summary>
        /// The overall moderation configuration for the Custom Model.
        /// </summary>
        [Output("overallModerationConfiguration")]
        public Output<Outputs.CustomModelOverallModerationConfiguration?> OverallModerationConfiguration { get; private set; } = null!;

        /// <summary>
        /// The positive class label of the Custom Model.
        /// </summary>
        [Output("positiveClassLabel")]
        public Output<string> PositiveClassLabel { get; private set; } = null!;

        /// <summary>
        /// The prediction threshold of the Custom Model.
        /// </summary>
        [Output("predictionThreshold")]
        public Output<double> PredictionThreshold { get; private set; } = null!;

        /// <summary>
        /// The replicas for the Custom Model.
        /// </summary>
        [Output("replicas")]
        public Output<int> Replicas { get; private set; } = null!;

        /// <summary>
        /// A single identifier that represents a bundle of resources: Memory, CPU, GPU, etc.
        /// </summary>
        [Output("resourceBundleId")]
        public Output<string?> ResourceBundleId { get; private set; } = null!;

        /// <summary>
        /// The runtime parameter values for the Custom Model.
        /// </summary>
        [Output("runtimeParameterValues")]
        public Output<ImmutableArray<Outputs.CustomModelRuntimeParameterValue>> RuntimeParameterValues { get; private set; } = null!;

        /// <summary>
        /// The ID of the source LLM Blueprint for the Custom Model.
        /// </summary>
        [Output("sourceLlmBlueprintId")]
        public Output<string?> SourceLlmBlueprintId { get; private set; } = null!;

        /// <summary>
        /// The source remote repositories for the Custom Model.
        /// </summary>
        [Output("sourceRemoteRepositories")]
        public Output<ImmutableArray<Outputs.CustomModelSourceRemoteRepository>> SourceRemoteRepositories { get; private set; } = null!;

        /// <summary>
        /// The target name of the Custom Model.
        /// </summary>
        [Output("targetName")]
        public Output<string> TargetName { get; private set; } = null!;

        /// <summary>
        /// The target type of the Custom Model.
        /// </summary>
        [Output("targetType")]
        public Output<string> TargetType { get; private set; } = null!;

        /// <summary>
        /// The name of the partition column in the training dataset assigned to the Custom Model.
        /// </summary>
        [Output("trainingDataPartitionColumn")]
        public Output<string?> TrainingDataPartitionColumn { get; private set; } = null!;

        /// <summary>
        /// The ID of the training dataset assigned to the Custom Model.
        /// </summary>
        [Output("trainingDatasetId")]
        public Output<string?> TrainingDatasetId { get; private set; } = null!;

        /// <summary>
        /// The name of the training dataset assigned to the Custom Model.
        /// </summary>
        [Output("trainingDatasetName")]
        public Output<string> TrainingDatasetName { get; private set; } = null!;

        /// <summary>
        /// The version ID of the training dataset assigned to the Custom Model.
        /// </summary>
        [Output("trainingDatasetVersionId")]
        public Output<string> TrainingDatasetVersionId { get; private set; } = null!;

        /// <summary>
        /// The list of Use Case IDs to add the Custom Model version to.
        /// </summary>
        [Output("useCaseIds")]
        public Output<ImmutableArray<string>> UseCaseIds { get; private set; } = null!;

        /// <summary>
        /// The ID of the latest Custom Model version.
        /// </summary>
        [Output("versionId")]
        public Output<string> VersionId { get; private set; } = null!;


        /// <summary>
        /// Create a CustomModel resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public CustomModel(string name, CustomModelArgs? args = null, CustomResourceOptions? options = null)
            : base("datarobot:index/customModel:CustomModel", name, args ?? new CustomModelArgs(), MakeResourceOptions(options, ""))
        {
        }

        private CustomModel(string name, Input<string> id, CustomModelState? state = null, CustomResourceOptions? options = null)
            : base("datarobot:index/customModel:CustomModel", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing CustomModel resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static CustomModel Get(string name, Input<string> id, CustomModelState? state = null, CustomResourceOptions? options = null)
        {
            return new CustomModel(name, id, state, options);
        }
    }

    public sealed class CustomModelArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The ID of the base environment for the Custom Model.
        /// </summary>
        [Input("baseEnvironmentId")]
        public Input<string>? BaseEnvironmentId { get; set; }

        /// <summary>
        /// The ID of the base environment version for the Custom Model.
        /// </summary>
        [Input("baseEnvironmentVersionId")]
        public Input<string>? BaseEnvironmentVersionId { get; set; }

        [Input("classLabels")]
        private InputList<string>? _classLabels;

        /// <summary>
        /// Class labels for multiclass classification. Cannot be used with class*labels*file.
        /// </summary>
        public InputList<string> ClassLabels
        {
            get => _classLabels ?? (_classLabels = new InputList<string>());
            set => _classLabels = value;
        }

        /// <summary>
        /// Path to file containing newline separated class labels for multiclass classification. Cannot be used with class_labels.
        /// </summary>
        [Input("classLabelsFile")]
        public Input<string>? ClassLabelsFile { get; set; }

        /// <summary>
        /// The description of the Custom Model.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// The list of tuples, where values in each tuple are the local filesystem path and the path the file should be placed in the Custom Model. If list is of strings, then basenames will be used for tuples.
        /// </summary>
        [Input("files")]
        public Input<object>? Files { get; set; }

        /// <summary>
        /// The path to a folder containing files to build the Custom Model. Each file in the folder is uploaded under path relative to a folder path.
        /// </summary>
        [Input("folderPath")]
        public Input<string>? FolderPath { get; set; }

        [Input("guardConfigurations")]
        private InputList<Inputs.CustomModelGuardConfigurationArgs>? _guardConfigurations;

        /// <summary>
        /// The guard configurations for the Custom Model.
        /// </summary>
        public InputList<Inputs.CustomModelGuardConfigurationArgs> GuardConfigurations
        {
            get => _guardConfigurations ?? (_guardConfigurations = new InputList<Inputs.CustomModelGuardConfigurationArgs>());
            set => _guardConfigurations = value;
        }

        /// <summary>
        /// Flag indicating if the Custom Model is a proxy model.
        /// </summary>
        [Input("isProxy")]
        public Input<bool>? IsProxy { get; set; }

        /// <summary>
        /// The language used to build the Custom Model.
        /// </summary>
        [Input("language")]
        public Input<string>? Language { get; set; }

        /// <summary>
        /// The memory in MB for the Custom Model.
        /// </summary>
        [Input("memoryMb")]
        public Input<int>? MemoryMb { get; set; }

        /// <summary>
        /// The name of the Custom Model.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The negative class label of the Custom Model.
        /// </summary>
        [Input("negativeClassLabel")]
        public Input<string>? NegativeClassLabel { get; set; }

        /// <summary>
        /// The network access for the Custom Model.
        /// </summary>
        [Input("networkAccess")]
        public Input<string>? NetworkAccess { get; set; }

        /// <summary>
        /// The overall moderation configuration for the Custom Model.
        /// </summary>
        [Input("overallModerationConfiguration")]
        public Input<Inputs.CustomModelOverallModerationConfigurationArgs>? OverallModerationConfiguration { get; set; }

        /// <summary>
        /// The positive class label of the Custom Model.
        /// </summary>
        [Input("positiveClassLabel")]
        public Input<string>? PositiveClassLabel { get; set; }

        /// <summary>
        /// The prediction threshold of the Custom Model.
        /// </summary>
        [Input("predictionThreshold")]
        public Input<double>? PredictionThreshold { get; set; }

        /// <summary>
        /// The replicas for the Custom Model.
        /// </summary>
        [Input("replicas")]
        public Input<int>? Replicas { get; set; }

        /// <summary>
        /// A single identifier that represents a bundle of resources: Memory, CPU, GPU, etc.
        /// </summary>
        [Input("resourceBundleId")]
        public Input<string>? ResourceBundleId { get; set; }

        [Input("runtimeParameterValues")]
        private InputList<Inputs.CustomModelRuntimeParameterValueArgs>? _runtimeParameterValues;

        /// <summary>
        /// The runtime parameter values for the Custom Model.
        /// </summary>
        public InputList<Inputs.CustomModelRuntimeParameterValueArgs> RuntimeParameterValues
        {
            get => _runtimeParameterValues ?? (_runtimeParameterValues = new InputList<Inputs.CustomModelRuntimeParameterValueArgs>());
            set => _runtimeParameterValues = value;
        }

        /// <summary>
        /// The ID of the source LLM Blueprint for the Custom Model.
        /// </summary>
        [Input("sourceLlmBlueprintId")]
        public Input<string>? SourceLlmBlueprintId { get; set; }

        [Input("sourceRemoteRepositories")]
        private InputList<Inputs.CustomModelSourceRemoteRepositoryArgs>? _sourceRemoteRepositories;

        /// <summary>
        /// The source remote repositories for the Custom Model.
        /// </summary>
        public InputList<Inputs.CustomModelSourceRemoteRepositoryArgs> SourceRemoteRepositories
        {
            get => _sourceRemoteRepositories ?? (_sourceRemoteRepositories = new InputList<Inputs.CustomModelSourceRemoteRepositoryArgs>());
            set => _sourceRemoteRepositories = value;
        }

        /// <summary>
        /// The target name of the Custom Model.
        /// </summary>
        [Input("targetName")]
        public Input<string>? TargetName { get; set; }

        /// <summary>
        /// The target type of the Custom Model.
        /// </summary>
        [Input("targetType")]
        public Input<string>? TargetType { get; set; }

        /// <summary>
        /// The name of the partition column in the training dataset assigned to the Custom Model.
        /// </summary>
        [Input("trainingDataPartitionColumn")]
        public Input<string>? TrainingDataPartitionColumn { get; set; }

        /// <summary>
        /// The ID of the training dataset assigned to the Custom Model.
        /// </summary>
        [Input("trainingDatasetId")]
        public Input<string>? TrainingDatasetId { get; set; }

        [Input("useCaseIds")]
        private InputList<string>? _useCaseIds;

        /// <summary>
        /// The list of Use Case IDs to add the Custom Model version to.
        /// </summary>
        public InputList<string> UseCaseIds
        {
            get => _useCaseIds ?? (_useCaseIds = new InputList<string>());
            set => _useCaseIds = value;
        }

        public CustomModelArgs()
        {
        }
        public static new CustomModelArgs Empty => new CustomModelArgs();
    }

    public sealed class CustomModelState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The ID of the base environment for the Custom Model.
        /// </summary>
        [Input("baseEnvironmentId")]
        public Input<string>? BaseEnvironmentId { get; set; }

        /// <summary>
        /// The ID of the base environment version for the Custom Model.
        /// </summary>
        [Input("baseEnvironmentVersionId")]
        public Input<string>? BaseEnvironmentVersionId { get; set; }

        [Input("classLabels")]
        private InputList<string>? _classLabels;

        /// <summary>
        /// Class labels for multiclass classification. Cannot be used with class*labels*file.
        /// </summary>
        public InputList<string> ClassLabels
        {
            get => _classLabels ?? (_classLabels = new InputList<string>());
            set => _classLabels = value;
        }

        /// <summary>
        /// Path to file containing newline separated class labels for multiclass classification. Cannot be used with class_labels.
        /// </summary>
        [Input("classLabelsFile")]
        public Input<string>? ClassLabelsFile { get; set; }

        /// <summary>
        /// The number of deployments for the Custom Model.
        /// </summary>
        [Input("deploymentsCount")]
        public Input<int>? DeploymentsCount { get; set; }

        /// <summary>
        /// The description of the Custom Model.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// The list of tuples, where values in each tuple are the local filesystem path and the path the file should be placed in the Custom Model. If list is of strings, then basenames will be used for tuples.
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
        /// The path to a folder containing files to build the Custom Model. Each file in the folder is uploaded under path relative to a folder path.
        /// </summary>
        [Input("folderPath")]
        public Input<string>? FolderPath { get; set; }

        /// <summary>
        /// The hash of the folder path contents.
        /// </summary>
        [Input("folderPathHash")]
        public Input<string>? FolderPathHash { get; set; }

        [Input("guardConfigurations")]
        private InputList<Inputs.CustomModelGuardConfigurationGetArgs>? _guardConfigurations;

        /// <summary>
        /// The guard configurations for the Custom Model.
        /// </summary>
        public InputList<Inputs.CustomModelGuardConfigurationGetArgs> GuardConfigurations
        {
            get => _guardConfigurations ?? (_guardConfigurations = new InputList<Inputs.CustomModelGuardConfigurationGetArgs>());
            set => _guardConfigurations = value;
        }

        /// <summary>
        /// Flag indicating if the Custom Model is a proxy model.
        /// </summary>
        [Input("isProxy")]
        public Input<bool>? IsProxy { get; set; }

        /// <summary>
        /// The language used to build the Custom Model.
        /// </summary>
        [Input("language")]
        public Input<string>? Language { get; set; }

        /// <summary>
        /// The memory in MB for the Custom Model.
        /// </summary>
        [Input("memoryMb")]
        public Input<int>? MemoryMb { get; set; }

        /// <summary>
        /// The name of the Custom Model.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The negative class label of the Custom Model.
        /// </summary>
        [Input("negativeClassLabel")]
        public Input<string>? NegativeClassLabel { get; set; }

        /// <summary>
        /// The network access for the Custom Model.
        /// </summary>
        [Input("networkAccess")]
        public Input<string>? NetworkAccess { get; set; }

        /// <summary>
        /// The overall moderation configuration for the Custom Model.
        /// </summary>
        [Input("overallModerationConfiguration")]
        public Input<Inputs.CustomModelOverallModerationConfigurationGetArgs>? OverallModerationConfiguration { get; set; }

        /// <summary>
        /// The positive class label of the Custom Model.
        /// </summary>
        [Input("positiveClassLabel")]
        public Input<string>? PositiveClassLabel { get; set; }

        /// <summary>
        /// The prediction threshold of the Custom Model.
        /// </summary>
        [Input("predictionThreshold")]
        public Input<double>? PredictionThreshold { get; set; }

        /// <summary>
        /// The replicas for the Custom Model.
        /// </summary>
        [Input("replicas")]
        public Input<int>? Replicas { get; set; }

        /// <summary>
        /// A single identifier that represents a bundle of resources: Memory, CPU, GPU, etc.
        /// </summary>
        [Input("resourceBundleId")]
        public Input<string>? ResourceBundleId { get; set; }

        [Input("runtimeParameterValues")]
        private InputList<Inputs.CustomModelRuntimeParameterValueGetArgs>? _runtimeParameterValues;

        /// <summary>
        /// The runtime parameter values for the Custom Model.
        /// </summary>
        public InputList<Inputs.CustomModelRuntimeParameterValueGetArgs> RuntimeParameterValues
        {
            get => _runtimeParameterValues ?? (_runtimeParameterValues = new InputList<Inputs.CustomModelRuntimeParameterValueGetArgs>());
            set => _runtimeParameterValues = value;
        }

        /// <summary>
        /// The ID of the source LLM Blueprint for the Custom Model.
        /// </summary>
        [Input("sourceLlmBlueprintId")]
        public Input<string>? SourceLlmBlueprintId { get; set; }

        [Input("sourceRemoteRepositories")]
        private InputList<Inputs.CustomModelSourceRemoteRepositoryGetArgs>? _sourceRemoteRepositories;

        /// <summary>
        /// The source remote repositories for the Custom Model.
        /// </summary>
        public InputList<Inputs.CustomModelSourceRemoteRepositoryGetArgs> SourceRemoteRepositories
        {
            get => _sourceRemoteRepositories ?? (_sourceRemoteRepositories = new InputList<Inputs.CustomModelSourceRemoteRepositoryGetArgs>());
            set => _sourceRemoteRepositories = value;
        }

        /// <summary>
        /// The target name of the Custom Model.
        /// </summary>
        [Input("targetName")]
        public Input<string>? TargetName { get; set; }

        /// <summary>
        /// The target type of the Custom Model.
        /// </summary>
        [Input("targetType")]
        public Input<string>? TargetType { get; set; }

        /// <summary>
        /// The name of the partition column in the training dataset assigned to the Custom Model.
        /// </summary>
        [Input("trainingDataPartitionColumn")]
        public Input<string>? TrainingDataPartitionColumn { get; set; }

        /// <summary>
        /// The ID of the training dataset assigned to the Custom Model.
        /// </summary>
        [Input("trainingDatasetId")]
        public Input<string>? TrainingDatasetId { get; set; }

        /// <summary>
        /// The name of the training dataset assigned to the Custom Model.
        /// </summary>
        [Input("trainingDatasetName")]
        public Input<string>? TrainingDatasetName { get; set; }

        /// <summary>
        /// The version ID of the training dataset assigned to the Custom Model.
        /// </summary>
        [Input("trainingDatasetVersionId")]
        public Input<string>? TrainingDatasetVersionId { get; set; }

        [Input("useCaseIds")]
        private InputList<string>? _useCaseIds;

        /// <summary>
        /// The list of Use Case IDs to add the Custom Model version to.
        /// </summary>
        public InputList<string> UseCaseIds
        {
            get => _useCaseIds ?? (_useCaseIds = new InputList<string>());
            set => _useCaseIds = value;
        }

        /// <summary>
        /// The ID of the latest Custom Model version.
        /// </summary>
        [Input("versionId")]
        public Input<string>? VersionId { get; set; }

        public CustomModelState()
        {
        }
        public static new CustomModelState Empty => new CustomModelState();
    }
}
