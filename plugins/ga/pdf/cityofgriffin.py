import re, urlparse, urllib, time, datetime

from bidmap.bidscrapers.pdfscraper.pdfscraper import PdfBidScraper
from bidmap.htmlparse.soupify import soupify

from bidmapdb.models import *

GOVINFO = {
    'name': 'Griffin Geogia',
    'location': 'Griffin, GA',

    'home_page_url': 'http://www.cityofgriffin.com',
    'bids_page_url': 'http://www.cityofgriffin.com/Departments/AdministrativeServices/Purchasing/BidOpportunities.aspx'
}

class GriffinGaBidScraper(PdfBidScraper):
    def __init__(self):
        super(GriffinGaBidScraper, self).__init__(GOVINFO)

    def scrape_bid_links(self, url):
        bids = []

        self.br.open(url)

        s = soupify(self.br.response().read())
        y = re.compile(r'^/LinkClick\.aspx\?')
        z = re.compile(r'^Bid:')
        f = lambda x: x.name == 'a' and re.search(y, x.get('href', '')) and re.search(z, x.text)

        for a in s.findAll(f):
            td = a.findParent('td')
            t = td.find(text='Title:')
            t = t.parent.nextSibling

            bid = Bid(org=self.org)
            bid.title = t
            bid.url = urlparse.urljoin(self.br.geturl(), a['href'])
            bid.url = urllib.quote(bid.url, ':/')
            bid.location = self.org.location

            d = a.findNext(text=re.compile(r'^Close Date:'))
            d = d.parent.nextSibling.strip()

            try:
                r = time.strptime(d, "%B %d, %Y")
                bid.due_date = datetime.date(day=r.tm_mday, month=r.tm_mon, year=r.tm_year)
            except:
                pass

            bids.append(bid)

        return bids

def get_scraper():
    return GriffinGaBidScraper()

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()
