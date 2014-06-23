from bidmap.bidscrapers.bidsaspx.bidsaspx import BidsAspxBidScraper

GOVINFO = {
    'name': 'Freeport New York',
    'location': 'Freeport, NY',

    'home_page_url': 'http://www.freeportny.gov',
    'bids_page_url': 'http://www.freeportny.gov/Bids.aspx'
}

def get_scraper():
    return BidsAspxBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()



