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
    public sealed class DeploymentHealthSettingsFairness
    {
        /// <summary>
        /// The protected class failing count for the fairness health settings.
        /// </summary>
        public readonly int? ProtectedClassFailingCount;
        /// <summary>
        /// The protected class warning count for the fairness health settings.
        /// </summary>
        public readonly int? ProtectedClassWarningCount;

        [OutputConstructor]
        private DeploymentHealthSettingsFairness(
            int? protectedClassFailingCount,

            int? protectedClassWarningCount)
        {
            ProtectedClassFailingCount = protectedClassFailingCount;
            ProtectedClassWarningCount = protectedClassWarningCount;
        }
    }
}