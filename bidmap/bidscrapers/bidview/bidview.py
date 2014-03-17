import re, urlparse

from bid import Bid
from bidmap.bidscrapers.bidscraper import BidScraper
from bidmap.htmlparse.soupify import soupify

class BidViewBidScraper(BidScraper):
    def __init__(self):
        super(BidViewBidScraper, self).__init__(govinfo)
        self.gov = govinfo

    def scrape_bid_links(self, url):
        bids = []

        self.br.open(url)

        s = soupify(self.br.response().read())
        r = re.compile(r'^bidView\.aspx\?bid=\d+$')

        for a in s.findAll('a', href=r):
            bid = Bid()
            bid.title = a.text
            bid.url = urlparse.urljoin(self.br.geturl(), a['href'])
            bids.append(bid)

        return bids
