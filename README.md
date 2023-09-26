# Python example module

This is an example of a Viam module using our Python SDK. This repo shows how to:

- Use a Python virtualenv to install your module's dependencies on the robot
- Write a simple module in Python
- Use CI to automatically publish a new version when you create a Github release

## Contents

- src: folder with python code
- exec.sh, setup.sh: entrypoint and dependencies setup for when this runs as a module on a robot
- Makefile: bundles your module into a tarball for distribution
- .github/workflows: uploads the module when you do a github release
- meta.json: Viam module configuration file
- requirements.txt: dependencies. When run as a module, setup.sh installs these in the virtualenv

## Forking this repo

If you want to copy this repo and run it yourself, you'll need to make a few changes:

### Create your own meta.json

1. Get the Viam CLI (todo: link to docs)
1. Rename the existing `meta.json` to `meta.json.old`
1. Use `viam module create` to create a copy in your own account
1. Copy all the fields except `name` from meta.json.old (your choice whether to make it public or private)

### Change all references to the `viam` namespace

You'll need to change all the namespace references in the codebase ('viam') to the namespace of your organization on Viam.

1. You should already have done this in meta.json above
1. In the "model" field in meta.json (on line 9 when this was written)
1. In the ModelFamily in wifi_sensor.py, [around here](src/wifi_sensor.py#L13).

### Set a secret if you want to use Github CI

Instructions for setting the secret are [here](https://github.com/viamrobotics/upload-module#setting-cli-config-secret).
