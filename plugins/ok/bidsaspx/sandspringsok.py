from bidmap.bidscrapers.bidsaspx.bidsaspx import BidsAspxBidScraper

GOVINFO = {
    'name': 'Sand Springs Oklahoma',
    'location': 'Sand Springs, OK',

    'home_page_url': 'http://www.sandspringsok.org',
    'bids_page_url': 'http://www.sandspringsok.org/Bids.aspx'
}

def get_scraper():
    return BidsAspxBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()



