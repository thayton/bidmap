from bidmap.bidscrapers.bidsaspx.bidsaspx import BidsAspxBidScraper

GOVINFO = {
    'name': 'Washington State Parks',
    'location': 'East Wenatchee, WA',

    'home_page_url': 'http://www.parks.wa.gov',
    'bids_page_url': 'http://www.parks.wa.gov/Bids.aspx'
}

def get_scraper():
    return BidsAspxBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()



