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

    public sealed class CustomModelOverallModerationConfigurationGetArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The timeout action of the overall moderation configuration.
        /// </summary>
        [Input("timeoutAction")]
        public Input<string>? TimeoutAction { get; set; }

        /// <summary>
        /// The timeout in seconds of the overall moderation configuration.
        /// </summary>
        [Input("timeoutSec")]
        public Input<int>? TimeoutSec { get; set; }

        public CustomModelOverallModerationConfigurationGetArgs()
        {
        }
        public static new CustomModelOverallModerationConfigurationGetArgs Empty => new CustomModelOverallModerationConfigurationGetArgs();
    }
}
