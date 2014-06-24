from bidmap.bidscrapers.bidsaspx.bidsaspx import BidsAspxBidScraper

GOVINFO = {
    'name': 'Sierra County California',
    'location': 'Downieville, CA',

    'home_page_url': 'http://www.sierracounty.ca.gov',
    'bids_page_url': 'http://www.sierracounty.ca.gov/bids.aspx'
}

def get_scraper():
    return BidsAspxBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()



