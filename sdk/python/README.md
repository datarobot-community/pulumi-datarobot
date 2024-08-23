# DataRobot Resource Provider

The DataRobot Resource Provider lets you manage [DataRobot](https://www.datarobot.com/) resources.

The provider is built on [terraform-provider-datarobot](https://github.com/datarobot-community/terraform-provider-datarobot).

To use this package, please install the [Pulumi CLI first](https://pulumi.com/).

## Installing

This package is available in many languages in the standard packaging formats.

### Go

To use from Go, use `go get` to grab the latest version of the library

```
$ go get github.com/datarobot-community/pulumi-datarobot/sdk/go/...
```

## Configuration

The following configuration points are available for the `datarobot` provider:

- `datarobot:apiKey` (environment: `DATAROBOT_API_KEY`) the API key for DataRobot.