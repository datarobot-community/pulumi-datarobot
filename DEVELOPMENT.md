# Development documentation

This repo is an automatic [bridge
provider](https://github.com/pulumi/pulumi-terraform-bridge) for the
[DataRobot Terraform
provider](https://github.com/datarobot-community/terraform-provider-datarobot)


## Releasing

To release, run the ["Upgrade provider"
Action](https://github.com/datarobot-community/pulumi-datarobot/actions/workflows/upgrade-provider.yml)
after the release of the Terraform provider.

If all goes well, it will generate PR. Review that PR after you've
confirmed it has picked up the correct Terraform provider version
([Sample
PR](https://github.com/datarobot-community/pulumi-datarobot/pull/202)).


After the merge, you are ready to release the new version. To do so,
create a Release matching the same tag as the Terraform Release. In
the sample, that is `v0.10.2`. After you do so, the
[Release](https://github.com/datarobot-community/pulumi-datarobot/actions/workflows/release.yml)
Action will pick it up and run go-releaser for all of our supported
SDKs and attach them back to the release tag you created.


## Validating Locally Prior to Release

We cannot pull back Pulumi releases easily as it requires a manual
e-mail process to do so. So, we recommend you do some smoke testing
locally with the newest release.

### Local testing procedure

* Checkout the main branch locally after the PR created above is merged.
* Ensure you have a valid NodeJS, .NET, JVM, and Python installation available locally in the environment when you are in the repo.
* Run `make generate_sdk` and resolve any errors that occur. Warnings are okay. It will drop installers into the `sdk` folder by language
* Run `make provider`. This will compile the binary of the provider for your platform that is required in addition to install the platform specific SDK.

Now, in your example Pulumi project, you should be ready to install the local development version. Here is the procedure for that. We'll show Python here because that is our most critical SDK

* First, install the Python package `pip install -e ~/path/to/pulumi-datarobot/sdk/python`
* Next, install the provider binary with `pulumi plugin install resource datarobot v0.0.0 -f ~/path/to/pulumi-datarobot/bin/pulumi-resource-datarobot`

From there, you should have everything ready to test with a `pulumi up`!