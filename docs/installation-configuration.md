---
title: DataRobot Installation & Configuration
meta_desc: Information on how to install the DataRobot provider.
layout: package
---

## Installation

The Pulumi `DataRobot` provider is available as a package in all Pulumi languages:

- Python: [`pulumi-datarobot`](https://pypi.org/project/pulumi-datarobot/)
- JavaScript/TypeScript: [`@pulumi/datarobot`](https://www.npmjs.com/package/@pulumi/datarobot)
- Go: [`github.com/pulumi/pulumi-datarobot/sdk`](https://pkg.go.dev/github.com/pulumi/pulumi-datarobot/sdk)
- .NET: [`Pulumi.datarobot`](https://www.nuget.org/packages/Pulumi.datarobot)

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
pip install pulumi-datarobot
```

### Go

To use from Go, use `go get` to grab the latest version of the library:

```bash
go get github.com/pulumi/pulumi-datarobot/sdk/go/...
```

### .NET

To use from .NET, install using `dotnet add package`:

```bash
dotnet add package Pulumi.datarobot
```

## Configuration

The following configuration points are available for the `datarobot` provider:

- `datarobot:apikey` (environment: `DATAROBOT_API_KEY`) - the API key for `datarobot`
- `datarobot:endpoint` (environment: `DATAROBOT_ENDPOINT`) - the endpoint for `datarobot`