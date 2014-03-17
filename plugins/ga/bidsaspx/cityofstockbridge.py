from bidmap.bidscrapers.bidsaspx.bidsaspx import BidsAspxBidScraper

GOVINFO = {
    'name': 'City of Stockbridge Georgia',
    'location': 'Stockbridge, GA',

    'home_page_url': 'http://www.cityofstockbridge-ga.gov',
    'bids_page_url': 'http://www.cityofstockbridge-ga.gov/bids.aspx'
}

def get_scraper():
    return BidsAspxBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()



