from bidmap.bidscrapers.bidview.bidview import BidViewBidScraper

GOVINFO = {
    'name': 'Maryville Missouri',
    'location': 'Maryville, MO',

    'home_page_url': 'http://www.maryville.org',
    'bids_page_url': 'http://www.maryville.org/bids.aspx'
}

def get_scraper():
    return BidViewBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()
