// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Datarobot.Inputs
{

    public sealed class DeploymentSettingsArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Used to associate predictions back to your actual data.
        /// </summary>
        [Input("associationId")]
        public Input<Inputs.DeploymentSettingsAssociationIdArgs>? AssociationId { get; set; }

        /// <summary>
        /// Used to compare the performance of the deployed model with the challenger models.
        /// </summary>
        [Input("challengerAnalysis")]
        public Input<bool>? ChallengerAnalysis { get; set; }

        /// <summary>
        /// Used to score predictions made by the challenger models and compare performance with the deployed model.
        /// </summary>
        [Input("predictionRowStorage")]
        public Input<bool>? PredictionRowStorage { get; set; }

        /// <summary>
        /// Settings for the predictions.
        /// </summary>
        [Input("predictionsSettings")]
        public Input<Inputs.DeploymentSettingsPredictionsSettingsArgs>? PredictionsSettings { get; set; }

        public DeploymentSettingsArgs()
        {
        }
        public static new DeploymentSettingsArgs Empty => new DeploymentSettingsArgs();
    }
}