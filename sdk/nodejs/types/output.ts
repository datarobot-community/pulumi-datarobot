// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";

export interface ApplicationSourceRuntimeParameterValue {
    /**
     * The name of the runtime parameter.
     */
    key: string;
    /**
     * The type of the runtime parameter.
     */
    type: string;
    /**
     * The value of the runtime parameter (type conversion is handled internally).
     */
    value: string;
}

export interface BatchPredictionJobDefinitionCsvSettings {
    /**
     * Fields are delimited by this character. Use the string tab to denote TSV (TAB separated values). Must be either a one-character string or the string tab.
     */
    delimiter: string;
    /**
     * Encoding for the CSV files.
     */
    encoding: string;
    /**
     * Fields containing the delimiter must be quoted using this character.
     */
    quotechar: string;
}

export interface BatchPredictionJobDefinitionIntakeSettings {
    /**
     * The name of specified database catalog for JDBC type.
     */
    catalog?: string;
    /**
     * The ID of the credentials for S3 or JDBC data source.
     */
    credentialId?: string;
    /**
     * The ID of the external data store connected to the JDBC data source.
     */
    dataStoreId?: string;
    /**
     * The ID of the dataset to score for dataset type.
     */
    datasetId?: string;
    /**
     * Any non-default endpoint URL for S3 access.
     */
    endpointUrl?: string;
    /**
     * Changing the fetchSize can be used to balance throughput and memory usage for JDBC type.
     */
    fetchSize?: number;
    /**
     * String path to file of scoring data for localFile type.
     */
    file?: string;
    /**
     * A self-supplied SELECT statement of the data set you wish to predict for JDBC type.
     */
    query?: string;
    /**
     * The name of specified database schema for JDBC type.
     */
    schema?: string;
    /**
     * The name of specified database table for JDBC type.
     */
    table?: string;
    /**
     * Type of data source.
     */
    type: string;
    /**
     * The URL to score (e.g.: s3://bucket/key) for S3 type.
     */
    url?: string;
}

export interface BatchPredictionJobDefinitionOutputSettings {
    /**
     * The name of specified database catalog for JDBC type.
     */
    catalog?: string;
    /**
     * If no existing table is detected, attempt to create it before writing data for JDBC type.
     */
    createTableIfNotExists?: boolean;
    /**
     * The ID of the credentials for S3 or JDBC data source.
     */
    credentialId?: string;
    /**
     * The ID of the external data store connected to the JDBC data source.
     */
    dataStoreId?: string;
    /**
     * Any non-default endpoint URL for S3 access.
     */
    endpointUrl?: string;
    /**
     * Path to save the scored data as CSV for localFile type.
     */
    path?: string;
    /**
     * The name of specified database schema for JDBC type.
     */
    schema?: string;
    /**
     * The type of insertion statement to create for JDBC type.
     */
    statementType?: string;
    /**
     * The name of specified database table for JDBC type.
     */
    table?: string;
    /**
     * Type of output.
     */
    type: string;
    /**
     * A list of strings containing those column names to be updated for JDBC type.
     */
    updateColumns?: string[];
    /**
     * The URL for storing the results (e.g.: s3://bucket/key) for S3 type.
     */
    url?: string;
    /**
     * A list of strings containing those column names to be selected for JDBC type.
     */
    whereColumns?: string[];
}

export interface BatchPredictionJobDefinitionPredictionInstance {
    /**
     * By default, prediction requests will use the API key of the user that created the job. This allows you to make requests on behalf of other users.
     */
    apiKey?: string;
    /**
     * If running a job against a prediction instance in the Managed AI Cloud, you must provide the organization level DataRobot-Key.
     */
    datarobotKey?: string;
    /**
     * Hostname of the prediction instance.
     */
    hostName: string;
    /**
     * Set to false to run prediction requests from the batch prediction job without SSL. Defaults to true.
     */
    sslEnabled: boolean;
}

