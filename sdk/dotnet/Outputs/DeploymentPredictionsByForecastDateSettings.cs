// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Datarobot.Outputs
{

    [OutputType]
    public sealed class DeploymentPredictionsByForecastDateSettings
    {
        /// <summary>
        /// The column name in prediction datasets to be used as forecast date.
        /// </summary>
        public readonly string? ColumnName;
        /// <summary>
        /// The datetime format of the forecast date column in prediction datasets.
        /// </summary>
        public readonly string? DatetimeFormat;
        /// <summary>
        /// Is ’True’ if predictions by forecast date is enabled for this deployment.
        /// </summary>
        public readonly bool Enabled;

        [OutputConstructor]
        private DeploymentPredictionsByForecastDateSettings(
            string? columnName,

            string? datetimeFormat,

            bool enabled)
        {
            ColumnName = columnName;
            DatetimeFormat = datetimeFormat;
            Enabled = enabled;
        }
    }
}