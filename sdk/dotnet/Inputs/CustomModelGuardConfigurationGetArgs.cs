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

    public sealed class CustomModelGuardConfigurationGetArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The deployment ID of this guard.
        /// </summary>
        [Input("deploymentId")]
        public Input<string>? DeploymentId { get; set; }

        /// <summary>
        /// The input column name of this guard.
        /// </summary>
        [Input("inputColumnName")]
        public Input<string>? InputColumnName { get; set; }

        /// <summary>
        /// The intervention for the guard configuration.
        /// </summary>
        [Input("intervention", required: true)]
        public Input<Inputs.CustomModelGuardConfigurationInterventionGetArgs> Intervention { get; set; } = null!;

        /// <summary>
        /// The LLM type for this guard.
        /// </summary>
        [Input("llmType")]
        public Input<string>? LlmType { get; set; }

        /// <summary>
        /// The name of the guard configuration.
        /// </summary>
        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        /// <summary>
        /// Configuration info for NeMo guards.
        /// </summary>
        [Input("nemoInfo")]
        public Input<Inputs.CustomModelGuardConfigurationNemoInfoGetArgs>? NemoInfo { get; set; }

        /// <summary>
        /// The OpenAI API base URL for this guard.
        /// </summary>
        [Input("openaiApiBase")]
        public Input<string>? OpenaiApiBase { get; set; }

        /// <summary>
        /// The ID of an OpenAI credential for this guard.
        /// </summary>
        [Input("openaiCredential")]
        public Input<string>? OpenaiCredential { get; set; }

        /// <summary>
        /// The ID of an OpenAI deployment for this guard.
        /// </summary>
        [Input("openaiDeploymentId")]
        public Input<string>? OpenaiDeploymentId { get; set; }

        /// <summary>
        /// The output column name of this guard.
        /// </summary>
        [Input("outputColumnName")]
        public Input<string>? OutputColumnName { get; set; }

        [Input("stages", required: true)]
        private InputList<string>? _stages;

        /// <summary>
        /// The list of stages for the guard configuration.
        /// </summary>
        public InputList<string> Stages
        {
            get => _stages ?? (_stages = new InputList<string>());
            set => _stages = value;
        }

        /// <summary>
        /// The template name of the guard configuration.
        /// </summary>
        [Input("templateName", required: true)]
        public Input<string> TemplateName { get; set; } = null!;

        public CustomModelGuardConfigurationGetArgs()
        {
        }
        public static new CustomModelGuardConfigurationGetArgs Empty => new CustomModelGuardConfigurationGetArgs();
    }
}
