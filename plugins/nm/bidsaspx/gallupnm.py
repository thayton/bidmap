from bidmap.bidscrapers.bidsaspx.bidsaspx import BidsAspxBidScraper

GOVINFO = {
    'name': 'Gallup New Mexico',
    'location': 'Gallup, NM',

    'home_page_url': 'http://www.gallupnm.gov',
    'bids_page_url': 'http://www.gallupnm.gov/Bids.aspx'
}

def get_scraper():
    return BidsAspxBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()



