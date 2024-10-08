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
    public sealed class DeploymentHealthSettingsPredictionsTimeliness
    {
        /// <summary>
        /// If predictions timeliness is enabled for this Deployment.
        /// </summary>
        public readonly bool Enabled;
        /// <summary>
        /// The expected frequency for the predictions timeliness health settings.
        /// </summary>
        public readonly string? ExpectedFrequency;

        [OutputConstructor]
        private DeploymentHealthSettingsPredictionsTimeliness(
            bool enabled,

            string? expectedFrequency)
        {
            Enabled = enabled;
            ExpectedFrequency = expectedFrequency;
        }
    }
}
