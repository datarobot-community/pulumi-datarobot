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

    public sealed class DeploymentPredictionsDataCollectionSettingsGetArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// If predictions data collections is enabled for this Deployment.
        /// </summary>
        [Input("enabled", required: true)]
        public Input<bool> Enabled { get; set; } = null!;

        public DeploymentPredictionsDataCollectionSettingsGetArgs()
        {
        }
        public static new DeploymentPredictionsDataCollectionSettingsGetArgs Empty => new DeploymentPredictionsDataCollectionSettingsGetArgs();
    }
}
