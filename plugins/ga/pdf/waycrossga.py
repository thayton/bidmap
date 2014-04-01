import re, urlparse

from bidmap.bidscrapers.pdfscraper.pdfscraper import PdfBidScraper
from bidmap.htmlparse.soupify import soupify

from bidmapdb.models import *

GOVINFO = {
    'name': 'Waycross Geogia',
    'location': 'Waycross, GA',

    'home_page_url': 'http://www.waycrossga.com',
    'bids_page_url': 'http://www.waycrossga.com/bids/'
}

class WaycrossGaBidScraper(PdfBidScraper):
    def __init__(self):
        super(WaycrossGaBidScraper, self).__init__(GOVINFO)

    def scrape_bid_links(self, url):
        bids = []

        self.br.open(url)

        s = soupify(self.br.response().read())
        r = re.compile(r'/Currentbids/[^.]+\.pdf$')
        x = {'class': 'learn-more-content'}
        d = s.find('div', attrs=x)
        d.ul.ul.extract()

        for a in d.findAll('a', href=r):
            bid = Bid(org=self.org)
            bid.title = a.text
            bid.url = urlparse.urljoin(self.br.geturl(), a['href'])
            bid.location = self.org.location
            bids.append(bid)

        return bids

def get_scraper():
    return WaycrossGaBidScraper()

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()
