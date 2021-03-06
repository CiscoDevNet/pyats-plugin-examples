# Unicon Plugin Example

Unicon package extends pyATS's base connection classes and implements the much
necesary boilerplate coding of handling various types of networked devices. The
core implementation of Unicon connections revolve around the concept of
*state machines* & *pattern matching*, where various platforms and device
specific information is stored and loaded via plugins.

This directiory contains a whole example of how to write an Unicon plugin 
package where:

- the plugin comes in a form standard python package
- is auto-discovered by Unicon upon installation
- enables Unicon to connect to one or more new platforms as defined by this
  plugin.

For more information on pyATS and Unicon, visit: 
https://developer.cisco.com/site/pyats/

## Using This Plugin

To use this plugin, clone this folder into your local pyATS environment, and:

```
$ cd unicon_plugin_example

# install this package permanently into this virtual environment
$ python setup.py install

# or, develop this package (where changes in src/ folder refect in your environment immediately)
$ python setup.py develop
```
