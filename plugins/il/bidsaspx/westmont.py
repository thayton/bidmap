from bidmap.bidscrapers.bidsaspx.bidsaspx import BidsAspxBidScraper

GOVINFO = {
    'name': 'Westmont Illinois',
    'location': 'Westmont, IL',

    'home_page_url': 'http://www.westmont.illinois.gov',
    'bids_page_url': 'http://www.westmont.illinois.gov/bids.aspx'
}

def get_scraper():
    return BidsAspxBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()



