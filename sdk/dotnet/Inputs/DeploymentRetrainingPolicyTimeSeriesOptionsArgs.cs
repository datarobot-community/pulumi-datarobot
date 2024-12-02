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

    public sealed class DeploymentRetrainingPolicyTimeSeriesOptionsArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The ID of the calendar to be used in this project.
        /// </summary>
        [Input("calendarId")]
        public Input<string>? CalendarId { get; set; }

        /// <summary>
        /// For time series projects only. Used to specify which differencing method to apply if the data is stationary. For classification problems simple and seasonal are not allowed. Parameter periodicities must be specified if seasonal is chosen. Defaults to auto.
        /// </summary>
        [Input("differencingMethod")]
        public Input<string>? DifferencingMethod { get; set; }

        /// <summary>
        /// Discount factor (alpha) used for exponentially weighted moving features.
        /// </summary>
        [Input("exponentiallyWeightedMovingAlpha")]
        public Input<double>? ExponentiallyWeightedMovingAlpha { get; set; }

        [Input("periodicities")]
        private InputList<Inputs.DeploymentRetrainingPolicyTimeSeriesOptionsPeriodicityArgs>? _periodicities;

        /// <summary>
        /// A list of periodicities for time series projects only. For classification problems periodicities are not allowed. If this is provided, parameter 'differencing*method' will default to 'seasonal' if not provided or 'auto'.
        /// </summary>
        public InputList<Inputs.DeploymentRetrainingPolicyTimeSeriesOptionsPeriodicityArgs> Periodicities
        {
            get => _periodicities ?? (_periodicities = new InputList<Inputs.DeploymentRetrainingPolicyTimeSeriesOptionsPeriodicityArgs>());
            set => _periodicities = value;
        }

        /// <summary>
        /// For time series projects only. Used to specify whether to treat data as exponential trend and apply transformations like log-transform. For classification problems always is not allowed. Defaults to auto.
        /// </summary>
        [Input("treatAsExponential")]
        public Input<string>? TreatAsExponential { get; set; }

        public DeploymentRetrainingPolicyTimeSeriesOptionsArgs()
        {
        }
        public static new DeploymentRetrainingPolicyTimeSeriesOptionsArgs Empty => new DeploymentRetrainingPolicyTimeSeriesOptionsArgs();
    }
}
