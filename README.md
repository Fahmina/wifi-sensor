# `python example module` modular resource

This module implements the Viam [Sensor API](https://docs.viam.com/build/program/apis/#sensor) in a `wifi_sensor:linux` model.
With this model, you can gather information about connected wireless signals on your Linux machine, including wifi network availability, signal strength, and noise.

## Requirements

You must have a Linux machine to use the `python example module` modular resource.

## Build and run

To use this module, follow these instructions to [add a module from the Viam Registry](https://docs.viam.com/registry/configure/#add-a-modular-resource-from-the-viam-registry) and select the `wifi_sensor:linux` model from the [`python-example-module` module](https://app.viam.com/module/viam/python-example-module).

## Configure your `wifi_sensor:linux` component

> [!NOTE]  
> Before configuring your `wifi_sensor:linux` component, you must [create a machine](https://docs.viam.com/manage/fleet/machines/#add-a-new-machine).

Navigate to the **Config** tab of your machine's page in [the Viam app](https://app.viam.com/).
Click on the **Components** subtab and click **Create component**.
Select the `sensor` type, then select the `wifi_sensor:linux` model. 
Enter a name for your component and click **Create**.

> [!NOTE]  
> For more information, see [Configure a Machine](https://docs.viam.com/manage/configuration/).

### Attributes

There are no attributes available for configuration with this service.

### Example configuration

```json
{
  "components": [
    {
      "name": "my-wifi-sensor",
      "model": "viam:wifi_sensor:linux",
      "type": "sensor",
      "namespace": "rdk",
      "attributes": {},
      "depends_on": []
    }
  ],
  "modules": [
    {
      "type": "registry",
      "name": "viam_python-example-module",
      "module_id": "viam:python-example-module",
      "version": "0.0.13"
    }
  ]
}
```

## Next steps

Once the `wifi_sensor` has started collecting data, you can view reported readings from the [**Data** tab](https://app.viam.com/data/view?view=sensors) in the Viam app, under the **Sensors** subtab.

You can also:

- [Filter your results](https://docs.viam.com/data/view/#filter-data) using specific search criteria.
- [Export your readings](https://docs.viam.com/data/export/) to your local workstation or another machine.
- [Query your results](https://docs.viam.com/data/query/) using SQL or MQL directly in the App or from a MQL-compatible client.
- [Visualize your results](https://docs.viam.com/data/visualize/) using popular third-party visualization platforms.
- [Change the data capture frequency](https://docs.viam.com/data/capture/#configure-data-capture-for-individual-components) or [cloud sync frequency](https://docs.viam.com/data/cloud-sync/#configuration)

## Learning resources

### Writing a module

This module includes basic module logic in its [`src/wifi_sensor.py`](https://github.com/viam-labs/python-example-module/blob/main/src/wifi_sensor.py) file.
Follow the instructions to [create your own module](https://docs.viam.com/registry/create/) to learn how to write a custom module that extends a Viam API.

#### Setting up a `virtualenv`

This module includes a `setup.sh` file to help configure a `virtualenv` for this module.
Follow the instructions to [prepare your Python virtual environment](https://docs.viam.com/build/program/python-venv/) to learn how to set up and distribute a `virtualenv` configuration with your custom module.

#### Use CI to automatically publish on release

This module includes a [`.github/workflows`](https://github.com/viam-labs/python-example-module/tree/main/.github/workflows) directory, which contains workflows that you can use to automatically publish a new version of your module to the Viam registry when you create a GitHub release.
For more information, see [Update a module using a GitHub action](https://docs.viam.com/registry/upload/#update-an-existing-module-using-a-github-action).

### Repository contents

- `src`: Directory containing Python source code.
- `exec.sh`, `setup.sh`: Entrypoint file and dependencies setup, and ran on your machine when running the module.
- `Makefile`: Builds and bundles your module into a tarball for distribution.
- `.github/workflows`: Uploads the module automatically when you create a GitHub release
- `meta.json`: The Viam module configuration file.
- `requirements.txt`: A file that defines your module's required dependencies. When run as a module, `setup.sh` installs these in the `virtualenv`.

### Forking this repo

If you want to copy this repository and use it as a foundation for your own module, you'll need to make a few changes:

#### Create your own meta.json

1. Get the [Viam CLI](https://docs.viam.com/manage/cli/#install) 
1. Rename the existing `meta.json` to `meta.json.old`
1. Use `viam module create` to create a copy in your own account
1. Copy all the fields except `name` from `meta.json.old` (your choice whether to make it public or private)

#### Change all references to the `viam` namespace

You'll need to change all the namespace references in the codebase ('viam') to the namespace of your organization on Viam.

1. You should already have done this in `meta.json` above
1. In the "model" field in `meta.json` (on line 9 when this was written)
1. In the ModelFamily in wifi_sensor.py, [around here](src/wifi_sensor.py#L13).

#### Set a secret if you want to use Github CI

Instructions for setting the secret are [here](https://github.com/viamrobotics/upload-module#setting-up-auth).

## Troubleshooting

- If you are not seeing sensor readings appear in the **Logs** tab on the Viam app, make sure that both the [Data capture](https://docs.viam.com/data/capture/) and [Cloud sync](https://docs.viam.com/data/cloud-sync/) features are enabled on the data management service, and that your `wifi_sensor:linux` component is [configured to capture data](https://docs.viam.com/data/capture/#configure-data-capture-for-individual-components).
