import re, urlparse, datetime

from bidmap.bidscrapers.bidscraper import BidScraper
from bidmap.htmlparse.soupify import soupify, get_all_text
from bidmap.txtextract.pdftohtml import pdftohtml

from bidmapdb.models import *

GOVINFO = {
    'name': 'Alpharetta Geogia',
    'location': 'Alpharetta, GA',

    'home_page_url': 'http://www.alpharetta.ga.us',
    'bids_page_url': 'http://www.alpharetta.ga.us/index.php?m=procurement'
}

class AlpharettaGaBidScraper(BidScraper):
    def __init__(self):
        super(AlpharettaGaBidScraper, self).__init__(GOVINFO)

    def scrape_bid_links(self, url):
        bids = []

        self.br.open(url)

        s = soupify(self.br.response().read())
        r = re.compile(r'^index\.php\?m=procurement&id=\d+$')
        v = re.compile(r'(\d{1,2})/(\d{1,2})/(\d{4})')

        for a in s.findAll('a', href=r):
            tr = a.findParent('tr')
            td = tr.findAll('td')

            # Verify open status
            if td[-1].text != 'OPEN':
                continue

            z = re.search(self.date_regex, td[1].contents[2])
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
        t = s.find(text=re.compile(r'^Contact:'))

        if t:
            p = t.findParent('p')
            bid.contact = get_all_text(p)

        f = lambda x: x.name == 'a' and x.text == 'Download Bid Package'
        a = s.find(f)
        u = urlparse.urljoin(self.br.geturl(), a['href'])

        self.br.open(u)

        d = self.br.response().read()
        s = soupify(pdftohtml(d))

        bid.description = get_all_text(s.html.body)
        bid.save()

def get_scraper():
    return AlpharettaGaBidScraper()

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()
