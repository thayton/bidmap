from bidmap.bidscrapers.bidsaspx.bidsaspx import BidsAspxBidScraper

GOVINFO = {
    'name': 'League City Texas',
    'location': 'League City, TX',

    'home_page_url': 'http://leaguecity-tx.gov',
    'bids_page_url': 'http://leaguecity-tx.gov/Bids.aspx'
}

def get_scraper():
    return BidsAspxBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()



