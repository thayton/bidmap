import re, urlparse

from bs4 import NavigableString
from bid import Bid
from bidmap.bidscrapers.bidscraper import BidScraper
from bidmap.htmlparse.soupify import soupify

GOVINFO = {
    'name': 'Howard County Maryland',
    'location': 'Ellicott City, MD',

    'home_page_url': 'http://www.howardcountymd.gov',
    'bids_page_url': 'http://www.howardcountymd.gov/DisplayPrimary.aspx?id=4294967759'
}

class HowardCountyBidScraper(BidScraper):
    def __init__(self):
        super(HowardCountyBidScraper, self).__init__(GOVINFO)

    def scrape_bid_links(self, url):
        bids = []

        self.br.open(url)

        s = soupify(self.br.response().read())

        r1 = re.compile(r'/WorkArea/linkit\.aspx\?LinkIdentifier=id&ItemID=\d+')
        r2 = re.compile(r'^RFP-\d+-\d+$')

        f = lambda x: x.name == 'a' and re.search(r1, x.get('href', '')) and re.search(r2, x.text)

        for a in s.findAll(f):
            p = a.findParent('p')
            p = p.findNextSibling('p')

            bid = Bid()
            bid.title = p.strong.text
            bid.url = urlparse.urljoin(self.br.geturl(), a['href'])
            bids.append(bid)

        return bids

def get_scraper():
    return HowardCountyBidScraper()

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()
