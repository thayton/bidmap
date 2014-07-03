from bidmap.bidscrapers.bidsaspx.bidsaspx import BidsAspxBidScraper

GOVINFO = {
    'name': 'Lake Stevens Washington',
    'location': 'Lake Stevens, WA',

    'home_page_url': 'http://www.ci.lake-stevens.wa.us',
    'bids_page_url': 'http://www.ci.lake-stevens.wa.us/Bids.aspx'
}

def get_scraper():
    return BidsAspxBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()



