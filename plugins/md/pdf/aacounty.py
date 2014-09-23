import re, urlparse, time, datetime

from bidmap.bidscrapers.pdfscraper.pdfscraper import PdfBidScraper
from bidmap.htmlparse.soupify import soupify

from bidmapdb.models import *

GOVINFO = {
    'name': 'Anne Arundel County Maryland',
    'location': 'Anne Arundel County, MD',

    'home_page_url': 'http://www.aacounty.org',
    'bids_page_url': 'http://www.aacounty.org/CentServ/Purchasing/solicitations.cfm#.UyCngOewL1U'
}

class AnneArundelBidScraper(PdfBidScraper):
    def __init__(self):
        super(AnneArundelBidScraper, self).__init__(GOVINFO)

    def scrape_bid_links(self, url):
        bids = []

        self.br.open(url)

        s = soupify(self.br.response().read())

        r1 = re.compile(r'\.pdf$')
        r2 = re.compile(r'window\.open')

        x = {'href': r1, 'onclick': r2}

        for a in s.findAll('a', attrs=x):
            if not a.previous.strip() == 'Bid Number:':
                continue

            title = a.findPrevious(text=re.compile(r'Title:'))
            title = re.sub(r'Title:', '', title)

            bid = Bid(org=self.org)
            bid.title = title
            bid.url = urlparse.urljoin(self.br.geturl(), a['href'])
            bid.location = self.org.location

            d = a.findNext(text=re.compile(r'^Due Date/Time:'))
            d = d.split(':')[1].strip()
            d = d.split('@')[0].strip()

            try:
                r = time.strptime(d, "%B %d, %Y")
                bid.due_date = datetime.date(day=r.tm_mday, month=r.tm_mon, year=r.tm_year)
            except:
                pass

            tr = a.findParent('tr')
            p = tr.find(text=re.compile(r'Project Manager:'))

            if p:
                bid.contact = p.parent.text

            bids.append(bid)

        return bids

def get_scraper():
    return AnneArundelBidScraper()

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()
