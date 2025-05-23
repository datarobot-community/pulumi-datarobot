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

    public sealed class CustomMetricJobRuntimeParameterValueGetArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The name of the runtime parameter.
        /// </summary>
        [Input("key", required: true)]
        public Input<string> Key { get; set; } = null!;

        /// <summary>
        /// The type of the runtime parameter.
        /// </summary>
        [Input("type", required: true)]
        public Input<string> Type { get; set; } = null!;

        /// <summary>
        /// The value of the runtime parameter (type conversion is handled internally).
        /// </summary>
        [Input("value", required: true)]
        public Input<string> Value { get; set; } = null!;

        public CustomMetricJobRuntimeParameterValueGetArgs()
        {
        }
        public static new CustomMetricJobRuntimeParameterValueGetArgs Empty => new CustomMetricJobRuntimeParameterValueGetArgs();
    }
}
