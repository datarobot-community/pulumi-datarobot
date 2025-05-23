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
    public sealed class NotificationChannelCustomHeader
    {
        /// <summary>
        /// The name of the header.
        /// </summary>
        public readonly string Name;
        /// <summary>
        /// The value of the header.
        /// </summary>
        public readonly string Value;

        [OutputConstructor]
        private NotificationChannelCustomHeader(
            string name,

            string value)
        {
            Name = name;
            Value = value;
        }
    }
}
