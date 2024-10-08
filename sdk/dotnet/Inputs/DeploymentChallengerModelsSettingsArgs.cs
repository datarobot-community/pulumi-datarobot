// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace DataRobotPulumi.Datarobot.Inputs
{

    public sealed class DeploymentChallengerModelsSettingsArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Is 'True' if challenger models is enabled for this deployment.
        /// </summary>
        [Input("enabled", required: true)]
        public Input<bool> Enabled { get; set; } = null!;

        public DeploymentChallengerModelsSettingsArgs()
        {
        }
        public static new DeploymentChallengerModelsSettingsArgs Empty => new DeploymentChallengerModelsSettingsArgs();
    }
}
