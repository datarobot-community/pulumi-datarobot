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
    /// Deployment Retraining Policy
    /// </summary>
    [DatarobotResourceType("datarobot:index/deploymentRetrainingPolicy:DeploymentRetrainingPolicy")]
    public partial class DeploymentRetrainingPolicy : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The the action to take on the resultant new model.
        /// </summary>
        [Output("action")]
        public Output<string> Action { get; private set; } = null!;

        /// <summary>
        /// Options for projects used to build new models.
        /// </summary>
        [Output("autopilotOptions")]
        public Output<Outputs.DeploymentRetrainingPolicyAutopilotOptions> AutopilotOptions { get; private set; } = null!;

        /// <summary>
        /// The ID of the Deployment for the Retraining Policy.
        /// </summary>
        [Output("deploymentId")]
        public Output<string> DeploymentId { get; private set; } = null!;

        /// <summary>
        /// The description of the Retraining Policy.
        /// </summary>
        [Output("description")]
        public Output<string> Description { get; private set; } = null!;

        /// <summary>
        /// The feature list strategy used for modeling.
        /// </summary>
        [Output("featureListStrategy")]
        public Output<string> FeatureListStrategy { get; private set; } = null!;

        /// <summary>
        /// Determines how the new model is selected when the retraining policy runs.
        /// </summary>
        [Output("modelSelectionStrategy")]
        public Output<string> ModelSelectionStrategy { get; private set; } = null!;

        /// <summary>
        /// The name of the Retraining Policy.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// Options for projects used to build new models.
        /// </summary>
        [Output("projectOptions")]
        public Output<Outputs.DeploymentRetrainingPolicyProjectOptions> ProjectOptions { get; private set; } = null!;

        /// <summary>
        /// The project option strategy used for modeling.
        /// </summary>
        [Output("projectOptionsStrategy")]
        public Output<string> ProjectOptionsStrategy { get; private set; } = null!;

        /// <summary>
        /// Time Series project options used to build new models.
        /// </summary>
        [Output("timeSeriesOptions")]
        public Output<Outputs.DeploymentRetrainingPolicyTimeSeriesOptions?> TimeSeriesOptions { get; private set; } = null!;

        /// <summary>
        /// Retraining policy trigger.
        /// </summary>
        [Output("trigger")]
        public Output<Outputs.DeploymentRetrainingPolicyTrigger?> Trigger { get; private set; } = null!;

        /// <summary>
        /// The ID of the use case to which the retraining policy belongs.
        /// </summary>
        [Output("useCaseId")]
        public Output<string?> UseCaseId { get; private set; } = null!;


        /// <summary>
        /// Create a DeploymentRetrainingPolicy resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public DeploymentRetrainingPolicy(string name, DeploymentRetrainingPolicyArgs args, CustomResourceOptions? options = null)
            : base("datarobot:index/deploymentRetrainingPolicy:DeploymentRetrainingPolicy", name, args ?? new DeploymentRetrainingPolicyArgs(), MakeResourceOptions(options, ""))
        {
        }

        private DeploymentRetrainingPolicy(string name, Input<string> id, DeploymentRetrainingPolicyState? state = null, CustomResourceOptions? options = null)
            : base("datarobot:index/deploymentRetrainingPolicy:DeploymentRetrainingPolicy", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing DeploymentRetrainingPolicy resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static DeploymentRetrainingPolicy Get(string name, Input<string> id, DeploymentRetrainingPolicyState? state = null, CustomResourceOptions? options = null)
        {
            return new DeploymentRetrainingPolicy(name, id, state, options);
        }
    }

    public sealed class DeploymentRetrainingPolicyArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The the action to take on the resultant new model.
        /// </summary>
        [Input("action")]
        public Input<string>? Action { get; set; }

        /// <summary>
        /// Options for projects used to build new models.
        /// </summary>
        [Input("autopilotOptions")]
        public Input<Inputs.DeploymentRetrainingPolicyAutopilotOptionsArgs>? AutopilotOptions { get; set; }

        /// <summary>
        /// The ID of the Deployment for the Retraining Policy.
        /// </summary>
        [Input("deploymentId", required: true)]
        public Input<string> DeploymentId { get; set; } = null!;

        /// <summary>
        /// The description of the Retraining Policy.
        /// </summary>
        [Input("description", required: true)]
        public Input<string> Description { get; set; } = null!;

        /// <summary>
        /// The feature list strategy used for modeling.
        /// </summary>
        [Input("featureListStrategy")]
        public Input<string>? FeatureListStrategy { get; set; }

        /// <summary>
        /// Determines how the new model is selected when the retraining policy runs.
        /// </summary>
        [Input("modelSelectionStrategy")]
        public Input<string>? ModelSelectionStrategy { get; set; }

        /// <summary>
        /// The name of the Retraining Policy.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// Options for projects used to build new models.
        /// </summary>
        [Input("projectOptions")]
        public Input<Inputs.DeploymentRetrainingPolicyProjectOptionsArgs>? ProjectOptions { get; set; }

        /// <summary>
        /// The project option strategy used for modeling.
        /// </summary>
        [Input("projectOptionsStrategy")]
        public Input<string>? ProjectOptionsStrategy { get; set; }

        /// <summary>
        /// Time Series project options used to build new models.
        /// </summary>
        [Input("timeSeriesOptions")]
        public Input<Inputs.DeploymentRetrainingPolicyTimeSeriesOptionsArgs>? TimeSeriesOptions { get; set; }

        /// <summary>
        /// Retraining policy trigger.
        /// </summary>
        [Input("trigger")]
        public Input<Inputs.DeploymentRetrainingPolicyTriggerArgs>? Trigger { get; set; }

        /// <summary>
        /// The ID of the use case to which the retraining policy belongs.
        /// </summary>
        [Input("useCaseId")]
        public Input<string>? UseCaseId { get; set; }

        public DeploymentRetrainingPolicyArgs()
        {
        }
        public static new DeploymentRetrainingPolicyArgs Empty => new DeploymentRetrainingPolicyArgs();
    }

    public sealed class DeploymentRetrainingPolicyState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The the action to take on the resultant new model.
        /// </summary>
        [Input("action")]
        public Input<string>? Action { get; set; }

        /// <summary>
        /// Options for projects used to build new models.
        /// </summary>
        [Input("autopilotOptions")]
        public Input<Inputs.DeploymentRetrainingPolicyAutopilotOptionsGetArgs>? AutopilotOptions { get; set; }

        /// <summary>
        /// The ID of the Deployment for the Retraining Policy.
        /// </summary>
        [Input("deploymentId")]
        public Input<string>? DeploymentId { get; set; }

        /// <summary>
        /// The description of the Retraining Policy.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// The feature list strategy used for modeling.
        /// </summary>
        [Input("featureListStrategy")]
        public Input<string>? FeatureListStrategy { get; set; }

        /// <summary>
        /// Determines how the new model is selected when the retraining policy runs.
        /// </summary>
        [Input("modelSelectionStrategy")]
        public Input<string>? ModelSelectionStrategy { get; set; }

        /// <summary>
        /// The name of the Retraining Policy.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// Options for projects used to build new models.
        /// </summary>
        [Input("projectOptions")]
        public Input<Inputs.DeploymentRetrainingPolicyProjectOptionsGetArgs>? ProjectOptions { get; set; }

        /// <summary>
        /// The project option strategy used for modeling.
        /// </summary>
        [Input("projectOptionsStrategy")]
        public Input<string>? ProjectOptionsStrategy { get; set; }

        /// <summary>
        /// Time Series project options used to build new models.
        /// </summary>
        [Input("timeSeriesOptions")]
        public Input<Inputs.DeploymentRetrainingPolicyTimeSeriesOptionsGetArgs>? TimeSeriesOptions { get; set; }

        /// <summary>
        /// Retraining policy trigger.
        /// </summary>
        [Input("trigger")]
        public Input<Inputs.DeploymentRetrainingPolicyTriggerGetArgs>? Trigger { get; set; }

        /// <summary>
        /// The ID of the use case to which the retraining policy belongs.
        /// </summary>
        [Input("useCaseId")]
        public Input<string>? UseCaseId { get; set; }

        public DeploymentRetrainingPolicyState()
        {
        }
        public static new DeploymentRetrainingPolicyState Empty => new DeploymentRetrainingPolicyState();
    }
}
