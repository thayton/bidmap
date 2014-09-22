import re, urlparse

from bidmap.bidscrapers.pdfscraper.pdfscraper import PdfBidScraper
from bidmap.htmlparse.soupify import soupify

from bidmapdb.models import *

GOVINFO = {
    'name': 'Howard County Maryland',
    'location': 'Ellicott City, MD',

    'home_page_url': 'http://www.howardcountymd.gov',
    'bids_page_url': 'http://www.howardcountymd.gov/DisplayPrimary.aspx?id=4294967759'
}

class HowardCountyBidScraper(PdfBidScraper):
    def __init__(self):
        super(HowardCountyBidScraper, self).__init__(GOVINFO)

    def scrape_bid_links(self, url):
        bids = []

        self.br.open(url)

        s = soupify(self.br.response().read())

        r1 = re.compile(r'/WorkArea/linkit\.aspx\?LinkIdentifier=id&ItemID=\d+')
        r2 = re.compile(r'^RFP-\d+-\d+$')

        f = lambda x: x.name == 'a' and re.search(r1, x.get('href', '')) and re.search(r2, x.text)

        for a in s.findAll(f):
            g = a.nextSibling.findNext('strong')

            bid = Bid(org=self.org)
            bid.title = g.em.text
            bid.url = urlparse.urljoin(self.br.geturl(), a['href'])
            bid.location = self.org.location
            bids.append(bid)

        return bids
        
def get_scraper():
    return HowardCountyBidScraper()

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()
