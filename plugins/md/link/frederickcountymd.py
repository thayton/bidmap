import re, urlparse

from bid import Bid
from bidmap.bidscrapers.bidscraper import BidScraper
from bidmap.htmlparse.soupify import soupify

GOVINFO = {
    'name': 'Frederick County Maryland',
    'location': 'Frederick, MD',

    'home_page_url': 'https://frederickcountymd.gov',
    'bids_page_url': 'https://frederickcountymd.gov/index.aspx?NID=1116'
}

class FrederickCountyBidScraper(BidScraper):
    def __init__(self):
        super(FrederickCountyBidScraper, self).__init__(GOVINFO)

    def scrape_bid_links(self, url):
        bids = []

        self.br.open(url)

        s = soupify(self.br.response().read())
        f = lambda x: x.name == 'a' and x.text == 'Invitation for Bid' or x.text == 'Summary'

        for a in s.findAll(f):
            t = a.previousSibling.previousSibling.previousSibling
            bid = Bid()
            bid.title = t
            bid.url = urlparse.urljoin(self.br.geturl(), a['href'])
            bids.append(bid)

        return bids

def get_scraper():
    return FrederickCountyBidScraper()

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()
