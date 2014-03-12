import re, urlparse

from bid import Bid
from bidmap.bidscrapers.bidscraper import BidScraper
from bidmap.htmlparse.soupify import soupify

GOVINFO = {
    'name': 'Gaithersburg Maryland',
    'location': 'Gaithersburg, MD',

    'home_page_url': 'http://www.gaithersburgmd.gov',
    'bids_page_url': 'http://www.gaithersburgmd.gov/poi/default.asp?POI_ID=210'
}

class GaithersburgBidScraper(BidScraper):
    def __init__(self):
        super(GaithersburgBidScraper, self).__init__(GOVINFO)

    def scrape_bid_links(self, url):
        bids = []

        self.br.open(url)

        s = soupify(self.br.response().read())
        r = re.compile(r'^/poi/default\.asp\?POI_ID=\d+&TOC=\d+')
        x = {'type': 'disc'}
        u = s.find('ul', attrs=x)

        for a in u.findAll('a', href=r):
            bid = Bid()
            bid.title = a.text
            bid.url = urlparse.urljoin(self.br.geturl(), a['href'])
            bids.append(bid)

        return bids

def get_scraper():
    return GaithersburgBidScraper()

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()
