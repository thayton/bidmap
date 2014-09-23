import re, urlparse, datetime

from bidmap.bidscrapers.bidscraper import BidScraper
from bidmap.htmlparse.soupify import soupify, get_all_text

from bidmapdb.models import *

GOVINFO = {
    'name': 'Prince Georges County Maryland',
    'location': 'Upper Marlboro, MD',

    'home_page_url': 'http://pgebid.co.pg.md.us',
    'bids_page_url': 'http://pgebid.co.pg.md.us/ebid/'
}

class PrinceGeorgesCountyBidScraper(BidScraper):
    def __init__(self):
        super(PrinceGeorgesCountyBidScraper, self).__init__(GOVINFO)

    def scrape_bid_links(self, url):
        bids = []

        self.br.open(url)

        s = soupify(self.br.response().read())
        r = re.compile(r'viewbid\.aspx\?bid_id=\d+$')

        for a in s.findAll('a', href=r):
            tr = a.findParent('tr')
            td = tr.findAll('td')

            z = re.search(self.date_regex, td[-2].text)
            if z:
                m,d,y = z.groups()

            bid = Bid(org=self.org)
            bid.title = td[1].text
            bid.url = urlparse.urljoin(self.br.geturl(), a['href'])

            if z:
                bid.due_date = datetime.date(day=int(d), month=int(m), year=int(y))

            bid.location = self.org.location
            bids.append(bid)

        return bids

    def scrape_bid_description(self, bid):
        self.br.open(bid.url)

        s = soupify(self.br.response().read())
        h = s.find('h1')
        t = h.findParent('table')

        bid.description = get_all_text(t)
        bid.save()

def get_scraper():
    return PrinceGeorgesCountyBidScraper()

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()
