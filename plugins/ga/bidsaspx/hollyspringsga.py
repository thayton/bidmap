from bidmap.bidscrapers.bidsaspx.bidsaspx import BidsAspxBidScraper

GOVINFO = {
    'name': 'Holly Springs Georgia',
    'location': 'Holly Springs, GA',

    'home_page_url': 'http://www.hollyspringsga.us',
    'bids_page_url': 'http://www.hollyspringsga.us/bids.aspx'
}

def get_scraper():
    return BidsAspxBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()



