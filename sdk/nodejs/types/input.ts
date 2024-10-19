// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";

export interface ApplicationSourceResourceSettings {
    /**
     * The replicas for the Application Source.
     */
    replicas?: pulumi.Input<number>;
}

export interface ApplicationSourceRuntimeParameterValue {
    /**
     * The name of the runtime parameter.
     */
    key: pulumi.Input<string>;
    /**
     * The type of the runtime parameter.
     */
    type: pulumi.Input<string>;
    /**
     * The value of the runtime parameter (type conversion is handled internally).
     */
    value: pulumi.Input<string>;
}

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
     * The LLM type for this guard.
     */
    llmType?: pulumi.Input<string>;
    /**
     * The name of the guard configuration.
     */
    name: pulumi.Input<string>;
    /**
     * The OpenAI API base URL for this guard.
     */
    openaiApiBase?: pulumi.Input<string>;
    /**
     * The ID of an OpenAI credential for this guard.
     */
    openaiCredential?: pulumi.Input<string>;
    /**
     * The ID of an OpenAI deployment for this guard.
     */
    openaiDeploymentId?: pulumi.Input<string>;
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
     * The JSON-encoded condition of the guard intervention. e.g. `{"comparand": 0.5, "comparator": "lessThan"}`
     */
    condition: pulumi.Input<string>;
    /**
     * The message of the guard intervention.
     */
    message?: pulumi.Input<string>;
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

export interface CustomModelRuntimeParameterValue {
    /**
     * The name of the runtime parameter.
     */
    key: pulumi.Input<string>;
    /**
     * The type of the runtime parameter.
     */
    type: pulumi.Input<string>;
    /**
     * The value of the runtime parameter (type conversion is handled internally).
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

export interface DeploymentAssociationIdSettings {
    /**
     * Whether to auto generate ID.
     */
    autoGenerateId?: pulumi.Input<boolean>;
    /**
     * Name of the columns to be used as association ID, currently only support a list of one string.
     */
    columnNames?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Whether the association ID column is required in prediction requests.
     */
    requiredInPredictionRequests?: pulumi.Input<boolean>;
}

export interface DeploymentBiasAndFairnessSettings {
    /**
     * A set of fairness metrics to use for calculating fairness.
     */
    fairnessMetricSet: pulumi.Input<string>;
    /**
     * Threshold value of the fairness metric. Cannot be less than 0 or greater than 1.
     */
    fairnessThreshold: pulumi.Input<number>;
    /**
     * A target value that should be treated as a positive outcome for the prediction.
     */
    preferableTargetValue: pulumi.Input<boolean>;
    /**
     * A list of features to mark as protected.
     */
    protectedFeatures: pulumi.Input<pulumi.Input<string>[]>;
}

export interface DeploymentChallengerModelsSettings {
    /**
     * Is 'True' if challenger models is enabled for this deployment.
     */
    enabled: pulumi.Input<boolean>;
}

export interface DeploymentChallengerReplaySettings {
    /**
     * If challenger replay is enabled.
     */
    enabled: pulumi.Input<boolean>;
}

export interface DeploymentDriftTrackingSettings {
    /**
     * If feature drift tracking is to be turned on.
     */
    featureDriftEnabled?: pulumi.Input<boolean>;
    /**
     * If target drift tracking is to be turned on.
     */
    targetDriftEnabled?: pulumi.Input<boolean>;
}

export interface DeploymentHealthSettings {
    /**
     * The accuracy health settings for this Deployment.
     */
    accuracy?: pulumi.Input<inputs.DeploymentHealthSettingsAccuracy>;
    /**
     * The actuals timeliness health settings for this Deployment.
     */
    actualsTimeliness?: pulumi.Input<inputs.DeploymentHealthSettingsActualsTimeliness>;
    /**
     * The custom metrics health settings for this Deployment.
     */
    customMetrics?: pulumi.Input<inputs.DeploymentHealthSettingsCustomMetrics>;
    /**
     * The data drift health settings for this Deployment.
     */
    dataDrift?: pulumi.Input<inputs.DeploymentHealthSettingsDataDrift>;
    /**
     * The fairness health settings for this Deployment.
     */
    fairness?: pulumi.Input<inputs.DeploymentHealthSettingsFairness>;
    /**
     * The predictions timeliness health settings for this Deployment.
     */
    predictionsTimeliness?: pulumi.Input<inputs.DeploymentHealthSettingsPredictionsTimeliness>;
    /**
     * The service health settings for this Deployment.
     */
    service?: pulumi.Input<inputs.DeploymentHealthSettingsService>;
}

