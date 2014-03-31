import re, urlparse

from bidmap.bidscrapers.bidscraper import BidScraper
from bidmap.htmlparse.soupify import soupify, get_all_text

from bidmapdb.models import *

class BidViewBidScraper(BidScraper):
    def __init__(self, govinfo):
        super(BidViewBidScraper, self).__init__(govinfo)
        self.gov = govinfo

    def scrape_bid_links(self, url):
        bids = []

        self.br.open(url)

        s = soupify(self.br.response().read())
        r = re.compile(r'^bidView\.aspx\?bid=\d+$')

        for a in s.findAll('a', href=r):
            bid = Bid(org=self.org)
            bid.title = a.text
            bid.url = urlparse.urljoin(self.br.geturl(), a['href'])
            bid.location = self.org.location
            bids.append(bid)

        return bids

    def scrape_bid_description(self, bid):
        self.br.open(bid.url)

        s = soupify(self.br.response().read())
        x = {'class': 'bidViewResultsLeft'}
        t = s.find('td', attrs=x)

        bid.description = get_all_text(t)
        bid.save()

