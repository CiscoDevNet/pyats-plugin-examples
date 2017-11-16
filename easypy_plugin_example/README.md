# Easypy Plugin Example

Easypy Plugins offers optional functionalities that may be added to easypy. Each
plugin must be configured first via a configuration YAML file before they can be
loaded, instantiated and run at various stages of execution.

This directiory contains a whole example of how to write an Easypy plugin
package where:

- the plugin comes in a form standard python package
- is auto-discovered by Easypy upon installation and configuration
- enables Easypy to run at various stages of execution defined by this plugin.

For more information on pyATS and Easypy, visit:
https://developer.cisco.com/site/pyats/

## Using This Plugin

To use this plugin, clone this folder into your local pyATS environment, and:

```
$ cd easypy_plugin_example

# install this package permanently into this virtual environment
$ python setup.py install

# or, develop this package (where changes in src/ folder refect in your environment immediately)
$ python setup.py develop

# enable this plugin globally (for all runs in this pyATS instance) at this virtual environment
$ cp easypy_config.yaml $VIRTUAL_ENV

# or, enable the plugin locally (for this run only) by passing in a config YAML via a command-line argument called -configuration.
$ easypy easypy_job.py -configuration easypy_config.yaml

```
