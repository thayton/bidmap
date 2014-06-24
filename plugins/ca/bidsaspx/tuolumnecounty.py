from bidmap.bidscrapers.bidsaspx.bidsaspx import BidsAspxBidScraper

GOVINFO = {
    'name': 'Tuolumne County California',
    'location': 'Sonora, CA',

    'home_page_url': 'http://www.tuolumnecounty.ca.gov',
    'bids_page_url': 'http://www.tuolumnecounty.ca.gov/bids.aspx'
}

def get_scraper():
    return BidsAspxBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()



