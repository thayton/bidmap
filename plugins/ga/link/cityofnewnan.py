import re, urlparse

from bidmap.bidscrapers.bidscraper import BidScraper
from bidmap.htmlparse.soupify import soupify

from bidmapdb.models import *

GOVINFO = {
    'name': 'Newnan Geogia',
    'location': 'Newnan, GA',

    'home_page_url': 'http://www.cityofnewnan.org',
    'bids_page_url': 'http://www.cityofnewnan.org/current_open_bids.php'
}

class NewnanGaBidScraper(BidScraper):
    def __init__(self):
        super(NewnanGaBidScraper, self).__init__(GOVINFO)

    def scrape_bid_links(self, url):
        bids = []

        self.br.open(url)

        s = soupify(self.br.response().read())
        ul = s.find('ul', id='toplevel')

        for a in ul.findAll('a'):
            bid = Bid(org=self.org)
            bid.title = a.text
            bid.url = urlparse.urljoin(self.br.geturl(), a['href'])
            bid.location = self.org.location
            bids.append(bid)

        return bids

def get_scraper():
    return NewnanGaBidScraper()

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()
