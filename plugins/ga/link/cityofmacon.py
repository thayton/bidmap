import re, urlparse, mechanize, datetime

from bidmap.bidscrapers.bidscraper import BidScraper
from bidmap.htmlparse.soupify import soupify, get_all_text

from bidmapdb.models import *

GOVINFO = {
    'name': 'City of Macon',
    'location': 'Macon, GA',

    'home_page_url': 'http://www.cityofmacon.net',
    'bids_page_url': 'http://www.cityofmacon.net/bids'
}

class MaconGaBidScraper(BidScraper):
    def __init__(self):
        super(MaconGaBidScraper, self).__init__(GOVINFO)

    def scrape_bid_links(self, url):
        bids = []

        self.br.open(url)

        pageno = 2
        done = False

        while True:
            s = soupify(self.br.response().read())
            r = re.compile(r'^/node/\d+$')

            for a in s.findAll('a', href=r):
                li = a.findParent('li')
                x = {'class': 'views-field-title'}
                title_div = li.find('div', attrs=x)

                y = {'class': 'views-field-field-closing-date-value'}
                closing_date_div = li.find('div', attrs=y)

                z = re.compile(r'(\d{2})/(\d{2})/(\d{4})')
                x = re.search(z, closing_date_div.span.text)

                # Stop once we start seeing bids whose closing date is later
                # than the current date
                m,d,y = [int(n) for n in x.groups()]

                closing_date = datetime.date(y,m,d)
                today = datetime.date.today()

                # If we've passed the closing date we're done
                if today > closing_date:
                    done = True
                    break

                bid = Bid(org=self.org)
                bid.title = title_div.span.text
                bid.url = urlparse.urljoin(self.br.geturl(), a['href'])
                bid.location = self.org.location
                bids.append(bid)

            if done:
                break

            try:
                self.br.follow_link(self.br.find_link(text='%d' % pageno))
                pageno += 1
            except mechanize.LinkNotFoundError:
                break

        return bids

def get_scraper():
    return MaconGaBidScraper()

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()
