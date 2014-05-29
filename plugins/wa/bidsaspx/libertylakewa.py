from bidmap.bidscrapers.bidsaspx.bidsaspx import BidsAspxBidScraper

GOVINFO = {
    'name': 'Liberty Lake Washington',
    'location': 'Liberty Lake, WA',

    'home_page_url': 'http://www.libertylakewa.gov',
    'bids_page_url': 'http://www.libertylakewa.gov/Bids.aspx'
}

def get_scraper():
    return BidsAspxBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()



