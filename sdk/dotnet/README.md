# DataRobot Pulumi Provider for .NET

The DataRobot Resource Provider lets you manage [DataRobot](https://www.datarobot.com/) resources with Pulumi Infrastructure as Code.

## Installation

Install the package using the .NET CLI or Package Manager:

```bash
# Using .NET CLI
dotnet add package DataRobotPulumi.Datarobot

# Using Package Manager Console in Visual Studio
Install-Package DataRobotPulumi.Datarobot
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

### C# Example

```csharp
using System.Threading.Tasks;
using Pulumi;
using DataRobotPulumi.Datarobot;

class Program
{
    static Task<int> Main() => Deployment.RunAsync<MyStack>();
}

class MyStack : Stack
{
    public MyStack()
    {
        // Create a DataRobot use case
        var useCase = new UseCase("my-use-case", new UseCaseArgs
        {
            Name = "ML Project Use Case",
            Description = "Created with Pulumi"
        });

        // Create a project from a dataset
        var project = new Project("my-project", new ProjectArgs
        {
            Name = "Customer Churn Prediction",
            DatasetUrl = "https://s3.amazonaws.com/datarobot-datasets/churn.csv",
            UseCaseId = useCase.Id
        });

        // Create a deployment
        var deployment = new Deployment("my-deployment", new DeploymentArgs
        {
            ProjectId = project.Id,
            ModelId = project.RecommendedModelId,
            EnvironmentId = "your-prediction-environment-id"
        });

        // Export important values
        this.UseCaseId = useCase.Id;
        this.ProjectId = project.Id;
        this.DeploymentId = deployment.Id;
    }

    [Output] public Output<string> UseCaseId { get; set; }
    [Output] public Output<string> ProjectId { get; set; }
    [Output] public Output<string> DeploymentId { get; set; }
}
```

### F# Example

```fsharp
module Program

open Pulumi
open Pulumi.FSharp
open DataRobotPulumi.Datarobot

let infra () =
    // Create a DataRobot use case
    let useCase = UseCase("my-use-case", UseCaseArgs(
        Name = input "ML Project Use Case",
        Description = input "Created with Pulumi"
    ))

    // Create a project from a dataset
    let project = Project("my-project", ProjectArgs(
        Name = input "Customer Churn Prediction",
        DatasetUrl = input "https://s3.amazonaws.com/datarobot-datasets/churn.csv",
        UseCaseId = useCase.Id
    ))

    // Create a deployment
    let deployment = Deployment("my-deployment", DeploymentArgs(
        ProjectId = project.Id,
        ModelId = project.RecommendedModelId,
        EnvironmentId = input "your-prediction-environment-id"
    ))

    // Export outputs
    dict [
        "useCaseId", useCase.Id :> obj
        "projectId", project.Id :> obj
        "deploymentId", deployment.Id :> obj
    ]

[<EntryPoint>]
let main _ = Deployment.run infra
```

## Examples

Complete examples are available in the [examples directory](https://github.com/datarobot-community/pulumi-datarobot/tree/main/examples/dotnet).

## Air-Gapped Environments

For air-gapped deployments:

### 1. Store state locally
```bash
pulumi login --local
```

### 2. Install .NET packages offline

Download NuGet packages:

```bash
# Create packages directory
mkdir packages

# Download package and dependencies
dotnet restore --packages packages

# Create a NuGet package archive
tar czf packages.tar.gz packages/
```

Transfer `packages.tar.gz` to your air-gapped system:

```bash
tar xzf packages.tar.gz

# Restore from local packages
dotnet restore --packages packages --source packages
```

### 3. Download DataRobot plugin manually

Download the plugin binary from the [releases page](https://github.com/datarobot-community/pulumi-datarobot/releases):

```bash
# Replace v0.10.26 with your version, e.g., v0.10.14
pulumi plugin install resource datarobot v0.10.26 --server \
  https://github.com/datarobot-community/pulumi-datarobot/releases/v0.10.26/
```

### 4. Skip update checks
```bash
export PULUMI_SKIP_UPDATE_CHECK=true
```

## Advanced Usage

### Custom Authentication

```csharp
// Using API token credential
var apiToken = new ApiTokenCredential("my-token", new ApiTokenCredentialArgs
{
    Name = "Production API Token",
    ApiToken = "your-secure-token"
});

// Using basic authentication
var basicAuth = new BasicCredential("my-basic-auth", new BasicCredentialArgs
{
    Name = "Basic Auth Credential",
    Username = "your-username",
    Password = "your-password"
});
```

### Working with Models

```csharp
// Register a custom model
var customModel = new CustomModel("my-custom-model", new CustomModelArgs
{
    Name = "Customer Segmentation Model",
    TargetType = "Regression",
    TargetName = "revenue",
    Description = "Custom model for customer revenue prediction"
});

// Create a registered model from leaderboard
var registeredModel = new RegisteredModelFromLeaderboard("my-registered-model", new RegisteredModelFromLeaderboardArgs
{
    ProjectId = project.Id,
    ModelId = "model-id-from-leaderboard",
    Name = "Best Performing Model"
});
```

### Advanced Stack Configuration

```csharp
public class DataRobotStack : Stack
{
    public DataRobotStack()
    {
        var config = new Config();

        // Read configuration values
        var environment = config.Require("environment");
        var datasetUrl = config.RequireSecret("datasetUrl");
        var apiToken = config.RequireSecret("apiToken");

        // Create resources based on environment
        var useCase = CreateUseCase(environment);
        var project = CreateProject(useCase, datasetUrl);
        var deployment = CreateDeployment(project, environment);

        // Export outputs with environment prefix
        this[$"{environment}UseCaseId"] = useCase.Id;
        this[$"{environment}ProjectId"] = project.Id;
        this[$"{environment}DeploymentUrl"] = deployment.Url;
    }

    private UseCase CreateUseCase(string environment)
    {
        return new UseCase($"use-case-{environment}", new UseCaseArgs
        {
            Name = $"ML Use Case - {environment.ToUpper()}",
            Description = $"Use case for {environment} environment"
        });
    }

    private Project CreateProject(UseCase useCase, Output<string> datasetUrl)
    {
        return new Project($"project-{useCase.Name}", new ProjectArgs
        {
            Name = $"ML Project - {useCase.Name}",
            DatasetUrl = datasetUrl,
            UseCaseId = useCase.Id
        });
    }

    private Deployment CreateDeployment(Project project, string environment)
    {
        var envConfig = environment == "production"
            ? "prod-prediction-env-id"
            : "dev-prediction-env-id";

        return new Deployment($"deployment-{environment}", new DeploymentArgs
        {
            ProjectId = project.Id,
            ModelId = project.RecommendedModelId,
            EnvironmentId = envConfig,
            Label = $"Model Deployment - {environment.ToUpper()}"
        });
    }
}
```

## Project Structure

For larger projects, organize your code:

```
MyDataRobotProject/
├── MyDataRobotProject.csproj
├── Program.cs               # Main program entry point
├── Stacks/
│   ├── DataRobotStack.cs   # Main stack definition
│   ├── ModelStack.cs       # Model-related resources
│   └── DeploymentStack.cs  # Deployment configurations
├── Components/
│   ├── UseCase.cs          # UseCase component
│   ├── Models.cs           # Model components
│   └── Infrastructure.cs   # Supporting infrastructure
├── Config/
│   ├── Pulumi.dev.yaml     # Development configuration
│   └── Pulumi.prod.yaml    # Production configuration
└── packages/               # Offline packages (for air-gapped)
```

## Project File Configuration

Example `.csproj` file:

```xml
<Project Sdk="Microsoft.NET.Sdk">

  <PropertyGroup>
    <OutputType>Exe</OutputType>
    <TargetFramework>net6.0</TargetFramework>
    <Nullable>enable</Nullable>
  </PropertyGroup>

  <ItemGroup>
    <PackageReference Include="Pulumi" Version="3.88.1" />
    <PackageReference Include="DataRobotPulumi.Datarobot" Version="v0.10.26" />
  </ItemGroup>

</Project>
```

## Testing

Example unit test using xUnit:

```csharp
using Xunit;
using Pulumi.Testing;
using System.Threading.Tasks;
using System.Collections.Immutable;

public class DataRobotStackTests
{
    [Fact]
    public async Task StackCreatesExpectedResources()
    {
        var resources = await Testing.RunAsync<DataRobotStack>();

        var useCases = resources.OfType<UseCase>();
        Assert.Single(useCases);

        var projects = resources.OfType<Project>();
        Assert.Single(projects);

        var deployments = resources.OfType<Deployment>();
        Assert.Single(deployments);
    }
}
```

## Resources

- [DataRobot Platform](https://www.datarobot.com/)
- [Pulumi Documentation](https://www.pulumi.com/docs/)
- [.NET Language Guide](https://www.pulumi.com/docs/languages-sdks/dotnet/)
- [Provider Documentation](https://github.com/datarobot-community/pulumi-datarobot)
- [NuGet Package](https://www.nuget.org/packages/DataRobotPulumi.Datarobot)
- [Report Issues](https://github.com/datarobot-community/pulumi-datarobot/issues)

## Version

Package version: v0.10.26
