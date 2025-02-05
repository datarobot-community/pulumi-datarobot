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
    public sealed class CustomMetricTimestamp
    {
        /// <summary>
        /// Column name.
        /// </summary>
        public readonly string? ColumnName;
        /// <summary>
        /// Format.
        /// </summary>
        public readonly string? TimeFormat;

        [OutputConstructor]
        private CustomMetricTimestamp(
            string? columnName,

            string? timeFormat)
        {
            ColumnName = columnName;
            TimeFormat = timeFormat;
        }
    }
}
