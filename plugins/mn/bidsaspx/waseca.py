from bidmap.bidscrapers.bidsaspx.bidsaspx import BidsAspxBidScraper

GOVINFO = {
    'name': 'Waseca County Minnesota',
    'location': 'Waseca, MN',

    'home_page_url': 'http://www.co.waseca.mn.us',
    'bids_page_url': 'http://www.co.waseca.mn.us/bids.aspx'
}

def get_scraper():
    return BidsAspxBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()



