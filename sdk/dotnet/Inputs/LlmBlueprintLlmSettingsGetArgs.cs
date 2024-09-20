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

    public sealed class LlmBlueprintLlmSettingsGetArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The maximum number of tokens allowed in the completion. The combined count of this value and prompt tokens must be below the model's maximum context size, where prompt token count is comprised of system prompt, user prompt, recent chat history, and vector database citations.
        /// </summary>
        [Input("maxCompletionLength")]
        public Input<int>? MaxCompletionLength { get; set; }

        /// <summary>
        /// Guides the style of the LLM response. It is a 'universal' prompt, prepended to all individual prompts.
        /// </summary>
        [Input("systemPrompt")]
        public Input<string>? SystemPrompt { get; set; }

        /// <summary>
        /// Controls the randomness of model output, where higher values return more diverse output and lower values return more deterministic results.
        /// </summary>
        [Input("temperature")]
        public Input<double>? Temperature { get; set; }

        /// <summary>
        /// Threshold that controls the selection of words included in the response, based on a cumulative probability cutoff for token selection. Higher numbers return more diverse options for outputs.
        /// </summary>
        [Input("topP")]
        public Input<double>? TopP { get; set; }

        public LlmBlueprintLlmSettingsGetArgs()
        {
        }
        public static new LlmBlueprintLlmSettingsGetArgs Empty => new LlmBlueprintLlmSettingsGetArgs();
    }
}
