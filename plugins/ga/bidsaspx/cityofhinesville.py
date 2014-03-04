from bidmap.bidscrapers.bidsaspx.bidsaspx import BidsAspxBidScraper

GOVINFO = {
    'name': 'City Of Hinesville',
    'location': 'Hinesville, GA',

    'home_page_url': 'http://www.cityofhinesville.org',
    'bids_page_url': 'http://www.cityofhinesville.org/bids.aspx'
}

def get_scraper():
    return BidsAspxBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()



