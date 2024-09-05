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
    /// The provider type for the datarobot package. By default, resources use package-wide configuration
    /// settings, however an explicit `Provider` instance may be created and passed during resource
    /// construction to achieve fine-grained programmatic control over provider settings. See the
    /// [documentation](https://www.pulumi.com/docs/reference/programming-model/#providers) for more information.
    /// </summary>
    [DatarobotResourceType("pulumi:providers:datarobot")]
    public partial class Provider : global::Pulumi.ProviderResource
    {
        /// <summary>
        /// Key to access DataRobot API
        /// </summary>
        [Output("apikey")]
        public Output<string?> Apikey { get; private set; } = null!;

        /// <summary>
        /// Endpoint for the DataRobot API
        /// </summary>
        [Output("endpoint")]
        public Output<string?> Endpoint { get; private set; } = null!;


        /// <summary>
        /// Create a Provider resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Provider(string name, ProviderArgs? args = null, CustomResourceOptions? options = null)
            : base("datarobot", name, args ?? new ProviderArgs(), MakeResourceOptions(options, ""))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                PluginDownloadURL = "github://api.github.com/datarobot-community/pulumi-datarobot",
                AdditionalSecretOutputs =
                {
                    "apikey",
                    "endpoint",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
    }

    public sealed class ProviderArgs : global::Pulumi.ResourceArgs
    {
        [Input("apikey")]
        private Input<string>? _apikey;

        /// <summary>
        /// Key to access DataRobot API
        /// </summary>
        public Input<string>? Apikey
        {
            get => _apikey;
            set
            {
                var emptySecret = Output.CreateSecret(0);
                _apikey = Output.Tuple<Input<string>?, int>(value, emptySecret).Apply(t => t.Item1);
            }
        }

        [Input("endpoint")]
        private Input<string>? _endpoint;

        /// <summary>
        /// Endpoint for the DataRobot API
        /// </summary>
        public Input<string>? Endpoint
        {
            get => _endpoint;
            set
            {
                var emptySecret = Output.CreateSecret(0);
                _endpoint = Output.Tuple<Input<string>?, int>(value, emptySecret).Apply(t => t.Item1);
            }
        }

        public ProviderArgs()
        {
        }
        public static new ProviderArgs Empty => new ProviderArgs();
    }
}
