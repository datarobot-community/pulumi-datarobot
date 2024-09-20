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
    public sealed class CustomModelResourceSettings
    {
        /// <summary>
        /// The memory in MB for the Custom Model.
        /// </summary>
        public readonly int? MemoryMb;
        /// <summary>
        /// The network access for the Custom Model.
        /// </summary>
        public readonly string? NetworkAccess;
        /// <summary>
        /// The replicas for the Custom Model.
        /// </summary>
        public readonly int? Replicas;

        [OutputConstructor]
        private CustomModelResourceSettings(
            int? memoryMb,

            string? networkAccess,

            int? replicas)
        {
            MemoryMb = memoryMb;
            NetworkAccess = networkAccess;
            Replicas = replicas;
        }
    }
}
