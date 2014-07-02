from bidmap.bidscrapers.bidsaspx.bidsaspx import BidsAspxBidScraper

GOVINFO = {
    'name': 'Ravalli County Montana',
    'location': 'Hamilton, MT',

    'home_page_url': 'http://ravalli.us',
    'bids_page_url': 'http://ravalli.us/Bids.aspx'
}

def get_scraper():
    return BidsAspxBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()



