from bidmap.bidscrapers.bidsaspx.bidsaspx import BidsAspxBidScraper

GOVINFO = {
    'name': 'Ontario County New York',
    'location': 'Canandaigua, NY',

    'home_page_url': 'http://www.co.ontario.ny.us',
    'bids_page_url': 'http://www.co.ontario.ny.us/Bids.aspx'
}

def get_scraper():
    return BidsAspxBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()



