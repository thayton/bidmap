from bidmap.bidscrapers.bidsaspx.bidsaspx import BidsAspxBidScraper

GOVINFO = {
    'name': 'Lakeland Tennessee',
    'location': 'Lakeland, TN',

    'home_page_url': 'http://www.lakelandtn.gov',
    'bids_page_url': 'http://www.lakelandtn.gov/Bids.aspx'
}

def get_scraper():
    return BidsAspxBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()


