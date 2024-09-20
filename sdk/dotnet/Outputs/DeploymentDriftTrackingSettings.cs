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
    public sealed class DeploymentDriftTrackingSettings
    {
        /// <summary>
        /// If feature drift tracking is to be turned on.
        /// </summary>
        public readonly bool? FeatureDriftEnabled;
        /// <summary>
        /// If target drift tracking is to be turned on.
        /// </summary>
        public readonly bool? TargetDriftEnabled;

        [OutputConstructor]
        private DeploymentDriftTrackingSettings(
            bool? featureDriftEnabled,

            bool? targetDriftEnabled)
        {
            FeatureDriftEnabled = featureDriftEnabled;
            TargetDriftEnabled = targetDriftEnabled;
        }
    }
}
