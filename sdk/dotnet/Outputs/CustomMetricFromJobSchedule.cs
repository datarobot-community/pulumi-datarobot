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
    public sealed class CustomMetricFromJobSchedule
    {
        /// <summary>
        /// Days of the month when the metric job will run.
        /// </summary>
        public readonly ImmutableArray<string> DayOfMonths;
        /// <summary>
        /// Days of the week when the metric job will run.
        /// </summary>
        public readonly ImmutableArray<string> DayOfWeeks;
        /// <summary>
        /// Hours of the day when the metric job will run.
        /// </summary>
        public readonly ImmutableArray<string> Hours;
        /// <summary>
        /// Minutes of the day when the metric job will run.
        /// </summary>
        public readonly ImmutableArray<string> Minutes;
        /// <summary>
        /// Months of the year when the metric job will run.
        /// </summary>
        public readonly ImmutableArray<string> Months;

        [OutputConstructor]
        private CustomMetricFromJobSchedule(
            ImmutableArray<string> dayOfMonths,

            ImmutableArray<string> dayOfWeeks,

            ImmutableArray<string> hours,

            ImmutableArray<string> minutes,

            ImmutableArray<string> months)
        {
            DayOfMonths = dayOfMonths;
            DayOfWeeks = dayOfWeeks;
            Hours = hours;
            Minutes = minutes;
            Months = months;
        }
    }
}