from bidmap.bidscrapers.bidsaspx.bidsaspx import BidsAspxBidScraper

GOVINFO = {
    'name': 'Warsaw Indiana',
    'location': 'Warsaw, IN',

    'home_page_url': 'http://www.warsaw.in.gov',
    'bids_page_url': 'http://www.warsaw.in.gov/Bids.aspx'
}

def get_scraper():
    return BidsAspxBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()



