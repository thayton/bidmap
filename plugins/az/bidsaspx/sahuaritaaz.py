from bidmap.bidscrapers.bidsaspx.bidsaspx import BidsAspxBidScraper

GOVINFO = {
    'name': 'Sahuarita Arizona',
    'location': 'Sahuarita, AZ',

    'home_page_url': 'http://sahuaritaaz.gov',
    'bids_page_url': 'http://sahuaritaaz.gov/Bids.aspx'
}

def get_scraper():
    return BidsAspxBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()



