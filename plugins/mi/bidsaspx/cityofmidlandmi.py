from bidmap.bidscrapers.bidsaspx.bidsaspx import BidsAspxBidScraper

GOVINFO = {
    'name': 'City of Midland Michigan',
    'location': 'Midland, MI',

    'home_page_url': 'http://www.cityofmidlandmi.gov',
    'bids_page_url': 'http://www.cityofmidlandmi.gov/bids.aspx'
}

def get_scraper():
    return BidsAspxBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()



