from bidmap.bidscrapers.bidsaspx.bidsaspx import BidsAspxBidScraper

GOVINFO = {
    'name': 'Sunnyside Washington',
    'location': 'Sunnyside, WA',

    'home_page_url': 'http://www.sunnyside-wa.gov',
    'bids_page_url': 'http://www.sunnyside-wa.gov/bids.aspx'
}

def get_scraper():
    return BidsAspxBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()



