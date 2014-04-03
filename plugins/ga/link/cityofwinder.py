import re, urlparse

from bidmap.bidscrapers.bidscraper import BidScraper
from bidmap.htmlparse.soupify import soupify, get_all_text

from bidmapdb.models import *

GOVINFO = {
    'name': 'Winder Geogia',
    'location': 'Winder, GA',

    'home_page_url': 'http://www.cityofwinder.com',
    'bids_page_url': 'http://www.cityofwinder.com/index.aspx?page=245'
}

class WinderGaBidScraper(BidScraper):
    def __init__(self):
        super(WinderGaBidScraper, self).__init__(GOVINFO)

    def scrape_bid_links(self, url):
        bids = []

        self.br.open(url)

        s = soupify(self.br.response().read())
        r = re.compile(r'^_ctl\d+_listDataGrid$')
        t = s.find('table', id=r)
        r = re.compile(r'^index\.aspx\?recordid=\d+')

        for a in t.findAll('a', href=r):
            bid = Bid(org=self.org)
            bid.title = a.text
            bid.url = urlparse.urljoin(self.br.geturl(), a['href'])
            bid.location = self.org.location
            bids.append(bid)

        return bids

def get_scraper():
    return WinderGaBidScraper()

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()
