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
    /// Deployment
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
    ///     var exampleCustomModel = new Datarobot.CustomModel("exampleCustomModel", new()
    ///     {
    ///         Description = "Description for the example custom model",
    ///         TargetType = "Binary",
    ///         TargetName = "my_label",
    ///         BaseEnvironmentId = "65f9b27eab986d30d4c64268",
    ///         Files = new[]
    ///         {
    ///             "example.py",
    ///         },
    ///     });
    /// 
    ///     var exampleRegisteredModel = new Datarobot.RegisteredModel("exampleRegisteredModel", new()
    ///     {
    ///         CustomModelVersionId = exampleCustomModel.VersionId,
    ///         Description = "Description for the example registered model",
    ///     });
    /// 
    ///     var examplePredictionEnvironment = new Datarobot.PredictionEnvironment("examplePredictionEnvironment", new()
    ///     {
    ///         Description = "Description for the example prediction environment",
    ///         Platform = "datarobotServerless",
    ///     });
    /// 
    ///     var exampleDeployment = new Datarobot.Deployment("exampleDeployment", new()
    ///     {
    ///         Label = "An example deployment",
    ///         PredictionEnvironmentId = examplePredictionEnvironment.Id,
    ///         RegisteredModelVersionId = exampleRegisteredModel.VersionId,
    ///         ChallengerModelsSettings = null,
    ///         ChallengerReplaySettings = null,
    ///         SegmentAnalysisSettings = null,
    ///         BiasAndFairnessSettings = null,
    ///         PredictionsByForecastDateSettings = null,
    ///         DriftTrackingSettings = null,
    ///         AssociationIdSettings = null,
    ///         PredictionsDataCollectionSettings = null,
    ///         PredictionWarningSettings = null,
    ///         PredictionIntervalsSettings = null,
    ///         PredictionsSettings = null,
    ///         HealthSettings = null,
    ///         RuntimeParameterValues = new[]
    ///         {
    ///             new Datarobot.Inputs.DeploymentRuntimeParameterValueArgs
    ///             {
    ///                 Key = "EXAMPLE_PARAM",
    ///                 Type = "string",
    ///                 Value = "val",
    ///             },
    ///         },
    ///     });
    /// 
    ///     return new Dictionary&lt;string, object?&gt;
    ///     {
    ///         ["datarobotDeploymentId"] = exampleDeployment.Id,
    ///     };
    /// });
    /// ```
    /// </summary>
    [DatarobotResourceType("datarobot:index/deployment:Deployment")]
    public partial class Deployment : global::Pulumi.CustomResource
    {
        /// <summary>
        /// Association ID settings for this Deployment.
        /// </summary>
        [Output("associationIdSettings")]
        public Output<Outputs.DeploymentAssociationIdSettings?> AssociationIdSettings { get; private set; } = null!;

        /// <summary>
        /// The batch monitoring settings for the Deployment.
        /// </summary>
        [Output("batchMonitoringSettings")]
        public Output<Outputs.DeploymentBatchMonitoringSettings?> BatchMonitoringSettings { get; private set; } = null!;

        /// <summary>
        /// Bias and fairness settings for the Deployment.
        /// </summary>
        [Output("biasAndFairnessSettings")]
        public Output<Outputs.DeploymentBiasAndFairnessSettings?> BiasAndFairnessSettings { get; private set; } = null!;

        /// <summary>
        /// The challenger models settings for the Deployment.
        /// </summary>
        [Output("challengerModelsSettings")]
        public Output<Outputs.DeploymentChallengerModelsSettings?> ChallengerModelsSettings { get; private set; } = null!;

        /// <summary>
        /// The challenger replay settings for the Deployment.
        /// </summary>
        [Output("challengerReplaySettings")]
        public Output<Outputs.DeploymentChallengerReplaySettings?> ChallengerReplaySettings { get; private set; } = null!;

        /// <summary>
        /// The drift tracking settings for the Deployment.
        /// </summary>
        [Output("driftTrackingSettings")]
        public Output<Outputs.DeploymentDriftTrackingSettings?> DriftTrackingSettings { get; private set; } = null!;

        /// <summary>
        /// The health settings for this Deployment.
        /// </summary>
        [Output("healthSettings")]
        public Output<Outputs.DeploymentHealthSettings?> HealthSettings { get; private set; } = null!;

        /// <summary>
        /// The importance of the Deployment.
        /// </summary>
        [Output("importance")]
        public Output<string> Importance { get; private set; } = null!;

        /// <summary>
        /// The label of the Deployment.
        /// </summary>
        [Output("label")]
        public Output<string> Label { get; private set; } = null!;

        /// <summary>
        /// The ID of the predication environment for this Deployment.
        /// </summary>
        [Output("predictionEnvironmentId")]
        public Output<string> PredictionEnvironmentId { get; private set; } = null!;

        /// <summary>
        /// The prediction intervals settings for this Deployment.
        /// </summary>
        [Output("predictionIntervalsSettings")]
        public Output<Outputs.DeploymentPredictionIntervalsSettings?> PredictionIntervalsSettings { get; private set; } = null!;

        /// <summary>
        /// The prediction warning settings for the Deployment.
        /// </summary>
        [Output("predictionWarningSettings")]
        public Output<Outputs.DeploymentPredictionWarningSettings?> PredictionWarningSettings { get; private set; } = null!;

        /// <summary>
        /// The predictions by forecase date settings for the Deployment.
        /// </summary>
        [Output("predictionsByForecastDateSettings")]
        public Output<Outputs.DeploymentPredictionsByForecastDateSettings?> PredictionsByForecastDateSettings { get; private set; } = null!;

        /// <summary>
        /// The predictions data collection settings for the Deployment.
        /// </summary>
        [Output("predictionsDataCollectionSettings")]
        public Output<Outputs.DeploymentPredictionsDataCollectionSettings?> PredictionsDataCollectionSettings { get; private set; } = null!;

        /// <summary>
        /// Settings for the predictions.
        /// </summary>
        [Output("predictionsSettings")]
        public Output<Outputs.DeploymentPredictionsSettings?> PredictionsSettings { get; private set; } = null!;

        /// <summary>
        /// The ID of the registered model version for this Deployment.
        /// </summary>
        [Output("registeredModelVersionId")]
        public Output<string> RegisteredModelVersionId { get; private set; } = null!;

        /// <summary>
        /// The runtime parameter values for the Deployment.
        /// </summary>
        [Output("runtimeParameterValues")]
        public Output<ImmutableArray<Outputs.DeploymentRuntimeParameterValue>> RuntimeParameterValues { get; private set; } = null!;

        /// <summary>
        /// The segment analysis settings for the Deployment.
        /// </summary>
        [Output("segmentAnalysisSettings")]
        public Output<Outputs.DeploymentSegmentAnalysisSettings?> SegmentAnalysisSettings { get; private set; } = null!;

        /// <summary>
        /// The list of Use Case IDs to add the Deployment to.
        /// </summary>
        [Output("useCaseIds")]
        public Output<ImmutableArray<string>> UseCaseIds { get; private set; } = null!;


        /// <summary>
        /// Create a Deployment resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Deployment(string name, DeploymentArgs args, CustomResourceOptions? options = null)
            : base("datarobot:index/deployment:Deployment", name, args ?? new DeploymentArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Deployment(string name, Input<string> id, DeploymentState? state = null, CustomResourceOptions? options = null)
            : base("datarobot:index/deployment:Deployment", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing Deployment resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Deployment Get(string name, Input<string> id, DeploymentState? state = null, CustomResourceOptions? options = null)
        {
            return new Deployment(name, id, state, options);
        }
    }

    public sealed class DeploymentArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Association ID settings for this Deployment.
        /// </summary>
        [Input("associationIdSettings")]
        public Input<Inputs.DeploymentAssociationIdSettingsArgs>? AssociationIdSettings { get; set; }

        /// <summary>
        /// The batch monitoring settings for the Deployment.
        /// </summary>
        [Input("batchMonitoringSettings")]
        public Input<Inputs.DeploymentBatchMonitoringSettingsArgs>? BatchMonitoringSettings { get; set; }

        /// <summary>
        /// Bias and fairness settings for the Deployment.
        /// </summary>
        [Input("biasAndFairnessSettings")]
        public Input<Inputs.DeploymentBiasAndFairnessSettingsArgs>? BiasAndFairnessSettings { get; set; }

        /// <summary>
        /// The challenger models settings for the Deployment.
        /// </summary>
        [Input("challengerModelsSettings")]
        public Input<Inputs.DeploymentChallengerModelsSettingsArgs>? ChallengerModelsSettings { get; set; }

        /// <summary>
        /// The challenger replay settings for the Deployment.
        /// </summary>
        [Input("challengerReplaySettings")]
        public Input<Inputs.DeploymentChallengerReplaySettingsArgs>? ChallengerReplaySettings { get; set; }

        /// <summary>
        /// The drift tracking settings for the Deployment.
        /// </summary>
        [Input("driftTrackingSettings")]
        public Input<Inputs.DeploymentDriftTrackingSettingsArgs>? DriftTrackingSettings { get; set; }

        /// <summary>
        /// The health settings for this Deployment.
        /// </summary>
        [Input("healthSettings")]
        public Input<Inputs.DeploymentHealthSettingsArgs>? HealthSettings { get; set; }

        /// <summary>
        /// The importance of the Deployment.
        /// </summary>
        [Input("importance")]
        public Input<string>? Importance { get; set; }

        /// <summary>
        /// The label of the Deployment.
        /// </summary>
        [Input("label", required: true)]
        public Input<string> Label { get; set; } = null!;

        /// <summary>
        /// The ID of the predication environment for this Deployment.
        /// </summary>
        [Input("predictionEnvironmentId", required: true)]
        public Input<string> PredictionEnvironmentId { get; set; } = null!;

        /// <summary>
        /// The prediction intervals settings for this Deployment.
        /// </summary>
        [Input("predictionIntervalsSettings")]
        public Input<Inputs.DeploymentPredictionIntervalsSettingsArgs>? PredictionIntervalsSettings { get; set; }

        /// <summary>
        /// The prediction warning settings for the Deployment.
        /// </summary>
        [Input("predictionWarningSettings")]
        public Input<Inputs.DeploymentPredictionWarningSettingsArgs>? PredictionWarningSettings { get; set; }

        /// <summary>
        /// The predictions by forecase date settings for the Deployment.
        /// </summary>
        [Input("predictionsByForecastDateSettings")]
        public Input<Inputs.DeploymentPredictionsByForecastDateSettingsArgs>? PredictionsByForecastDateSettings { get; set; }

        /// <summary>
        /// The predictions data collection settings for the Deployment.
        /// </summary>
        [Input("predictionsDataCollectionSettings")]
        public Input<Inputs.DeploymentPredictionsDataCollectionSettingsArgs>? PredictionsDataCollectionSettings { get; set; }

        /// <summary>
        /// Settings for the predictions.
        /// </summary>
        [Input("predictionsSettings")]
        public Input<Inputs.DeploymentPredictionsSettingsArgs>? PredictionsSettings { get; set; }

        /// <summary>
        /// The ID of the registered model version for this Deployment.
        /// </summary>
        [Input("registeredModelVersionId", required: true)]
        public Input<string> RegisteredModelVersionId { get; set; } = null!;

        [Input("runtimeParameterValues")]
        private InputList<Inputs.DeploymentRuntimeParameterValueArgs>? _runtimeParameterValues;

        /// <summary>
        /// The runtime parameter values for the Deployment.
        /// </summary>
        public InputList<Inputs.DeploymentRuntimeParameterValueArgs> RuntimeParameterValues
        {
            get => _runtimeParameterValues ?? (_runtimeParameterValues = new InputList<Inputs.DeploymentRuntimeParameterValueArgs>());
            set => _runtimeParameterValues = value;
        }

        /// <summary>
        /// The segment analysis settings for the Deployment.
        /// </summary>
        [Input("segmentAnalysisSettings")]
        public Input<Inputs.DeploymentSegmentAnalysisSettingsArgs>? SegmentAnalysisSettings { get; set; }

        [Input("useCaseIds")]
        private InputList<string>? _useCaseIds;

        /// <summary>
        /// The list of Use Case IDs to add the Deployment to.
        /// </summary>
        public InputList<string> UseCaseIds
        {
            get => _useCaseIds ?? (_useCaseIds = new InputList<string>());
            set => _useCaseIds = value;
        }

        public DeploymentArgs()
        {
        }
        public static new DeploymentArgs Empty => new DeploymentArgs();
    }

    public sealed class DeploymentState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Association ID settings for this Deployment.
        /// </summary>
        [Input("associationIdSettings")]
        public Input<Inputs.DeploymentAssociationIdSettingsGetArgs>? AssociationIdSettings { get; set; }

        /// <summary>
        /// The batch monitoring settings for the Deployment.
        /// </summary>
        [Input("batchMonitoringSettings")]
        public Input<Inputs.DeploymentBatchMonitoringSettingsGetArgs>? BatchMonitoringSettings { get; set; }

        /// <summary>
        /// Bias and fairness settings for the Deployment.
        /// </summary>
        [Input("biasAndFairnessSettings")]
        public Input<Inputs.DeploymentBiasAndFairnessSettingsGetArgs>? BiasAndFairnessSettings { get; set; }

        /// <summary>
        /// The challenger models settings for the Deployment.
        /// </summary>
        [Input("challengerModelsSettings")]
        public Input<Inputs.DeploymentChallengerModelsSettingsGetArgs>? ChallengerModelsSettings { get; set; }

        /// <summary>
        /// The challenger replay settings for the Deployment.
        /// </summary>
        [Input("challengerReplaySettings")]
        public Input<Inputs.DeploymentChallengerReplaySettingsGetArgs>? ChallengerReplaySettings { get; set; }

        /// <summary>
        /// The drift tracking settings for the Deployment.
        /// </summary>
        [Input("driftTrackingSettings")]
        public Input<Inputs.DeploymentDriftTrackingSettingsGetArgs>? DriftTrackingSettings { get; set; }

        /// <summary>
        /// The health settings for this Deployment.
        /// </summary>
        [Input("healthSettings")]
        public Input<Inputs.DeploymentHealthSettingsGetArgs>? HealthSettings { get; set; }

        /// <summary>
        /// The importance of the Deployment.
        /// </summary>
        [Input("importance")]
        public Input<string>? Importance { get; set; }

        /// <summary>
        /// The label of the Deployment.
        /// </summary>
        [Input("label")]
        public Input<string>? Label { get; set; }

        /// <summary>
        /// The ID of the predication environment for this Deployment.
        /// </summary>
        [Input("predictionEnvironmentId")]
        public Input<string>? PredictionEnvironmentId { get; set; }

        /// <summary>
        /// The prediction intervals settings for this Deployment.
        /// </summary>
        [Input("predictionIntervalsSettings")]
        public Input<Inputs.DeploymentPredictionIntervalsSettingsGetArgs>? PredictionIntervalsSettings { get; set; }

        /// <summary>
        /// The prediction warning settings for the Deployment.
        /// </summary>
        [Input("predictionWarningSettings")]
        public Input<Inputs.DeploymentPredictionWarningSettingsGetArgs>? PredictionWarningSettings { get; set; }

        /// <summary>
        /// The predictions by forecase date settings for the Deployment.
        /// </summary>
        [Input("predictionsByForecastDateSettings")]
        public Input<Inputs.DeploymentPredictionsByForecastDateSettingsGetArgs>? PredictionsByForecastDateSettings { get; set; }

        /// <summary>
        /// The predictions data collection settings for the Deployment.
        /// </summary>
        [Input("predictionsDataCollectionSettings")]
        public Input<Inputs.DeploymentPredictionsDataCollectionSettingsGetArgs>? PredictionsDataCollectionSettings { get; set; }

        /// <summary>
        /// Settings for the predictions.
        /// </summary>
        [Input("predictionsSettings")]
        public Input<Inputs.DeploymentPredictionsSettingsGetArgs>? PredictionsSettings { get; set; }

        /// <summary>
        /// The ID of the registered model version for this Deployment.
        /// </summary>
        [Input("registeredModelVersionId")]
        public Input<string>? RegisteredModelVersionId { get; set; }

        [Input("runtimeParameterValues")]
        private InputList<Inputs.DeploymentRuntimeParameterValueGetArgs>? _runtimeParameterValues;

        /// <summary>
        /// The runtime parameter values for the Deployment.
        /// </summary>
        public InputList<Inputs.DeploymentRuntimeParameterValueGetArgs> RuntimeParameterValues
        {
            get => _runtimeParameterValues ?? (_runtimeParameterValues = new InputList<Inputs.DeploymentRuntimeParameterValueGetArgs>());
            set => _runtimeParameterValues = value;
        }

        /// <summary>
        /// The segment analysis settings for the Deployment.
        /// </summary>
        [Input("segmentAnalysisSettings")]
        public Input<Inputs.DeploymentSegmentAnalysisSettingsGetArgs>? SegmentAnalysisSettings { get; set; }

        [Input("useCaseIds")]
        private InputList<string>? _useCaseIds;

        /// <summary>
        /// The list of Use Case IDs to add the Deployment to.
        /// </summary>
        public InputList<string> UseCaseIds
        {
            get => _useCaseIds ?? (_useCaseIds = new InputList<string>());
            set => _useCaseIds = value;
        }

        public DeploymentState()
        {
        }
        public static new DeploymentState Empty => new DeploymentState();
    }
}
