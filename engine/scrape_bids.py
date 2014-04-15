#!/usr/bin/env python

import os, sys, mechanize, logging, glob
from bid_scraper_engine import BidScraperEngine

if __name__ == '__main__':
    if len(sys.argv) != 3:
        sys.stderr.write('usage: %s <plugins-dir> <results-dir>\n' % sys.argv[0])
        sys.exit(1)

    engine = BidScraperEngine(plugin_dir=sys.argv[1], results_dir=sys.argv[2])
    engine.load_plugins()
    engine.run()
