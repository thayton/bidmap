from bidmap.bidscrapers.bidsaspx.bidsaspx import BidsAspxBidScraper

GOVINFO = {
    'name': 'Plainview Texas',
    'location': 'Plainview, TX',

    'home_page_url': 'http://www.plainviewtx.org',
    'bids_page_url': 'http://www.plainviewtx.org/Bids.aspx'
}

def get_scraper():
    return BidsAspxBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()



