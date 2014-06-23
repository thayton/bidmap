from bidmap.bidscrapers.bidsaspx.bidsaspx import BidsAspxBidScraper

GOVINFO = {
    'name': 'Knoxville Iowa',
    'location': 'Knoxville, IA',

    'home_page_url': 'http://www.knoxvilleia.gov',
    'bids_page_url': 'http://www.knoxvilleia.gov/Bids.aspx'
}

def get_scraper():
    return BidsAspxBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()



