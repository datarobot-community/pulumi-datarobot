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

    public sealed class CustomModelSourceRemoteRepositoryGetArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The ID of the source remote repository.
        /// </summary>
        [Input("id", required: true)]
        public Input<string> Id { get; set; } = null!;

        /// <summary>
        /// The reference of the source remote repository.
        /// </summary>
        [Input("ref", required: true)]
        public Input<string> Ref { get; set; } = null!;

        [Input("sourcePaths", required: true)]
        private InputList<string>? _sourcePaths;

        /// <summary>
        /// The list of source paths in the source remote repository.
        /// </summary>
        public InputList<string> SourcePaths
        {
            get => _sourcePaths ?? (_sourcePaths = new InputList<string>());
            set => _sourcePaths = value;
        }

        public CustomModelSourceRemoteRepositoryGetArgs()
        {
        }
        public static new CustomModelSourceRemoteRepositoryGetArgs Empty => new CustomModelSourceRemoteRepositoryGetArgs();
    }
}
