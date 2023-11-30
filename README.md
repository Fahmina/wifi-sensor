# Python example module: Linux wifi Sensor

This module extends the Viam sensor API to gather information about connected wireless signals.
This module serves as a simple example of a Viam module built using our Python SDK, including:

- Setting up a Python virtualenv to handle dependencies.
- Writing a custom module to perform a simple task.
- Using continuous integration (CI) to automatically publish a new version when you create a GitHub release.

## Getting started

To use this module, follow the instructions to [add a module from the Viam registry](https://docs.viam.com/registry/configure/), select the **Sensor** component, then select the `wifi_sensor:linux` model from the [`python-example-module` module](https://app.viam.com/module/viam/python-example-module).

### Configuration

1. If you haven’t already, [create a robot](https://docs.viam.com/manage/fleet/robots/#add-a-new-robot) and [install `viam-server`](https://docs.viam.com/installation/).
2. [Add the data management service](https://docs.viam.com/data/capture/#add-the-data-management-service) to your machine.
3. Ensure that both [Data capture](https://docs.viam.com/data/capture/) and [Cloud sync](https://docs.viam.com/data/cloud-sync/) are enabled for the data management service.
4. Then, [enable data capture for your `wifi_sensor` component](https://docs.viam.com/data/capture/#configure-data-capture-for-individual-components) as well.

### View sensor readings

Once the `wifi_sensor` has started collecting data, you can view reported readings from the [**Data** tab](https://app.viam.com/data/view?view=sensors) in the Viam app, under the **Sensors** subtab.
You can also:

- [Filter your results](https://docs.viam.com/data/view/#filter-data) using specific search criteria.
- [Export your readings](https://docs.viam.com/data/export/) to your local workstation or another machine.
- [Query your results](https://docs.viam.com/data/query/) using SQL or MQL directly in the App or from a MQL-compatible client.

## Writing a module

This module includes basic module logic in its [`src/wifi_sensor.py`](https://github.com/viam-labs/python-example-module/blob/main/src/wifi_sensor.py) file.
Follow the instructions to [create your own module](https://docs.viam.com/registry/create/) to learn how to write a custom module that extends a Viam API.

### Setting up a `vitualenv`

This module includes a `setup.sh` file to help configure a `virtualenv` for this module.
Follow the instructions to [prepare your Python virtual environment](https://docs.viam.com/build/program/python-venv/) to learn how to set up and distribute a `virtualenv` configuration with your custom module.

### Use CI to automatically publish on release

This module includes a [`.github/workflows`](https://github.com/viam-labs/python-example-module/tree/main/.github/workflows) directory, which contains workflows that you can use to automatically publish a new version of your module to the Viam registry when you create a GitHub release.
For more information, see [Update a module using a GitHub action](https://docs.viam.com/registry/upload/#update-an-existing-module-using-a-github-action).

## Next Steps

- To view the reported readings from your wifi sensor, go to the [**Data** tab](https://docs.viam.com/manage/fleet/robots/#control).
- To write code using your wifi sensor, use one of the [available SDKs](https://docs.viam.com/program/).
- To view examples using a sensor component, explore [these tutorials](https://docs.viam.com/tutorials/).

## Repository contents

- `src`: Directory containing Python source code.
- `exec.sh`, `setup.sh`: Entrypoint file and dependencies setup, and ran on your machine when running the module.
- `Makefile`: Builds and bundles your module into a tarball for distribution.
- `.github/workflows`: Uploads the module automatically when you create a GitHub release
- `meta.json`: The Viam module configuration file.
- `requirements.txt`: A file that defines your module's required dependencies. When run as a module, `setup.sh` installs these in the `virtualenv`.

## Forking this repo

If you want to copy this repo and run it yourself, you'll need to make a few changes:

### Create your own meta.json

1. Get the [Viam CLI](https://docs.viam.com/manage/cli/#install) 
1. Rename the existing `meta.json` to `meta.json.old`
1. Use `viam module create` to create a copy in your own account
1. Copy all the fields except `name` from `meta.json.old` (your choice whether to make it public or private)

### Change all references to the `viam` namespace

You'll need to change all the namespace references in the codebase ('viam') to the namespace of your organization on Viam.

1. You should already have done this in `meta.json` above
1. In the "model" field in `meta.json` (on line 9 when this was written)
1. In the ModelFamily in wifi_sensor.py, [around here](src/wifi_sensor.py#L13).

### Set a secret if you want to use Github CI

Instructions for setting the secret are [here](https://github.com/viamrobotics/upload-module#setting-up-auth).

## Troubleshooting

- If you are not seeing sensor readings appear in the **Logs** tab on the Viam app, make sure that both the [Data capture](https://docs.viam.com/data/capture/) and [Cloud sync](https://docs.viam.com/data/cloud-sync/) features are enabled on the data management service, and that your `wifi_sensor:linux` component is [configured to capture data](https://docs.viam.com/data/capture/#configure-data-capture-for-individual-components).
