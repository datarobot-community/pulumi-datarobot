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
    public sealed class DeploymentHealthSettingsAccuracy
    {
        /// <summary>
        /// The batch count for the accuracy health settings.
        /// </summary>
        public readonly int? BatchCount;
        /// <summary>
        /// The failing threshold for the accuracy health settings.
        /// </summary>
        public readonly double? FailingThreshold;
        /// <summary>
        /// The measurement for the accuracy health settings.
        /// </summary>
        public readonly string? Measurement;
        /// <summary>
        /// The metric for the accuracy health settings.
        /// </summary>
        public readonly string? Metric;
        /// <summary>
        /// The warning threshold for the accuracy health settings.
        /// </summary>
        public readonly double? WarningThreshold;

        [OutputConstructor]
        private DeploymentHealthSettingsAccuracy(
            int? batchCount,

            double? failingThreshold,

            string? measurement,

            string? metric,

            double? warningThreshold)
        {
            BatchCount = batchCount;
            FailingThreshold = failingThreshold;
            Measurement = measurement;
            Metric = metric;
            WarningThreshold = warningThreshold;
        }
    }
}
