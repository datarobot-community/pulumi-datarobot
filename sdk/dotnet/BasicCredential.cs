// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Datarobot
{
    [DatarobotResourceType("datarobot:index/basicCredential:BasicCredential")]
    public partial class BasicCredential : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The description of the Basic Credential.
        /// </summary>
        [Output("description")]
        public Output<string> Description { get; private set; } = null!;

        /// <summary>
        /// The name of the Basic Credential.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// The password of the Basic Credential.
        /// </summary>
        [Output("password")]
        public Output<string> Password { get; private set; } = null!;

        /// <summary>
        /// The user of the Basic Credential.
        /// </summary>
        [Output("user")]
        public Output<string> User { get; private set; } = null!;


        /// <summary>
        /// Create a BasicCredential resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public BasicCredential(string name, BasicCredentialArgs args, CustomResourceOptions? options = null)
            : base("datarobot:index/basicCredential:BasicCredential", name, args ?? new BasicCredentialArgs(), MakeResourceOptions(options, ""))
        {
        }

        private BasicCredential(string name, Input<string> id, BasicCredentialState? state = null, CustomResourceOptions? options = null)
            : base("datarobot:index/basicCredential:BasicCredential", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                AdditionalSecretOutputs =
                {
                    "password",
                    "user",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing BasicCredential resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static BasicCredential Get(string name, Input<string> id, BasicCredentialState? state = null, CustomResourceOptions? options = null)
        {
            return new BasicCredential(name, id, state, options);
        }
    }

    public sealed class BasicCredentialArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The description of the Basic Credential.
        /// </summary>
        [Input("description", required: true)]
        public Input<string> Description { get; set; } = null!;

        /// <summary>
        /// The name of the Basic Credential.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("password", required: true)]
        private Input<string>? _password;

        /// <summary>
        /// The password of the Basic Credential.
        /// </summary>
        public Input<string>? Password
        {
            get => _password;
            set
            {
                var emptySecret = Output.CreateSecret(0);
                _password = Output.Tuple<Input<string>?, int>(value, emptySecret).Apply(t => t.Item1);
            }
        }

        [Input("user", required: true)]
        private Input<string>? _user;

        /// <summary>
        /// The user of the Basic Credential.
        /// </summary>
        public Input<string>? User
        {
            get => _user;
            set
            {
                var emptySecret = Output.CreateSecret(0);
                _user = Output.Tuple<Input<string>?, int>(value, emptySecret).Apply(t => t.Item1);
            }
        }

        public BasicCredentialArgs()
        {
        }
        public static new BasicCredentialArgs Empty => new BasicCredentialArgs();
    }

    public sealed class BasicCredentialState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The description of the Basic Credential.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// The name of the Basic Credential.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("password")]
        private Input<string>? _password;

        /// <summary>
        /// The password of the Basic Credential.
        /// </summary>
        public Input<string>? Password
        {
            get => _password;
            set
            {
                var emptySecret = Output.CreateSecret(0);
                _password = Output.Tuple<Input<string>?, int>(value, emptySecret).Apply(t => t.Item1);
            }
        }

        [Input("user")]
        private Input<string>? _user;

        /// <summary>
        /// The user of the Basic Credential.
        /// </summary>
        public Input<string>? User
        {
            get => _user;
            set
            {
                var emptySecret = Output.CreateSecret(0);
                _user = Output.Tuple<Input<string>?, int>(value, emptySecret).Apply(t => t.Item1);
            }
        }

        public BasicCredentialState()
        {
        }
        public static new BasicCredentialState Empty => new BasicCredentialState();
    }
}
