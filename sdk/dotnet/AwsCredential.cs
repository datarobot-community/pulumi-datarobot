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
    /// AWS Credential
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
    ///     var example = new Datarobot.AwsCredential("example", new()
    ///     {
    ///         AwsAccessKeyId = "example_access_key_id",
    ///         AwsSecretAccessKey = "example_secret_access_key",
    ///         AwsSessionToken = "example_session_token",
    ///         Description = "Description for the example AWS credential",
    ///     });
    /// 
    /// });
    /// ```
    /// </summary>
    [DatarobotResourceType("datarobot:index/awsCredential:AwsCredential")]
    public partial class AwsCredential : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The AWS Access Key ID.
        /// </summary>
        [Output("awsAccessKeyId")]
        public Output<string?> AwsAccessKeyId { get; private set; } = null!;

        /// <summary>
        /// The AWS Secret Access Key.
        /// </summary>
        [Output("awsSecretAccessKey")]
        public Output<string?> AwsSecretAccessKey { get; private set; } = null!;

        /// <summary>
        /// The AWS Session Token.
        /// </summary>
        [Output("awsSessionToken")]
        public Output<string?> AwsSessionToken { get; private set; } = null!;

        /// <summary>
        /// The ID of the saved shared secure configuration. If specified, cannot include awsAccessKeyId, awsSecretAccessKey or awsSessionToken.
        /// </summary>
        [Output("configId")]
        public Output<string?> ConfigId { get; private set; } = null!;

        /// <summary>
        /// The description of the AWS Credential.
        /// </summary>
        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        /// <summary>
        /// The name of the AWS Credential.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;


        /// <summary>
        /// Create a AwsCredential resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public AwsCredential(string name, AwsCredentialArgs? args = null, CustomResourceOptions? options = null)
            : base("datarobot:index/awsCredential:AwsCredential", name, args ?? new AwsCredentialArgs(), MakeResourceOptions(options, ""))
        {
        }

        private AwsCredential(string name, Input<string> id, AwsCredentialState? state = null, CustomResourceOptions? options = null)
            : base("datarobot:index/awsCredential:AwsCredential", name, state, MakeResourceOptions(options, id))
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
                    "awsSecretAccessKey",
                    "awsSessionToken",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing AwsCredential resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static AwsCredential Get(string name, Input<string> id, AwsCredentialState? state = null, CustomResourceOptions? options = null)
        {
            return new AwsCredential(name, id, state, options);
        }
    }

    public sealed class AwsCredentialArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The AWS Access Key ID.
        /// </summary>
        [Input("awsAccessKeyId")]
        public Input<string>? AwsAccessKeyId { get; set; }

        [Input("awsSecretAccessKey")]
        private Input<string>? _awsSecretAccessKey;

        /// <summary>
        /// The AWS Secret Access Key.
        /// </summary>
        public Input<string>? AwsSecretAccessKey
        {
            get => _awsSecretAccessKey;
            set
            {
                var emptySecret = Output.CreateSecret(0);
                _awsSecretAccessKey = Output.Tuple<Input<string>?, int>(value, emptySecret).Apply(t => t.Item1);
            }
        }

        [Input("awsSessionToken")]
        private Input<string>? _awsSessionToken;

        /// <summary>
        /// The AWS Session Token.
        /// </summary>
        public Input<string>? AwsSessionToken
        {
            get => _awsSessionToken;
            set
            {
                var emptySecret = Output.CreateSecret(0);
                _awsSessionToken = Output.Tuple<Input<string>?, int>(value, emptySecret).Apply(t => t.Item1);
            }
        }

        /// <summary>
        /// The ID of the saved shared secure configuration. If specified, cannot include awsAccessKeyId, awsSecretAccessKey or awsSessionToken.
        /// </summary>
        [Input("configId")]
        public Input<string>? ConfigId { get; set; }

        /// <summary>
        /// The description of the AWS Credential.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// The name of the AWS Credential.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        public AwsCredentialArgs()
        {
        }
        public static new AwsCredentialArgs Empty => new AwsCredentialArgs();
    }

    public sealed class AwsCredentialState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The AWS Access Key ID.
        /// </summary>
        [Input("awsAccessKeyId")]
        public Input<string>? AwsAccessKeyId { get; set; }

        [Input("awsSecretAccessKey")]
        private Input<string>? _awsSecretAccessKey;

        /// <summary>
        /// The AWS Secret Access Key.
        /// </summary>
        public Input<string>? AwsSecretAccessKey
        {
            get => _awsSecretAccessKey;
            set
            {
                var emptySecret = Output.CreateSecret(0);
                _awsSecretAccessKey = Output.Tuple<Input<string>?, int>(value, emptySecret).Apply(t => t.Item1);
            }
        }

        [Input("awsSessionToken")]
        private Input<string>? _awsSessionToken;

        /// <summary>
        /// The AWS Session Token.
        /// </summary>
        public Input<string>? AwsSessionToken
        {
            get => _awsSessionToken;
            set
            {
                var emptySecret = Output.CreateSecret(0);
                _awsSessionToken = Output.Tuple<Input<string>?, int>(value, emptySecret).Apply(t => t.Item1);
            }
        }

        /// <summary>
        /// The ID of the saved shared secure configuration. If specified, cannot include awsAccessKeyId, awsSecretAccessKey or awsSessionToken.
        /// </summary>
        [Input("configId")]
        public Input<string>? ConfigId { get; set; }

        /// <summary>
        /// The description of the AWS Credential.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// The name of the AWS Credential.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        public AwsCredentialState()
        {
        }
        public static new AwsCredentialState Empty => new AwsCredentialState();
    }
}