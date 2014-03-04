from bidmap.bidscrapers.bidsaspx.bidsaspx import BidsAspxBidScraper

GOVINFO = {
    'name': 'The City of East Point',
    'location': 'East Point, GA',

    'home_page_url': 'http://ga-eastpoint.civicplus.com',
    'bids_page_url': 'http://ga-eastpoint.civicplus.com/bids.aspx'
}

def get_scraper():
    return BidsAspxBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()



