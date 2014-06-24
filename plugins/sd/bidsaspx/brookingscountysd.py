from bidmap.bidscrapers.bidsaspx.bidsaspx import BidsAspxBidScraper

GOVINFO = {
    'name': 'Brookings County South Dakota',
    'location': 'Brookings, SD',

    'home_page_url': 'http://www.brookingscountysd.gov',
    'bids_page_url': 'http://www.brookingscountysd.gov/Bids.aspx'
}

def get_scraper():
    return BidsAspxBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()



