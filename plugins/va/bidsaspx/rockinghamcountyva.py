from bidmap.bidscrapers.bidsaspx.bidsaspx import BidsAspxBidScraper

GOVINFO = {
    'name': 'Rockingham County',
    'location': 'Harrisonburg, VA',

    'home_page_url': 'http://www.rockinghamcountyva.gov',
    'bids_page_url': 'http://www.rockinghamcountyva.gov/Bids.aspx'
}

def get_scraper():
    return BidsAspxBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()



