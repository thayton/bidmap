import re, urlparse

from bid import Bid
from bidmap.bidscrapers.bidscraper import BidScraper
from bidmap.htmlparse.soupify import soupify

GOVINFO = {
    'name': 'Mcrae Geogia',
    'location': 'Mcrae, GA',

    'home_page_url': 'http://www.mcraega.org',
    'bids_page_url': 'http://www.mcraega.org/bid-invitations.html'
}

class McraeGaBidScraper(BidScraper):
    def __init__(self):
        super(McraeGaBidScraper, self).__init__(GOVINFO)

    def scrape_bid_links(self, url):
        bids = []

        self.br.open(url)

        s = soupify(self.br.response().read())
        r = re.compile(r'\.doc$')

        for a in s.findAll('a', href=r):
            if len(a.text) == 0:
                continue

            bid = Bid()
            bid.title = a.text
            bid.url = urlparse.urljoin(self.br.geturl(), a['href'])
            bids.append(bid)

        return bids

def get_scraper():
    return McraeGaBidScraper()

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()
