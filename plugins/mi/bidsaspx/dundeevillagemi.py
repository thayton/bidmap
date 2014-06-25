from bidmap.bidscrapers.bidsaspx.bidsaspx import BidsAspxBidScraper

GOVINFO = {
    'name': 'Dundee Village Michigan',
    'location': 'Dundee, MI',

    'home_page_url': 'http://dundeevillagemi.gov',
    'bids_page_url': 'http://dundeevillagemi.gov/Bids.aspx'
}

def get_scraper():
    return BidsAspxBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()



