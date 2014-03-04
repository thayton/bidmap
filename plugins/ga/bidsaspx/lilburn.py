from bidmap.bidscrapers.bidsaspx.bidsaspx import BidsAspxBidScraper

GOVINFO = {
    'name': 'City of Lilburn',
    'location': 'Lilburn, GA',

    'home_page_url': 'http://www.cityoflilburn.com',
    'bids_page_url': 'http://www.cityoflilburn.com/Bids.aspx'
}

def get_scraper():
    return BidsAspxBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()



