#!/usr/bin/env python

"""
Engine for running multiple bid scraping plugins at the same time.
"""

import urlparse
import logging
import random

from plugin_runner import PluginRunner
from task_manager import TaskManager
from plugin_loader import PluginLoader

class BidScraperEngine(TaskManager):
    def __init__(self, plugin_dir, results_dir, logfile='/var/log/bidmap/bid_scraper_engine.log'):
        self.plugin_dir = plugin_dir
        self.results_dir = results_dir
        self.logfile = logfile
        self.plugins = []
        self.pldr = PluginLoader()

        self.logger = logging.getLogger('bidmap')
        self.logger.setLevel(logging.DEBUG)

        fh = logging.FileHandler(filename=logfile, mode='w')
        fh.setLevel(logging.DEBUG)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)

        self.logger.addHandler(fh)

        super(BidScraperEngine, self).__init__()

    def load_plugins(self):
        self.pldr.load_plugins([self.plugin_dir])
        random.shuffle(self.pldr.plugins)

        tasks = [PluginRunner(plugin=p, results_dir=self.results_dir, logfile=self.logfile) for p in self.pldr.plugins]
        self.set_task_list(tasks=tasks)

        self.logger.info('loaded %d plugins' % len(self.pldr.plugins))

    def task_launched(self, task, pid):
        self.logger.info('Task %d for plugin %s launched' % (int(pid), task.plugin))

    def task_completed(self, task, pid):
        self.logger.info('Task %d for plugin %s completed' % (int(pid), task.plugin))

if __name__ == '__main__':
    engine = BidScraperEngine(plugin_dir='../plugins/ga/', results_dir='results/')
    engine.load_plugins()
    engine.run()

