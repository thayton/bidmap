import re, urlparse

from bidmap.bidscrapers.pdfscraper.pdfscraper import PdfBidScraper
from bidmap.htmlparse.soupify import soupify

from bidmapdb.models import *

GOVINFO = {
    'name': 'Thomson Geogia',
    'location': 'Thomson, GA',

    'home_page_url': 'http://www.thomson-mcduffie.com',
    'bids_page_url': 'http://www.thomson-mcduffie.com/citycounty/business-development/bids-procurement'
}

class ThomsonGaBidScraper(PdfBidScraper):
    def __init__(self):
        super(ThomsonGaBidScraper, self).__init__(GOVINFO)

    def scrape_bid_links(self, url):
        bids = []

        self.br.open(url)

        s = soupify(self.br.response().read())
        r = re.compile(r'/bids_procurement/[^.]+\.pdf$')

        for a in s.findAll('a', href=r):
            bid = Bid(org=self.org)
            bid.title = a.text
            bid.url = urlparse.urljoin(self.br.geturl(), a['href'])
            bid.location = self.org.location
            bids.append(bid)

        return bids

def get_scraper():
    return ThomsonGaBidScraper()

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()
