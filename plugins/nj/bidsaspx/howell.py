from bidmap.bidscrapers.bidsaspx.bidsaspx import BidsAspxBidScraper

GOVINFO = {
    'name': 'Howell New Jersey',
    'location': 'Howell, NJ',

    'home_page_url': 'http://www.twp.howell.nj.us',
    'bids_page_url': 'http://www.twp.howell.nj.us/bids.aspx'
}

def get_scraper():
    return BidsAspxBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()



