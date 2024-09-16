// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Datarobot.Inputs
{

    public sealed class DeploymentPredictionIntervalsSettingsArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Whether prediction intervals are enabled for this deployment.
        /// </summary>
        [Input("enabled", required: true)]
        public Input<bool> Enabled { get; set; } = null!;

        [Input("percentiles")]
        private InputList<int>? _percentiles;

        /// <summary>
        /// List of enabled prediction intervals’ sizes for this deployment.
        /// </summary>
        public InputList<int> Percentiles
        {
            get => _percentiles ?? (_percentiles = new InputList<int>());
            set => _percentiles = value;
        }

        public DeploymentPredictionIntervalsSettingsArgs()
        {
        }
        public static new DeploymentPredictionIntervalsSettingsArgs Empty => new DeploymentPredictionIntervalsSettingsArgs();
    }
}