export interface BatchPredictionJobDefinitionSchedule {
    /**
     * Days of the month when the job will run.
     */
    dayOfMonths: string[];
    /**
     * Days of the week when the job will run.
     */
    dayOfWeeks: string[];
    /**
     * Hours of the day when the job will run.
     */
    hours: string[];
    /**
     * Minutes of the day when the job will run.
     */
    minutes: string[];
    /**
     * Months of the year when the job will run.
     */
    months: string[];
}

export interface BatchPredictionJobDefinitionTimeseriesSettings {
    /**
     * Forecast point for the dataset, used for the forecast predictions. May be passed if timeseries_settings.type=forecast.
     */
    forecastPoint?: string;
    /**
     * End date for historical predictions. May be passed if timeseries_settings.type=historical.
     */
    predictionsEndDate?: string;
    /**
     * Start date for historical predictions. May be passed if timeseries_settings.type=historical.
     */
    predictionsStartDate?: string;
    /**
     * If True, missing values in the known in advance features are allowed in the forecast window at the prediction time. Default is False.
     */
    relaxKnownInAdvanceFeaturesCheck: boolean;
    /**
     * Type of time-series prediction. Must be 'forecast' or 'historical'. Default is 'forecast'.
     */
    type?: string;
}

export interface CustomJobRuntimeParameterValue {
    /**
     * The name of the runtime parameter.
     */
    key: string;
    /**
     * The type of the runtime parameter.
     */
    type: string;
    /**
     * The value of the runtime parameter (type conversion is handled internally).
     */
    value: string;
}

export interface CustomMetricFromJobBatch {
    /**
     * Column name.
     */
    columnName?: string;
}

export interface CustomMetricFromJobParameterOverride {
    /**
     * The name of the runtime parameter.
     */
    key: string;
    /**
     * The type of the runtime parameter.
     */
    type: string;
    /**
     * The value of the runtime parameter (type conversion is handled internally).
     */
    value: string;
}

export interface CustomMetricFromJobSampleCount {
    /**
     * Column name.
     */
    columnName: string;
}

export interface CustomMetricFromJobSchedule {
    /**
     * Days of the month when the metric job will run.
     */
    dayOfMonths: string[];
    /**
     * Days of the week when the metric job will run.
     */
    dayOfWeeks: string[];
    /**
     * Hours of the day when the metric job will run.
     */
    hours: string[];
    /**
     * Minutes of the day when the metric job will run.
     */
    minutes: string[];
    /**
     * Months of the year when the metric job will run.
     */
    months: string[];
}

export interface CustomMetricFromJobTimestamp {
    /**
     * Column name.
     */
    columnName?: string;
    /**
     * Format.
     */
    timeFormat?: string;
}

export interface CustomMetricFromJobValue {
    /**
     * Column name.
     */
    columnName?: string;
}

export interface CustomMetricJobRuntimeParameterValue {
    /**
     * The name of the runtime parameter.
     */
    key: string;
    /**
     * The type of the runtime parameter.
     */
    type: string;
    /**
     * The value of the runtime parameter (type conversion is handled internally).
     */
    value: string;
}

export interface CustomModelGuardConfiguration {
    /**
     * The deployment ID of this guard.
     */
    deploymentId?: string;
    /**
     * The input column name of this guard.
     */
    inputColumnName?: string;
    /**
     * The intervention for the guard configuration.
     */
    intervention: outputs.CustomModelGuardConfigurationIntervention;
    /**
     * The LLM type for this guard.
     */
    llmType?: string;
    /**
     * The name of the guard configuration.
     */
    name: string;
    /**
     * Configuration info for NeMo guards.
     */
    nemoInfo?: outputs.CustomModelGuardConfigurationNemoInfo;
    /**
     * The OpenAI API base URL for this guard.
     */
    openaiApiBase?: string;
    /**
     * The ID of an OpenAI credential for this guard.
     */
    openaiCredential?: string;
    /**
     * The ID of an OpenAI deployment for this guard.
     */
    openaiDeploymentId?: string;
    /**
     * The output column name of this guard.
     */
    outputColumnName?: string;
    /**
     * The list of stages for the guard configuration.
     */
    stages: string[];
    /**
     * The template name of the guard configuration.
     */
    templateName: string;
}

