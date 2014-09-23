import re, urlparse, time, datetime

from bidmap.bidscrapers.bidscraper import BidScraper
from bidmap.htmlparse.soupify import soupify

from bidmapdb.models import *

GOVINFO = {
    'name': 'Garrett County Maryland',
    'location': 'Oakland, MD',

    'home_page_url': 'http://garrettcounty.org',
    'bids_page_url': 'http://garrettcounty.org/purchasing/current-bids'
}

class GarrettCountyBidScraper(BidScraper):
    def __init__(self):
        super(GarrettCountyBidScraper, self).__init__(GOVINFO)

    def scrape_bid_links(self, url):
        bids = []

        self.br.open(url)

        s = soupify(self.br.response().read())
        r = re.compile(r'^/purchasing/bid-form\?bidnumb=\d+')

        for a in s.findAll('a', href=r):
            bid = Bid(org=self.org)
            bid.title = a.text
            bid.url = urlparse.urljoin(self.br.geturl(), a['href'])
            bid.location = self.org.location

            d = a.findNext(text=re.compile(r'Due:'))
            d = d.split(':')[1].strip()

            try:
                r = time.strptime(d, "%B %d, %Y")
                bid.due_date = datetime.date(day=r.tm_mday, month=r.tm_mon, year=r.tm_year)
            except:
                pass

            bids.append(bid)

        return bids

    def scrape_bid_description(self, bid):
        # XXX bid document is behind a registration wall
        bid.save()

def get_scraper():
    return GarrettCountyBidScraper()

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()
