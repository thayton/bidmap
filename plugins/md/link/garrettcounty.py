import re, urlparse

from bid import Bid
from bidmap.bidscrapers.bidscraper import BidScraper
from bidmap.htmlparse.soupify import soupify

GOVINFO = {
    'name': 'Garrett County Maryland',
    'location': 'Oakland, MD',

    'home_page_url': 'http://garrettcounty.org',
    'bids_page_url': 'http://garrettcounty.org/purchasing/current-bids'
}

class GarrettCountyBidScraper(BidScraper):
    def __init__(self):
        super(GarrettCountyBidScraper, self).__init__(GOVINFO)

    def scrape_bid_links(self, url):
        bids = []

        self.br.open(url)

        s = soupify(self.br.response().read())
        r = re.compile(r'^/purchasing/bid-form\?bidnumb=\d+')

        for a in s.findAll('a', href=r):
            bid = Bid()
            bid.title = a.text
            bid.url = urlparse.urljoin(self.br.geturl(), a['href'])
            bids.append(bid)

        return bids

def get_scraper():
    return GarrettCountyBidScraper()

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()
