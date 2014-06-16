from bidmap.bidscrapers.bidsaspx.bidsaspx import BidsAspxBidScraper

GOVINFO = {
    'name': 'Danville Virginia',
    'location': 'Danville, VA',

    'home_page_url': 'http://www.danville-va.gov',
    'bids_page_url': 'http://www.danville-va.gov/bids.aspx'
}

def get_scraper():
    return BidsAspxBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()