export interface CustomModelGuardConfigurationIntervention {
    /**
     * The action of the guard intervention.
     */
    action: string;
    /**
     * The JSON-encoded condition of the guard intervention. e.g. `{"comparand": 0.5, "comparator": "lessThan"}`
     */
    condition: string;
    /**
     * The message of the guard intervention.
     */
    message: string;
}

export interface CustomModelGuardConfigurationNemoInfo {
    /**
     * The actions for the NeMo information.
     */
    actions?: string;
    /**
     * NeMo guardrails blocked terms list.
     */
    blockedTerms?: string;
    /**
     * NeMo guardrails prompts.
     */
    llmPrompts?: string;
    /**
     * Overall NeMo configuration YAML.
     */
    mainConfig?: string;
    /**
     * NeMo guardrails configuration Colang.
     */
    railsConfig?: string;
}

export interface CustomModelOverallModerationConfiguration {
    /**
     * The timeout action of the overall moderation configuration.
     */
    timeoutAction: string;
    /**
     * The timeout in seconds of the overall moderation configuration.
     */
    timeoutSec: number;
}

export interface CustomModelRuntimeParameterValue {
    /**
     * The name of the runtime parameter.
     */
    key: string;
    /**
     * The type of the runtime parameter.
     */
    type: string;
    /**
     * The value of the runtime parameter (type conversion is handled internally).
     */
    value: string;
}

export interface CustomModelSourceRemoteRepository {
    /**
     * The ID of the source remote repository.
     */
    id: string;
    /**
     * The reference of the source remote repository.
     */
    ref: string;
    /**
     * The list of source paths in the source remote repository.
     */
    sourcePaths: string[];
}

export interface DatasourceParams {
    /**
     * The Catalog name in the database if supported.
     */
    catalog?: string;
    /**
     * The id of the DataStore.
     */
    dataStoreId: string;
    /**
     * A user specified fetch size in the range [1, 20000]. By default a fetchSize will be assigned to balance throughput and memory usage.
     */
    fetchSize?: number;
    /**
     * The name of the partition column.
     */
    partitionColumn?: string;
    /**
     * The user-specified path for BLOB storage.
     */
    path?: string;
    /**
     * The user specified SQL query.
     */
    query?: string;
    /**
     * The name of the schema associated with the table.
     */
    schema?: string;
    /**
     * The name of specified database table.
     */
    table?: string;
}

export interface DeploymentAssociationIdSettings {
    /**
     * Whether to auto generate ID.
     */
    autoGenerateId?: boolean;
    /**
     * Name of the columns to be used as association ID, currently only support a list of one string.
     */
    columnNames?: string[];
    /**
     * Whether the association ID column is required in prediction requests.
     */
    requiredInPredictionRequests?: boolean;
}

export interface DeploymentBiasAndFairnessSettings {
    /**
     * A set of fairness metrics to use for calculating fairness.
     */
    fairnessMetricSet: string;
    /**
     * Threshold value of the fairness metric. Cannot be less than 0 or greater than 1.
     */
    fairnessThreshold: number;
    /**
     * A target value that should be treated as a positive outcome for the prediction.
     */
    preferableTargetValue: boolean;
    /**
     * A list of features to mark as protected.
     */
    protectedFeatures: string[];
}

export interface DeploymentChallengerModelsSettings {
    /**
     * Is 'True' if challenger models is enabled for this deployment.
     */
    enabled: boolean;
}

export interface DeploymentChallengerReplaySettings {
    /**
     * If challenger replay is enabled.
     */
    enabled: boolean;
}

export interface DeploymentDriftTrackingSettings {
    /**
     * If feature drift tracking is to be turned on.
     */
    featureDriftEnabled?: boolean;
    /**
     * If target drift tracking is to be turned on.
     */
    targetDriftEnabled?: boolean;
}

