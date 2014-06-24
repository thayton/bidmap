from bidmap.bidscrapers.bidsaspx.bidsaspx import BidsAspxBidScraper

GOVINFO = {
    'name': 'City of Eudora Kansas',
    'location': 'Eudora, KS',

    'home_page_url': 'http://www.cityofeudoraks.gov',
    'bids_page_url': 'http://www.cityofeudoraks.gov/Bids.aspx'
}

def get_scraper():
    return BidsAspxBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()



