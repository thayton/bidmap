from bidmap.bidscrapers.bidsaspx.bidsaspx import BidsAspxBidScraper

GOVINFO = {
    'name': 'Millington Tennessee',
    'location': 'Millington, TN',

    'home_page_url': 'http://www.millingtontn.gov',
    'bids_page_url': 'http://www.millingtontn.gov/bids.aspx'
}

def get_scraper():
    return BidsAspxBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()



