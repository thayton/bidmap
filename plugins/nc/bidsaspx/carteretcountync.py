from bidmap.bidscrapers.bidsaspx.bidsaspx import BidsAspxBidScraper

GOVINFO = {
    'name': 'Carteret County North Carolina',
    'location': 'Beaufort, NC',

    'home_page_url': 'http://www.carteretcountync.gov',
    'bids_page_url': 'http://www.carteretcountync.gov/Bids.aspx'
}

def get_scraper():
    return BidsAspxBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()



