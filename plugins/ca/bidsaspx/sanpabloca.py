from bidmap.bidscrapers.bidsaspx.bidsaspx import BidsAspxBidScraper

GOVINFO = {
    'name': 'San Pablo California',
    'location': 'San Pablo, CA',

    'home_page_url': 'http://sanpabloca.gov',
    'bids_page_url': 'http://sanpabloca.gov/Bids.aspx'
}

def get_scraper():
    return BidsAspxBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()



