# DataRobot Pulumi Provider for Go

The DataRobot Resource Provider lets you manage [DataRobot](https://www.datarobot.com/) resources with Pulumi Infrastructure as Code.

## Installation

Add the module to your Go project:

```bash
go get {{PACKAGE_NAME}}
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

```go
package main

import (
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"{{PACKAGE_NAME}}"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		// Create a DataRobot use case
		useCase, err := datarobot.NewUseCase(ctx, "my-use-case", &datarobot.UseCaseArgs{
			Name:        pulumi.String("ML Project Use Case"),
			Description: pulumi.String("Created with Pulumi"),
		})
		if err != nil {
			return err
		}

		// Create a project from a dataset
		project, err := datarobot.NewProject(ctx, "my-project", &datarobot.ProjectArgs{
			Name:       pulumi.String("Customer Churn Prediction"),
			DatasetUrl: pulumi.String("https://s3.amazonaws.com/datarobot-datasets/churn.csv"),
			UseCaseId:  useCase.ID(),
		})
		if err != nil {
			return err
		}

		// Create a deployment
		deployment, err := datarobot.NewDeployment(ctx, "my-deployment", &datarobot.DeploymentArgs{
			ProjectId:     project.ID(),
			ModelId:       project.RecommendedModelId,
			EnvironmentId: pulumi.String("your-prediction-environment-id"),
		})
		if err != nil {
			return err
		}

		// Export important values
		ctx.Export("useCaseId", useCase.ID())
		ctx.Export("projectId", project.ID())
		ctx.Export("deploymentId", deployment.ID())

		return nil
	})
}
```

## Examples

Complete examples are available in the [examples directory](https://github.com/datarobot-community/pulumi-datarobot/tree/main/{{EXAMPLES_PATH}}).

## Air-Gapped Environments

For air-gapped deployments:

### 1. Store state locally
```bash
pulumi login --local
```

### 2. Download Go dependencies offline

Use Go modules with vendoring:

```bash
# Download dependencies
go mod download

# Create vendor directory
go mod vendor

# Create a tar archive
tar czf vendor.tar.gz vendor/ go.mod go.sum
```

Transfer `vendor.tar.gz` to your air-gapped system and extract:

```bash
tar xzf vendor.tar.gz
go build -mod=vendor
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

```go
// Using API token credential
apiToken, err := datarobot.NewApiTokenCredential(ctx, "my-token", &datarobot.ApiTokenCredentialArgs{
	Name:     pulumi.String("Production API Token"),
	ApiToken: pulumi.String("your-secure-token"),
})
if err != nil {
	return err
}

// Using basic authentication
basicAuth, err := datarobot.NewBasicCredential(ctx, "my-basic-auth", &datarobot.BasicCredentialArgs{
	Name:     pulumi.String("Basic Auth Credential"),
	Username: pulumi.String("your-username"),
	Password: pulumi.String("your-password"),
})
if err != nil {
	return err
}
```

### Working with Models

```go
// Register a custom model
customModel, err := datarobot.NewCustomModel(ctx, "my-custom-model", &datarobot.CustomModelArgs{
	Name:        pulumi.String("Customer Segmentation Model"),
	TargetType:  pulumi.String("Regression"),
	TargetName:  pulumi.String("revenue"),
	Description: pulumi.String("Custom model for customer revenue prediction"),
})
if err != nil {
	return err
}

// Create a registered model from leaderboard
registeredModel, err := datarobot.NewRegisteredModelFromLeaderboard(ctx, "my-registered-model", &datarobot.RegisteredModelFromLeaderboardArgs{
	ProjectId: project.ID(),
	ModelId:   pulumi.String("model-id-from-leaderboard"),
	Name:      pulumi.String("Best Performing Model"),
})
if err != nil {
	return err
}
```

### Error Handling and Resource Management

```go
func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		// Create resources with proper error handling
		useCase, err := createUseCase(ctx)
		if err != nil {
			return err
		}

		project, err := createProject(ctx, useCase.ID())
		if err != nil {
			return err
		}

		deployment, err := createDeployment(ctx, project)
		if err != nil {
			return err
		}

		// Export outputs
		ctx.Export("deploymentUrl", deployment.Url)
		return nil
	})
}

func createUseCase(ctx *pulumi.Context) (*datarobot.UseCase, error) {
	return datarobot.NewUseCase(ctx, "use-case", &datarobot.UseCaseArgs{
		Name:        pulumi.String("Production Use Case"),
		Description: pulumi.String("ML use case for production workloads"),
	})
}

func createProject(ctx *pulumi.Context, useCaseId pulumi.IDOutput) (*datarobot.Project, error) {
	return datarobot.NewProject(ctx, "project", &datarobot.ProjectArgs{
		Name:       pulumi.String("Production ML Project"),
		DatasetUrl: pulumi.String("s3://my-bucket/training-data.csv"),
		UseCaseId:  useCaseId,
	})
}

func createDeployment(ctx *pulumi.Context, project *datarobot.Project) (*datarobot.Deployment, error) {
	return datarobot.NewDeployment(ctx, "deployment", &datarobot.DeploymentArgs{
		ProjectId:     project.ID(),
		ModelId:       project.RecommendedModelId,
		EnvironmentId: pulumi.String("production-env-id"),
		Label:         pulumi.String("Production Model"),
	})
}
```

## Project Structure

For larger projects, organize your code:

```
my-datarobot-project/
├── main.go                 # Main Pulumi program
├── go.mod
├── go.sum
├── components/
│   ├── models.go          # Model-related resources
│   ├── deployments.go     # Deployment configurations
│   └── infrastructure.go  # Supporting infrastructure
├── config/
│   ├── dev.yaml          # Development configuration
│   └── prod.yaml         # Production configuration
└── vendor/               # Vendored dependencies (for air-gapped)
```

## Go Module Configuration

Example `go.mod`:

```go
module my-datarobot-project

go 1.21

require (
    github.com/pulumi/pulumi/sdk/v3 v3.88.1
    {{PACKAGE_NAME}} v{{VERSION}}
)
```

## Resources

- [DataRobot Platform](https://www.datarobot.com/)
- [Pulumi Documentation](https://www.pulumi.com/docs/)
- [Go Language Guide](https://www.pulumi.com/docs/languages-sdks/go/)
- [Provider Documentation](https://github.com/datarobot-community/pulumi-datarobot)
- [Go Package Documentation](https://pkg.go.dev/{{PACKAGE_NAME}})
- [Report Issues](https://github.com/datarobot-community/pulumi-datarobot/issues)

## Version

Package version: {{VERSION}}
