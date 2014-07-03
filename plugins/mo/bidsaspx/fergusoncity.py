from bidmap.bidscrapers.bidsaspx.bidsaspx import BidsAspxBidScraper

GOVINFO = {
    'name': 'Ferguson City Missouri',
    'location': 'Ferguson City, MO',

    'home_page_url': 'http://www.fergusoncity.com',
    'bids_page_url': 'http://www.fergusoncity.com/Bids.aspx'
}

def get_scraper():
    return BidsAspxBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()



