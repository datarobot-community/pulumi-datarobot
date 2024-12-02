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
    public sealed class DeploymentRetrainingPolicyTrigger
    {
        /// <summary>
        /// Custom job ID for the retraining policy.
        /// </summary>
        public readonly string? CustomJobId;
        /// <summary>
        /// Minimal interval between policy runs in ISO 8601 duration string.
        /// </summary>
        public readonly string? MinIntervalBetweenRuns;
        /// <summary>
        /// Schedule for the retraining policy.
        /// </summary>
        public readonly Outputs.DeploymentRetrainingPolicyTriggerSchedule? Schedule;
        /// <summary>
        /// Identifies when trigger type is based on deployment a health status, whether the policy will run when health status declines to failing.
        /// </summary>
        public readonly bool? StatusDeclinesToFailing;
        /// <summary>
        /// Identifies when trigger type is based on deployment a health status, whether the policy will run when health status declines to warning.
        /// </summary>
        public readonly bool? StatusDeclinesToWarning;
        /// <summary>
        /// Identifies when trigger type is based on deployment a health status, whether the policy will run when health status still in decline.
        /// </summary>
        public readonly bool? StatusStillInDecline;
        /// <summary>
        /// Type of retraining policy trigger.
        /// </summary>
        public readonly string? Type;

        [OutputConstructor]
        private DeploymentRetrainingPolicyTrigger(
            string? customJobId,

            string? minIntervalBetweenRuns,

            Outputs.DeploymentRetrainingPolicyTriggerSchedule? schedule,

            bool? statusDeclinesToFailing,

            bool? statusDeclinesToWarning,

            bool? statusStillInDecline,

            string? type)
        {
            CustomJobId = customJobId;
            MinIntervalBetweenRuns = minIntervalBetweenRuns;
            Schedule = schedule;
            StatusDeclinesToFailing = statusDeclinesToFailing;
            StatusDeclinesToWarning = statusDeclinesToWarning;
            StatusStillInDecline = statusStillInDecline;
            Type = type;
        }
    }
}