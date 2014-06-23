from bidmap.bidscrapers.bidsaspx.bidsaspx import BidsAspxBidScraper

GOVINFO = {
    'name': 'Mission Hills Kansas',
    'location': 'Mission Hills, KS',

    'home_page_url': 'http://www.missionhillsks.gov',
    'bids_page_url': 'http://www.missionhillsks.gov/Bids.aspx'
}

def get_scraper():
    return BidsAspxBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()



