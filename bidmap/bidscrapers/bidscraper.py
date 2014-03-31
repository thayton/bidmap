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
        city = city.strip()
        state = state.strip()

        try:
            location = Location.objects.get(city=city, state=state, country='US')
        except ObjectDoesNotExist:
            location = Location(city=city, state=state, country='US')
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

    def get_bid_cmp(self):
        """
        Bid comparison function to be used when comparing whether two bids are
        equivalent. The default is to assume that if the url/data fields of two
        bids objects are equivalent then the two bids are the same. 

        Inherited classes may override this field for more complex comparison 
        operations.
        """
        return lambda x,y: x.url == y.url and x.url_data == y.url_data

    def prune_unlisted_bids(self, listed_bids, use_bid_cmp=False):
        """
        Remove dead bids from the database - these are bids whose links 
        are in the  database that are no longer listed on the government
        bids site.
        
        Callers can set use_bid_cmp=True and then define get_bid_cmp()
        to return a comparison function of their choosing if the url,url_data
        comparison used here does not suffice.
        """
        num_deleted = 0

        if use_bid_cmp:
            cmp = self.get_bid_cmp()

            for bid in self.org.bid_set.all():
                if not find(cmp, bid, listed_bids):
                    self.logger.debug('Deleting bid (%s) for org %s' % (bid.url, self.org))
                    bid.delete()
                    num_deleted += 1
        else:
            stored_bids_set = set([('%s' % j.url, '%s' % j.url_data) for j in self.org.bid_set.all()])
            listed_bids_set = set([('%s' % j.url, '%s' % j.url_data) for j in listed_bids])

            bids_to_delete = stored_bids_set - listed_bids_set

            self.logger.info('%d bids to delete' % len(bids_to_delete))

            for entry in bids_to_delete:
                for bid in self.org.bid_set.filter(url=entry[0], url_data=entry[1]):
                    self.logger.debug('Deleting bid (%s) for org %s' % (bid.url, self.org))
                    bid.delete()
                    num_deleted += 1

        self.logger.info('Deleted %d unlisted bids' % num_deleted)

    def new_bids(self, listed_bids, use_bid_cmp=False):
        ''' 
        Determine which bids on site are new when compared to the database of bids 
        already downloaded

        Callers can set use_bid_cmp=True and then define get_bid_cmp() to return a 
        comparison function of their choosing if the url,url_data comparison used 
        here does not suffice.
        '''
        self.logger.debug('Extracting new bids from %d bids listed' % len(listed_bids))
        new_bids = []

        if use_bid_cmp:
            cmp = self.get_bid_cmp()

            for bid in listed_bids:
                if not find(cmp, bid, self.org.bid_set.all()) and \
                   not find(cmp, bid, new_bids): # don't allow dups in new_bids
                    self.logger.debug('New bid (%s) at org %s' % (bid.url, self.org))
                    new_bids.append(bid)
        else:
            for bid in listed_bids:
                if self.org.bid_set.filter(url=bid.url, url_data=bid.url_data).count() == 0:
                    self.logger.debug('New bid (%s) at org %s' % (bid.url, self.org))
                    new_bids.append(bid)

        self.logger.info('%d new bid listings' % len(new_bids))            
        return new_bids

    def scrape_bid_description(self, bid):
        '''
        Derived class should override this method with routine
        to scrape the bid contents for the links scraped in
        scrape_bid_links method
        '''
        self.logger.debug('%s' % bid)

    def scrape_bids(self):
        ''' Derived class should override this method with
        scraping routine specific to each site '''
        bid_list = self.scrape_bid_links(self.gov['bids_page_url'])
        self.prune_unlisted_bids(bid_list)
        new_bids = self.new_bids(bid_list)
        for bid in new_bids:
            self.scrape_bid_description(bid)
