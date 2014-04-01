import re, urlparse

from bidmap.bidscrapers.pdfscraper.pdfscraper import PdfBidScraper
from bidmap.htmlparse.soupify import soupify

from bidmapdb.models import *

GOVINFO = {
    'name': 'Hapeville Geogia',
    'location': 'Hapeville, GA',

    'home_page_url': 'http://www.hapeville.org',
    'bids_page_url': 'http://www.hapeville.org/index.aspx?NID=360'
}

class HapevilleGaBidScraper(PdfBidScraper):
    def __init__(self):
        super(HapevilleGaBidScraper, self).__init__(GOVINFO)

    def scrape_bid_links(self, url):
        bids = []

        self.br.open(url)

        s = soupify(self.br.response().read())
        r = re.compile(r'^/DocumentView\.aspx\?DID=\d+$')
        x = {'href': r, 'class': 'Hyperlink', 'title': True}

        for a in s.findAll('a', attrs=x):
            bid = Bid(org=self.org)
            bid.title = a['title']
            bid.url = urlparse.urljoin(self.br.geturl(), a['href'])
            bid.location = self.org.location
            bids.append(bid)

        return bids

def get_scraper():
    return HapevilleGaBidScraper()

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()
