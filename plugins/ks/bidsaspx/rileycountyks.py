from bidmap.bidscrapers.bidsaspx.bidsaspx import BidsAspxBidScraper

GOVINFO = {
    'name': 'Riley County Kansas',
    'location': 'Manhattan, KS',

    'home_page_url': 'http://www.rileycountyks.gov',
    'bids_page_url': 'http://www.rileycountyks.gov/bids.aspx'
}

def get_scraper():
    return BidsAspxBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()



