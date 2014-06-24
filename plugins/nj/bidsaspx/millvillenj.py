from bidmap.bidscrapers.bidsaspx.bidsaspx import BidsAspxBidScraper

GOVINFO = {
    'name': 'Millville New Jersey',
    'location': 'Millville, NJ',

    'home_page_url': 'http://www.millvillenj.gov',
    'bids_page_url': 'http://www.millvillenj.gov/bids.aspx'
}

def get_scraper():
    return BidsAspxBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()



