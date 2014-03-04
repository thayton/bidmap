from bidmap.bidscrapers.bidsaspx.bidsaspx import BidsAspxBidScraper

GOVINFO = {
    'name': 'Cartersville Georgia',
    'location': 'Cartersville, GA',

    'home_page_url': 'http://ga-cartersville2.civiccities.com',
    'bids_page_url': 'http://ga-cartersville2.civiccities.com/bids.aspx'
}

def get_scraper():
    return BidsAspxBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()



