# DataRobot Pulumi Provider for Python

The DataRobot Resource Provider lets you manage [DataRobot](https://www.datarobot.com/) resources with Pulumi Infrastructure as Code.

## Installation

Install the package using `pip`:

```bash
pip install pulumi_datarobot
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

```python
import pulumi
import pulumi_datarobot as dr

# Create a DataRobot use case
use_case = dr.UseCase("my-use-case",
    name="ML Project Use Case",
    description="Created with Pulumi")

# Create a project from a dataset
project = dr.Project("my-project",
    name="Customer Churn Prediction",
    dataset_url="https://s3.amazonaws.com/datarobot-datasets/churn.csv",
    use_case_id=use_case.id)

# Create a deployment
deployment = dr.Deployment("my-deployment",
    project_id=project.id,
    model_id=project.recommended_model_id,
    environment_id="your-prediction-environment-id")

# Export important values
pulumi.export("use_case_id", use_case.id)
pulumi.export("project_id", project.id)
pulumi.export("deployment_id", deployment.id)
```

## Examples

Complete examples are available in the [examples directory](https://github.com/datarobot-community/pulumi-datarobot/tree/main/examples/python).

## Air-Gapped Environments

For air-gapped deployments:

### 1. Store state locally
```bash
pulumi login --local
```

### 2. Install Python dependencies offline

Create wheel directory and download packages:
```bash
mkdir wheels
pip wheel pulumi-datarobot -w wheels/
tar cf wheels.tar wheels/
```

Transfer `wheels.tar` to your air-gapped system, then install:
```bash
tar xf wheels.tar
pip install wheels/* -f wheels/ --no-index
```

### 3. Download DataRobot plugin manually

Download the plugin binary from the [releases page](https://github.com/datarobot-community/pulumi-datarobot/releases):

```bash
# Replace v0.10.28 with your version, e.g., v0.10.14
pulumi plugin install resource datarobot v0.10.28 --server \
  https://github.com/datarobot-community/pulumi-datarobot/releases/v0.10.28/
```

### 4. Skip update checks
```bash
export PULUMI_SKIP_UPDATE_CHECK=true
```

## Advanced Usage

### Custom Authentication

```python
import pulumi_datarobot as dr

# Using API token credential
api_token = dr.ApiTokenCredential("my-token",
    name="Production API Token",
    api_token="your-secure-token")

# Using basic authentication
basic_auth = dr.BasicCredential("my-basic-auth",
    name="Basic Auth Credential",
    username="your-username",
    password="your-password")
```

### Working with Models

```python
# Register a custom model
custom_model = dr.CustomModel("my-custom-model",
    name="Customer Segmentation Model",
    target_type="Regression",
    target_name="revenue",
    description="Custom model for customer revenue prediction")

# Create a registered model from leaderboard
registered_model = dr.RegisteredModelFromLeaderboard("my-registered-model",
    project_id=project.id,
    model_id="model-id-from-leaderboard",
    name="Best Performing Model")
```

## Resources

- [DataRobot Platform](https://www.datarobot.com/)
- [Pulumi Documentation](https://www.pulumi.com/docs/)
- [Provider Documentation](https://github.com/datarobot-community/pulumi-datarobot)
- [Report Issues](https://github.com/datarobot-community/pulumi-datarobot/issues)

## Version

Package version: v0.10.28
