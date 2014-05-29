from bidmap.bidscrapers.bidsaspx.bidsaspx import BidsAspxBidScraper

GOVINFO = {
    'name': 'Desoto County',
    'location': 'Hernando, MS',

    'home_page_url': 'http://www.desotocountyms.gov',
    'bids_page_url': 'http://www.desotocountyms.gov/Bids.aspx'
}

def get_scraper():
    return BidsAspxBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()



