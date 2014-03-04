from bidmap.bidscrapers.bidsaspx.bidsaspx import BidsAspxBidScraper

GOVINFO = {
    'name': 'Norfolk City Government',
    'location': 'Norfolk, VA',

    'home_page_url': 'http://www.norfolk.gov',
    'bids_page_url': 'http://www.norfolk.gov/bids.aspx'
}

def get_scraper():
    return BidsAspxBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()