export interface DeploymentHealthSettingsAccuracy {
    /**
     * The batch count for the accuracy health settings.
     */
    batchCount?: pulumi.Input<number>;
    /**
     * The failing threshold for the accuracy health settings.
     */
    failingThreshold?: pulumi.Input<number>;
    /**
     * The measurement for the accuracy health settings.
     */
    measurement?: pulumi.Input<string>;
    /**
     * The metric for the accuracy health settings.
     */
    metric?: pulumi.Input<string>;
    /**
     * The warning threshold for the accuracy health settings.
     */
    warningThreshold?: pulumi.Input<number>;
}

export interface DeploymentHealthSettingsActualsTimeliness {
    /**
     * If acutals timeliness is enabled for this Deployment.
     */
    enabled: pulumi.Input<boolean>;
    /**
     * The expected frequency for the actuals timeliness health settings.
     */
    expectedFrequency?: pulumi.Input<string>;
}

export interface DeploymentHealthSettingsCustomMetrics {
    /**
     * The failing conditions for the custom metrics health settings.
     */
    failingConditions?: pulumi.Input<pulumi.Input<inputs.DeploymentHealthSettingsCustomMetricsFailingCondition>[]>;
    /**
     * The warning conditions for the custom metrics health settings.
     */
    warningConditions?: pulumi.Input<pulumi.Input<inputs.DeploymentHealthSettingsCustomMetricsWarningCondition>[]>;
}

export interface DeploymentHealthSettingsCustomMetricsFailingCondition {
    /**
     * The compare operator for the failing condition of the custom metrics health settings.
     */
    compareOperator: pulumi.Input<string>;
    /**
     * The metric ID for the failing condition of the custom metrics health settings.
     */
    metricId: pulumi.Input<string>;
    /**
     * The threshold for the failing condition of the custom metrics health settings.
     */
    threshold: pulumi.Input<number>;
}

export interface DeploymentHealthSettingsCustomMetricsWarningCondition {
    /**
     * The compare operator for the warning condition of the custom metrics health settings.
     */
    compareOperator: pulumi.Input<string>;
    /**
     * The metric ID for the warning condition of the custom metrics health settings.
     */
    metricId: pulumi.Input<string>;
    /**
     * The threshold for the warning condition of the custom metrics health settings.
     */
    threshold: pulumi.Input<number>;
}

export interface DeploymentHealthSettingsDataDrift {
    /**
     * The batch count for the data drift health settings.
     */
    batchCount?: pulumi.Input<number>;
    /**
     * The drift threshold for the data drift health settings.
     */
    driftThreshold?: pulumi.Input<number>;
    /**
     * The exclude features for the data drift health settings.
     */
    excludeFeatures?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The high importance failing count for the data drift health settings.
     */
    highImportanceFailingCount?: pulumi.Input<number>;
    /**
     * The high importance warning count for the data drift health settings.
     */
    highImportanceWarningCount?: pulumi.Input<number>;
    /**
     * The importance threshold for the data drift health settings.
     */
    importanceThreshold?: pulumi.Input<number>;
    /**
     * The low importance failing count for the data drift health settings.
     */
    lowImportanceFailingCount?: pulumi.Input<number>;
    /**
     * The low importance warning count for the data drift health settings.
     */
    lowImportanceWarningCount?: pulumi.Input<number>;
    /**
     * The starred features for the data drift health settings.
     */
    starredFeatures?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The time interval for the data drift health settings.
     */
    timeInterval?: pulumi.Input<string>;
}

