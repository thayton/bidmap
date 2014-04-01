import re, urlparse, urllib

from bidmap.bidscrapers.pdfscraper.pdfscraper import PdfBidScraper
from bidmap.htmlparse.soupify import soupify

from bidmapdb.models import *

GOVINFO = {
    'name': 'Jesup Geogia',
    'location': 'Jesup, GA',

    'home_page_url': 'http://www.jesupga.gov',
    'bids_page_url': 'http://www.jesupga.gov/bids.html'
}

class JesupGaBidScraper(PdfBidScraper):
    def __init__(self):
        super(JesupGaBidScraper, self).__init__(GOVINFO)

    def scrape_bid_links(self, url):
        bids = []

        self.br.open(url)

        s = soupify(self.br.response().read())
        d = s.find('div', id='mainContent')
        r = re.compile(r'\.pdf$')

        for a in d.findAll('a', href=r):
            bid = Bid(org=self.org)
            bid.title = a.text
            bid.url = urlparse.urljoin(self.br.geturl(), a['href'])
            bid.url = urllib.quote(bid.url, ':/')
            bid.location = self.org.location
            bids.append(bid)

        return bids

def get_scraper():
    return JesupGaBidScraper()

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()
