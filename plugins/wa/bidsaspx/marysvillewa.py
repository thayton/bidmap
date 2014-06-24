from bidmap.bidscrapers.bidsaspx.bidsaspx import BidsAspxBidScraper

GOVINFO = {
    'name': 'Marysville Washington',
    'location': 'Marysville, WA',

    'home_page_url': 'http://www.marysvillewa.gov',
    'bids_page_url': 'http://www.marysvillewa.gov/Bids.aspx'
}

def get_scraper():
    return BidsAspxBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()



