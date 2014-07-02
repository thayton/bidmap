from bidmap.bidscrapers.bidsaspx.bidsaspx import BidsAspxBidScraper

GOVINFO = {
    'name': 'Roanoke Texas',
    'location': 'Roanoke, TX',

    'home_page_url': 'http://www.roanoketexas.com',
    'bids_page_url': 'http://www.roanoketexas.com/Bids.aspx'
}

def get_scraper():
    return BidsAspxBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()



