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
    public sealed class DeploymentChallengerModelsSettings
    {
        /// <summary>
        /// Is 'True' if challenger models is enabled for this deployment.
        /// </summary>
        public readonly bool Enabled;

        [OutputConstructor]
        private DeploymentChallengerModelsSettings(bool enabled)
        {
            Enabled = enabled;
        }
    }
}
