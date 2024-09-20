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
    public sealed class DeploymentSegmentAnalysisSettings
    {
        /// <summary>
        /// A list of strings that gives the segment attributes selected for tracking.
        /// </summary>
        public readonly ImmutableArray<string> Attributes;
        /// <summary>
        /// Set to 'True' if segment analysis is enabled for this deployment.
        /// </summary>
        public readonly bool Enabled;

        [OutputConstructor]
        private DeploymentSegmentAnalysisSettings(
            ImmutableArray<string> attributes,

            bool enabled)
        {
            Attributes = attributes;
            Enabled = enabled;
        }
    }
}
