from bidmap.bidscrapers.bidsaspx.bidsaspx import BidsAspxBidScraper

GOVINFO = {
    'name': 'Hagerstown Maryland',
    'location': 'Hagerstown, MD',

    'home_page_url': 'http://www.hagerstownmd.org',
    'bids_page_url': 'http://www.hagerstownmd.org/Bids.aspx'
}

def get_scraper():
    return BidsAspxBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()



