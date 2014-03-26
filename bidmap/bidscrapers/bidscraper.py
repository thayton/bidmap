import os
import sys
import logging

sys.path.append(os.path.realpath(os.path.join(os.path.dirname(__file__), '../../bidmap_django/')))
sys.path.append(os.path.realpath(os.path.join(os.path.dirname(__file__), '../../bidmap_django/bidmap_django/')))

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

from django import db 
from django.core.exceptions import ObjectDoesNotExist

from bidmap.browser.bidmap_browser import BidMapBrowser
from bidmapdb.models import *

class BidScraper(object):
    def __init__(self, govinfo=None):
        self.gov = govinfo
        self.br = BidMapBrowser()
        self.br.set_handle_robots(False)
        self.init_logger()

        if govinfo is not None:
            self.set_org(govinfo)
            self.logger.debug('Initialized scraper for organization %s' % self.org.name)
            self.logger.debug('%s currently has %d bids in database' % (self.org.name, self.org.bid_set.count()))

    def set_org(self, govinfo):
        try:
            org = Organization.objects.get(home_page_url=govinfo['home_page_url'])
        except ObjectDoesNotExist:
            org = Organization()

        org.name = govinfo['name']

        org.home_page_url = govinfo['home_page_url']
        org.bids_page_url = govinfo['bids_page_url']

        city,state = govinfo['location'].split(',')
        city = city.lower().strip()
        state = state.lower().strip()

        try:
            location = Location.objects.get(city=city, state=state, country='us')
        except ObjectDoesNotExist:
            location = Location(city=city, state=state, country='us')
            location.save()

        org.location = location
        org.save()

        self.org = org

    def class_name(self):
        ''' For logging purposes '''
        return '%s' % type(self).__name__

    def reset_database_connection(self):
        db.close_connection()

    def init_logger(self):
        self.logger = logging.getLogger('bidmap.BidScraper.%s' % self.class_name())
        self.logger.setLevel(logging.DEBUG)

        sh = None
        for handler in self.logger.handlers:
            if isinstance(handler, logging.StreamHandler):
                sh = handler

        if not sh:
            sh = logging.StreamHandler()
            sh.setLevel(logging.DEBUG)        

            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            sh.setFormatter(formatter)

            self.logger.addHandler(sh)
        
    def scrape_bid_links(self, url):
        ''' Derived class should override this method with
        scraping routine specific to each site '''
        pass

    def prune_unlisted_bids(self, bid_list):
        ''' Remvoe bids from the database that are no longer 
        listed on the site '''
        pass

    def new_bids(self, bid_list):
        ''' Determine which bids on site are new when 
        compared to the database of bids already downloaded'''
        return bid_list

    def scrape_bids(self):
        ''' Derived class should override this method with
        scraping routine specific to each site '''
        bid_list = self.scrape_bid_links(self.gov['bids_page_url'])
        self.prune_unlisted_bids(bid_list)
        new_bids = self.new_bids(bid_list)
        for bid in new_bids:
            self.logger.debug('%s' % bid)


