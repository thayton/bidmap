from bidmap.bidscrapers.bidsaspx.bidsaspx import BidsAspxBidScraper

GOVINFO = {
    'name': 'Morgan County Georgia',
    'location': 'Madison, GA',

    'home_page_url': 'http://www.morganga.org',
    'bids_page_url': 'http://www.morganga.org/bids.aspx'
}

def get_scraper():
    return BidsAspxBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()



