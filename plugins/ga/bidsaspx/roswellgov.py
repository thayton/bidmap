from bidmap.bidscrapers.bidsaspx.bidsaspx import BidsAspxBidScraper

GOVINFO = {
    'name': 'City of Roswell, Georgia',
    'location': 'Roswell, GA',

    'home_page_url': 'http://www.roswellgov.com',
    'bids_page_url': 'http://www.roswellgov.com/bids.aspx'
}

def get_scraper():
    return BidsAspxBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()



