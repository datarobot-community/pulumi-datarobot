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
    /// registered model
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
    ///     var exampleCustomModel = new Datarobot.CustomModel("exampleCustomModel", new()
    ///     {
    ///         Description = "Description for the example custom model",
    ///         TargetType = "Binary",
    ///         TargetName = "my_label",
    ///         BaseEnvironmentName = "[GenAI] Python 3.11 with Moderations",
    ///         Files = new[]
    ///         {
    ///             "example.py",
    ///         },
    ///     });
    /// 
    ///     var exampleRegisteredModel = new Datarobot.RegisteredModel("exampleRegisteredModel", new()
    ///     {
    ///         CustomModelVersionId = exampleCustomModel.VersionId,
    ///         Description = "Description for the example registered model",
    ///     });
    /// 
    ///     var examplePredictionEnvironment = new Datarobot.PredictionEnvironment("examplePredictionEnvironment", new()
    ///     {
    ///         Description = "Description for the example prediction environment",
    ///         Platform = "datarobotServerless",
    ///     });
    /// 
    ///     return new Dictionary&lt;string, object?&gt;
    ///     {
    ///         ["datarobotRegisteredModelId"] = exampleRegisteredModel.Id,
    ///         ["datarobotRegisteredModelVersionId"] = exampleRegisteredModel.VersionId,
    ///     };
    /// });
    /// ```
    /// </summary>
    [DatarobotResourceType("datarobot:index/registeredModel:RegisteredModel")]
    public partial class RegisteredModel : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The ID of the custom model version for this Registered Model.
        /// </summary>
        [Output("customModelVersionId")]
        public Output<string> CustomModelVersionId { get; private set; } = null!;

        /// <summary>
        /// The description of the Registered Model.
        /// </summary>
        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        /// <summary>
        /// The name of the Registered Model.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// The ID of the Registered Model Version.
        /// </summary>
        [Output("versionId")]
        public Output<string> VersionId { get; private set; } = null!;

        /// <summary>
        /// The name of the Registered Model Version.
        /// </summary>
        [Output("versionName")]
        public Output<string> VersionName { get; private set; } = null!;


        /// <summary>
        /// Create a RegisteredModel resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public RegisteredModel(string name, RegisteredModelArgs args, CustomResourceOptions? options = null)
            : base("datarobot:index/registeredModel:RegisteredModel", name, args ?? new RegisteredModelArgs(), MakeResourceOptions(options, ""))
        {
        }

        private RegisteredModel(string name, Input<string> id, RegisteredModelState? state = null, CustomResourceOptions? options = null)
            : base("datarobot:index/registeredModel:RegisteredModel", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing RegisteredModel resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static RegisteredModel Get(string name, Input<string> id, RegisteredModelState? state = null, CustomResourceOptions? options = null)
        {
            return new RegisteredModel(name, id, state, options);
        }
    }

    public sealed class RegisteredModelArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The ID of the custom model version for this Registered Model.
        /// </summary>
        [Input("customModelVersionId", required: true)]
        public Input<string> CustomModelVersionId { get; set; } = null!;

        /// <summary>
        /// The description of the Registered Model.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// The name of the Registered Model.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The name of the Registered Model Version.
        /// </summary>
        [Input("versionName")]
        public Input<string>? VersionName { get; set; }

        public RegisteredModelArgs()
        {
        }
        public static new RegisteredModelArgs Empty => new RegisteredModelArgs();
    }

    public sealed class RegisteredModelState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The ID of the custom model version for this Registered Model.
        /// </summary>
        [Input("customModelVersionId")]
        public Input<string>? CustomModelVersionId { get; set; }

        /// <summary>
        /// The description of the Registered Model.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// The name of the Registered Model.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The ID of the Registered Model Version.
        /// </summary>
        [Input("versionId")]
        public Input<string>? VersionId { get; set; }

        /// <summary>
        /// The name of the Registered Model Version.
        /// </summary>
        [Input("versionName")]
        public Input<string>? VersionName { get; set; }

        public RegisteredModelState()
        {
        }
        public static new RegisteredModelState Empty => new RegisteredModelState();
    }
}
