from bidmap.bidscrapers.bidsaspx.bidsaspx import BidsAspxBidScraper

GOVINFO = {
    'name': 'City of Alliance Ohio',
    'location': 'Alliance, OH',

    'home_page_url': 'http://www.cityofalliance.com',
    'bids_page_url': 'http://www.cityofalliance.com/bids.aspx'
}

def get_scraper():
    return BidsAspxBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()



