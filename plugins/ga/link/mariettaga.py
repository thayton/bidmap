import re, urlparse

from bid import Bid
from bidmap.bidscrapers.bidscraper import BidScraper
from bidmap.htmlparse.soupify import soupify

GOVINFO = {
    'name': 'Marietta Geogia',
    'location': 'Marietta, GA',

    'home_page_url': 'http://www.mariettaga.gov',
    'bids_page_url': 'http://www.mariettaga.gov/city/cityhall/purchasing/bids'
}

class MariettaGaBidScraper(BidScraper):
    def __init__(self):
        super(MariettaGaBidScraper, self).__init__(GOVINFO)

    def scrape_bid_links(self, url):
        bids = []

        self.br.open(url)

        s = soupify(self.br.response().read())
        r = re.compile(r'viewbid\?id=\d+$')

        for a in s.findAll('a', href=r):
            tr = a.findParent('tr')
            td = tr.findAll('td')

            bid = Bid()
            bid.title = td[1].span.text
            bid.url = urlparse.urljoin(self.br.geturl(), a['href'])
            bids.append(bid)

        return bids

    def scrape_bids(self):
        bid_list = self.scrape_bid_links(self.gov['bids_page_url'])
        for bid in bid_list:
            print bid

def get_scraper():
    return MariettaGaBidScraper()

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()
