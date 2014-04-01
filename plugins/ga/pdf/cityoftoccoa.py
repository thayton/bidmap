import re, urlparse

from bidmap.bidscrapers.pdfscraper.pdfscraper import PdfBidScraper
from bidmap.htmlparse.soupify import soupify

from bidmapdb.models import *

GOVINFO = {
    'name': 'Toccoa Geogia',
    'location': 'Toccoa, GA',

    'home_page_url': 'http://www.cityoftoccoa.com',
    'bids_page_url': 'http://www.cityoftoccoa.com/bidops.cfm?lid=4121'
}

class ToccoaGaBidScraper(PdfBidScraper):
    def __init__(self):
        super(ToccoaGaBidScraper, self).__init__(GOVINFO)

    def scrape_bid_links(self, url):
        bids = []

        self.br.open(url)

        s = soupify(self.br.response().read())
        r = re.compile(r'/BidSpecs/[^.]+\.pdf$')

        for a in s.findAll('a', href=r):
            g = a.findPrevious('strong')
            bid = Bid(org=self.org)
            bid.title = g.text
            bid.url = urlparse.urljoin(self.br.geturl(), a['href'])
            bid.location = self.org.location
            bids.append(bid)

        return bids

def get_scraper():
    return ToccoaGaBidScraper()

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()
