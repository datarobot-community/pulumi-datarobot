# DataRobot Resource Provider

The DataRobot Resource Provider lets you manage [DataRobot](https://www.datarobot.com/) resources.

The provider is built on [terraform-provider-datarobot](https://github.com/datarobot-community/terraform-provider-datarobot).

To use this package, please install the [Pulumi CLI first](https://www.pulumi.com/docs/install/).

### Prerequisites

There are a few additional steps to build this Provider locally since it has not been published to the Pulumi Registry yet.

Ensure the following tools are installed and present in your `$PATH`:

- [`pulumictl`](https://github.com/pulumi/pulumictl#installation)
- [Go >= 1.17](https://golang.org/dl/)
- [`make`](https://formulae.brew.sh/formula/make)
- [Python](https://www.python.org/downloads/) (called as `python3`) and [pip](https://pypi.org/project/pip/). For recent versions of MacOS, the system-installed version is fine.
- [NodeJS](https://nodejs.org/en/) Active or maintenance version ([Node.js Releases](https://nodejs.org/en/about/previous-releases)).  We recommend using [nvm](https://github.com/nvm-sh/nvm) to manage NodeJS installations.
- [Yarn](https://yarnpkg.com/)
- [TypeScript](https://www.typescriptlang.org/)
- [.NET](https://dotnet.microsoft.com/download)

You may skip installing any languages that you are not interested in testing in right now. Go is the only language required to test in Pulumi YAML

Although the steps below contain Unix commands, the Provider can also be tested on Windows.
It is recommended to use Powershell to run the `make` commands and the Windows equivalents for `cp`, `export`, etc.

## Configuration

The following configuration points are available for the DataRobot provider:

- `datarobot:apikey` (environment: `DATAROBOT_API_KEY`) - the API key for DataRobot
- `datarobot:endpoint` (environment: `DATAROBOT_ENDPOINT`) - the endpoint for DataRobot

## Run the Low-Code Monitored RAG Example

1. In a terminal clone the `pulumi-datarobot` repository:

    ~~~ shell
    git clone https://github.com/datarobot-community/pulumi-datarobot.git
    ~~~

1. Build the Provider locally.
This step is only required because we have not published the Provider to the Pulumi Registry yet.

    ~~~ shell
    make provider
    ~~~

1. Copy the generated binary into your PATH.

    ~~~ shell
    cp bin/pulumi-resource-datarobot $GOPATH/bin 
    ~~~

    Depending on your setup, this could require `sudo` permissions.
    Windows users may need to rename the `pulumi-resource-datarobot` binary to `pulumi-resource-datarobot.exe` to make it executable.

1. Go to the `examples/low_code_rag` directory.

    ~~~ shell
    cd examples/low_code_rag
    ~~~

1. The provider requires an API key set in an environment variable named `DATROBOT_API_KEY`. Copy the [API key](https://docs.datarobot.com/en/docs/get-started/acct-mgmt/acct-settings/api-key-mgmt.html#api-key-management) from the DataRobot console and create the `DATAROBOT_API_KEY` environment variable.

    ~~~ shell
    export DATAROBOT_API_KEY=<YOUR_API_KEY>
    ~~~

    Where `<your API key>` is the API key you copied from the DataRobot Console.
 
 1. The example requires Google Cloud service account credentials in order to call the Google Vertex AI API. Follow [this guide](https://cloud.google.com/iam/docs/keys-create-delete#creating) to create a service account key for your Google account.
 Download the service account key file and save it as `google_credentials.json` in the current directory.

1. Create the resources.

    By defualt, Pulumi will prompt you to login to their Pulumi Cloud service to manage the state files.
    To store and manage the state files locally instead, run `pulumi login --local` before continuing.
    This will create the `.pulumi` directory in your home directory to manage the state.

    ~~~ shell
    pulumi up
    ~~~

    Enter a name for your Pulumi stack when prompted.
    Enter `yes` when asked if you want to perform the update.

1. Once the creation is complete, navigate to the `datarobotChatApplicationUrl` to view your chat application.

    ~~~ shell
    Outputs:
        datarobotChatApplicationUrl: {
            value: "<your_chat_application_url>"
        }

    Resources:
        + 12 created
    ~~~

1. (optional) Delete the resources when you are done.

    ~~~ shell
    pulumi down
    ~~~

    Choose your stack name when prompted and enter `yes` to perform this destroy. 

## Python Example

Follow these steps to run the Python example.
Since the Python SDK is not published yet, it must be built and overriden locally.

1. Install local Python SDK.

    ~~~ shell
    make install_python_sdk
    ~~~

1. Navigate to the example directory.

    ~~~ shell
    cd examples/py
    ~~~

1. Create the resources.

    ~~~ shell
    pulumi up
    ~~~

    If the command fails, try adding the location where the local SDK was installed to your PYTHONPATH. For example:
    ~~~ shell
    export PYTHONPATH="${PYTHONPATH}:/opt/homebrew/lib/python3.12/site-packages"
    ~~~

## Typescript Example

1. Install local Typescript SDK.

    ~~~ shell
    make install_nodejs_sdk
    ~~~

1. Navigate to the example directory.

    ~~~ shell
    cd examples/ts
    ~~~

1. Link the local Provider

    ~~~ shell
    npm install
    yarn link @pulumi/datarobot
    ~~~

1. Create the resources.

    ~~~ shell
    pulumi up
    ~~~
