import re, urlparse, datetime

from bidmap.bidscrapers.bidscraper import BidScraper
from bidmap.htmlparse.soupify import soupify, get_all_text
from bidmap.txtextract.pdftohtml import pdftohtml

from bidmapdb.models import *

GOVINFO = {
    'name': 'Mcdonough Geogia',
    'location': 'Mcdonough, GA',

    'home_page_url': 'http://www.mcdonoughga.org',
    'bids_page_url': 'http://www.mcdonoughga.org/departments/finance/faqs/procurement'
}

class McdonoughGaBidScraper(BidScraper):
    def __init__(self):
        super(McdonoughGaBidScraper, self).__init__(GOVINFO)

    def scrape_bid_links(self, url):
        bids = []

        self.br.open(url)

        s = soupify(self.br.response().read())
        r = re.compile(r'procurement/-item-\d+$')
        v = re.compile(r'(\d{1,2})/(\d{1,2})/(\d{4})')

        for a in s.findAll('a', href=r):
            tr = a.findParent('tr')
            td = tr.findAll('td')

            # Verify open status
            if td[-1].text != 'Open':
                continue

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
        r = re.compile(r'showdocument\?id=\d+$')
        a = s.find('a', href=r)
        u = urlparse.urljoin(self.br.geturl(), a['href'])

        self.br.open(u)

        d = self.br.response().read()
        s = soupify(pdftohtml(d))

        bid.description = get_all_text(s.html.body)
        bid.save()

def get_scraper():
    return McdonoughGaBidScraper()

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()
