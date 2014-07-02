from bidmap.bidscrapers.bidsaspx.bidsaspx import BidsAspxBidScraper

GOVINFO = {
    'name': 'Chester County Pennsylvania',
    'location': 'West Chester, PA',

    'home_page_url': 'http://www.chesco.org',
    'bids_page_url': 'http://www.chesco.org/Bids.aspx'
}

def get_scraper():
    return BidsAspxBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()



