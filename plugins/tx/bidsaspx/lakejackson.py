from bidmap.bidscrapers.bidsaspx.bidsaspx import BidsAspxBidScraper

GOVINFO = {
    'name': 'Lake Jackson Texas',
    'location': 'Lake Jackson, TX',

    'home_page_url': 'http://www.lakejackson-tx.gov',
    'bids_page_url': 'http://www.lakejackson-tx.gov/Bids.aspx'
}

def get_scraper():
    return BidsAspxBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()



