import re, urlparse, time, datetime

from bidmap.bidscrapers.bidscraper import BidScraper
from bidmap.htmlparse.soupify import soupify, get_all_text

from bidmapdb.models import *

GOVINFO = {
    'name': 'Harford County Maryland',
    'location': 'Harford, MD',

    'home_page_url': 'http://www.harfordcountymd.gov',
    'bids_page_url': 'http://www.harfordcountymd.gov/procurement/BidBoard.cfm'
}

class HarfordCountyBidScraper(BidScraper):
    def __init__(self):
        super(HarfordCountyBidScraper, self).__init__(GOVINFO)

    def scrape_bid_links(self, url):
        bids = []

        self.br.open(url)

        s = soupify(self.br.response().read())
        r = re.compile(r'^BidBoard\.cfm\?BidID=\d+$')

        for a in s.findAll('a', href=r):
            tr = a.findParent('tr')
            td = tr.findAll('td')

            bid = Bid(org=self.org)
            bid.title = a.text
            bid.url = urlparse.urljoin(self.br.geturl(), a['href'])
            bid.location = self.org.location

            v = re.compile(r'(\d{1,2})[/.](\d{1,2})[/.](\d{2,4})') # date regex
            z = re.search(v, td[-4].text)

            if z:
                m,d,y = z.groups()
                bid.due_date = datetime.date(day=int(d), month=int(m), year=int(y))

            bids.append(bid)

        return bids

    def scrape_bid_description(self, bid):
        self.br.open(bid.url)
        
        s = soupify(self.br.response().read())
        r = re.compile(r'^Agent')
        f = lambda x: x.name == 'b' and re.search(r, x.text)
        b = s.find(f)

        if b:
            t = b.findParent('table')
            bid.contact = get_all_text(t)

        b = s.find('blockquote')

        bid.description = get_all_text(b)
        bid.save()

def get_scraper():
    return HarfordCountyBidScraper()

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()