export interface DeploymentHealthSettings {
    /**
     * The accuracy health settings for this Deployment.
     */
    accuracy?: outputs.DeploymentHealthSettingsAccuracy;
    /**
     * The actuals timeliness health settings for this Deployment.
     */
    actualsTimeliness?: outputs.DeploymentHealthSettingsActualsTimeliness;
    /**
     * The custom metrics health settings for this Deployment.
     */
    customMetrics?: outputs.DeploymentHealthSettingsCustomMetrics;
    /**
     * The data drift health settings for this Deployment.
     */
    dataDrift?: outputs.DeploymentHealthSettingsDataDrift;
    /**
     * The fairness health settings for this Deployment.
     */
    fairness?: outputs.DeploymentHealthSettingsFairness;
    /**
     * The predictions timeliness health settings for this Deployment.
     */
    predictionsTimeliness?: outputs.DeploymentHealthSettingsPredictionsTimeliness;
    /**
     * The service health settings for this Deployment.
     */
    service?: outputs.DeploymentHealthSettingsService;
}

export interface DeploymentHealthSettingsAccuracy {
    /**
     * The batch count for the accuracy health settings.
     */
    batchCount?: number;
    /**
     * The failing threshold for the accuracy health settings.
     */
    failingThreshold?: number;
    /**
     * The measurement for the accuracy health settings.
     */
    measurement?: string;
    /**
     * The metric for the accuracy health settings.
     */
    metric?: string;
    /**
     * The warning threshold for the accuracy health settings.
     */
    warningThreshold?: number;
}

export interface DeploymentHealthSettingsActualsTimeliness {
    /**
     * If acutals timeliness is enabled for this Deployment.
     */
    enabled: boolean;
    /**
     * The expected frequency for the actuals timeliness health settings.
     */
    expectedFrequency?: string;
}

export interface DeploymentHealthSettingsCustomMetrics {
    /**
     * The failing conditions for the custom metrics health settings.
     */
    failingConditions?: outputs.DeploymentHealthSettingsCustomMetricsFailingCondition[];
    /**
     * The warning conditions for the custom metrics health settings.
     */
    warningConditions?: outputs.DeploymentHealthSettingsCustomMetricsWarningCondition[];
}

export interface DeploymentHealthSettingsCustomMetricsFailingCondition {
    /**
     * The compare operator for the failing condition of the custom metrics health settings.
     */
    compareOperator: string;
    /**
     * The metric ID for the failing condition of the custom metrics health settings.
     */
    metricId: string;
    /**
     * The threshold for the failing condition of the custom metrics health settings.
     */
    threshold: number;
}

export interface DeploymentHealthSettingsCustomMetricsWarningCondition {
    /**
     * The compare operator for the warning condition of the custom metrics health settings.
     */
    compareOperator: string;
    /**
     * The metric ID for the warning condition of the custom metrics health settings.
     */
    metricId: string;
    /**
     * The threshold for the warning condition of the custom metrics health settings.
     */
    threshold: number;
}

export interface DeploymentHealthSettingsDataDrift {
    /**
     * The batch count for the data drift health settings.
     */
    batchCount?: number;
    /**
     * The drift threshold for the data drift health settings.
     */
    driftThreshold?: number;
    /**
     * The exclude features for the data drift health settings.
     */
    excludeFeatures?: string[];
    /**
     * The high importance failing count for the data drift health settings.
     */
    highImportanceFailingCount?: number;
    /**
     * The high importance warning count for the data drift health settings.
     */
    highImportanceWarningCount?: number;
    /**
     * The importance threshold for the data drift health settings.
     */
    importanceThreshold?: number;
    /**
     * The low importance failing count for the data drift health settings.
     */
    lowImportanceFailingCount?: number;
    /**
     * The low importance warning count for the data drift health settings.
     */
    lowImportanceWarningCount?: number;
    /**
     * The starred features for the data drift health settings.
     */
    starredFeatures?: string[];
    /**
     * The time interval for the data drift health settings.
     */
    timeInterval?: string;
}

export interface DeploymentHealthSettingsFairness {
    /**
     * The protected class failing count for the fairness health settings.
     */
    protectedClassFailingCount?: number;
    /**
     * The protected class warning count for the fairness health settings.
     */
    protectedClassWarningCount?: number;
}

