// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Datarobot.Inputs
{

    public sealed class DeploymentHealthSettingsServiceArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The batch count for the service health settings.
        /// </summary>
        [Input("batchCount", required: true)]
        public Input<int> BatchCount { get; set; } = null!;

        public DeploymentHealthSettingsServiceArgs()
        {
        }
        public static new DeploymentHealthSettingsServiceArgs Empty => new DeploymentHealthSettingsServiceArgs();
    }
}
