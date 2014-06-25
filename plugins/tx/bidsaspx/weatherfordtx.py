from bidmap.bidscrapers.bidsaspx.bidsaspx import BidsAspxBidScraper

GOVINFO = {
    'name': 'Weatherford Texas',
    'location': 'Weatherford, TX',

    'home_page_url': 'http://www.weatherfordtx.gov',
    'bids_page_url': 'http://www.weatherfordtx.gov/Bids.aspx'
}

def get_scraper():
    return BidsAspxBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()



