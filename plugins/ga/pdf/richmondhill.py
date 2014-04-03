import re, urlparse

from bidmap.bidscrapers.pdfscraper.pdfscraper import PdfBidScraper
from bidmap.htmlparse.soupify import soupify

from bidmapdb.models import *

GOVINFO = {
    'name': 'Richmond Hill Geogia',
    'location': 'Richmond Hill, GA',

    'home_page_url': 'http://www.richmondhill-ga.gov',
    'bids_page_url': 'http://www.richmondhill-ga.gov/index.aspx?nid=143'
}

class RichmondHillGaBidScraper(PdfBidScraper):
    def __init__(self):
        super(RichmondHillGaBidScraper, self).__init__(GOVINFO)

    def scrape_bid_links(self, url):
        bids = []

        self.br.open(url)

        s = soupify(self.br.response().read())
        r = re.compile(r'^/DocumentCenter/View/\d+$')
        f = lambda x: x.name == 'a' and re.search(r, x.get('href', '')) and x.text == 'here'
        x = {'class': 'Subhead2'}

        for a in s.findAll(f):
            p = a.findPrevious('span', attrs=x)

            bid = Bid(org=self.org)
            bid.title = p.text
            bid.url = urlparse.urljoin(self.br.geturl(), a['href'])
            bid.location = self.org.location
            bids.append(bid)

        return bids

def get_scraper():
    return RichmondHillGaBidScraper()

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()
