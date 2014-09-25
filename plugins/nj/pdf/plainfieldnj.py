import re, urlparse

from bidmap.bidscrapers.pdfscraper.pdfscraper import PdfBidScraper
from bidmap.htmlparse.soupify import soupify, get_all_text

from bidmapdb.models import *

GOVINFO = {
    'name': 'Plainfield new jersey',
    'location': 'Plainfield, NJ',

    'home_page_url': 'http://www.plainfieldnj.gov',
    'bids_page_url': 'http://www.plainfieldnj.gov/bids.aspx'
}

class PlainfieldBidScraper(PdfBidScraper):
    def __init__(self):
        super(PlainfieldBidScraper, self).__init__(GOVINFO)

    def scrape_bid_links(self, url):
        bids = []

        self.br.open(url)

        s = soupify(self.br.response().read())
        r = re.compile(r'\.pdf$')
        x = {'target': '_blank', 'href': r}

        for a in s.findAll('a', attrs=x):
            if a.parent.name != 'td':
                continue

            bid = Bid(org=self.org)
            bid.title = a.text
            bid.url = urlparse.urljoin(self.br.geturl(), a['href'])
            bid.location = self.org.location
            bids.append(bid)

        return bids
        
def get_scraper():
    return PlainfieldBidScraper()

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()
