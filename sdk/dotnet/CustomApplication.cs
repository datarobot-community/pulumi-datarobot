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
    /// Custom Application
    /// </summary>
    [DatarobotResourceType("datarobot:index/customApplication:CustomApplication")]
    public partial class CustomApplication : global::Pulumi.CustomResource
    {
        /// <summary>
        /// Whether auto stopping is allowed for the Custom Application.
        /// </summary>
        [Output("allowAutoStopping")]
        public Output<bool> AllowAutoStopping { get; private set; } = null!;

        /// <summary>
        /// The URL of the Custom Application.
        /// </summary>
        [Output("applicationUrl")]
        public Output<string> ApplicationUrl { get; private set; } = null!;

        /// <summary>
        /// Whether external access is enabled for the Custom Application.
        /// </summary>
        [Output("externalAccessEnabled")]
        public Output<bool> ExternalAccessEnabled { get; private set; } = null!;

        /// <summary>
        /// The list of external email addresses that have access to the Custom Application.
        /// </summary>
        [Output("externalAccessRecipients")]
        public Output<ImmutableArray<string>> ExternalAccessRecipients { get; private set; } = null!;

        /// <summary>
        /// The name of the Custom Application.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// The resources for the Custom Application.
        /// </summary>
        [Output("resources")]
        public Output<Outputs.CustomApplicationResources?> Resources { get; private set; } = null!;

        /// <summary>
        /// The ID of the Custom Application Source.
        /// </summary>
        [Output("sourceId")]
        public Output<string> SourceId { get; private set; } = null!;

        /// <summary>
        /// The version ID of the Custom Application Source.
        /// </summary>
        [Output("sourceVersionId")]
        public Output<string> SourceVersionId { get; private set; } = null!;

        /// <summary>
        /// The list of Use Case IDs to add the Custom Application to.
        /// </summary>
        [Output("useCaseIds")]
        public Output<ImmutableArray<string>> UseCaseIds { get; private set; } = null!;


        /// <summary>
        /// Create a CustomApplication resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public CustomApplication(string name, CustomApplicationArgs args, CustomResourceOptions? options = null)
            : base("datarobot:index/customApplication:CustomApplication", name, args ?? new CustomApplicationArgs(), MakeResourceOptions(options, ""))
        {
        }

        private CustomApplication(string name, Input<string> id, CustomApplicationState? state = null, CustomResourceOptions? options = null)
            : base("datarobot:index/customApplication:CustomApplication", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing CustomApplication resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static CustomApplication Get(string name, Input<string> id, CustomApplicationState? state = null, CustomResourceOptions? options = null)
        {
            return new CustomApplication(name, id, state, options);
        }
    }

    public sealed class CustomApplicationArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Whether auto stopping is allowed for the Custom Application.
        /// </summary>
        [Input("allowAutoStopping")]
        public Input<bool>? AllowAutoStopping { get; set; }

        /// <summary>
        /// Whether external access is enabled for the Custom Application.
        /// </summary>
        [Input("externalAccessEnabled")]
        public Input<bool>? ExternalAccessEnabled { get; set; }

        [Input("externalAccessRecipients")]
        private InputList<string>? _externalAccessRecipients;

        /// <summary>
        /// The list of external email addresses that have access to the Custom Application.
        /// </summary>
        public InputList<string> ExternalAccessRecipients
        {
            get => _externalAccessRecipients ?? (_externalAccessRecipients = new InputList<string>());
            set => _externalAccessRecipients = value;
        }

        /// <summary>
        /// The name of the Custom Application.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The resources for the Custom Application.
        /// </summary>
        [Input("resources")]
        public Input<Inputs.CustomApplicationResourcesArgs>? Resources { get; set; }

        /// <summary>
        /// The version ID of the Custom Application Source.
        /// </summary>
        [Input("sourceVersionId", required: true)]
        public Input<string> SourceVersionId { get; set; } = null!;

        [Input("useCaseIds")]
        private InputList<string>? _useCaseIds;

        /// <summary>
        /// The list of Use Case IDs to add the Custom Application to.
        /// </summary>
        public InputList<string> UseCaseIds
        {
            get => _useCaseIds ?? (_useCaseIds = new InputList<string>());
            set => _useCaseIds = value;
        }

        public CustomApplicationArgs()
        {
        }
        public static new CustomApplicationArgs Empty => new CustomApplicationArgs();
    }

    public sealed class CustomApplicationState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Whether auto stopping is allowed for the Custom Application.
        /// </summary>
        [Input("allowAutoStopping")]
        public Input<bool>? AllowAutoStopping { get; set; }

        /// <summary>
        /// The URL of the Custom Application.
        /// </summary>
        [Input("applicationUrl")]
        public Input<string>? ApplicationUrl { get; set; }

        /// <summary>
        /// Whether external access is enabled for the Custom Application.
        /// </summary>
        [Input("externalAccessEnabled")]
        public Input<bool>? ExternalAccessEnabled { get; set; }

        [Input("externalAccessRecipients")]
        private InputList<string>? _externalAccessRecipients;

        /// <summary>
        /// The list of external email addresses that have access to the Custom Application.
        /// </summary>
        public InputList<string> ExternalAccessRecipients
        {
            get => _externalAccessRecipients ?? (_externalAccessRecipients = new InputList<string>());
            set => _externalAccessRecipients = value;
        }

        /// <summary>
        /// The name of the Custom Application.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The resources for the Custom Application.
        /// </summary>
        [Input("resources")]
        public Input<Inputs.CustomApplicationResourcesGetArgs>? Resources { get; set; }

        /// <summary>
        /// The ID of the Custom Application Source.
        /// </summary>
        [Input("sourceId")]
        public Input<string>? SourceId { get; set; }

        /// <summary>
        /// The version ID of the Custom Application Source.
        /// </summary>
        [Input("sourceVersionId")]
        public Input<string>? SourceVersionId { get; set; }

        [Input("useCaseIds")]
        private InputList<string>? _useCaseIds;

        /// <summary>
        /// The list of Use Case IDs to add the Custom Application to.
        /// </summary>
        public InputList<string> UseCaseIds
        {
            get => _useCaseIds ?? (_useCaseIds = new InputList<string>());
            set => _useCaseIds = value;
        }

        public CustomApplicationState()
        {
        }
        public static new CustomApplicationState Empty => new CustomApplicationState();
    }
}
