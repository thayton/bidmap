from bidmap.bidscrapers.bidsaspx.bidsaspx import BidsAspxBidScraper

GOVINFO = {
    'name': 'Orange County Virginia',
    'location': 'Orange, VA',

    'home_page_url': 'http://orangecountyva.gov',
    'bids_page_url': 'http://orangecountyva.gov/Bids.aspx'
}

def get_scraper():
    return BidsAspxBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()



