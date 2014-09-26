import re, urlparse, time, datetime

from bidmap.bidscrapers.pdfscraper.pdfscraper import PdfBidScraper
from bidmap.htmlparse.soupify import soupify

from bidmapdb.models import *

GOVINFO = {
    'name': 'Doraville Geogia',
    'location': 'Doraville, GA',

    'home_page_url': 'http://www.doravillega.us',
    'bids_page_url': 'http://www.doravillega.us/procurement-opportunities/'
}

class DoravilleGaBidScraper(PdfBidScraper):
    def __init__(self):
        super(DoravilleGaBidScraper, self).__init__(GOVINFO)

    def scrape_bid_links(self, url):
        bids = []

        self.br.open(url)

        s = soupify(self.br.response().read())
        r = re.compile(r'\bRFP[^.]+\.pdf$')

        for a in s.findAll('a', href=r):
            tr = a.findParent('tr')
            td = tr.findAll('td')

            bid = Bid(org=self.org)
            bid.title = a.text
            bid.url = urlparse.urljoin(self.br.geturl(), a['href'])
            bid.location = self.org.location
            
            d = td[-1].text.split(',', 1)[1]
            d = d.split('at')[0].strip()

            try:
                r = time.strptime(d, "%B %d, %Y")
                bid.due_date = datetime.date(day=r.tm_mday, month=r.tm_mon, year=r.tm_year)
            except:
                pass

            bids.append(bid)

        return bids

def get_scraper():
    return DoravilleGaBidScraper()

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()
