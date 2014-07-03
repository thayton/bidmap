from bidmap.bidscrapers.bidsaspx.bidsaspx import BidsAspxBidScraper

GOVINFO = {
    'name': 'City of Norcross Georgia',
    'location': 'Norcross, GA',

    'home_page_url': 'http://ga-norcross.civicplus.com',
    'bids_page_url': 'http://ga-norcross.civicplus.com/bids.aspx'
}

def get_scraper():
    return BidsAspxBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()



