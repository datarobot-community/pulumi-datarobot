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
    /// remote repository
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
    ///     var example = new Datarobot.RemoteRepository("example", new()
    ///     {
    ///         Description = "Description for the example remote repository",
    ///         Location = "https://github.com/datarobot/datarobot-user-models",
    ///         SourceType = "github",
    ///     });
    /// 
    /// });
    /// ```
    /// </summary>
    [DatarobotResourceType("datarobot:index/remoteRepository:RemoteRepository")]
    public partial class RemoteRepository : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The description of the Remote Repository.
        /// </summary>
        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        /// <summary>
        /// The location of the Remote Repository.
        /// </summary>
        [Output("location")]
        public Output<string> Location { get; private set; } = null!;

        /// <summary>
        /// The name of the Remote Repository.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// The personal access token for the Remote Repository.
        /// </summary>
        [Output("personalAccessToken")]
        public Output<string?> PersonalAccessToken { get; private set; } = null!;

        /// <summary>
        /// The source type of the Remote Repository.
        /// </summary>
        [Output("sourceType")]
        public Output<string> SourceType { get; private set; } = null!;


        /// <summary>
        /// Create a RemoteRepository resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public RemoteRepository(string name, RemoteRepositoryArgs args, CustomResourceOptions? options = null)
            : base("datarobot:index/remoteRepository:RemoteRepository", name, args ?? new RemoteRepositoryArgs(), MakeResourceOptions(options, ""))
        {
        }

        private RemoteRepository(string name, Input<string> id, RemoteRepositoryState? state = null, CustomResourceOptions? options = null)
            : base("datarobot:index/remoteRepository:RemoteRepository", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing RemoteRepository resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static RemoteRepository Get(string name, Input<string> id, RemoteRepositoryState? state = null, CustomResourceOptions? options = null)
        {
            return new RemoteRepository(name, id, state, options);
        }
    }

    public sealed class RemoteRepositoryArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The description of the Remote Repository.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// The location of the Remote Repository.
        /// </summary>
        [Input("location", required: true)]
        public Input<string> Location { get; set; } = null!;

        /// <summary>
        /// The name of the Remote Repository.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The personal access token for the Remote Repository.
        /// </summary>
        [Input("personalAccessToken")]
        public Input<string>? PersonalAccessToken { get; set; }

        /// <summary>
        /// The source type of the Remote Repository.
        /// </summary>
        [Input("sourceType", required: true)]
        public Input<string> SourceType { get; set; } = null!;

        public RemoteRepositoryArgs()
        {
        }
        public static new RemoteRepositoryArgs Empty => new RemoteRepositoryArgs();
    }

    public sealed class RemoteRepositoryState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The description of the Remote Repository.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// The location of the Remote Repository.
        /// </summary>
        [Input("location")]
        public Input<string>? Location { get; set; }

        /// <summary>
        /// The name of the Remote Repository.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The personal access token for the Remote Repository.
        /// </summary>
        [Input("personalAccessToken")]
        public Input<string>? PersonalAccessToken { get; set; }

        /// <summary>
        /// The source type of the Remote Repository.
        /// </summary>
        [Input("sourceType")]
        public Input<string>? SourceType { get; set; }

        public RemoteRepositoryState()
        {
        }
        public static new RemoteRepositoryState Empty => new RemoteRepositoryState();
    }
}
