from bidmap.bidscrapers.bidsaspx.bidsaspx import BidsAspxBidScraper

GOVINFO = {
    'name': 'Rockville Maryland',
    'location': 'Rockville, MD',

    'home_page_url': 'http://www.rockvillemd.gov',
    'bids_page_url': 'http://www.rockvillemd.gov/bids.aspx'
}

def get_scraper():
    return BidsAspxBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()



