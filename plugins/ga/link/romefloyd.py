import re, urlparse

from bidmap.bidscrapers.bidscraper import BidScraper
from bidmap.htmlparse.soupify import soupify

from bidmapdb.models import *

GOVINFO = {
    'name': 'Rome Geogia',
    'location': 'Rome, GA',

    'home_page_url': 'http://www.romefloyd.com',
    'bids_page_url': 'http://www.romefloyd.com/Administration/BidsandRFPs/RomeCity/tabid/491/agentType/ViewSearch/CustomFieldIDs/9/SearchValues/Open/sortBy/Type/sortDir/Ascending/Default.aspx'
}

class RomeGaBidScraper(BidScraper):
    def __init__(self):
        super(RomeGaBidScraper, self).__init__(GOVINFO)

    def scrape_bid_links(self, url):
        bids = []

        self.br.open(url)

        s = soupify(self.br.response().read())
        r = re.compile(r'/View/PropertyID/\d+/')

        for a in s.findAll('a', href=r):
            bid = Bid(org=self.org)
            bid.title = a.text
            bid.url = urlparse.urljoin(self.br.geturl(), a['href'])
            bid.location = self.org.location
            bids.append(bid)

        return bids

def get_scraper():
    return RomeGaBidScraper()

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()
