from bidmap.bidscrapers.bidsaspx.bidsaspx import BidsAspxBidScraper

GOVINFO = {
    'name': 'The Woodlands Township Texas',
    'location': 'The Woodlands, TX',

    'home_page_url': 'http://www.thewoodlandstownship-tx.gov',
    'bids_page_url': 'http://www.thewoodlandstownship-tx.gov/bids.aspx'
}

def get_scraper():
    return BidsAspxBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()



