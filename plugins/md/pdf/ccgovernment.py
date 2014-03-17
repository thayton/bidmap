import re, urlparse

from bid import Bid
from bidmap.bidscrapers.bidscraper import BidScraper
from bidmap.htmlparse.soupify import soupify

GOVINFO = {
    'name': 'Carroll County Maryland',
    'location': 'Carroll County, MD',

    'home_page_url': 'http://ccgovernment.carr.org',
    'bids_page_url': 'http://ccgovernment.carr.org/ccg/bidnotce/'
}

class CarrollCountyBidScraper(BidScraper):
    def __init__(self):
        super(CarrollCountyBidScraper, self).__init__(GOVINFO)

    def scrape_bid_links(self, url):
        bids = []

        self.br.open(url)

        s = soupify(self.br.response().read())
        r = re.compile(r'\.pdf$')
        x = {'action': r}

        for f in s.findAll('form', attrs=x):
            b = f.findPrevious(text='Bid Number:')
            t = b.findPrevious('br').previous

            bid = Bid()
            bid.title = t
            bid.url = urlparse.urljoin(self.br.geturl(), f['action'])
            bids.append(bid)

        return bids

def get_scraper():
    return CarrollCountyBidScraper()

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()
