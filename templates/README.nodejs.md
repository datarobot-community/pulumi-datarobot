# DataRobot Pulumi Provider for TypeScript/JavaScript

The DataRobot Resource Provider lets you manage [DataRobot](https://www.datarobot.com/) resources with Pulumi Infrastructure as Code.

## Installation

Install the package using npm or yarn:

```bash
# Using npm
npm install {{PACKAGE_NAME}}

# Using yarn
yarn add {{PACKAGE_NAME}}
```

## Configuration

Configure the provider using environment variables or Pulumi config:

```bash
# Environment variables
export DATAROBOT_API_TOKEN=your_api_token
export DATAROBOT_ENDPOINT=https://your.datarobot.instance/api/v2

# OR using Pulumi config
pulumi config set datarobot:apikey --secret your_api_token
pulumi config set datarobot:endpoint https://your.datarobot.instance/api/v2
```

## Quick Start

### TypeScript

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as datarobot from "{{PACKAGE_NAME}}";

// Create a DataRobot use case
const useCase = new datarobot.UseCase("my-use-case", {
    name: "ML Project Use Case",
    description: "Created with Pulumi",
});

// Create a project from a dataset
const project = new datarobot.Project("my-project", {
    name: "Customer Churn Prediction",
    datasetUrl: "https://s3.amazonaws.com/datarobot-datasets/churn.csv",
    useCaseId: useCase.id,
});

// Create a deployment
const deployment = new datarobot.Deployment("my-deployment", {
    projectId: project.id,
    modelId: project.recommendedModelId,
    environmentId: "your-prediction-environment-id",
});

// Export important values
export const useCaseId = useCase.id;
export const projectId = project.id;
export const deploymentId = deployment.id;
```

### JavaScript

```javascript
const pulumi = require("@pulumi/pulumi");
const datarobot = require("{{PACKAGE_NAME}}");

// Create a DataRobot use case
const useCase = new datarobot.UseCase("my-use-case", {
    name: "ML Project Use Case",
    description: "Created with Pulumi",
});

// Create a project from a dataset
const project = new datarobot.Project("my-project", {
    name: "Customer Churn Prediction",
    datasetUrl: "https://s3.amazonaws.com/datarobot-datasets/churn.csv",
    useCaseId: useCase.id,
});

// Create a deployment
const deployment = new datarobot.Deployment("my-deployment", {
    projectId: project.id,
    modelId: project.recommendedModelId,
    environmentId: "your-prediction-environment-id",
});

// Export important values
exports.useCaseId = useCase.id;
exports.projectId = project.id;
exports.deploymentId = deployment.id;
```

## Examples

Complete examples are available in the [examples directory](https://github.com/datarobot-community/pulumi-datarobot/tree/main/{{EXAMPLES_PATH}}).

## Air-Gapped Environments

For air-gapped deployments:

### 1. Store state locally
```bash
pulumi login --local
```

### 2. Install Node.js dependencies offline

Download packages with dependencies:
```bash
# Create offline package directory
mkdir offline-packages
cd offline-packages

# Download the package and all dependencies
npm pack {{PACKAGE_NAME}}
npm pack @pulumi/pulumi

# Create a package-lock.json for offline install
npm install --package-lock-only {{PACKAGE_NAME}}
```

Transfer the packages to your air-gapped system and install:
```bash
# Install from local packages
npm install ./offline-packages/*.tgz
```

### 3. Download DataRobot plugin manually

Download the plugin binary from the [releases page](https://github.com/datarobot-community/pulumi-datarobot/releases):

```bash
# Replace {{VERSION}} with your version, e.g., v0.10.14
pulumi plugin install resource datarobot {{VERSION}} --server \
  https://github.com/datarobot-community/pulumi-datarobot/releases/{{VERSION}}/
```

### 4. Skip update checks
```bash
export PULUMI_SKIP_UPDATE_CHECK=true
```

## Advanced Usage

### Custom Authentication

```typescript
import * as datarobot from "{{PACKAGE_NAME}}";

// Using API token credential
const apiToken = new datarobot.ApiTokenCredential("my-token", {
    name: "Production API Token",
    apiToken: "your-secure-token",
});

// Using basic authentication
const basicAuth = new datarobot.BasicCredential("my-basic-auth", {
    name: "Basic Auth Credential",
    username: "your-username",
    password: "your-password",
});
```

### Working with Models

```typescript
// Register a custom model
const customModel = new datarobot.CustomModel("my-custom-model", {
    name: "Customer Segmentation Model",
    targetType: "Regression",
    targetName: "revenue",
    description: "Custom model for customer revenue prediction",
});

// Create a registered model from leaderboard
const registeredModel = new datarobot.RegisteredModelFromLeaderboard("my-registered-model", {
    projectId: project.id,
    modelId: "model-id-from-leaderboard",
    name: "Best Performing Model",
});
```

### Environment Configuration

```typescript
// Create a prediction environment
const predictionEnv = new datarobot.PredictionEnvironment("my-prediction-env", {
    name: "Production Environment",
    description: "Environment for production deployments",
    platform: "datarobot",
});

// Create a custom application
const customApp = new datarobot.CustomApplication("my-custom-app", {
    name: "Customer Portal",
    sourceVersionId: "source-version-id",
    useCase: useCase.id,
});
```

## Project Structure

For larger projects, organize your code:

```
my-datarobot-project/
├── index.ts                 # Main Pulumi program
├── package.json
├── tsconfig.json
├── components/
│   ├── models.ts           # Model-related resources
│   ├── deployments.ts      # Deployment configurations
│   └── infrastructure.ts   # Supporting infrastructure
└── config/
    ├── dev.yaml           # Development configuration
    └── prod.yaml          # Production configuration
```

## Resources

- [DataRobot Platform](https://www.datarobot.com/)
- [Pulumi Documentation](https://www.pulumi.com/docs/)
- [TypeScript Guide](https://www.pulumi.com/docs/languages-sdks/javascript/)
- [Provider Documentation](https://github.com/datarobot-community/pulumi-datarobot)
- [Report Issues](https://github.com/datarobot-community/pulumi-datarobot/issues)

## Version

Package version: {{VERSION}}
