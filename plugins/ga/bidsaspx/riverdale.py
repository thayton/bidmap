from bidmap.bidscrapers.bidsaspx.bidsaspx import BidsAspxBidScraper

GOVINFO = {
    'name': 'Riverdale Georgia',
    'location': 'Riverdale, GA',

    'home_page_url': 'http://ga-riverdale2.civicplus.com',
    'bids_page_url': 'http://ga-riverdale2.civicplus.com/bids.aspx'
}

def get_scraper():
    return BidsAspxBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()



