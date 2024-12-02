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

    public sealed class BatchPredictionJobDefinitionTimeseriesSettingsGetArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Forecast point for the dataset, used for the forecast predictions. May be passed if timeseries_settings.type=forecast.
        /// </summary>
        [Input("forecastPoint")]
        public Input<string>? ForecastPoint { get; set; }

        /// <summary>
        /// End date for historical predictions. May be passed if timeseries_settings.type=historical.
        /// </summary>
        [Input("predictionsEndDate")]
        public Input<string>? PredictionsEndDate { get; set; }

        /// <summary>
        /// Start date for historical predictions. May be passed if timeseries_settings.type=historical.
        /// </summary>
        [Input("predictionsStartDate")]
        public Input<string>? PredictionsStartDate { get; set; }

        /// <summary>
        /// If True, missing values in the known in advance features are allowed in the forecast window at the prediction time. Default is False.
        /// </summary>
        [Input("relaxKnownInAdvanceFeaturesCheck")]
        public Input<bool>? RelaxKnownInAdvanceFeaturesCheck { get; set; }

        /// <summary>
        /// Type of time-series prediction. Must be 'forecast' or 'historical'. Default is 'forecast'.
        /// </summary>
        [Input("type")]
        public Input<string>? Type { get; set; }

        public BatchPredictionJobDefinitionTimeseriesSettingsGetArgs()
        {
        }
        public static new BatchPredictionJobDefinitionTimeseriesSettingsGetArgs Empty => new BatchPredictionJobDefinitionTimeseriesSettingsGetArgs();
    }
}