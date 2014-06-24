from bidmap.bidscrapers.bidsaspx.bidsaspx import BidsAspxBidScraper

GOVINFO = {
    'name': 'Bainbridge Washington',
    'location': 'Bainbridge, WA',

    'home_page_url': 'http://www.bainbridgewa.gov',
    'bids_page_url': 'http://www.bainbridgewa.gov/bids.aspx'
}

def get_scraper():
    return BidsAspxBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()



