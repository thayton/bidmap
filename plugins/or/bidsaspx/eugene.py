from bidmap.bidscrapers.bidsaspx.bidsaspx import BidsAspxBidScraper

GOVINFO = {
    'name': 'Eugene Oregon',
    'location': 'Eugene, OR',

    'home_page_url': 'http://www.eugene-or.gov',
    'bids_page_url': 'http://www.eugene-or.gov/bids.aspx'
}

def get_scraper():
    return BidsAspxBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()



