// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Datarobot.Inputs
{

    public sealed class DeploymentHealthSettingsDataDriftArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The batch count for the data drift health settings.
        /// </summary>
        [Input("batchCount")]
        public Input<int>? BatchCount { get; set; }

        /// <summary>
        /// The drift threshold for the data drift health settings.
        /// </summary>
        [Input("driftThreshold")]
        public Input<double>? DriftThreshold { get; set; }

        [Input("excludeFeatures")]
        private InputList<string>? _excludeFeatures;

        /// <summary>
        /// The exclude features for the data drift health settings.
        /// </summary>
        public InputList<string> ExcludeFeatures
        {
            get => _excludeFeatures ?? (_excludeFeatures = new InputList<string>());
            set => _excludeFeatures = value;
        }

        /// <summary>
        /// The high importance failing count for the data drift health settings.
        /// </summary>
        [Input("highImportanceFailingCount")]
        public Input<int>? HighImportanceFailingCount { get; set; }

        /// <summary>
        /// The high importance warning count for the data drift health settings.
        /// </summary>
        [Input("highImportanceWarningCount")]
        public Input<int>? HighImportanceWarningCount { get; set; }

        /// <summary>
        /// The importance threshold for the data drift health settings.
        /// </summary>
        [Input("importanceThreshold")]
        public Input<double>? ImportanceThreshold { get; set; }

        /// <summary>
        /// The low importance failing count for the data drift health settings.
        /// </summary>
        [Input("lowImportanceFailingCount")]
        public Input<int>? LowImportanceFailingCount { get; set; }

        /// <summary>
        /// The low importance warning count for the data drift health settings.
        /// </summary>
        [Input("lowImportanceWarningCount")]
        public Input<int>? LowImportanceWarningCount { get; set; }

        [Input("starredFeatures")]
        private InputList<string>? _starredFeatures;

        /// <summary>
        /// The starred features for the data drift health settings.
        /// </summary>
        public InputList<string> StarredFeatures
        {
            get => _starredFeatures ?? (_starredFeatures = new InputList<string>());
            set => _starredFeatures = value;
        }

        /// <summary>
        /// The time interval for the data drift health settings.
        /// </summary>
        [Input("timeInterval")]
        public Input<string>? TimeInterval { get; set; }

        public DeploymentHealthSettingsDataDriftArgs()
        {
        }
        public static new DeploymentHealthSettingsDataDriftArgs Empty => new DeploymentHealthSettingsDataDriftArgs();
    }
}