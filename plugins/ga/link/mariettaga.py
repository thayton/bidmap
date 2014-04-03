import re, urlparse, datetime

from bidmap.bidscrapers.bidscraper import BidScraper
from bidmap.htmlparse.soupify import soupify, get_all_text

from bidmapdb.models import *

GOVINFO = {
    'name': 'Marietta Geogia',
    'location': 'Marietta, GA',

    'home_page_url': 'http://www.mariettaga.gov',
    'bids_page_url': 'http://www.mariettaga.gov/city/cityhall/purchasing/bids'
}

class MariettaGaBidScraper(BidScraper):
    def __init__(self):
        super(MariettaGaBidScraper, self).__init__(GOVINFO)

    def scrape_bid_links(self, url):
        bids = []

        self.br.open(url)

        s = soupify(self.br.response().read())
        r = re.compile(r'viewbid\?id=\d+$')
        v = re.compile(r'(\d{1,2})/(\d{1,2})/(\d{4})')

        for a in s.findAll('a', href=r):
            tr = a.findParent('tr')
            td = tr.findAll('td')

            z = re.search(v, td[-1].text)
            if z:
                m,d,y = z.groups()

            bid = Bid(org=self.org)
            bid.title = td[1].span.text
            bid.url = urlparse.urljoin(self.br.geturl(), a['href'])

            if z:
                bid.due_date = datetime.date(day=int(d), month=int(m), year=int(y))

            bid.location = self.org.location
            bids.append(bid)

        return bids

    def scrape_bid_description(self, bid):
        self.br.open(bid.url)

        s = soupify(self.br.response().read())
        r = re.compile(r'PurchasingBids')
        t = s.find('table', id=r)

        bid.description = get_all_text(t)
        bid.save()

def get_scraper():
    return MariettaGaBidScraper()

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()
