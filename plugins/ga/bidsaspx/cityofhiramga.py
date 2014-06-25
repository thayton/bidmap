from bidmap.bidscrapers.bidsaspx.bidsaspx import BidsAspxBidScraper

GOVINFO = {
    'name': 'City of Hiram Georgia',
    'location': 'Hiram, GA',

    'home_page_url': 'http://www.cityofhiramga.gov',
    'bids_page_url': 'http://www.cityofhiramga.gov/Bids.aspx'
}

def get_scraper():
    return BidsAspxBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()



