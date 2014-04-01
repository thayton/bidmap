import re, urlparse

from bidmap.bidscrapers.pdfscraper.pdfscraper import PdfBidScraper
from bidmap.htmlparse.soupify import soupify

from bidmapdb.models import *

GOVINFO = {
    'name': 'Thomasville Geogia',
    'location': 'Thomasville, GA',

    'home_page_url': 'http://www.thomasville.org',
    'bids_page_url': 'http://www.thomasville.org/Content/Default/10/272/225/city-of-thomasville/doing-business/bid-opportunities.html'
}

class ThomasvilleGaBidScraper(PdfBidScraper):
    def __init__(self):
        super(ThomasvilleGaBidScraper, self).__init__(GOVINFO)

    def scrape_bid_links(self, url):
        bids = []

        self.br.open(url)

        s = soupify(self.br.response().read())
        d = s.find('div', id='content')

        for ul in d.findAll('ul', recursive=False):
            h3 = ul.findPrevious('h3')
            if h3.text != 'Bid Documents:':
                continue

            bid = Bid(org=self.org)
            bid.title = ul.li.a.text
            bid.url = urlparse.urljoin(self.br.geturl(), ul.li.a['href'])
            bid.location = self.org.location
            bids.append(bid)

        return bids

def get_scraper():
    return ThomasvilleGaBidScraper()

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()
