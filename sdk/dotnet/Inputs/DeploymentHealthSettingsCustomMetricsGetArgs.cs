// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Datarobot.Inputs
{

    public sealed class DeploymentHealthSettingsCustomMetricsGetArgs : global::Pulumi.ResourceArgs
    {
        [Input("failingConditions")]
        private InputList<Inputs.DeploymentHealthSettingsCustomMetricsFailingConditionGetArgs>? _failingConditions;

        /// <summary>
        /// The failing conditions for the custom metrics health settings.
        /// </summary>
        public InputList<Inputs.DeploymentHealthSettingsCustomMetricsFailingConditionGetArgs> FailingConditions
        {
            get => _failingConditions ?? (_failingConditions = new InputList<Inputs.DeploymentHealthSettingsCustomMetricsFailingConditionGetArgs>());
            set => _failingConditions = value;
        }

        [Input("warningConditions")]
        private InputList<Inputs.DeploymentHealthSettingsCustomMetricsWarningConditionGetArgs>? _warningConditions;

        /// <summary>
        /// The warning conditions for the custom metrics health settings.
        /// </summary>
        public InputList<Inputs.DeploymentHealthSettingsCustomMetricsWarningConditionGetArgs> WarningConditions
        {
            get => _warningConditions ?? (_warningConditions = new InputList<Inputs.DeploymentHealthSettingsCustomMetricsWarningConditionGetArgs>());
            set => _warningConditions = value;
        }

        public DeploymentHealthSettingsCustomMetricsGetArgs()
        {
        }
        public static new DeploymentHealthSettingsCustomMetricsGetArgs Empty => new DeploymentHealthSettingsCustomMetricsGetArgs();
    }
}