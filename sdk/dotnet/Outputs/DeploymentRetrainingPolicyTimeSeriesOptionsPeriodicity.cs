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
    public sealed class DeploymentRetrainingPolicyTimeSeriesOptionsPeriodicity
    {
        /// <summary>
        /// The number of time steps.
        /// </summary>
        public readonly int TimeSteps;
        /// <summary>
        /// The time unit or ROW if windowsBasisUnit is ROW
        /// </summary>
        public readonly string TimeUnit;

        [OutputConstructor]
        private DeploymentRetrainingPolicyTimeSeriesOptionsPeriodicity(
            int timeSteps,

            string timeUnit)
        {
            TimeSteps = timeSteps;
            TimeUnit = timeUnit;
        }
    }
}
