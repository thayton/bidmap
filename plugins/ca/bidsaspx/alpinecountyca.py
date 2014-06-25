from bidmap.bidscrapers.bidsaspx.bidsaspx import BidsAspxBidScraper

GOVINFO = {
    'name': 'Alpine County California',
    'location': 'Markleeville, CA',

    'home_page_url': 'http://www.alpinecountyca.gov',
    'bids_page_url': 'http://www.alpinecountyca.gov/bids.aspx'
}

def get_scraper():
    return BidsAspxBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()



