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

    public sealed class DeploymentRetrainingPolicyTriggerScheduleGetArgs : global::Pulumi.ResourceArgs
    {
        [Input("dayOfMonths", required: true)]
        private InputList<string>? _dayOfMonths;

        /// <summary>
        /// Days of the month when the job will run.
        /// </summary>
        public InputList<string> DayOfMonths
        {
            get => _dayOfMonths ?? (_dayOfMonths = new InputList<string>());
            set => _dayOfMonths = value;
        }

        [Input("dayOfWeeks", required: true)]
        private InputList<string>? _dayOfWeeks;

        /// <summary>
        /// Days of the week when the job will run.
        /// </summary>
        public InputList<string> DayOfWeeks
        {
            get => _dayOfWeeks ?? (_dayOfWeeks = new InputList<string>());
            set => _dayOfWeeks = value;
        }

        [Input("hours", required: true)]
        private InputList<string>? _hours;

        /// <summary>
        /// Hours of the day when the job will run.
        /// </summary>
        public InputList<string> Hours
        {
            get => _hours ?? (_hours = new InputList<string>());
            set => _hours = value;
        }

        [Input("minutes", required: true)]
        private InputList<string>? _minutes;

        /// <summary>
        /// Minutes of the day when the job will run.
        /// </summary>
        public InputList<string> Minutes
        {
            get => _minutes ?? (_minutes = new InputList<string>());
            set => _minutes = value;
        }

        [Input("months", required: true)]
        private InputList<string>? _months;

        /// <summary>
        /// Months of the year when the job will run.
        /// </summary>
        public InputList<string> Months
        {
            get => _months ?? (_months = new InputList<string>());
            set => _months = value;
        }

        public DeploymentRetrainingPolicyTriggerScheduleGetArgs()
        {
        }
        public static new DeploymentRetrainingPolicyTriggerScheduleGetArgs Empty => new DeploymentRetrainingPolicyTriggerScheduleGetArgs();
    }
}
