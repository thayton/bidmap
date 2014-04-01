import re, urlparse

from bidmap.bidscrapers.pdfscraper.pdfscraper import PdfBidScraper
from bidmap.htmlparse.soupify import soupify

from bidmapdb.models import *

GOVINFO = {
    'name': 'Kennesaw Geogia',
    'location': 'Kennesaw, GA',

    'home_page_url': 'http://www.kennesaw-ga.gov',
    'bids_page_url': 'http://www.kennesaw-ga.gov/business/doing-business/bids-a-rfps'
}

class KennesawGaBidScraper(PdfBidScraper):
    def __init__(self):
        super(KennesawGaBidScraper, self).__init__(GOVINFO)

    def scrape_bid_links(self, url):
        bids = []

        self.br.open(url)

        s = soupify(self.br.response().read())
        r = re.compile(r'\.pdf$')

        for a in s.findAll('a', href=r):
            bid = Bid(org=self.org)
            bid.title = a.text
            bid.url = urlparse.urljoin(self.br.geturl(), a['href'])
            bid.location = self.org.location
            bids.append(bid)

        return bids

def get_scraper():
    return KennesawGaBidScraper()

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()
