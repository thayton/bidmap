#!/usr/bin/env python

import os
import re
import sys
import imp
import logging

from urlparse import urlparse

class FileFilter:
    """
    Class for recursively loading a list of files, filtered by their extension, from a given a directory
    """
    def __init__(self):
        pass

    def get_files(self, directory, ext):
        """ 
        Recursively descend into a directory and
        return all plugin files found 
        """
        def is_notdir(f):
            return os.path.isdir(f) is False

        def is_plugin(f):
            return os.path.splitext(f)[1] == ext

        dirents = [ os.path.join(directory, f) for f in os.listdir(directory) ]

        ret = filter(is_notdir, dirents)
        ret = filter(is_plugin, ret)

        for d in filter(os.path.isdir, dirents):
            ret.extend(self.get_files(d, '.py'))

        return ret

class PluginLoader:
    """
    Class for loading bid scraping plugins. 
    """
    def __init__(self):
        self.plugins = []
        self.file_filter = FileFilter()
        self.logger = logging.getLogger('bidmap.PluginLoader')
        self.logger.setLevel(logging.DEBUG)

    def load_plugins(self, dirlist, exclude=[]):
        """
        Load plugins from files unless they are in the exclude list
        """
        for directory in dirlist:
            files = self.file_filter.get_files(directory, '.py')
            for f in files:
                plug = self.load_plugin(f)
                if self.plug_name(plug) not in exclude:
                    #
                    # Plugin can mark itself to be skipped by setting
                    # the 'skip' attribute. 
                    #
                    if getattr(plug, 'skip', None) != None:
                        continue

                    self.plugins.append(plug)

    def load_plugin(self, path):
        modname = os.path.splitext(os.path.basename(path))[0]
        try:
            mod = imp.load_source(modname, path)
            return mod
        except ImportError, e:
            self.logger.error("load_plugin failed - error:", e)
    
    def get_plugin(self, site):
        """ Return the plugin used for scraping bids from the given site """
        for plugin in self.plugins:
            if site == plugin.__name__:
                return plugin
            
        return None

    def plug_name(self, plug_module):
        netloc = urlparse(plug_module.GOVINFO['home_page_url']).netloc
        tld = netloc.rsplit('.', 1)[1]

        name = tld + '-' + plug_module.__name__
        return name
        

if __name__ == '__main__':
    pldr = PluginLoader()
    pldr.load_plugins(['../plugins/ga/'])

    plug = pldr.get_plugin('cityofcovington')

    bid_scraper = plug.get_scraper()
    bid_scraper.scrape_bids()

