import re, urlparse

from bid import Bid
from bidmap.bidscrapers.bidscraper import BidScraper
from bidmap.htmlparse.soupify import soupify

GOVINFO = {
    'name': 'Prince Georges County Maryland',
    'location': 'Upper Marlboro, MD',

    'home_page_url': 'http://pgebid.co.pg.md.us',
    'bids_page_url': 'http://pgebid.co.pg.md.us/ebid/'
}

class PrinceGeorgesCountyBidScraper(BidScraper):
    def __init__(self):
        super(PrinceGeorgesCountyBidScraper, self).__init__(GOVINFO)

    def scrape_bid_links(self, url):
        bids = []

        self.br.open(url)

        s = soupify(self.br.response().read())
        r = re.compile(r'viewbid\.aspx\?bid_id=\d+$')

        for a in s.findAll('a', href=r):
            tr = a.findParent('tr')
            td = tr.findAll('td')

            bid = Bid()
            bid.title = td[1].text
            bid.url = urlparse.urljoin(self.br.geturl(), a['href'])
            bids.append(bid)

        return bids

def get_scraper():
    return PrinceGeorgesCountyBidScraper()

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()
