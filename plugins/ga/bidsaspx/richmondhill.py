from bidmap.bidscrapers.bidsaspx.bidsaspx import BidsAspxBidScraper

GOVINFO = {
    'name': 'Richmond Hill Georgia',
    'location': 'Richmond Hill, GA',

    'home_page_url': 'http://www.richmondhill-ga.gov',
    'bids_page_url': 'http://www.richmondhill-ga.gov/Bids.aspx'
}

def get_scraper():
    return BidsAspxBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()



