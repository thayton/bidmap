import re, urlparse

from bidmap.bidscrapers.bidscraper import BidScraper
from bidmap.htmlparse.soupify import soupify, get_all_text
from bidmap.txtextract.doctohtml import doctohtml

from bidmapdb.models import *

class DocBidScraper(BidScraper):
    def __init__(self, govinfo):
        super(DocBidScraper, self).__init__(govinfo)
        self.gov = govinfo

    def scrape_bid_description(self, bid):
        self.br.open(bid.url)

        d = self.br.response().read()
        s = soupify(doctohtml(d))

        bid.description = get_all_text(s.html.body)
        bid.save()
