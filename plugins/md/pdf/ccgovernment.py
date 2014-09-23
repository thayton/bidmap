import re, urlparse, datetime

from bidmap.bidscrapers.pdfscraper.pdfscraper import PdfBidScraper
from bidmap.htmlparse.soupify import soupify

from bidmapdb.models import *

GOVINFO = {
    'name': 'Carroll County Maryland',
    'location': 'Carroll County, MD',

    'home_page_url': 'http://ccgovernment.carr.org',
    'bids_page_url': 'http://ccgovernment.carr.org/ccg/bidnotce/'
}

class CarrollCountyBidScraper(PdfBidScraper):
    def __init__(self):
        super(CarrollCountyBidScraper, self).__init__(GOVINFO)

    def scrape_bid_links(self, url):
        bids = []

        self.br.open(url)

        s = soupify(self.br.response().read())
        r = re.compile(r'^files/[^.]+\.pdf$')

        for a in s.findAll('a', href=r):
            bid = Bid(self.org)
            bid.title = a.text
            bid.url = urlparse.urljoin(self.br.geturl(), a['href'])
            bid.location = self.org.location

            x = re.compile(r'lblSubDate')
            p = a.findNext('span', id=x)

            if p:
                z = re.search(self.date_regex, p.text)
                if z:
                    m,d,y = z.groups()
                    bid.due_date = datetime.date(day=int(d), month=int(m), year=int(y))                

            bids.append(bid)

        return bids

def get_scraper():
    return CarrollCountyBidScraper()

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()
