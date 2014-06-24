from bidmap.bidscrapers.bidsaspx.bidsaspx import BidsAspxBidScraper

GOVINFO = {
    'name': 'Douglas County Nevada',
    'location': 'Minden, NV',

    'home_page_url': 'http://douglascountynv.gov',
    'bids_page_url': 'http://douglascountynv.gov/bids.aspx'
}

def get_scraper():
    return BidsAspxBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()



