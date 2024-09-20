// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace DataRobotPulumi.Datarobot
{
    /// <summary>
    /// Playground
    /// 
    /// ## Example Usage
    /// 
    /// ```csharp
    /// using System.Collections.Generic;
    /// using System.Linq;
    /// using Pulumi;
    /// using Datarobot = DataRobotPulumi.Datarobot;
    /// 
    /// return await Deployment.RunAsync(() =&gt; 
    /// {
    ///     var exampleUseCase = new Datarobot.UseCase("exampleUseCase");
    /// 
    ///     var examplePlayground = new Datarobot.Playground("examplePlayground", new()
    ///     {
    ///         UseCaseId = exampleUseCase.Id,
    ///     });
    /// 
    ///     return new Dictionary&lt;string, object?&gt;
    ///     {
    ///         ["exampleId"] = examplePlayground.Id,
    ///     };
    /// });
    /// ```
    /// </summary>
    [DatarobotResourceType("datarobot:index/playground:Playground")]
    public partial class Playground : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The description of the Playground.
        /// </summary>
        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        /// <summary>
        /// The name of the Playground.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// The id of the Playground.
        /// </summary>
        [Output("useCaseId")]
        public Output<string> UseCaseId { get; private set; } = null!;


        /// <summary>
        /// Create a Playground resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Playground(string name, PlaygroundArgs args, CustomResourceOptions? options = null)
            : base("datarobot:index/playground:Playground", name, args ?? new PlaygroundArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Playground(string name, Input<string> id, PlaygroundState? state = null, CustomResourceOptions? options = null)
            : base("datarobot:index/playground:Playground", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing Playground resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Playground Get(string name, Input<string> id, PlaygroundState? state = null, CustomResourceOptions? options = null)
        {
            return new Playground(name, id, state, options);
        }
    }

    public sealed class PlaygroundArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The description of the Playground.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// The name of the Playground.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The id of the Playground.
        /// </summary>
        [Input("useCaseId", required: true)]
        public Input<string> UseCaseId { get; set; } = null!;

        public PlaygroundArgs()
        {
        }
        public static new PlaygroundArgs Empty => new PlaygroundArgs();
    }

    public sealed class PlaygroundState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The description of the Playground.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// The name of the Playground.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The id of the Playground.
        /// </summary>
        [Input("useCaseId")]
        public Input<string>? UseCaseId { get; set; }

        public PlaygroundState()
        {
        }
        public static new PlaygroundState Empty => new PlaygroundState();
    }
}
