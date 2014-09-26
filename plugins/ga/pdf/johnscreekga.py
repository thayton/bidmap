import re, urlparse

from bidmap.bidscrapers.pdfscraper.pdfscraper import PdfBidScraper
from bidmap.htmlparse.soupify import soupify

from bidmapdb.models import *

GOVINFO = {
    'name': 'Johns Creek Geogia',
    'location': 'Johns Creek, GA',

    'home_page_url': 'http://www.johnscreekga.gov',
    'bids_page_url': 'http://www.johnscreekga.gov/services/purchasing.aspx'
}

class JohnsCreekGaBidScraper(PdfBidScraper):
    def __init__(self):
        super(JohnsCreekGaBidScraper, self).__init__(GOVINFO)

    def scrape_bid_links(self, url):
        bids = []

        self.br.open(url)

        s = soupify(self.br.response().read())
        r = re.compile(r'\.pdf$')
        f = lambda x: x.name == 'a' and re.search(r, x.get('href', '')) and x.text == 'Read more'

        for a in s.findAll(f):
            h3 = a.findPrevious('h3')
            bid = Bid(org=self.org)
            bid.title = h3.text
            bid.url = urlparse.urljoin(self.br.geturl(), a['href'])
            bid.location = self.org.location
            bids.append(bid)

        return bids

def get_scraper():
    return JohnsCreekGaBidScraper()

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()
