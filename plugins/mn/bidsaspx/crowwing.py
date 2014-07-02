from bidmap.bidscrapers.bidsaspx.bidsaspx import BidsAspxBidScraper

GOVINFO = {
    'name': 'Crow Wing County Minnesota',
    'location': 'Brainerd, MN',

    'home_page_url': 'http://www.crowwing.us',
    'bids_page_url': 'http://www.crowwing.us/bids.aspx'
}

def get_scraper():
    return BidsAspxBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()



