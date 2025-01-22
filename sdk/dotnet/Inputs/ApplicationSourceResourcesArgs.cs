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

    public sealed class ApplicationSourceResourcesArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The replicas for the Application Source.
        /// </summary>
        [Input("replicas")]
        public Input<int>? Replicas { get; set; }

        /// <summary>
        /// The resource label for the Application Source.
        /// </summary>
        [Input("resourceLabel")]
        public Input<string>? ResourceLabel { get; set; }

        /// <summary>
        /// The session affinity for the Application Source.
        /// </summary>
        [Input("sessionAffinity")]
        public Input<bool>? SessionAffinity { get; set; }

        public ApplicationSourceResourcesArgs()
        {
        }
        public static new ApplicationSourceResourcesArgs Empty => new ApplicationSourceResourcesArgs();
    }
}
