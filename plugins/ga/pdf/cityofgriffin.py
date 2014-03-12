import re, urlparse

from bid import Bid
from bidmap.bidscrapers.bidscraper import BidScraper
from bidmap.htmlparse.soupify import soupify

GOVINFO = {
    'name': 'Griffin Geogia',
    'location': 'Griffin, GA',

    'home_page_url': 'http://www.cityofgriffin.com',
    'bids_page_url': 'http://www.cityofgriffin.com/Departments/AdministrativeServices/Purchasing/BidOpportunities.aspx'
}

class GriffinGaBidScraper(BidScraper):
    def __init__(self):
        super(GriffinGaBidScraper, self).__init__(GOVINFO)

    def scrape_bid_links(self, url):
        bids = []

        self.br.open(url)

        s = soupify(self.br.response().read())
        r = re.compile(r'/rfps/[^.]+\.pdf$')
        f = lambda x: x.name == 'a' and re.search(r, x.get('href', '')) and x.text == 'Open'

        for a in s.findAll(f):
            td = a.findParent('td')
            t = td.find(text='Title:')
            t = t.parent.nextSibling

            bid = Bid()
            bid.title = t
            bid.url = urlparse.urljoin(self.br.geturl(), a['href'])
            bids.append(bid)

        return bids

def get_scraper():
    return GriffinGaBidScraper()

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()
