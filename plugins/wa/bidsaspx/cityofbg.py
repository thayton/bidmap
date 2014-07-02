from bidmap.bidscrapers.bidsaspx.bidsaspx import BidsAspxBidScraper

GOVINFO = {
    'name': 'City of Battle Ground Washington',
    'location': 'Battle Ground, WA',

    'home_page_url': 'http://www.cityofbg.org',
    'bids_page_url': 'http://www.cityofbg.org/bids.aspx'
}

def get_scraper():
    return BidsAspxBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()



