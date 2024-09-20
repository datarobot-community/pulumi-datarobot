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
    /// Api Token Credential
    /// </summary>
    [DatarobotResourceType("datarobot:index/googleCloudCredential:GoogleCloudCredential")]
    public partial class GoogleCloudCredential : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The name of the Google Cloud Credential.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// The source file of the Google Cloud Credential.
        /// </summary>
        [Output("sourceFile")]
        public Output<string> SourceFile { get; private set; } = null!;


        /// <summary>
        /// Create a GoogleCloudCredential resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public GoogleCloudCredential(string name, GoogleCloudCredentialArgs args, CustomResourceOptions? options = null)
            : base("datarobot:index/googleCloudCredential:GoogleCloudCredential", name, args ?? new GoogleCloudCredentialArgs(), MakeResourceOptions(options, ""))
        {
        }

        private GoogleCloudCredential(string name, Input<string> id, GoogleCloudCredentialState? state = null, CustomResourceOptions? options = null)
            : base("datarobot:index/googleCloudCredential:GoogleCloudCredential", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing GoogleCloudCredential resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static GoogleCloudCredential Get(string name, Input<string> id, GoogleCloudCredentialState? state = null, CustomResourceOptions? options = null)
        {
            return new GoogleCloudCredential(name, id, state, options);
        }
    }

    public sealed class GoogleCloudCredentialArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The name of the Google Cloud Credential.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The source file of the Google Cloud Credential.
        /// </summary>
        [Input("sourceFile", required: true)]
        public Input<string> SourceFile { get; set; } = null!;

        public GoogleCloudCredentialArgs()
        {
        }
        public static new GoogleCloudCredentialArgs Empty => new GoogleCloudCredentialArgs();
    }

    public sealed class GoogleCloudCredentialState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The name of the Google Cloud Credential.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The source file of the Google Cloud Credential.
        /// </summary>
        [Input("sourceFile")]
        public Input<string>? SourceFile { get; set; }

        public GoogleCloudCredentialState()
        {
        }
        public static new GoogleCloudCredentialState Empty => new GoogleCloudCredentialState();
    }
}
