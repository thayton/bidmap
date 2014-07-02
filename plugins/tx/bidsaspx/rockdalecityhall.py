from bidmap.bidscrapers.bidsaspx.bidsaspx import BidsAspxBidScraper

GOVINFO = {
    'name': 'Rockdale City Hall Texas',
    'location': 'Rockdale, TX',

    'home_page_url': 'http://www.rockdalecityhall.com',
    'bids_page_url': 'http://www.rockdalecityhall.com/bids.aspx'
}

def get_scraper():
    return BidsAspxBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()



