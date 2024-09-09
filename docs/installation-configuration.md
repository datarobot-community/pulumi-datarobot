---
title: DataRobot Installation & Configuration
meta_desc: Information on how to install the DataRobot provider.
layout: package
---

## Installation

The Pulumi `DataRobot` provider is available as a package in all Pulumi languages:

- Python: [`pulumi-datarobot`](https://pypi.org/project/pulumi-datarobot/)
- JavaScript/TypeScript: [`@datarobot/pulumi-datarobot`](https://www.npmjs.com/package/@datarobot/pulumi-datarobot)
- Go: [`github.com/datarobot-community/pulumi-datarobot/sdk`](https://pkg.go.dev/github.com/datarobot-community/pulumi-datarobot/sdk)
- .NET: _coming soon_

### Provider Binary

The DataRobot provider binary is a third party binary. It can be installed using the `pulumi plugin` command.

```sh
pulumi plugin install resource datarobot <version> --server github://api.github.com/datarobot-community/pulumi-datarobot
```

Replace the version string with your desired version.

## Configuration

You must configure the DataRobot provider for Pulumi with a [DataRobot API Key](https://docs.datarobot.com/en/docs/get-started/acct-mgmt/acct-settings/api-key-mgmt.html#api-key-management) before the provider can be used to access and manage items in your DataRobot account.

- `datarobot:apikey` (environment: `DATAROBOT_API_KEY`) - the API key for `datarobot`

Once you have your API Key, there are two ways to provide it to Pulumi:

1. Set the environment variable for the preferred method. For example, to set the environment variable for an API Key:

   ```sh
   $ export DATAROBOT_API_KEY=XXXXXXXXXXXXXX
   ```

2. If you prefer to store your API Key alongside your Pulumi stack for easy multi-user access, use configuration to set them.

   ```sh
   $ pulumi config set pulumi-datarobot:apikey --secret
   Value: <paste api key here>
   ```

Make sure to pass `--secret` when setting any sensitive data (in this example `pulumi-datarobot:apikey`) so that it's properly encrypted. The complete list of configuration parameters is in the [DataRobot provider for Pulumi README](https://github.com/datarobot-community/pulumi-datarobot/blob/main/README.md#configuration).
