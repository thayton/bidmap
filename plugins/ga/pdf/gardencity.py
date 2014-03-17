import re, urlparse

from bid import Bid
from bidmap.bidscrapers.bidscraper import BidScraper
from bidmap.htmlparse.soupify import soupify

GOVINFO = {
    'name': 'Garden City Geogia',
    'location': 'Garden City, GA',

    'home_page_url': 'http://www.gardencity-ga.gov',
    'bids_page_url': 'http://www.gardencity-ga.gov/index.aspx?page=112'
}

class GardenCityGaBidScraper(BidScraper):
    def __init__(self):
        super(GardenCityGaBidScraper, self).__init__(GOVINFO)

    def scrape_bid_links(self, url):
        bids = []

        self.br.open(url)

        s = soupify(self.br.response().read())
        d = s.find('div', id=re.compile(r'^_ctl\d+_content$'))
        r = re.compile(r'^Modules/ShowDocument\.aspx\?documentid=\d+$')

        for a in d.findAll('a', href=r):
            bid = Bid()
            bid.title = a.text
            bid.url = urlparse.urljoin(self.br.geturl(), a['href'])
            bids.append(bid)

        return bids

def get_scraper():
    return GardenCityGaBidScraper()

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()
