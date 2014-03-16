import re, urlparse

from bid import Bid
from bidmap.bidscrapers.bidscraper import BidScraper
from bidmap.htmlparse.soupify import soupify

GOVINFO = {
    'name': 'Hapeville Geogia',
    'location': 'Hapeville, GA',

    'home_page_url': 'http://www.hapeville.org',
    'bids_page_url': 'http://www.hapeville.org/index.aspx?NID=360'
}

class HapevilleGaBidScraper(BidScraper):
    def __init__(self):
        super(HapevilleGaBidScraper, self).__init__(GOVINFO)

    def scrape_bid_links(self, url):
        bids = []

        self.br.open(url)

        s = soupify(self.br.response().read())
        r = re.compile(r'^/DocumentView\.aspx\?DID=\d+$')
        x = {'href': r, 'class': 'Hyperlink', 'title': True}

        for a in s.findAll('a', attrs=x):
            bid = Bid()
            bid.title = a['title']
            bid.url = urlparse.urljoin(self.br.geturl(), a['href'])
            bids.append(bid)

        return bids

def get_scraper():
    return HapevilleGaBidScraper()

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()
