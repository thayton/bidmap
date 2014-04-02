import re, urlparse

from bidmap.bidscrapers.bidscraper import BidScraper
from bidmap.htmlparse.soupify import soupify

from bidmapdb.models import *

GOVINFO = {
    'name': 'Alpharetta Geogia',
    'location': 'Alpharetta, GA',

    'home_page_url': 'http://www.alpharetta.ga.us',
    'bids_page_url': 'http://www.alpharetta.ga.us/index.php?m=procurement'
}

class AlpharettaGaBidScraper(BidScraper):
    def __init__(self):
        super(AlpharettaGaBidScraper, self).__init__(GOVINFO)

    def scrape_bid_links(self, url):
        bids = []

        self.br.open(url)

        s = soupify(self.br.response().read())
        r = re.compile(r'^index\.php\?m=procurement&id=\d+$')

        for a in s.findAll('a', href=r):
            tr = a.findParent('tr')
            td = tr.findAll('td')

            # Verify open status
            if td[-1].text != 'OPEN':
                continue

            bid = Bid(org=self.org)
            bid.title = a.text
            bid.url = urlparse.urljoin(self.br.geturl(), a['href'])
            bid.location = self.org.location
            bids.append(bid)

        return bids

def get_scraper():
    return AlpharettaGaBidScraper()

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()
