// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Datarobot.Inputs
{

    public sealed class DeploymentHealthSettingsArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The accuracy health settings for this Deployment.
        /// </summary>
        [Input("accuracy")]
        public Input<Inputs.DeploymentHealthSettingsAccuracyArgs>? Accuracy { get; set; }

        /// <summary>
        /// The actuals timeliness health settings for this Deployment.
        /// </summary>
        [Input("actualsTimeliness")]
        public Input<Inputs.DeploymentHealthSettingsActualsTimelinessArgs>? ActualsTimeliness { get; set; }

        /// <summary>
        /// The custom metrics health settings for this Deployment.
        /// </summary>
        [Input("customMetrics")]
        public Input<Inputs.DeploymentHealthSettingsCustomMetricsArgs>? CustomMetrics { get; set; }

        /// <summary>
        /// The data drift health settings for this Deployment.
        /// </summary>
        [Input("dataDrift")]
        public Input<Inputs.DeploymentHealthSettingsDataDriftArgs>? DataDrift { get; set; }

        /// <summary>
        /// The fairness health settings for this Deployment.
        /// </summary>
        [Input("fairness")]
        public Input<Inputs.DeploymentHealthSettingsFairnessArgs>? Fairness { get; set; }

        /// <summary>
        /// The predictions timeliness health settings for this Deployment.
        /// </summary>
        [Input("predictionsTimeliness")]
        public Input<Inputs.DeploymentHealthSettingsPredictionsTimelinessArgs>? PredictionsTimeliness { get; set; }

        /// <summary>
        /// The service health settings for this Deployment.
        /// </summary>
        [Input("service")]
        public Input<Inputs.DeploymentHealthSettingsServiceArgs>? Service { get; set; }

        public DeploymentHealthSettingsArgs()
        {
        }
        public static new DeploymentHealthSettingsArgs Empty => new DeploymentHealthSettingsArgs();
    }
}