// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Datarobot.Inputs
{

    public sealed class CustomModelGuardConfigurationInterventionConditionArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The comparand of the guard condition.
        /// </summary>
        [Input("comparand", required: true)]
        public Input<double> Comparand { get; set; } = null!;

        /// <summary>
        /// The comparator of the guard condition.
        /// </summary>
        [Input("comparator", required: true)]
        public Input<string> Comparator { get; set; } = null!;

        public CustomModelGuardConfigurationInterventionConditionArgs()
        {
        }
        public static new CustomModelGuardConfigurationInterventionConditionArgs Empty => new CustomModelGuardConfigurationInterventionConditionArgs();
    }
}
