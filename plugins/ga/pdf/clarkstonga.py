import re, urlparse

from bid import Bid
from bidmap.bidscrapers.bidscraper import BidScraper
from bidmap.htmlparse.soupify import soupify

GOVINFO = {
    'name': 'Clarkston Geogia',
    'location': 'Clarkston, GA',

    'home_page_url': 'http://www.clarkstonga.gov',
    'bids_page_url': 'http://www.clarkstonga.gov/index.php/business/request-for-proposals-quotes-rfp-rfq'
}

class ClarkstonGaBidScraper(BidScraper):
    def __init__(self):
        super(ClarkstonGaBidScraper, self).__init__(GOVINFO)

    def scrape_bid_links(self, url):
        bids = []

        self.br.open(url)

        s = soupify(self.br.response().read())
        r = re.compile(r'/index\.php/i-want-to/get-resource-documents/category/')
        d = s.find('div', id='ja-content-main')
        z = re.compile(r'\s*\(Concluded\)', re.I)

        for a in d.findAll('a', href=r):
            if re.search(z, a.text):
                continue

            bid = Bid()
            bid.title = a.text
            bid.url = urlparse.urljoin(self.br.geturl(), a['href'])
            bids.append(bid)

        return bids

def get_scraper():
    return ClarkstonGaBidScraper()

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()
