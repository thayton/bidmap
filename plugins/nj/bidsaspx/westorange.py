from bidmap.bidscrapers.bidsaspx.bidsaspx import BidsAspxBidScraper

GOVINFO = {
    'name': 'West Orange New Jersey',
    'location': 'West Orange, NJ',

    'home_page_url': 'http://www.westorange.org',
    'bids_page_url': 'http://www.westorange.org/Bids.aspx'
}

def get_scraper():
    return BidsAspxBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()



