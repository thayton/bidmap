import re, urlparse

from bid import Bid
from bidmap.bidscrapers.bidscraper import BidScraper
from bidmap.htmlparse.soupify import soupify

GOVINFO = {
    'name': 'Saint Marys Maryland',
    'location': 'Saint Marys, MD',

    'home_page_url': 'http://www.co.saint-marys.md.us',
    'bids_page_url': 'http://www.co.saint-marys.md.us/bids/openbids.asp'
}

class SaintMarysBidScraper(BidScraper):
    def __init__(self):
        super(SaintMarysBidScraper, self).__init__(GOVINFO)

    def scrape_bid_links(self, url):
        bids = []

        self.br.open(url)

        s = soupify(self.br.response().read())
        r = re.compile(r'^\s*Solicitation')
        f = lambda x: x.name == 'td' and re.search(r, x.text)

        for t in s.findAll(f):
            bid = Bid()
            bid.title = t.text
            bid.url = self.br.geturl()
            bids.append(bid)

        return bids

def get_scraper():
    return SaintMarysBidScraper()

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()
