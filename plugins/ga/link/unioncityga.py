import re, urlparse

from bidmap.bidscrapers.bidscraper import BidScraper
from bidmap.htmlparse.soupify import soupify

from bidmapdb.models import *

GOVINFO = {
    'name': 'Union City Geogia',
    'location': 'Union City, GA',

    'home_page_url': 'http://www.unioncityga.org',
    'bids_page_url': 'http://www.unioncityga.org/index.aspx?page=150'
}

class UnionCityGaBidScraper(BidScraper):
    def __init__(self):
        super(UnionCityGaBidScraper, self).__init__(GOVINFO)

    def scrape_bid_links(self, url):
        bids = []

        self.br.open(url)

        s = soupify(self.br.response().read())
        r = re.compile(r'^index\.aspx\?recordid=\d+')
        v = re.compile(r'(\d{1,2})/(\d{1,2})/(\d{4})') # date regex

        for a in s.findAll('a', href=r):
            tr = a.findParent('tr')
            td = tr.findAll('td')

            z = re.search(v, td[-1].text)
            if z:
                m,d,y = z.groups()
            
            bid = Bid(org=self.org)
            bid.title = a.text
            bid.url = urlparse.urljoin(self.br.geturl(), a['href'])
            bid.location = self.org.location

            if z:
                bid.due_date = datetime.date(day=int(d), month=int(m), year=int(y))

            bids.append(bid)

        return bids

def get_scraper():
    return UnionCityGaBidScraper()

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()
