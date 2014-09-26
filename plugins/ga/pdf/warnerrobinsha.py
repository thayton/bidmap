import re, urlparse, time, datetime

from bidmap.bidscrapers.pdfscraper.pdfscraper import PdfBidScraper
from bidmap.htmlparse.soupify import soupify

from bidmapdb.models import *

GOVINFO = {
    'name': 'Warner Robins Houston County',
    'location': 'Warner Robins, GA',

    'home_page_url': 'http://www.warnerrobinsha.com',
    'bids_page_url': 'http://www.warnerrobinsha.com/bids.htm'
}

class WarnerRobinsGaBidScraper(PdfBidScraper):
    def __init__(self):
        super(WarnerRobinsGaBidScraper, self).__init__(GOVINFO)

    def scrape_bid_links(self, url):
        bids = []

        self.br.open(url)

        s = soupify(self.br.response().read())
        r = re.compile(r'\.pdf$')
        z = re.compile(r'^RFP -')
        f = lambda x: x.name == 'a' and re.search(r, x.get('href', '')) and re.search(z, x.text)

        for a in s.findAll(f):
            bid = Bid(org=self.org)
            bid.title = a.strong.text
            bid.url = urlparse.urljoin(self.br.geturl(), a['href'])
            bid.location = self.org.location

            d = a.strong.nextSibling
            d = ' '.join(d.split())
            d = d.split(',', 1)[1].strip()
            d = d.rsplit(' ', 1)[0].strip()
            
            try:
                r = time.strptime(d, "%b %d, %Y")
                bid.due_date = datetime.date(day=r.tm_mday, month=r.tm_mon, year=r.tm_year)
            except:
                pass

            bids.append(bid)

        return bids

def get_scraper():
    return WarnerRobinsGaBidScraper()

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()
