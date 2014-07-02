from bidmap.bidscrapers.bidsaspx.bidsaspx import BidsAspxBidScraper

GOVINFO = {
    'name': 'Claremore City Oklahoma',
    'location': 'Claremore City, OK',

    'home_page_url': 'http://www.claremorecity.com',
    'bids_page_url': 'http://www.claremorecity.com/Bids.aspx'
}

def get_scraper():
    return BidsAspxBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()



