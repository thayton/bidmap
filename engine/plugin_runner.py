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
from serialize import serialize_org

sys.path.append(os.path.realpath(os.path.join(os.path.dirname(__file__), '../bidmap_django/')))
sys.path.append(os.path.realpath(os.path.join(os.path.dirname(__file__), '../bidmap_django/bidmap_django/')))

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

from django.core.exceptions import ObjectDoesNotExist
from bidmapdb.models import *

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
        bid_scraper.reset_database_connection()

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
        try:
            org = Organization.objects.get(home_page_url=self.plugin.GOVINFO['home_page_url'])
        except ObjectDoesNotExist:
            return

        file = self.make_plugin_filename()
        path = '%s/%s.json' % (self.results_dir, file)

        try:
            so = serialize_org(org)

            f = open(path, 'w')
            f.write(json.dumps(so, indent=2))
            f.close()
        except Exception, e:
            sys.stderr.write("Exception: %s\n" % e)
            sys.exc_clear()

        num_bids = org.bid_set.count()
        self.logger.info('Saved %d bids for org %s to file %s' % (num_bids, org.name, path))

    def make_plugin_filename(self):
        """
        Return the filename we'll use to store results for a given plugin.
        """
        netloc = urlparse(self.plugin.GOVINFO['home_page_url']).netloc
        tld = netloc.rsplit('.', 1)[1]

        filename = tld + '-' + self.plugin.__name__
        return filename

if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.stderr.write('usage: %s <plugin>\n' % sys.argv[0])
        sys.exit(1)

    pldr = PluginLoader()
    plug = pldr.load_plugin(sys.argv[1])

    plugin_runner = PluginRunner(plugin=plug, results_dir='results/')
    plugin_runner.run()
