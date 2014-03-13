import re, urlparse

from bid import Bid
from bidmap.bidscrapers.bidscraper import BidScraper
from bidmap.htmlparse.soupify import soupify

GOVINFO = {
    'name': 'Jesup Geogia',
    'location': 'Jesup, GA',

    'home_page_url': 'http://www.jesupga.gov',
    'bids_page_url': 'http://www.jesupga.gov/bids.html'
}

class JesupGaBidScraper(BidScraper):
    def __init__(self):
        super(JesupGaBidScraper, self).__init__(GOVINFO)

    def scrape_bid_links(self, url):
        bids = []

        self.br.open(url)

        s = soupify(self.br.response().read())
        d = s.find('div', id='mainContent')
        r = re.compile(r'\.pdf$')

        for a in d.findAll('a', href=r):
            bid = Bid()
            bid.title = a.text
            bid.url = urlparse.urljoin(self.br.geturl(), a['href'])
            bids.append(bid)

        return bids

def get_scraper():
    return JesupGaBidScraper()

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()
