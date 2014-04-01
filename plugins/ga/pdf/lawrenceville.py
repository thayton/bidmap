import re, urlparse

from bidmap.bidscrapers.pdfscraper.pdfscraper import PdfBidScraper
from bidmap.htmlparse.soupify import soupify

from bidmapdb.models import *

GOVINFO = {
    'name': 'Lawrenceville Geogia',
    'location': 'Lawrenceville, GA',

    'home_page_url': 'http://www.lawrencevillega.org',
    'bids_page_url': 'http://www.lawrencevillega.org/government/special-notices/'
}

class LawrencevilleGaBidScraper(PdfBidScraper):
    def __init__(self):
        super(LawrencevilleGaBidScraper, self).__init__(GOVINFO)

    def scrape_bid_links(self, url):
        bids = []

        self.br.open(url)

        s = soupify(self.br.response().read())
        r = re.compile(r'\.pdf$')
        f = lambda x: x.name == 'a' and re.search(r, x.get('href', '')) and x.text == 'click here'

        for a in s.findAll(f):
            t = a.findPrevious('strong')
            bid = Bid(org=self.org)
            bid.title = t.text
            bid.url = urlparse.urljoin(self.br.geturl(), a['href'])
            bid.location = self.org.location
            bids.append(bid)

        return bids

def get_scraper():
    return LawrencevilleGaBidScraper()

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()
