from bidmap.bidscrapers.bidsaspx.bidsaspx import BidsAspxBidScraper

GOVINFO = {
    'name': 'Brookfield Wisconsin',
    'location': 'Brookfield, WI',

    'home_page_url': 'http://www.ci.brookfield.wi.us',
    'bids_page_url': 'http://www.ci.brookfield.wi.us/Bids.aspx'
}

def get_scraper():
    return BidsAspxBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()



