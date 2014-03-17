from bidmap.bidscrapers.bidsaspx.bidsaspx import BidsAspxBidScraper

GOVINFO = {
    'name': 'Coconino Arizona',
    'location': 'Coconino, AZ',

    'home_page_url': 'http://www.coconino.az.gov',
    'bids_page_url': 'http://www.coconino.az.gov/Bids.aspx'
}

def get_scraper():
    return BidsAspxBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()



