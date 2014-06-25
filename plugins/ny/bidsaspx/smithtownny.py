from bidmap.bidscrapers.bidsaspx.bidsaspx import BidsAspxBidScraper

GOVINFO = {
    'name': 'Smithtown New York',
    'location': 'Smithtown, NY',

    'home_page_url': 'http://www.smithtownny.gov',
    'bids_page_url': 'http://www.smithtownny.gov/bids.aspx'
}

def get_scraper():
    return BidsAspxBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()



