import re, urlparse

from bidmap.bidscrapers.bidscraper import BidScraper
from bidmap.htmlparse.soupify import soupify

from bidmapdb.models import *

GOVINFO = {
    'name': 'Decatur Geogia',
    'location': 'Decatur, GA',

    'home_page_url': 'http://www.decaturga.com',
    'bids_page_url': 'http://www.decaturga.com/index.aspx?page=186'
}

class DecaturGaBidScraper(BidScraper):
    def __init__(self):
        super(DecaturGaBidScraper, self).__init__(GOVINFO)

    def scrape_bid_links(self, url):
        bids = []

        self.br.open(url)

        s = soupify(self.br.response().read())
        r = re.compile(r'ShowDocument\.aspx\?documentid=\d+$')

        for a in s.findAll('a', href=r):
            bid = Bid(org=self.org)
            bid.title = a.text
            bid.url = urlparse.urljoin(self.br.geturl(), a['href'])
            bid.location = self.org.location
            bids.append(bid)

        return bids

def get_scraper():
    return DecaturGaBidScraper()

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()
