import re, urlparse

from bidmap.bidscrapers.pdfscraper.pdfscraper import PdfBidScraper
from bidmap.htmlparse.soupify import soupify

from bidmapdb.models import *

GOVINFO = {
    'name': 'Kent County Public Schools',
    'location': 'Rock Hall, MD',

    'home_page_url': 'http://www.kent.k12.md.us',
    'bids_page_url': 'http://www.kent.k12.md.us/index.php/requests-for-bids'
}

class KentBidScraper(BidScraper):
    def __init__(self):
        super(KentBidScraper, self).__init__(GOVINFO)

    def scrape_bid_links(self, url):
        bids = []

        self.br.open(url)

        s = soupify(self.br.response().read())
        r = re.compile(r'\.pdf$')
        x = {'href': r, 'class': 'at_url'}

        for a in s.findAll('a', attrs=x):
            if len(a.text) == 0:
                continue

            bid = Bid(org=self.org)
            bid.title = a.text
            bid.url = urlparse.urljoin(self.br.geturl(), a['href'])
            bid.location = self.org.location
            bids.append(bid)

        return bids

def get_scraper():
    return KentBidScraper()

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()
