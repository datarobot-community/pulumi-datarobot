// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Datarobot.Inputs
{

    public sealed class VectorDatabaseChunkingParametersGetArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The percentage of overlap between chunks.
        /// </summary>
        [Input("chunkOverlapPercentage")]
        public Input<double>? ChunkOverlapPercentage { get; set; }

        /// <summary>
        /// The size of the chunks.
        /// </summary>
        [Input("chunkSize")]
        public Input<double>? ChunkSize { get; set; }

        /// <summary>
        /// The method used to chunk the data.
        /// </summary>
        [Input("chunkingMethod")]
        public Input<string>? ChunkingMethod { get; set; }

        /// <summary>
        /// The id of the Embedding Model.
        /// </summary>
        [Input("embeddingModel")]
        public Input<string>? EmbeddingModel { get; set; }

        /// <summary>
        /// Whether the separator is a regex.
        /// </summary>
        [Input("isSeparatorRegex")]
        public Input<bool>? IsSeparatorRegex { get; set; }

        [Input("separators")]
        private InputList<string>? _separators;

        /// <summary>
        /// The separators used to split the data.
        /// </summary>
        public InputList<string> Separators
        {
            get => _separators ?? (_separators = new InputList<string>());
            set => _separators = value;
        }

        public VectorDatabaseChunkingParametersGetArgs()
        {
        }
        public static new VectorDatabaseChunkingParametersGetArgs Empty => new VectorDatabaseChunkingParametersGetArgs();
    }
}
