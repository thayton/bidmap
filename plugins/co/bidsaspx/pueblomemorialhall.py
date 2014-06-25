from bidmap.bidscrapers.bidsaspx.bidsaspx import BidsAspxBidScraper

GOVINFO = {
    'name': 'Pueblo Memorial Hall Colorado',
    'location': 'Pueblo, CO',

    'home_page_url': 'http://pueblomemorialhall.com',
    'bids_page_url': 'http://pueblomemorialhall.com/Bids.aspx'
}

def get_scraper():
    return BidsAspxBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()



