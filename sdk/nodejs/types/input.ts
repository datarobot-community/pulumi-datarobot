// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";

export interface CustomModelGuardConfiguration {
    /**
     * The deployment ID of this guard.
     */
    deploymentId?: pulumi.Input<string>;
    /**
     * The input column name of this guard.
     */
    inputColumnName?: pulumi.Input<string>;
    /**
     * The intervention for the guard configuration.
     */
    intervention: pulumi.Input<inputs.CustomModelGuardConfigurationIntervention>;
    /**
     * The name of the guard configuration.
     */
    name: pulumi.Input<string>;
    /**
     * The output column name of this guard.
     */
    outputColumnName?: pulumi.Input<string>;
    /**
     * The list of stages for the guard configuration.
     */
    stages: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The template name of the guard configuration.
     */
    templateName: pulumi.Input<string>;
}

export interface CustomModelGuardConfigurationIntervention {
    /**
     * The action of the guard intervention.
     */
    action: pulumi.Input<string>;
    /**
     * The list of conditions for the guard intervention.
     */
    condition: pulumi.Input<inputs.CustomModelGuardConfigurationInterventionCondition>;
    /**
     * The message of the guard intervention.
     */
    message?: pulumi.Input<string>;
}

export interface CustomModelGuardConfigurationInterventionCondition {
    /**
     * The comparand of the guard condition.
     */
    comparand: pulumi.Input<number>;
    /**
     * The comparator of the guard condition.
     */
    comparator: pulumi.Input<string>;
}

export interface CustomModelOverallModerationConfiguration {
    /**
     * The timeout action of the overall moderation configuration.
     */
    timeoutAction?: pulumi.Input<string>;
    /**
     * The timeout in seconds of the overall moderation configuration.
     */
    timeoutSec?: pulumi.Input<number>;
}

export interface CustomModelRuntimeParameter {
    /**
     * The name of the runtime parameter.
     */
    key: pulumi.Input<string>;
    /**
     * The type of the runtime parameter.
     */
    type: pulumi.Input<string>;
    /**
     * The value of the runtime parameter.
     */
    value: pulumi.Input<string>;
}

export interface CustomModelSourceRemoteRepository {
    /**
     * The ID of the source remote repository.
     */
    id: pulumi.Input<string>;
    /**
     * The reference of the source remote repository.
     */
    ref: pulumi.Input<string>;
    /**
     * The list of source paths in the source remote repository.
     */
    sourcePaths: pulumi.Input<pulumi.Input<string>[]>;
}

export interface DeploymentSettings {
    /**
     * Used to associate predictions back to your actual data.
     */
    associationId?: pulumi.Input<inputs.DeploymentSettingsAssociationId>;
    /**
     * Used to compare the performance of the deployed model with the challenger models.
     */
    challengerAnalysis?: pulumi.Input<boolean>;
    /**
     * Used to score predictions made by the challenger models and compare performance with the deployed model.
     */
    predictionRowStorage?: pulumi.Input<boolean>;
    /**
     * Settings for the predictions.
     */
    predictionsSettings?: pulumi.Input<inputs.DeploymentSettingsPredictionsSettings>;
}

export interface DeploymentSettingsAssociationId {
    /**
     * Whether to automatically generate an association ID.
     */
    autoGenerateId: pulumi.Input<boolean>;
    /**
     * The name of the feature to use as the association ID.
     */
    featureName: pulumi.Input<string>;
}

export interface DeploymentSettingsPredictionsSettings {
    /**
     * The maximum number of computes to use for predictions.
     */
    maxComputes: pulumi.Input<number>;
    /**
     * The minimum number of computes to use for predictions.
     */
    minComputes: pulumi.Input<number>;
    /**
     * Whether to use real-time predictions.
     */
    realTime: pulumi.Input<boolean>;
}

export interface VectorDatabaseChunkingParameters {
    /**
     * The percentage of overlap between chunks.
     */
    chunkOverlapPercentage?: pulumi.Input<number>;
    /**
     * The size of the chunks.
     */
    chunkSize?: pulumi.Input<number>;
    /**
     * The method used to chunk the data.
     */
    chunkingMethod?: pulumi.Input<string>;
    /**
     * The id of the Embedding Model.
     */
    embeddingModel?: pulumi.Input<string>;
    /**
     * Whether the separator is a regex.
     */
    isSeparatorRegex?: pulumi.Input<boolean>;
    /**
     * The separators used to split the data.
     */
    separators?: pulumi.Input<pulumi.Input<string>[]>;
}
