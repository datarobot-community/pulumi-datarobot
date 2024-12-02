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

    public sealed class BatchPredictionJobDefinitionPredictionInstanceGetArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// By default, prediction requests will use the API key of the user that created the job. This allows you to make requests on behalf of other users.
        /// </summary>
        [Input("apiKey")]
        public Input<string>? ApiKey { get; set; }

        /// <summary>
        /// If running a job against a prediction instance in the Managed AI Cloud, you must provide the organization level DataRobot-Key.
        /// </summary>
        [Input("datarobotKey")]
        public Input<string>? DatarobotKey { get; set; }

        /// <summary>
        /// Hostname of the prediction instance.
        /// </summary>
        [Input("hostName", required: true)]
        public Input<string> HostName { get; set; } = null!;

        /// <summary>
        /// Set to false to run prediction requests from the batch prediction job without SSL. Defaults to true.
        /// </summary>
        [Input("sslEnabled")]
        public Input<bool>? SslEnabled { get; set; }

        public BatchPredictionJobDefinitionPredictionInstanceGetArgs()
        {
        }
        public static new BatchPredictionJobDefinitionPredictionInstanceGetArgs Empty => new BatchPredictionJobDefinitionPredictionInstanceGetArgs();
    }
}