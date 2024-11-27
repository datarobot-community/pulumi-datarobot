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
    public sealed class BatchPredictionJobDefinitionTimeseriesSettings
    {
        /// <summary>
        /// Forecast point for the dataset, used for the forecast predictions. May be passed if timeseries_settings.type=forecast.
        /// </summary>
        public readonly string? ForecastPoint;
        /// <summary>
        /// End date for historical predictions. May be passed if timeseries_settings.type=historical.
        /// </summary>
        public readonly string? PredictionsEndDate;
        /// <summary>
        /// Start date for historical predictions. May be passed if timeseries_settings.type=historical.
        /// </summary>
        public readonly string? PredictionsStartDate;
        /// <summary>
        /// If True, missing values in the known in advance features are allowed in the forecast window at the prediction time. Default is False.
        /// </summary>
        public readonly bool? RelaxKnownInAdvanceFeaturesCheck;
        /// <summary>
        /// Type of time-series prediction. Must be 'forecast' or 'historical'. Default is 'forecast'.
        /// </summary>
        public readonly string? Type;

        [OutputConstructor]
        private BatchPredictionJobDefinitionTimeseriesSettings(
            string? forecastPoint,

            string? predictionsEndDate,

            string? predictionsStartDate,

            bool? relaxKnownInAdvanceFeaturesCheck,

            string? type)
        {
            ForecastPoint = forecastPoint;
            PredictionsEndDate = predictionsEndDate;
            PredictionsStartDate = predictionsStartDate;
            RelaxKnownInAdvanceFeaturesCheck = relaxKnownInAdvanceFeaturesCheck;
            Type = type;
        }
    }
}
