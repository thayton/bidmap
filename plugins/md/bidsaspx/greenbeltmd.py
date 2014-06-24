from bidmap.bidscrapers.bidsaspx.bidsaspx import BidsAspxBidScraper

GOVINFO = {
    'name': 'Greenbelt Maryland',
    'location': 'Greenbelt, MD',

    'home_page_url': 'http://www.greenbeltmd.gov',
    'bids_page_url': 'http://www.greenbeltmd.gov/Bids.aspx'
}

def get_scraper():
    return BidsAspxBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()



