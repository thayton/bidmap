from bidmap.bidscrapers.bidsaspx.bidsaspx import BidsAspxBidScraper

GOVINFO = {
    'name': 'Waynesboro Georgia',
    'location': 'Waynesboro, GA',

    'home_page_url': 'http://www.waynesboroga.com',
    'bids_page_url': 'http://www.waynesboroga.com/Bids.aspx'
}

def get_scraper():
    return BidsAspxBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()



