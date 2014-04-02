import re, urlparse, datetime

from bidmap.bidscrapers.bidscraper import BidScraper
from bidmap.htmlparse.soupify import soupify, get_all_text

from bidmapdb.models import *

class BidsAspxBidScraper(BidScraper):
    def __init__(self, govinfo):
        super(BidsAspxBidScraper, self).__init__(govinfo)
        self.gov = govinfo

    def scrape_bid_links(self, url):
        bids = []

        self.br.open(url)

        s = soupify(self.br.response().read())
        r = re.compile(r'bids\.aspx\?bidID=\d+$')
        v = re.compile(r'(\d{1,2})/(\d{1,2})/(\d{4})')

        for a in s.findAll('a', href=r):
            if a.get('style', False):
                continue

            tr = a.findParent('tr')
            td = tr.findAll('td')
            sp = td[-1].findAll('span')
            
            z = re.search(v, sp[-1].text)
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
        x = {'summary': 'Bid Details'}
        t = s.find('table', attrs=x)

        bid.description = get_all_text(t)
        bid.save()
