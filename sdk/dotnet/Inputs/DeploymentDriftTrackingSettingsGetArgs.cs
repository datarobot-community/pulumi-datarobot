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

    public sealed class DeploymentDriftTrackingSettingsGetArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// If feature drift tracking is to be turned on.
        /// </summary>
        [Input("featureDriftEnabled")]
        public Input<bool>? FeatureDriftEnabled { get; set; }

        /// <summary>
        /// The feature selection method to be used for drift tracking.
        /// </summary>
        [Input("featureSelection")]
        public Input<string>? FeatureSelection { get; set; }

        /// <summary>
        /// If target drift tracking is to be turned on.
        /// </summary>
        [Input("targetDriftEnabled")]
        public Input<bool>? TargetDriftEnabled { get; set; }

        [Input("trackedFeatures")]
        private InputList<string>? _trackedFeatures;

        /// <summary>
        /// List of features to be tracked for drift.
        /// </summary>
        public InputList<string> TrackedFeatures
        {
            get => _trackedFeatures ?? (_trackedFeatures = new InputList<string>());
            set => _trackedFeatures = value;
        }

        public DeploymentDriftTrackingSettingsGetArgs()
        {
        }
        public static new DeploymentDriftTrackingSettingsGetArgs Empty => new DeploymentDriftTrackingSettingsGetArgs();
    }
}