export interface DeploymentHealthSettingsPredictionsTimeliness {
    /**
     * If predictions timeliness is enabled for this Deployment.
     */
    enabled: boolean;
    /**
     * The expected frequency for the predictions timeliness health settings.
     */
    expectedFrequency?: string;
}

export interface DeploymentHealthSettingsService {
    /**
     * The batch count for the service health settings.
     */
    batchCount: number;
}

export interface DeploymentPredictionIntervalsSettings {
    /**
     * Whether prediction intervals are enabled for this deployment.
     */
    enabled: boolean;
    /**
     * List of enabled prediction intervals’ sizes for this deployment.
     */
    percentiles?: number[];
}

export interface DeploymentPredictionWarningSettings {
    /**
     * The custom boundaries for prediction warnings.
     */
    customBoundaries?: outputs.DeploymentPredictionWarningSettingsCustomBoundaries;
    /**
     * If target prediction warning is enabled for this Deployment.
     */
    enabled: boolean;
}

export interface DeploymentPredictionWarningSettingsCustomBoundaries {
    /**
     * All predictions less than provided value will be considered anomalous.
     */
    lowerBoundary?: number;
    /**
     * All predictions greater than provided value will be considered anomalous.
     */
    upperBoundary?: number;
}

export interface DeploymentPredictionsByForecastDateSettings {
    /**
     * The column name in prediction datasets to be used as forecast date.
     */
    columnName?: string;
    /**
     * The datetime format of the forecast date column in prediction datasets.
     */
    datetimeFormat?: string;
    /**
     * Is ’True’ if predictions by forecast date is enabled for this deployment.
     */
    enabled: boolean;
}

export interface DeploymentPredictionsDataCollectionSettings {
    /**
     * If predictions data collections is enabled for this Deployment.
     */
    enabled: boolean;
}

export interface DeploymentPredictionsSettings {
    /**
     * The maximum number of computes to use for predictions.
     */
    maxComputes: number;
    /**
     * The minimum number of computes to use for predictions.
     */
    minComputes: number;
}

export interface DeploymentRetrainingPolicyAutopilotOptions {
    /**
     * Blend best models during Autopilot run. This option is not supported in SHAP-only mode.
     */
    blendBestModels: boolean;
    /**
     * The autopiltot mode.
     */
    mode: string;
    /**
     * Run Autopilot on Leakage Removed feature list (if exists).
     */
    runLeakageRemovedFeatureList: boolean;
    /**
     * Keep only models that can be converted to scorable java code during Autopilot run.
     */
    scoringCodeOnly: boolean;
    /**
     * Include only models with SHAP value support.
     */
    shapOnlyMode: boolean;
}

export interface DeploymentRetrainingPolicyProjectOptions {
    /**
     * The partitioning method for projects used to build new models.
     */
    cvMethod: string;
    /**
     * The percentage of dataset to assign to holdout set in projects used to build new models.
     */
    holdoutPct: number;
    /**
     * The model selection metric in projects used to build new models.
     */
    metric?: string;
    /**
     * The number of cross validation folds to use for projects used to build new models.
     */
    reps: number;
    /**
     * The percentage of dataset to assign to validation set in projects used to build new models.
     */
    validationPct?: number;
    /**
     * The validation type for projects used to build new models.
     */
    validationType: string;
}

export interface DeploymentRetrainingPolicyTimeSeriesOptions {
    /**
     * The ID of the calendar to be used in this project.
     */
    calendarId?: string;
    /**
     * For time series projects only. Used to specify which differencing method to apply if the data is stationary. For classification problems simple and seasonal are not allowed. Parameter periodicities must be specified if seasonal is chosen. Defaults to auto.
     */
    differencingMethod?: string;
    /**
     * Discount factor (alpha) used for exponentially weighted moving features.
     */
    exponentiallyWeightedMovingAlpha?: number;
    /**
     * A list of periodicities for time series projects only. For classification problems periodicities are not allowed. If this is provided, parameter 'differencing*method' will default to 'seasonal' if not provided or 'auto'.
     */
    periodicities?: outputs.DeploymentRetrainingPolicyTimeSeriesOptionsPeriodicity[];
    /**
     * For time series projects only. Used to specify whether to treat data as exponential trend and apply transformations like log-transform. For classification problems always is not allowed. Defaults to auto.
     */
    treatAsExponential?: string;
}

