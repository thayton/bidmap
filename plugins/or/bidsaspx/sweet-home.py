from bidmap.bidscrapers.bidsaspx.bidsaspx import BidsAspxBidScraper

GOVINFO = {
    'name': 'Sweet Home Oregon',
    'location': 'Sweet Home, OR',

    'home_page_url': 'http://www.sweet-home.or.us',
    'bids_page_url': 'http://www.sweet-home.or.us/bids.aspx'
}

def get_scraper():
    return BidsAspxBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()



