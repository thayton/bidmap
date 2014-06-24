from bidmap.bidscrapers.bidsaspx.bidsaspx import BidsAspxBidScraper

GOVINFO = {
    'name': 'South Miami Florida',
    'location': 'South Miami, FL',

    'home_page_url': 'http://www.southmiamifl.gov',
    'bids_page_url': 'http://www.southmiamifl.gov/bids.aspx'
}

def get_scraper():
    return BidsAspxBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()



