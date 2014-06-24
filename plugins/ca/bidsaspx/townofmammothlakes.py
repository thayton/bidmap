from bidmap.bidscrapers.bidsaspx.bidsaspx import BidsAspxBidScraper

GOVINFO = {
    'name': 'Town of Mammoth Lakes California',
    'location': 'Mammoth Lakes, CA',

    'home_page_url': 'http://www.townofmammothlakes.ca.gov',
    'bids_page_url': 'http://www.townofmammothlakes.ca.gov/Bids.aspx'
}

def get_scraper():
    return BidsAspxBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()



