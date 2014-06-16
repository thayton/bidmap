from bidmap.bidscrapers.bidsaspx.bidsaspx import BidsAspxBidScraper

GOVINFO = {
    'name': 'Concord New Hampshire',
    'location': 'Concord, NH',

    'home_page_url': 'http://concordnh.gov',
    'bids_page_url': 'http://concordnh.gov/bids.aspx'
}

def get_scraper():
    return BidsAspxBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()



