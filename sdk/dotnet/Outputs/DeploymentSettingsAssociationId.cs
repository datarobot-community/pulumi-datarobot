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
    public sealed class DeploymentSettingsAssociationId
    {
        /// <summary>
        /// Whether to automatically generate an association ID.
        /// </summary>
        public readonly bool AutoGenerateId;
        /// <summary>
        /// The name of the feature to use as the association ID.
        /// </summary>
        public readonly string FeatureName;
        /// <summary>
        /// Whether the association ID is required in prediction requests.
        /// </summary>
        public readonly bool RequiredInPredictionRequests;

        [OutputConstructor]
        private DeploymentSettingsAssociationId(
            bool autoGenerateId,

            string featureName,

            bool requiredInPredictionRequests)
        {
            AutoGenerateId = autoGenerateId;
            FeatureName = featureName;
            RequiredInPredictionRequests = requiredInPredictionRequests;
        }
    }
}
