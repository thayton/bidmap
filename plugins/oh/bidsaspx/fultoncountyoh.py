from bidmap.bidscrapers.bidsaspx.bidsaspx import BidsAspxBidScraper

GOVINFO = {
    'name': 'Fulton County Ohio',
    'location': 'Wauseon, OH',

    'home_page_url': 'http://www.fultoncountyoh.com',
    'bids_page_url': 'http://www.fultoncountyoh.com/bids.aspx'
}

def get_scraper():
    return BidsAspxBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()



