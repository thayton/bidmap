from bidmap.bidscrapers.bidsaspx.bidsaspx import BidsAspxBidScraper

GOVINFO = {
    'name': 'Des Moines Washington',
    'location': 'Des Moines, WA',

    'home_page_url': 'http://www.desmoineswa.gov',
    'bids_page_url': 'http://www.desmoineswa.gov/Bids.aspx'
}

def get_scraper():
    return BidsAspxBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()



