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
    public sealed class DeploymentHealthSettingsCustomMetricsFailingCondition
    {
        /// <summary>
        /// The compare operator for the failing condition of the custom metrics health settings.
        /// </summary>
        public readonly string CompareOperator;
        /// <summary>
        /// The metric ID for the failing condition of the custom metrics health settings.
        /// </summary>
        public readonly string MetricId;
        /// <summary>
        /// The threshold for the failing condition of the custom metrics health settings.
        /// </summary>
        public readonly double Threshold;

        [OutputConstructor]
        private DeploymentHealthSettingsCustomMetricsFailingCondition(
            string compareOperator,

            string metricId,

            double threshold)
        {
            CompareOperator = compareOperator;
            MetricId = metricId;
            Threshold = threshold;
        }
    }
}
