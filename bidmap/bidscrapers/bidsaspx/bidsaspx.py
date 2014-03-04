import re, urlparse

from bid import Bid
from bidmap.bidscrapers.bidscraper import BidScraper
from bidmap.htmlparse.soupify import soupify

class BidsAspxBidScraper(BidScraper):
    def __init__(self, govinfo):
        super(BidsAspxBidScraper, self).__init__(govinfo)
        self.gov = govinfo

    def scrape_bid_links(self, url):
        bids = []

        self.br.open(url)

        s = soupify(self.br.response().read())
        r = re.compile(r'bids\.aspx\?bidID=\d+$')

        for a in s.findAll('a', href=r):
            if a.get('style', False):
                continue

            bid = Bid()
            bid.title = a.text
            bid.url = urlparse.urljoin(self.br.geturl(), a['href'])
            bids.append(bid)

        return bids

    def scrape_bids(self):
        bid_list = self.scrape_bid_links(self.gov['bids_page_url'])
        for bid in bid_list:
            print bid

def get_scraper():
    return BidsAspxBidScraper()


