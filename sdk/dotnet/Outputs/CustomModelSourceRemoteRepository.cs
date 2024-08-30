// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Datarobot.Outputs
{

    [OutputType]
    public sealed class CustomModelSourceRemoteRepository
    {
        /// <summary>
        /// The ID of the source remote repository.
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// The reference of the source remote repository.
        /// </summary>
        public readonly string Ref;
        /// <summary>
        /// The list of source paths in the source remote repository.
        /// </summary>
        public readonly ImmutableArray<string> SourcePaths;

        [OutputConstructor]
        private CustomModelSourceRemoteRepository(
            string id,

            string @ref,

            ImmutableArray<string> sourcePaths)
        {
            Id = id;
            Ref = @ref;
            SourcePaths = sourcePaths;
        }
    }
}