export interface DeploymentHealthSettingsFairness {
    /**
     * The protected class failing count for the fairness health settings.
     */
    protectedClassFailingCount?: pulumi.Input<number>;
    /**
     * The protected class warning count for the fairness health settings.
     */
    protectedClassWarningCount?: pulumi.Input<number>;
}

export interface DeploymentHealthSettingsPredictionsTimeliness {
    /**
     * If predictions timeliness is enabled for this Deployment.
     */
    enabled: pulumi.Input<boolean>;
    /**
     * The expected frequency for the predictions timeliness health settings.
     */
    expectedFrequency?: pulumi.Input<string>;
}

export interface DeploymentHealthSettingsService {
    /**
     * The batch count for the service health settings.
     */
    batchCount: pulumi.Input<number>;
}

export interface DeploymentPredictionIntervalsSettings {
    /**
     * Whether prediction intervals are enabled for this deployment.
     */
    enabled: pulumi.Input<boolean>;
    /**
     * List of enabled prediction intervals’ sizes for this deployment.
     */
    percentiles?: pulumi.Input<pulumi.Input<number>[]>;
}

export interface DeploymentPredictionWarningSettings {
    /**
     * The custom boundaries for prediction warnings.
     */
    customBoundaries?: pulumi.Input<inputs.DeploymentPredictionWarningSettingsCustomBoundaries>;
    /**
     * If target prediction warning is enabled for this Deployment.
     */
    enabled: pulumi.Input<boolean>;
}

export interface DeploymentPredictionWarningSettingsCustomBoundaries {
    /**
     * All predictions less than provided value will be considered anomalous.
     */
    lowerBoundary?: pulumi.Input<number>;
    /**
     * All predictions greater than provided value will be considered anomalous.
     */
    upperBoundary?: pulumi.Input<number>;
}

export interface DeploymentPredictionsByForecastDateSettings {
    /**
     * The column name in prediction datasets to be used as forecast date.
     */
    columnName?: pulumi.Input<string>;
    /**
     * The datetime format of the forecast date column in prediction datasets.
     */
    datetimeFormat?: pulumi.Input<string>;
    /**
     * Is ’True’ if predictions by forecast date is enabled for this deployment.
     */
    enabled: pulumi.Input<boolean>;
}

export interface DeploymentPredictionsDataCollectionSettings {
    /**
     * If predictions data collections is enabled for this Deployment.
     */
    enabled: pulumi.Input<boolean>;
}

export interface DeploymentPredictionsSettings {
    /**
     * The maximum number of computes to use for predictions.
     */
    maxComputes: pulumi.Input<number>;
    /**
     * The minimum number of computes to use for predictions.
     */
    minComputes: pulumi.Input<number>;
}

export interface DeploymentSegmentAnalysisSettings {
    /**
     * A list of strings that gives the segment attributes selected for tracking.
     */
    attributes?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Set to 'True' if segment analysis is enabled for this deployment.
     */
    enabled: pulumi.Input<boolean>;
}

export interface LlmBlueprintLlmSettings {
    /**
     * The maximum number of tokens allowed in the completion. The combined count of this value and prompt tokens must be below the model's maximum context size, where prompt token count is comprised of system prompt, user prompt, recent chat history, and vector database citations.
     */
    maxCompletionLength?: pulumi.Input<number>;
    /**
     * Guides the style of the LLM response. It is a 'universal' prompt, prepended to all individual prompts.
     */
    systemPrompt?: pulumi.Input<string>;
    /**
     * Controls the randomness of model output, where higher values return more diverse output and lower values return more deterministic results.
     */
    temperature?: pulumi.Input<number>;
    /**
     * Threshold that controls the selection of words included in the response, based on a cumulative probability cutoff for token selection. Higher numbers return more diverse options for outputs.
     */
    topP?: pulumi.Input<number>;
}

export interface LlmBlueprintVectorDatabaseSettings {
    /**
     * The maximum number of documents to retrieve from the Vector Database.
     */
    maxDocumentsRetrievedPerPrompt?: pulumi.Input<number>;
    /**
     * The maximum number of tokens to retrieve from the Vector Database.
     */
    maxTokens?: pulumi.Input<number>;
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
