// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Datarobot
{
    /// <summary>
    /// LLMBlueprint
    /// 
    /// ## Example Usage
    /// 
    /// ```csharp
    /// using System.Collections.Generic;
    /// using System.Linq;
    /// using Pulumi;
    /// using Datarobot = Pulumi.Datarobot;
    /// 
    /// return await Deployment.RunAsync(() =&gt; 
    /// {
    ///     var exampleUseCase = new Datarobot.UseCase("exampleUseCase");
    /// 
    ///     var examplePlayground = new Datarobot.Playground("examplePlayground", new()
    ///     {
    ///         Description = "Description for the example playground",
    ///         UseCaseId = exampleUseCase.Id,
    ///     });
    /// 
    ///     var exampleLlmBlueprint = new Datarobot.LlmBlueprint("exampleLlmBlueprint", new()
    ///     {
    ///         Description = "Description for the example LLM blueprint",
    ///         PlaygroundId = examplePlayground.Id,
    ///         LlmId = "azure-openai-gpt-3.5-turbo",
    ///     });
    /// 
    ///     return new Dictionary&lt;string, object?&gt;
    ///     {
    ///         ["exampleId"] = exampleLlmBlueprint.Id,
    ///     };
    /// });
    /// ```
    /// </summary>
    [DatarobotResourceType("datarobot:index/llmBlueprint:LlmBlueprint")]
    public partial class LlmBlueprint : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The description of the LLM Blueprint.
        /// </summary>
        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        /// <summary>
        /// The id of the LLM for the LLM Blueprint.
        /// </summary>
        [Output("llmId")]
        public Output<string> LlmId { get; private set; } = null!;

        /// <summary>
        /// The name of the LLM Blueprint.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// The id of the Playground for the LLM Blueprint.
        /// </summary>
        [Output("playgroundId")]
        public Output<string> PlaygroundId { get; private set; } = null!;

        /// <summary>
        /// The id of the Vector Database for the LLM Blueprint.
        /// </summary>
        [Output("vectorDatabaseId")]
        public Output<string?> VectorDatabaseId { get; private set; } = null!;


        /// <summary>
        /// Create a LlmBlueprint resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public LlmBlueprint(string name, LlmBlueprintArgs args, CustomResourceOptions? options = null)
            : base("datarobot:index/llmBlueprint:LlmBlueprint", name, args ?? new LlmBlueprintArgs(), MakeResourceOptions(options, ""))
        {
        }

        private LlmBlueprint(string name, Input<string> id, LlmBlueprintState? state = null, CustomResourceOptions? options = null)
            : base("datarobot:index/llmBlueprint:LlmBlueprint", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                PluginDownloadURL = "github://api.github.com/datarobot-community/pulumi-datarobot",
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing LlmBlueprint resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static LlmBlueprint Get(string name, Input<string> id, LlmBlueprintState? state = null, CustomResourceOptions? options = null)
        {
            return new LlmBlueprint(name, id, state, options);
        }
    }

    public sealed class LlmBlueprintArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The description of the LLM Blueprint.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// The id of the LLM for the LLM Blueprint.
        /// </summary>
        [Input("llmId", required: true)]
        public Input<string> LlmId { get; set; } = null!;

        /// <summary>
        /// The name of the LLM Blueprint.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The id of the Playground for the LLM Blueprint.
        /// </summary>
        [Input("playgroundId", required: true)]
        public Input<string> PlaygroundId { get; set; } = null!;

        /// <summary>
        /// The id of the Vector Database for the LLM Blueprint.
        /// </summary>
        [Input("vectorDatabaseId")]
        public Input<string>? VectorDatabaseId { get; set; }

        public LlmBlueprintArgs()
        {
        }
        public static new LlmBlueprintArgs Empty => new LlmBlueprintArgs();
    }

    public sealed class LlmBlueprintState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The description of the LLM Blueprint.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// The id of the LLM for the LLM Blueprint.
        /// </summary>
        [Input("llmId")]
        public Input<string>? LlmId { get; set; }

        /// <summary>
        /// The name of the LLM Blueprint.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The id of the Playground for the LLM Blueprint.
        /// </summary>
        [Input("playgroundId")]
        public Input<string>? PlaygroundId { get; set; }

        /// <summary>
        /// The id of the Vector Database for the LLM Blueprint.
        /// </summary>
        [Input("vectorDatabaseId")]
        public Input<string>? VectorDatabaseId { get; set; }

        public LlmBlueprintState()
        {
        }
        public static new LlmBlueprintState Empty => new LlmBlueprintState();
    }
}
