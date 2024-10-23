# DataRobot Resource Provider

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