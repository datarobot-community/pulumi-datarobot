# DataRobot Resource Provider

The DataRobot Resource Provider lets you manage [DataRobot](https://www.datarobot.com/) resources.
The provider is built on [terraform-provider-datarobot](https://github.com/datarobot-community/terraform-provider-datarobot).
To use this package, please install the [Pulumi CLI](https://pulumi.io/) first.

## Installing

This package is available for several languages/platforms:

### Python

To use from Python, install using `pip`:

```bash
pip install pulumi_datarobot
```

### Javscript/Typescript

To use from JavaScript or TypeScript in Node.js, install using either `npm`:

```bash
npm install @datarobot/pulumi-datarobot
```

or `yarn`:

```bash
yarn add @datarobot/pulumi-datarobot
```

### Go

Coming soon...

### .NET

Coming soon...

### YAML

No install necessary, just run `pulumi up`.

## Configuration

The following configuration points are available for the DataRobot provider:

- `datarobot:apikey` (environment: `DATAROBOT_API_KEY`) - the API key for DataRobot
- `datarobot:endpoint` (environment: `DATAROBOT_ENDPOINT`) - the endpoint for DataRobot

## Examples

See [datarobot-pulumi examples](https://github.com/datarobot-community/pulumi-datarobot/tree/main/examples)
