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
    public sealed class CustomApplicationResources
    {
        /// <summary>
        /// The number of replicas for the Custom Application.
        /// </summary>
        public readonly int? Replicas;
        /// <summary>
        /// The resource label for the Custom Application.
        /// </summary>
        public readonly string? ResourceLabel;
        /// <summary>
        /// Whether to service web requests on the root path for the Custom Application.
        /// </summary>
        public readonly bool? ServiceWebRequestsOnRootPath;
        /// <summary>
        /// Whether session affinity is enabled for the Custom Application.
        /// </summary>
        public readonly bool? SessionAffinity;

        [OutputConstructor]
        private CustomApplicationResources(
            int? replicas,

            string? resourceLabel,

            bool? serviceWebRequestsOnRootPath,

            bool? sessionAffinity)
        {
            Replicas = replicas;
            ResourceLabel = resourceLabel;
            ServiceWebRequestsOnRootPath = serviceWebRequestsOnRootPath;
            SessionAffinity = sessionAffinity;
        }
    }
}
