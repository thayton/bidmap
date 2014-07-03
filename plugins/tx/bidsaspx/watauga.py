from bidmap.bidscrapers.bidsaspx.bidsaspx import BidsAspxBidScraper

GOVINFO = {
    'name': 'Watauga Texas',
    'location': 'Watauga, TX',

    'home_page_url': 'http://www.ci.watauga.tx.us/',
    'bids_page_url': 'http://www.ci.watauga.tx.us/Bids.aspx'
}

def get_scraper():
    return BidsAspxBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()



