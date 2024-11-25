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

    public sealed class CustomModelGuardConfigurationNemoInfoGetArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The actions for the NeMo information.
        /// </summary>
        [Input("actions")]
        public Input<string>? Actions { get; set; }

        /// <summary>
        /// NeMo guardrails blocked terms list.
        /// </summary>
        [Input("blockedTerms")]
        public Input<string>? BlockedTerms { get; set; }

        /// <summary>
        /// NeMo guardrails prompts.
        /// </summary>
        [Input("llmPrompts")]
        public Input<string>? LlmPrompts { get; set; }

        /// <summary>
        /// Overall NeMo configuration YAML.
        /// </summary>
        [Input("mainConfig")]
        public Input<string>? MainConfig { get; set; }

        /// <summary>
        /// NeMo guardrails configuration Colang.
        /// </summary>
        [Input("railsConfig")]
        public Input<string>? RailsConfig { get; set; }

        public CustomModelGuardConfigurationNemoInfoGetArgs()
        {
        }
        public static new CustomModelGuardConfigurationNemoInfoGetArgs Empty => new CustomModelGuardConfigurationNemoInfoGetArgs();
    }
}
