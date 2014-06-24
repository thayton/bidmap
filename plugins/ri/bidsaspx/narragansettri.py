from bidmap.bidscrapers.bidsaspx.bidsaspx import BidsAspxBidScraper

GOVINFO = {
    'name': 'Narragansett Rhode Island',
    'location': 'Narragansett, RI',

    'home_page_url': 'http://www.narragansettri.gov',
    'bids_page_url': 'http://www.narragansettri.gov/bids.aspx'
}

def get_scraper():
    return BidsAspxBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()



