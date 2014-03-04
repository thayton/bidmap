from bidmap.bidscrapers.bidsaspx.bidsaspx import BidsAspxBidScraper

GOVINFO = {
    'name': 'Warner Robins Georgia',
    'location': 'Warner Robins, GA',

    'home_page_url': 'http://www.wrga.gov',
    'bids_page_url': 'http://www.wrga.gov/Bids.aspx'
}

def get_scraper():
    return BidsAspxBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()



