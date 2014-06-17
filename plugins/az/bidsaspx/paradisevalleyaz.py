from bidmap.bidscrapers.bidsaspx.bidsaspx import BidsAspxBidScraper

GOVINFO = {
    'name': 'Paradise Valley Arizona',
    'location': 'Paradise Valley, AZ',

    'home_page_url': 'http://www.paradisevalleyaz.gov',
    'bids_page_url': 'http://www.paradisevalleyaz.gov/Bids.aspx'
}

def get_scraper():
    return BidsAspxBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()



