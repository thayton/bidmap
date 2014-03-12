import re, urlparse

from bid import Bid
from bidmap.bidscrapers.bidscraper import BidScraper
from bidmap.htmlparse.soupify import soupify

GOVINFO = {
    'name': 'Bainbridge Geogia',
    'location': 'Bainbridge, GA',

    'home_page_url': 'http://www.bainbridgecity.com',
    'bids_page_url': 'http://www.bainbridgecity.com/egov/apps/document/center.egov?path=browse&id=9'
}

class BainbridgeGaBidScraper(BidScraper):
    def __init__(self):
        super(BainbridgeGaBidScraper, self).__init__(GOVINFO)

    def scrape_bid_links(self, url):
        bids = []

        self.br.open(url)

        s = soupify(self.br.response().read())
        r = re.compile(r'center\.egov\?path=doc&id=\d+&id2=\d+&linked=0')

        for a in s.findAll('a', href=r):
            if len(a.text) == 0:
                continue

            bid = Bid()
            bid.title = a.text
            bid.url = urlparse.urljoin(self.br.geturl(), a['href'])
            bids.append(bid)

        return bids

def get_scraper():
    return BainbridgeGaBidScraper()

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()
