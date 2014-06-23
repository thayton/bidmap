from bidmap.bidscrapers.bidsaspx.bidsaspx import BidsAspxBidScraper

GOVINFO = {
    'name': 'Belton Texas',
    'location': 'Belton, TX',

    'home_page_url': 'http://www.beltontexas.gov',
    'bids_page_url': 'http://www.beltontexas.gov/bids.aspx'
}

def get_scraper():
    return BidsAspxBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()



