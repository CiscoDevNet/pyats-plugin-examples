'''
Unicon Plugin Example Implementation
------------------------------------

In this example, we will implement a sample Unicon connection plugin supporting
an imaginary platform named "orz" by inhering from the built-in Unicon Cisco
IOSv connection plugin.

Note:
    Make sure the content of this file contains the Connection subclass
    this plugin implements. 

'''

# import the base dependencies
# (extending built-in plugins)

from unicon.plugins.ios.iosv import IosvSingleRpConnection

from .statemachine import ORZSingleRpStateMachine
from .services import OrzServiceList
from .settings import OrzSettings

class ORZSingleRPConnection(IosvSingleRpConnection):
    '''ORZSingleRPConnection
    
    Imaginary Orz platform support. Because our imaginary platform was inspired
    from Cisco IOSv platform, we are extending (inhering) from its plugin.
    '''

    # each connection plugin needs to declare the os it supports
    os = 'orz'

    # there's no specific series in this imaginary platform
    # set it to None to indicate so
    series = None

    # single-rp chasis or dual-rp chasis
    chassis_type = 'single_rp'

    # each connection class must be accompanied by its own state machine class
    # a state machine class provides the connection implementation the means of
    # recognizing the current state the device is in, all available subsequent
    # states, and how to switch between states. (eg, from exec -> config)
    state_machine_class = ORZSingleRpStateMachine

    # all subcommands (eg, connection methods) are called services, and are
    # listed under the ServiceList class. The ServiceList class aggregates all
    # services (classes) that implements the actual methods into one top-level
    # location, to be managed by the connection class.
    subcommand_list = OrzServiceList

    # any key/value setting pairs goes here
    settings = OrzSettings()
