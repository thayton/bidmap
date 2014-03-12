import re, urlparse

from bid import Bid
from bidmap.bidscrapers.bidscraper import BidScraper
from bidmap.htmlparse.soupify import soupify

GOVINFO = {
    'name': 'Forest Park Geogia',
    'location': 'Forest Park, GA',

    'home_page_url': 'http://www.forestparkga.org',
    'bids_page_url': 'http://www.forestparkga.org/request-for-proposals.aspx'
}

class ForestParkGaBidScraper(BidScraper):
    def __init__(self):
        super(ForestParkGaBidScraper, self).__init__(GOVINFO)

    def scrape_bid_links(self, url):
        bids = []

        self.br.open(url)

        s = soupify(self.br.response().read())
        r = re.compile(r'\.pdf$')
        f = lambda x: x.name == 'a' and re.search(r, x.get('href', '')) and x.text == 'Download RFP'

        for a in s.findAll(f):
            p = a.parent
            bid = Bid()
            bid.title = p.strong.text
            bid.url = urlparse.urljoin(self.br.geturl(), a['href'])
            bids.append(bid)

        return bids

def get_scraper():
    return ForestParkGaBidScraper()

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()
