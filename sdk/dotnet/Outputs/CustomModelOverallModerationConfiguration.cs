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
    public sealed class CustomModelOverallModerationConfiguration
    {
        /// <summary>
        /// The timeout action of the overall moderation configuration.
        /// </summary>
        public readonly string? TimeoutAction;
        /// <summary>
        /// The timeout in seconds of the overall moderation configuration.
        /// </summary>
        public readonly int? TimeoutSec;

        [OutputConstructor]
        private CustomModelOverallModerationConfiguration(
            string? timeoutAction,

            int? timeoutSec)
        {
            TimeoutAction = timeoutAction;
            TimeoutSec = timeoutSec;
        }
    }
}
