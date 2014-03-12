import re, urlparse

from bid import Bid
from bidmap.bidscrapers.bidscraper import BidScraper
from bidmap.htmlparse.soupify import soupify

GOVINFO = {
    'name': 'Gainesville Geogia',
    'location': 'Gainesville, GA',

    'home_page_url': 'http://www.gainesville.org',
    'bids_page_url': 'http://www.gainesville.org/purchasing/'
}

class GainesvilleGaBidScraper(BidScraper):
    def __init__(self):
        super(GainesvilleGaBidScraper, self).__init__(GOVINFO)

    def scrape_bid_links(self, url):
        bids = []

        self.br.open(url)

        s = soupify(self.br.response().read())
        t = s.find('table', id='jobs-table')

        r1 = re.compile(r'rfp-\d+-[^.]+\.pdf$')
        r2 = re.compile(r'^RFP #\d+')

        f = lambda x: x.name == 'a' and re.search(r1, x.get('href', '')) and re.search(r2, x.text)

        for a in t.findAll(f):
            bid = Bid()
            bid.title = a.text
            bid.url = urlparse.urljoin(self.br.geturl(), a['href'])
            bids.append(bid)

        return bids

def get_scraper():
    return GainesvilleGaBidScraper()

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()
