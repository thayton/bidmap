from bidmap.bidscrapers.bidsaspx.bidsaspx import BidsAspxBidScraper

GOVINFO = {
    'name': 'City of New Port Richey Florida',
    'location': 'New Port Richey, FL',

    'home_page_url': 'http://cityofnewportrichey.org',
    'bids_page_url': 'http://cityofnewportrichey.org/bids.aspx'
}

def get_scraper():
    return BidsAspxBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()



