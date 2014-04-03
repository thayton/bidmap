import re, urlparse, datetime

from bidmap.bidscrapers.bidscraper import BidScraper
from bidmap.htmlparse.soupify import soupify, get_all_text

from bidmapdb.models import *

GOVINFO = {
    'name': 'Covington Geogia',
    'location': 'Covington, GA',

    'home_page_url': 'http://www.cityofcovington.org',
    'bids_page_url': 'http://www.cityofcovington.org/Business/Bids/Pages/Current-Bid-Postings.aspx'
}

class CovingtonGaBidScraper(BidScraper):
    def __init__(self):
        super(CovingtonGaBidScraper, self).__init__(GOVINFO)

    def scrape_bid_links(self, url):
        bids = []

        self.br.open(url)

        s = soupify(self.br.response().read())
        x = {'summary': 'Current Bid Postings '}
        t = s.find('table', attrs=x)
        r = re.compile(r'/Bids/')
        v = re.compile(r'(\d{1,2})/(\d{1,2})/(\d{4})')

        for a in t.findAll('a', href=r):
            tr = a.findParent('tr')
            td = tr.findAll('td')

            z = re.search(v, td[-2].text)
            if z:
                m,d,y = z.groups()

            bid = Bid(org=self.org)
            bid.title = a.text
            bid.url = urlparse.urljoin(self.br.geturl(), a['href'])

            if z:
                bid.due_date = datetime.date(day=int(d), month=int(m), year=int(y))

            bid.location = self.org.location
            bids.append(bid)

        return bids

    def scrape_bid_description(self, bid):
        self.br.open(bid.url)

        s = soupify(self.br.response().read())
        x = {'class': 'ms-formtable'}
        t = s.find('table', attrs=x)

        bid.description = get_all_text(t)
        bid.save()

def get_scraper():
    return CovingtonGaBidScraper()

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()
