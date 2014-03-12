import re, urlparse

from bid import Bid
from bidmap.bidscrapers.bidscraper import BidScraper
from bidmap.htmlparse.soupify import soupify

GOVINFO = {
    'name': 'Mcdonough Geogia',
    'location': 'Mcdonough, GA',

    'home_page_url': 'http://www.mcdonoughga.org',
    'bids_page_url': 'http://www.mcdonoughga.org/departments/finance/faqs/procurement'
}

class McdonoughGaBidScraper(BidScraper):
    def __init__(self):
        super(McdonoughGaBidScraper, self).__init__(GOVINFO)

    def scrape_bid_links(self, url):
        bids = []

        self.br.open(url)

        s = soupify(self.br.response().read())
        r = re.compile(r'procurement/-item-\d+$')

        for a in s.findAll('a', href=r):
            tr = a.findParent('tr')
            td = tr.findAll('td')

            # Verify open status
            if td[-1].text != 'Open':
                continue

            bid = Bid()
            bid.title = a.text
            bid.url = urlparse.urljoin(self.br.geturl(), a['href'])
            bids.append(bid)

        return bids

def get_scraper():
    return McdonoughGaBidScraper()

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()
