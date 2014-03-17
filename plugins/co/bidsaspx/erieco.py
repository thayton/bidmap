from bidmap.bidscrapers.bidsaspx.bidsaspx import BidsAspxBidScraper

GOVINFO = {
    'name': 'Erie Colorado',
    'location': 'Erie, CO',

    'home_page_url': 'http://www.erieco.gov',
    'bids_page_url': 'http://www.erieco.gov/Bids.aspx'
}

def get_scraper():
    return BidsAspxBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()



