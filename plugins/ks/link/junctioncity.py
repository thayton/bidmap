import re, urlparse

from bid import Bid
from bidmap.bidscrapers.bidscraper import BidScraper
from bidmap.htmlparse.soupify import soupify

GOVINFO = {
    'name': 'Junction City Kansas',
    'location': 'Junction City, KS',

    'home_page_url': 'http://www.junctioncity-ks.gov',
    'bids_page_url': 'http://www.junctioncity-ks.gov/bids.aspx'
}

class JunctionCityBidScraper(BidScraper):
    def __init__(self):
        super(JunctionCityBidScraper, self).__init__(GOVINFO)

    def scrape_bid_links(self, url):
        bids = []

        self.br.open(url)

        s = soupify(self.br.response().read())
        r = re.compile(r'^bidView\.aspx\?bid=\d+$')

        for a in s.findAll('a', href=r):
            bid = Bid()
            bid.title = a.text
            bid.url = urlparse.urljoin(self.br.geturl(), a['href'])
            bids.append(bid)

        return bids

def get_scraper():
    return JunctionCityBidScraper()

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()
