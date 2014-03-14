import re, urlparse

from bid import Bid
from bidmap.bidscrapers.bidscraper import BidScraper
from bidmap.htmlparse.soupify import soupify

GOVINFO = {
    'name': 'Commerce Geogia',
    'location': 'Commerce, GA',

    'home_page_url': 'http://www.commercega.org',
    'bids_page_url': 'http://www.commercega.org/Content/Default/5/64/0/doing-business/request-for-proposals-and-bid\'s.html'
}

class CommerceGaBidScraper(BidScraper):
    def __init__(self):
        super(CommerceGaBidScraper, self).__init__(GOVINFO)

    def scrape_bid_links(self, url):
        bids = []

        self.br.open(url)

        s = soupify(self.br.response().read())
        r1 = re.compile(r'^RFP')
        r2 = re.compile(r'\.pdf$')
        f = lambda x: x.name == 'a' and re.search(r2, x.get('href', '')) and re.search(r1, x.text)

        for a in s.findAll(f):
            bid = Bid()
            bid.title = a.text
            bid.url = urlparse.urljoin(self.br.geturl(), a['href'])
            bids.append(bid)

        return bids

def get_scraper():
    return CommerceGaBidScraper()

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()
