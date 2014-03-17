from bidmap.bidscrapers.bidsaspx.bidsaspx import BidsAspxBidScraper

GOVINFO = {
    'name': 'Charleston South Carolina',
    'location': 'Charleston, SC',

    'home_page_url': 'http://www.charleston-sc.gov',
    'bids_page_url': 'http://www.charleston-sc.gov/Bids.aspx'
}

def get_scraper():
    return BidsAspxBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()



