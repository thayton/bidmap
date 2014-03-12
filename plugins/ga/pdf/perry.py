import re, urlparse

from bid import Bid
from bidmap.bidscrapers.bidscraper import BidScraper
from bidmap.htmlparse.soupify import soupify

GOVINFO = {
    'name': 'Perry Geogia',
    'location': 'Perry, GA',

    'home_page_url': 'http://www.perry-ga.gov',
    'bids_page_url': 'http://www.perry-ga.gov/bids.php'
}

class PerryGaBidScraper(BidScraper):
    def __init__(self):
        super(PerryGaBidScraper, self).__init__(GOVINFO)

    def scrape_bid_links(self, url):
        bids = []

        self.br.open(url)

        s = soupify(self.br.response().read())
        r = re.compile(r'Bid[^.]+\.pdf$')

        for a in s.findAll('a', href=r):
            bid = Bid()
            bid.title = a.text
            bid.url = urlparse.urljoin(self.br.geturl(), a['href'])
            bids.append(bid)

        return bids

def get_scraper():
    return PerryGaBidScraper()

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()
