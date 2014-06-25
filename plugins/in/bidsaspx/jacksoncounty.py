from bidmap.bidscrapers.bidsaspx.bidsaspx import BidsAspxBidScraper

GOVINFO = {
    'name': 'Jackson County Indiana',
    'location': 'Brownstown, IN',

    'home_page_url': 'http://www.jacksoncounty.in.gov',
    'bids_page_url': 'http://www.jacksoncounty.in.gov/Bids.aspx'
}

def get_scraper():
    return BidsAspxBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()



