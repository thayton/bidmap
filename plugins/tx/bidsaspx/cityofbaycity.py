from bidmap.bidscrapers.bidsaspx.bidsaspx import BidsAspxBidScraper

GOVINFO = {
    'name': 'City of Bay City Texas',
    'location': 'Bay City, TX',

    'home_page_url': 'http://www.cityofbaycity.org',
    'bids_page_url': 'http://www.cityofbaycity.org/Bids.aspx'
}

def get_scraper():
    return BidsAspxBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()



