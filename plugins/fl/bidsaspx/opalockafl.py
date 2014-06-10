from bidmap.bidscrapers.bidsaspx.bidsaspx import BidsAspxBidScraper

GOVINFO = {
    'name': 'Opa Locka Florida',
    'location': 'Opa Locka, FL',

    'home_page_url': 'http://www.opalockafl.gov',
    'bids_page_url': 'http://www.opalockafl.gov/bids.aspx'
}

def get_scraper():
    return BidsAspxBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()



