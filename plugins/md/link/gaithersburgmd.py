import re, urlparse

from bidmap.bidscrapers.bidscraper import BidScraper
from bidmap.htmlparse.soupify import soupify, get_all_text

from bidmapdb.models import *

GOVINFO = {
    'name': 'Gaithersburg Maryland',
    'location': 'Gaithersburg, MD',

    'home_page_url': 'http://www.gaithersburgmd.gov',
    'bids_page_url': 'http://www.gaithersburgmd.gov/government/procurement/current-bids'
}

class GaithersburgBidScraper(BidScraper):
    def __init__(self):
        super(GaithersburgBidScraper, self).__init__(GOVINFO)

    def scrape_bid_links(self, url):
        bids = []

        self.br.open(url)

        s = soupify(self.br.response().read())
        r = re.compile(r'/current-bids/[^/]+$')

        for a in s.findAll('a', href=r):
            if not a.h1:
                continue

            bid = Bid(org=self.org)
            bid.title = a.text
            bid.url = urlparse.urljoin(self.br.geturl(), a['href'])
            bid.location = self.org.location
            bids.append(bid)

        return bids

    def scrape_bid_description(self, bid):
        self.br.open(bid.url)
        
        s = soupify(self.br.response().read())
        x = {'class': 'body-content'}
        y = {'class': 'promo'}
        n = s.find('section', attrs=y)

        bid.contact = n.text

        m = re.search(self.email_regex, n.text)
        if m:
            bid.email = m.group(0)

        d = s.find('div', attrs=x)

        bid.desc = get_all_text(d)
        bid.save()

def get_scraper():
    return GaithersburgBidScraper()

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()
