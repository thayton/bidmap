from bidmap.bidscrapers.bidsaspx.bidsaspx import BidsAspxBidScraper

GOVINFO = {
    'name': 'Missouri City Texas',
    'location': 'Missouri City, TX',

    'home_page_url': 'http://www.missouricitytx.gov',
    'bids_page_url': 'http://www.missouricitytx.gov/Bids.aspx'
}

def get_scraper():
    return BidsAspxBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()



