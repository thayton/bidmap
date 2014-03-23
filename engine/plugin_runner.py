#!/usr/bin/env python

"""
Wrapper around a plugin that handles opening a plugin, running the plugin, and then
saving the results to a file.

If you look in the task_manager.py code you'll see that after a new process gets
forked, the run() method of the spawned task is what gets called. The 
"""

import os
import re
import sys
import json
import logging
import random
import traceback

from plugin_loader import PluginLoader, FileFilter
from urlparse import urlparse
from datetime import date

class PluginRunner(object):
    def __init__(self, plugin, results_dir='results', logfile='/var/log/bidmap/plugin_runner.log'):
        self.plugin = plugin
        self.results_dir = results_dir
        self.logger = logging.getLogger('bidmap')
        self.logger.setLevel(logging.DEBUG)

        fh = None
        for handler in self.logger.handlers:
            if isinstance(handler, logging.FileHandler):
                fh = handler

        if not fh:
            fh = logging.FileHandler(filename=logfile, mode='w')
            fh.setLevel(logging.DEBUG)

            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            fh.setFormatter(formatter)

            self.logger.addHandler(fh)
        
    def __str__(self):
        return '%s' % self.plugin

    def run(self):
        self.run_plugin()
        self.save_bids()

    def run_plugin(self):
        self.logger.info('running plugin %s' % self.plugin)

        bid_scraper = self.plugin.get_scraper()
#
# XXX Uncomment this once the code for determining the delta
#     of new bids to add / old bids to remove has been written
#
#        bid_scraper.reset_database_connection()
#
        try:
            bid_scraper.scrape_bids()
        except Exception, e:
            self.logger.warning('plugin %s generated exception: %s' % (self.plugin, e))
            self.logger.warning('%s' % traceback.format_exc())
            sys.stderr.write("Exception: %s\n" % e)
            sys.exc_clear()

    def save_bids(self):
        """
        Save bid results to disk. 
        """
        pass

if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.stderr.write('usage: %s <plugin>\n' % sys.argv[0])
        sys.exit(1)

    pldr = PluginLoader()
    plug = pldr.load_plugin(sys.argv[1])

    plugin_runner = PluginRunner(plugin=plug, results_dir='.')
    plugin_runner.run()
