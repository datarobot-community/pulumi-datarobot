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

    public sealed class DeploymentRetrainingPolicyProjectOptionsGetArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The partitioning method for projects used to build new models.
        /// </summary>
        [Input("cvMethod")]
        public Input<string>? CvMethod { get; set; }

        /// <summary>
        /// The percentage of dataset to assign to holdout set in projects used to build new models.
        /// </summary>
        [Input("holdoutPct")]
        public Input<double>? HoldoutPct { get; set; }

        /// <summary>
        /// The model selection metric in projects used to build new models.
        /// </summary>
        [Input("metric")]
        public Input<string>? Metric { get; set; }

        /// <summary>
        /// The number of cross validation folds to use for projects used to build new models.
        /// </summary>
        [Input("reps")]
        public Input<double>? Reps { get; set; }

        /// <summary>
        /// The percentage of dataset to assign to validation set in projects used to build new models.
        /// </summary>
        [Input("validationPct")]
        public Input<double>? ValidationPct { get; set; }

        /// <summary>
        /// The validation type for projects used to build new models.
        /// </summary>
        [Input("validationType")]
        public Input<string>? ValidationType { get; set; }

        public DeploymentRetrainingPolicyProjectOptionsGetArgs()
        {
        }
        public static new DeploymentRetrainingPolicyProjectOptionsGetArgs Empty => new DeploymentRetrainingPolicyProjectOptionsGetArgs();
    }
}