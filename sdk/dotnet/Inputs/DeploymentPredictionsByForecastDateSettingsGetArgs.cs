// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Datarobot.Inputs
{

    public sealed class DeploymentPredictionsByForecastDateSettingsGetArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The column name in prediction datasets to be used as forecast date.
        /// </summary>
        [Input("columnName")]
        public Input<string>? ColumnName { get; set; }

        /// <summary>
        /// The datetime format of the forecast date column in prediction datasets.
        /// </summary>
        [Input("datetimeFormat")]
        public Input<string>? DatetimeFormat { get; set; }

        /// <summary>
        /// Is ’True’ if predictions by forecast date is enabled for this deployment.
        /// </summary>
        [Input("enabled", required: true)]
        public Input<bool> Enabled { get; set; } = null!;

        public DeploymentPredictionsByForecastDateSettingsGetArgs()
        {
        }
        public static new DeploymentPredictionsByForecastDateSettingsGetArgs Empty => new DeploymentPredictionsByForecastDateSettingsGetArgs();
    }
}