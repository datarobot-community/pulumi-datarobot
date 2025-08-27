## DataRobot Resource Provider

The DataRobot Resource Provider lets you manage [DataRobot](https://www.datarobot.com/) resources.
The provider is built on [terraform-provider-datarobot](https://github.com/datarobot-community/terraform-provider-datarobot).
To use this package, please install the [Pulumi CLI](https://pulumi.io/) first.

## Installing

This package is available for several languages/platforms:

- Python: [`pulumi-datarobot`](https://pypi.org/project/pulumi-datarobot/)
- JavaScript/TypeScript: [`@datarobot/pulumi-datarobot`](https://www.npmjs.com/package/@datarobot/pulumi-datarobot)
- Go: [`github.com/datarobot-community/pulumi-datarobot/sdk`](https://pkg.go.dev/github.com/datarobot-community/pulumi-datarobot/sdk)
- .NET: [`DataRobotPulumi.Datarobot`](https://www.nuget.org/packages/DataRobotPulumi.Datarobot)

### Python

To use from Python, install using `pip`:

```bash
pip install pulumi_datarobot
```

### Javascript/Typescript

To use from JavaScript or TypeScript in Node.js, install using either `npm`:

```bash
npm install @datarobot/pulumi-datarobot
```

or `yarn`:

```bash
yarn add @datarobot/pulumi-datarobot
```

### Go

```
go get github.com/datarobot-community/pulumi-datarobot/sdk/go/...
```

### .NET

To use from .NET, install using `dotnet add package`:

```
dotnet add package DataRobotPulumi.Datarobot
```

### YAML

No install necessary, just run `pulumi up`.

## Configuration

The following configuration points are available for the DataRobot provider:

- `datarobot:apikey` (environment: `DATAROBOT_API_TOKEN`) - the API key for DataRobot
- `datarobot:endpoint` (environment: `DATAROBOT_ENDPOINT`) - the endpoint for DataRobot

## Examples

See [datarobot-pulumi examples](https://github.com/datarobot-community/pulumi-datarobot/tree/main/examples)

## Air-Gapped Environments

Keep the following items in mind if running in an air-gapped environment:

- Run `pulumi login --local` to store state files on your local filesystem, instead of the default Pulumi Cloud. Pulumi binaries are available [here](https://www.pulumi.com/docs/iac/download-install/).
- Set `DATAROBOT_ENDPOINT`: https://{datarobot.example.com}/api/v2
    (replacing {datarobot.example.com} with your specific deployment endpoint)
- For Python, the [pulumi](https://pypi.org/project/pulumi/) and [pulumi-datarobot](https://pypi.org/project/pulumi-datarobot/) packages must be installed in the air-gapped system.

    Example using `pip wheel`:

    1. create a directory where you want to store package wheels.

    ```bash
    mkdir folder_containing_wheel
    ```

    2. Now install wheels of the python library you want to install

    ```bash
    pip wheel pulumi-datarobot -w folder_containing_wheel
    ```

    This will store all your required dependent wheels of the `pulumi-datarobot` package in the folder. you can check it with doing ls -ltr`.

    3. Now, you can make a tar file of this folder.

    ```bash
    tar cf folder_containing_wheel.tar folder_containing_wheel/
    ```

    and you can transfer it to your air-gapped system.

    Now untar the folder.

    ```bash
    tar xf folder_containing_wheel.tar
    cd folder_containing_wheel/
    ```

    now install wheels from the folder.

    ```bash
    pip install * -f ./ --no-index
    ```

You will also need to download the binary plugin from this repository. Click on the version that matches the Python package
version from our [Releases](https://github.com/datarobot-community/pulumi-datarobot/releases) page, download the tar.gz
for the correct architecture of your computer. For Codespaces, that is `*-linux-amd64.tar.gz`. After you've extracted it
install it with `pulumi plugin install resource datarobot <version> -f <path-to-extracted-folder>`

## Rate limited by GitHub?

GitHub has hard limits on API calls that cannot be changed. If you are running into this when running deployment tasks
you have a couple of options. You can wait until the [rate limit](https://docs.github.com/en/enterprise-cloud@latest/rest/using-the-rest-api/rate-limits-for-the-rest-api?apiVersion=2022-11-28#primary-rate-limit-for-unauthenticated-users) expires or you can do a direct download from the releases page which will not use the API and hit the limit.

To directly download the plugin and bypass the GitHub API run `pulumi plugin install resource datarobot <version> --server https://github.com/datarobot-community/pulumi-datarobot/releases/download/<version>/`

For example, to download version 0.10.14, you can run `pulumi plugin install resource datarobot v0.10.14 --server https://github.com/datarobot-community/pulumi-datarobot/releases/download/v0.10.14/` prior to running the deploy to directly install the plugin.
