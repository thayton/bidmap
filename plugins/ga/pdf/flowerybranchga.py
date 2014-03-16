import re, urlparse

from bid import Bid
from bidmap.bidscrapers.bidscraper import BidScraper
from bidmap.htmlparse.soupify import soupify

GOVINFO = {
    'name': 'Flowery Branch Geogia',
    'location': 'Flowery Branch, GA',

    'home_page_url': 'http://www.flowerybranchga.org',
    'bids_page_url': 'http://www.flowerybranchga.org/RFPs.html'
}

class FloweryBranchGaBidScraper(BidScraper):
    def __init__(self):
        super(FloweryBranchGaBidScraper, self).__init__(GOVINFO)

    def scrape_bid_links(self, url):
        bids = []

        self.br.open(url)

        s = soupify(self.br.response().read())
        r = re.compile(r'\.pdf$')

        for a in s.findAll('a', href=r):
            bid = Bid()
            bid.title = a.text
            bid.url = urlparse.urljoin(self.br.geturl(), a['href'])
            bids.append(bid)

        return bids

def get_scraper():
    return FloweryBranchGaBidScraper()

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()
