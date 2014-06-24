from bidmap.bidscrapers.bidsaspx.bidsaspx import BidsAspxBidScraper

GOVINFO = {
    'name': 'Clayton Delaware',
    'location': 'Clayton, DE',

    'home_page_url': 'http://www.clayton.delaware.gov',
    'bids_page_url': 'http://www.clayton.delaware.gov/Bids.aspx'
}

def get_scraper():
    return BidsAspxBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()



