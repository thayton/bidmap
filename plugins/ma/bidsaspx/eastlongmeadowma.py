from bidmap.bidscrapers.bidsaspx.bidsaspx import BidsAspxBidScraper

GOVINFO = {
    'name': 'East Longmeadow Massachusetts',
    'location': 'East Longmeadow, MA',

    'home_page_url': 'http://www.eastlongmeadowma.gov',
    'bids_page_url': 'http://www.eastlongmeadowma.gov/Bids.aspx'
}

def get_scraper():
    return BidsAspxBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()



