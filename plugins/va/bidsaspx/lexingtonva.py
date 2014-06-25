from bidmap.bidscrapers.bidsaspx.bidsaspx import BidsAspxBidScraper

GOVINFO = {
    'name': 'Lexington Virginia',
    'location': 'Lexington, VA',

    'home_page_url': 'http://www.lexingtonva.gov',
    'bids_page_url': 'http://www.lexingtonva.gov/Bids.aspx'
}

def get_scraper():
    return BidsAspxBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()



