from bidmap.bidscrapers.bidsaspx.bidsaspx import BidsAspxBidScraper

GOVINFO = {
    'name': 'Malibu California',
    'location': 'Malibu, CA',

    'home_page_url': 'http://www.malibu-ca.gov',
    'bids_page_url': 'http://www.malibu-ca.gov/Bids.aspx'
}

def get_scraper():
    return BidsAspxBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()



