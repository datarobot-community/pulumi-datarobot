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

    public sealed class DeploymentSegmentAnalysisSettingsGetArgs : global::Pulumi.ResourceArgs
    {
        [Input("attributes")]
        private InputList<string>? _attributes;

        /// <summary>
        /// A list of strings that gives the segment attributes selected for tracking.
        /// </summary>
        public InputList<string> Attributes
        {
            get => _attributes ?? (_attributes = new InputList<string>());
            set => _attributes = value;
        }

        /// <summary>
        /// Set to 'True' if segment analysis is enabled for this deployment.
        /// </summary>
        [Input("enabled", required: true)]
        public Input<bool> Enabled { get; set; } = null!;

        public DeploymentSegmentAnalysisSettingsGetArgs()
        {
        }
        public static new DeploymentSegmentAnalysisSettingsGetArgs Empty => new DeploymentSegmentAnalysisSettingsGetArgs();
    }
}
