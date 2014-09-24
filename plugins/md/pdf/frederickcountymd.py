import re, urlparse, time, datetime

from bidmap.bidscrapers.pdfscraper.pdfscraper import PdfBidScraper
from bidmap.htmlparse.soupify import soupify

from bidmapdb.models import *

GOVINFO = {
    'name': 'Frederick County Maryland',
    'location': 'Frederick, MD',

    'home_page_url': 'https://frederickcountymd.gov',
    'bids_page_url': 'https://frederickcountymd.gov/index.aspx?NID=1116'
}

class FrederickCountyBidScraper(PdfBidScraper):
    def __init__(self):
        super(FrederickCountyBidScraper, self).__init__(GOVINFO)

    def scrape_bid_links(self, url):
        bids = []

        self.br.open(url)

        s = soupify(self.br.response().read())
        f = lambda x: x.name == 'a' and x.text == 'Invitation for Bid' or x.text == 'Summary'

        for a in s.findAll(f):
            t = a.previousSibling.previousSibling.previousSibling
            bid = Bid(org=self.org)
            bid.title = t
            bid.url = urlparse.urljoin(self.br.geturl(), a['href'])
            bid.location = self.org.location

            tr = a.findParent('tr')
            d = tr.find(text=re.compile(r'\bDue:'))

            if d:
                d = d.split(':')[1].strip()
                d = d.split('at')[0].strip()

                try:
                    r = time.strptime(d, "%B %d, %Y")
                    bid.due_date = datetime.date(day=r.tm_mday, month=r.tm_mon, year=r.tm_year)
                except:
                    pass

            bids.append(bid)

        return bids

def get_scraper():
    return FrederickCountyBidScraper()

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()
