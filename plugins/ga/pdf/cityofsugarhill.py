import re, urlparse

from bid import Bid
from bidmap.bidscrapers.bidscraper import BidScraper
from bidmap.htmlparse.soupify import soupify

GOVINFO = {
    'name': 'Sugarhill Geogia',
    'location': 'Sugarhill, GA',

    'home_page_url': 'http://www.cityofsugarhill.com',
    'bids_page_url': 'http://www.cityofsugarhill.com/content/11595/12079/default.aspx'
}

class SugarhillGaBidScraper(BidScraper):
    def __init__(self):
        super(SugarhillGaBidScraper, self).__init__(GOVINFO)

    def scrape_bid_links(self, url):
        bids = []

        self.br.open(url)

        s = soupify(self.br.response().read())
        r = re.compile(r'RFP[^.]+\.pdf$')

        for a in s.findAll('a', href=r):
            bid = Bid()
            bid.title = a.text
            bid.url = urlparse.urljoin(self.br.geturl(), a['href'])
            bids.append(bid)

        return bids

def get_scraper():
    return SugarhillGaBidScraper()

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()
