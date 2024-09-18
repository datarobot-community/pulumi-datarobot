// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Datarobot.Inputs
{

    public sealed class DeploymentHealthSettingsCustomMetricsArgs : global::Pulumi.ResourceArgs
    {
        [Input("failingConditions")]
        private InputList<Inputs.DeploymentHealthSettingsCustomMetricsFailingConditionArgs>? _failingConditions;

        /// <summary>
        /// The failing conditions for the custom metrics health settings.
        /// </summary>
        public InputList<Inputs.DeploymentHealthSettingsCustomMetricsFailingConditionArgs> FailingConditions
        {
            get => _failingConditions ?? (_failingConditions = new InputList<Inputs.DeploymentHealthSettingsCustomMetricsFailingConditionArgs>());
            set => _failingConditions = value;
        }

        [Input("warningConditions")]
        private InputList<Inputs.DeploymentHealthSettingsCustomMetricsWarningConditionArgs>? _warningConditions;

        /// <summary>
        /// The warning conditions for the custom metrics health settings.
        /// </summary>
        public InputList<Inputs.DeploymentHealthSettingsCustomMetricsWarningConditionArgs> WarningConditions
        {
            get => _warningConditions ?? (_warningConditions = new InputList<Inputs.DeploymentHealthSettingsCustomMetricsWarningConditionArgs>());
            set => _warningConditions = value;
        }

        public DeploymentHealthSettingsCustomMetricsArgs()
        {
        }
        public static new DeploymentHealthSettingsCustomMetricsArgs Empty => new DeploymentHealthSettingsCustomMetricsArgs();
    }
}
