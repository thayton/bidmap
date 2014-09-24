import re, urlparse, datetime

from bidmap.bidscrapers.bidscraper import BidScraper
from bidmap.htmlparse.soupify import soupify, get_all_text

from bidmapdb.models import *

GOVINFO = {
    'name': 'Saint Marys Maryland',
    'location': 'Saint Marys, MD',

    'home_page_url': 'http://www.co.saint-marys.md.us',
    'bids_page_url': 'http://www.co.saint-marys.md.us/bids/openbids.asp'
}

class SaintMarysBidScraper(BidScraper):
    def __init__(self):
        super(SaintMarysBidScraper, self).__init__(GOVINFO)

    def scrape_bids(self):
        self.br.open(self.org.bids_page_url)

        s = soupify(self.br.response().read())
        r = re.compile(r'^\s*Solicitation')
        f = lambda x: x.name == 'td' and re.search(r, x.text)

        self.org.bid_set.all().delete()

        for td in s.findAll(f):
            tr = td.findParent('tr')
            td = tr.findAll('td')

            bid = Bid(org=self.org)
            bid.title = td[0].text
            bid.url = self.br.geturl()
            bid.description = get_all_text(td[1])

            z = re.search(self.date_regex, td[-3].text)
            if z:
                m,d,y = z.groups()
                bid.due_date = datetime.date(day=int(d), month=int(m), year=int(y))

            bid.save()


def get_scraper():
    return SaintMarysBidScraper()

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()
