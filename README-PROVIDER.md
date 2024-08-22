# Foo Resource Provider

The Foo Resource Provider lets you manage [Foo](http://example.com) resources.

## Installing

This package is available for several languages/platforms:

### Node.js (JavaScript/TypeScript)

To use from JavaScript or TypeScript in Node.js, install using either `npm`:

```bash
npm install @pulumi/datarobot
```

or `yarn`:

```bash
yarn add @pulumi/datarobot
```

### Python

To use from Python, install using `pip`:

```bash
pip install pulumi_datarobot
```

### Go

To use from Go, use `go get` to grab the latest version of the library:

```bash
go get github.com/datarobot-community/pulumi-datarobot/sdk/go/...
```

### .NET

To use from .NET, install using `dotnet add package`:

```bash
dotnet add package Pulumi.Datarobot
```

## Configuration

The following configuration points are available for the `foo` provider:

- `foo:apiKey` (environment: `DATAROBOT_API_TOKEN`) - the API key for `DataRobot`
- (Optional) `foo:endpoint` (environment: `FOO_REGION`) - the endpoint for the DataRobot service

## Reference

For detailed reference documentation, please visit [the Pulumi registry](https://www.pulumi.com/registry/packages/datarobot/api-docs/).
