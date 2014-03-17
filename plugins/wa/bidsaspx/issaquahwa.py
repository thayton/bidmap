from bidmap.bidscrapers.bidsaspx.bidsaspx import BidsAspxBidScraper

GOVINFO = {
    'name': 'Issaquah Washington',
    'location': 'Issaquah, WA',

    'home_page_url': 'http://www.issaquahwa.gov',
    'bids_page_url': 'http://www.issaquahwa.gov/Bids.aspx'
}

def get_scraper():
    return BidsAspxBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()



