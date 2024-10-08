// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace DataRobotPulumi.Datarobot.Inputs
{

    public sealed class DeploymentHealthSettingsAccuracyGetArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The batch count for the accuracy health settings.
        /// </summary>
        [Input("batchCount")]
        public Input<int>? BatchCount { get; set; }

        /// <summary>
        /// The failing threshold for the accuracy health settings.
        /// </summary>
        [Input("failingThreshold")]
        public Input<double>? FailingThreshold { get; set; }

        /// <summary>
        /// The measurement for the accuracy health settings.
        /// </summary>
        [Input("measurement")]
        public Input<string>? Measurement { get; set; }

        /// <summary>
        /// The metric for the accuracy health settings.
        /// </summary>
        [Input("metric")]
        public Input<string>? Metric { get; set; }

        /// <summary>
        /// The warning threshold for the accuracy health settings.
        /// </summary>
        [Input("warningThreshold")]
        public Input<double>? WarningThreshold { get; set; }

        public DeploymentHealthSettingsAccuracyGetArgs()
        {
        }
        public static new DeploymentHealthSettingsAccuracyGetArgs Empty => new DeploymentHealthSettingsAccuracyGetArgs();
    }
}
