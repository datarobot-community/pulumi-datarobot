# DataRobot Resource Provider

The DataRobot Resource Provider lets you manage [DataRobot](https://www.datarobot.com/) resources.

The provider is built on [terraform-provider-datarobot](https://github.com/datarobot-community/terraform-provider-datarobot).

To use this package, please install the [Pulumi CLI first](https://pulumi.com/).

## Run the Low-Code Monitored RAG Example

1. In a terminal clone the `pulumi-datarobot` repository:

    ~~~ shell
    git clone https://github.com/datarobot-community/pulumi-datarobot.git
    ~~~

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