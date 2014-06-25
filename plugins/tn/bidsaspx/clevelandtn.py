from bidmap.bidscrapers.bidsaspx.bidsaspx import BidsAspxBidScraper

GOVINFO = {
    'name': 'Cleveland Tennessee',
    'location': 'Cleveland, TN',

    'home_page_url': 'http://clevelandtn.gov',
    'bids_page_url': 'http://clevelandtn.gov/Bids.aspx'
}

def get_scraper():
    return BidsAspxBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()



