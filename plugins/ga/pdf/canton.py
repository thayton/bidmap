import re, urlparse

from bidmap.bidscrapers.pdfscraper.pdfscraper import PdfBidScraper
from bidmap.htmlparse.soupify import soupify, get_all_text

from bidmapdb.models import *

GOVINFO = {
    'name': 'Canton Geogia',
    'location': 'Canton, GA',

    'home_page_url': 'http://www.canton-georgia.com',
    'bids_page_url': 'http://www.canton-georgia.com/bidtab.html'
}

class CantonGaBidScraper(PdfBidScraper):
    def __init__(self):
        super(CantonGaBidScraper, self).__init__(GOVINFO)

    def scrape_bid_links(self, url):
        bids = []

        self.br.open(url)

        s = soupify(self.br.response().read())
        r = re.compile(r'\.pdf$')
        f = lambda x: x.name == 'a' and re.search(r, x.get('href', '')) and x.text == 'RFP'

        for a in s.findAll(f):
            tr = a.findParent('tr')
            td = tr.findAll('td')

            bid = Bid(org=self.org)
            bid.title = td[2].text
            bid.url = urlparse.urljoin(self.br.geturl(), a['href'])
            bid.location = self.org.location
            bids.append(bid)

        return bids
        
def get_scraper():
    return CantonGaBidScraper()

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()
