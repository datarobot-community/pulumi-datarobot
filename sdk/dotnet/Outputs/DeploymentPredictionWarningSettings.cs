// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace DataRobotPulumi.Datarobot.Outputs
{

    [OutputType]
    public sealed class DeploymentPredictionWarningSettings
    {
        /// <summary>
        /// The custom boundaries for prediction warnings.
        /// </summary>
        public readonly Outputs.DeploymentPredictionWarningSettingsCustomBoundaries? CustomBoundaries;
        /// <summary>
        /// If target prediction warning is enabled for this Deployment.
        /// </summary>
        public readonly bool Enabled;

        [OutputConstructor]
        private DeploymentPredictionWarningSettings(
            Outputs.DeploymentPredictionWarningSettingsCustomBoundaries? customBoundaries,

            bool enabled)
        {
            CustomBoundaries = customBoundaries;
            Enabled = enabled;
        }
    }
}
