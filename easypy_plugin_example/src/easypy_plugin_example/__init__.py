'''
Easypy Plugin Example Implementation
------------------------------------

In this example, we will implement a sample Easypy plugin that saluting the
world before and after each job and task.

Arguments:
    This plugin supports one optional argument (print_timestamp) to be passed in
    when run under easypy for demonstration purposes.
    print_timestamp: flag, enable to print out the job/task runtime.

Actions:
    - pre_job: pre easypy job execution action
    - post_job: post easypy job execution action
    - pre_task: pre easypy task execution action
    - post_task: post easypy task execution action

Examples:
    # to run under easypy
    bash$ easypy pyats_example_job.py -configuration easypy_config.yaml
    # or with optional argument
    bash$ easypy pyats_example_job.py -configuration easypy_config.yaml --print_timestamp

'''

# import the base dependencies
# (extending built-in plugins)

# Example
# --------
#
#   hello-world plugin

import logging
import argparse
import datetime

from ats.easypy.plugins.bases import BasePlugin

logger = logging.getLogger(__name__)

class HelloWorldPlugin(BasePlugin):
    '''HelloWorld Plugin

    Runs before and after each job and task, saluting the world and printing
    out the job/task runtime if a custom flag is used.
    '''

    # each plugin may have a unique name
    # set it by setting the 'name' class variable.
    # (defaults to the current class name)
    name = 'HelloWorld'

    # each plugin may have a parser to parse its own command line arguments.
    # these parsers are invoked automatically by the parser engine during
    # easypy startup. (always use add_help=False)
    parser = argparse.ArgumentParser(add_help = False)

    # always create a plugin's own parser group
    # and add arguments to that group instead
    hello_world_grp = parser.add_argument_group('Hello World')

    # custom arguments shall always use -- as prefix
    # positional custom arguments are NOT allowed.
    hello_world_grp.add_argument('--print_timestamp',
                                 action = 'store_true',
                                 default = False)

    # plugins may define its own class constructor __init__, though, it
    # must respect the parent __init__, so super() needs to be called.
    # any additional arguments defined in the plugin config file would be
    # passed to here as keyword arguments
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # define your plugin's stage actions as methods
    # as this plugin should run pre and post job
    # we need to deifne 'pre_job' and 'post_job' methods.

    # define the pre-job action
    # if 'job' is specified as a function argument, the current Job
    # object is provided as input to this action method when called
    def pre_job(self, job):

        # plugin parser results are always stored as 'self.args'
        if self.args.print_timestamp:
            self.job_start = datetime.datetime.now()
            logger.info('Current time is: %s' % self.job_start)

        logger.info('Pre-Job %s: Hello World!' % job.name)

    # define post_job action
    def post_job(self, job):

        if self.args.print_timestamp:
            self.job_end = datetime.datetime.now()
            logger.info('Job run took: %s' % self.job_end - self.job_start)

        logger.info('Post-Job %s: Hello World!' % job.name)

    # similarly, with pre and post-task methods
    # if a 'task' argument is specified as a function argument, the current
    # Task object is provided as input to this action method on call.
    def pre_task(self, task):
        if self.args.print_timestamp:
            self.task_start = datetime.datetime.now()
            logger.info('Current time is: %s' % self.task_start)

        logger.info('Pre-Task %s: Hello World!' % task.taskid)

    def post_task(self, task):
        if self.args.print_timestamp:
            self.task_end = datetime.datetime.now()
            logger.info('Task run took: %s' %
                        self.task_end - self.task_start)

        logger.info('Post-Task %s: Hello World!' % task.taskid)