from bidmap.bidscrapers.bidsaspx.bidsaspx import BidsAspxBidScraper

GOVINFO = {
    'name': 'City of Safford Arizona',
    'location': 'Safford, AZ',

    'home_page_url': 'http://www.cityofsafford.us',
    'bids_page_url': 'http://www.cityofsafford.us/bids.aspx'
}

def get_scraper():
    return BidsAspxBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()



