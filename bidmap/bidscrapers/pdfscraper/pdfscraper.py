import re, urlparse

from bidmap.bidscrapers.bidscraper import BidScraper
from bidmap.htmlparse.soupify import soupify, get_all_text
from bidmap.txtextract.pdftohtml import pdftohtml

from bidmapdb.models import *

class PdfBidScraper(BidScraper):
    def __init__(self, govinfo):
        super(PdfBidScraper, self).__init__(govinfo)
        self.gov = govinfo

    def scrape_bid_description(self, bid):
        self.br.open(bid.url)

        d = self.br.response().read()
        s = soupify(pdftohtml(d))

        bid.description = get_all_text(s.html.body)
        bid.save()
