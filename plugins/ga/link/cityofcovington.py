import re, urlparse

from bid import Bid
from bidmap.bidscrapers.bidscraper import BidScraper
from bidmap.htmlparse.soupify import soupify

GOVINFO = {
    'name': 'Covington Geogia',
    'location': 'Covington, GA',

    'home_page_url': 'http://www.cityofcovington.org',
    'bids_page_url': 'http://www.cityofcovington.org/Business/Bids/Pages/Current-Bid-Postings.aspx'
}

class CovingtonGaBidScraper(BidScraper):
    def __init__(self):
        super(CovingtonGaBidScraper, self).__init__(GOVINFO)

    def scrape_bid_links(self, url):
        bids = []

        self.br.open(url)

        s = soupify(self.br.response().read())
        x = {'summary': 'Current Bid Postings '}
        t = s.find('table', attrs=x)
        r = re.compile(r'/Bids/')

        for a in t.findAll('a', href=r):
            bid = Bid()
            bid.title = a.text
            bid.url = urlparse.urljoin(self.br.geturl(), a['href'])
            bids.append(bid)

        return bids

def get_scraper():
    return CovingtonGaBidScraper()

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()