export interface DeploymentRetrainingPolicyTimeSeriesOptionsPeriodicity {
    /**
     * The number of time steps.
     */
    timeSteps: number;
    /**
     * The time unit or ROW if windowsBasisUnit is ROW
     */
    timeUnit: string;
}

export interface DeploymentRetrainingPolicyTrigger {
    /**
     * Custom job ID for the retraining policy.
     */
    customJobId?: string;
    /**
     * Minimal interval between policy runs in ISO 8601 duration string.
     */
    minIntervalBetweenRuns?: string;
    /**
     * Schedule for the retraining policy.
     */
    schedule?: outputs.DeploymentRetrainingPolicyTriggerSchedule;
    /**
     * Identifies when trigger type is based on deployment a health status, whether the policy will run when health status declines to failing.
     */
    statusDeclinesToFailing: boolean;
    /**
     * Identifies when trigger type is based on deployment a health status, whether the policy will run when health status declines to warning.
     */
    statusDeclinesToWarning: boolean;
    /**
     * Identifies when trigger type is based on deployment a health status, whether the policy will run when health status still in decline.
     */
    statusStillInDecline: boolean;
    /**
     * Type of retraining policy trigger.
     */
    type?: string;
}

export interface DeploymentRetrainingPolicyTriggerSchedule {
    /**
     * Days of the month when the job will run.
     */
    dayOfMonths: string[];
    /**
     * Days of the week when the job will run.
     */
    dayOfWeeks: string[];
    /**
     * Hours of the day when the job will run.
     */
    hours: string[];
    /**
     * Minutes of the day when the job will run.
     */
    minutes: string[];
    /**
     * Months of the year when the job will run.
     */
    months: string[];
}

export interface DeploymentSegmentAnalysisSettings {
    /**
     * A list of strings that gives the segment attributes selected for tracking.
     */
    attributes?: string[];
    /**
     * Set to 'True' if segment analysis is enabled for this deployment.
     */
    enabled: boolean;
}

export interface LlmBlueprintLlmSettings {
    /**
     * The maximum number of tokens allowed in the completion. The combined count of this value and prompt tokens must be below the model's maximum context size, where prompt token count is comprised of system prompt, user prompt, recent chat history, and vector database citations.
     */
    maxCompletionLength?: number;
    /**
     * Guides the style of the LLM response. It is a 'universal' prompt, prepended to all individual prompts.
     */
    systemPrompt?: string;
    /**
     * Controls the randomness of model output, where higher values return more diverse output and lower values return more deterministic results.
     */
    temperature?: number;
    /**
     * Threshold that controls the selection of words included in the response, based on a cumulative probability cutoff for token selection. Higher numbers return more diverse options for outputs.
     */
    topP?: number;
}

export interface LlmBlueprintVectorDatabaseSettings {
    /**
     * The maximum number of documents to retrieve from the Vector Database.
     */
    maxDocumentsRetrievedPerPrompt?: number;
    /**
     * The maximum number of tokens to retrieve from the Vector Database.
     */
    maxTokens?: number;
}

export interface VectorDatabaseChunkingParameters {
    /**
     * The percentage of overlap between chunks.
     */
    chunkOverlapPercentage: number;
    /**
     * The size of the chunks.
     */
    chunkSize: number;
    /**
     * The method used to chunk the data.
     */
    chunkingMethod: string;
    /**
     * The id of the Embedding Model.
     */
    embeddingModel: string;
    /**
     * Whether the separator is a regex.
     */
    isSeparatorRegex: boolean;
    /**
     * The separators used to split the data.
     */
    separators: string[];
}

