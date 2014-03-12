import re, urlparse

from bid import Bid
from bidmap.bidscrapers.bidscraper import BidScraper
from bidmap.htmlparse.soupify import soupify

GOVINFO = {
    'name': 'Johns Creek Geogia',
    'location': 'Johns Creek, GA',

    'home_page_url': 'http://www.johnscreekga.gov',
    'bids_page_url': 'http://www.johnscreekga.gov/services/purchasing.aspx'
}

class JohnsCreekGaBidScraper(BidScraper):
    def __init__(self):
        super(JohnsCreekGaBidScraper, self).__init__(GOVINFO)

    def scrape_bid_links(self, url):
        bids = []

        self.br.open(url)

        s = soupify(self.br.response().read())
        r = re.compile(r'RFQ-\d+-\d+_bid+\.pdf$')

        for a in s.findAll('a', href=r):
            h3 = a.findPrevious('h3')
            bid = Bid()
            bid.title = h3.text
            bid.url = urlparse.urljoin(self.br.geturl(), a['href'])
            bids.append(bid)

        return bids

def get_scraper():
    return JohnsCreekGaBidScraper()

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()
