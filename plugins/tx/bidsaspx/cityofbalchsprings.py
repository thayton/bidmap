from bidmap.bidscrapers.bidsaspx.bidsaspx import BidsAspxBidScraper

GOVINFO = {
    'name': 'City of Balch Springs Texas',
    'location': 'Balch Springs, TX',

    'home_page_url': 'http://www.cityofbalchsprings.com',
    'bids_page_url': 'http://www.cityofbalchsprings.com/bids.aspx'
}

def get_scraper():
    return BidsAspxBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()



