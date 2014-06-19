from bidmap.bidscrapers.bidsaspx.bidsaspx import BidsAspxBidScraper

GOVINFO = {
    'name': 'Fort Lupton Colorado',
    'location': 'Fort Lupton, CO',

    'home_page_url': 'http://www.fortluptonco.gov',
    'bids_page_url': 'http://www.fortluptonco.gov/bids.aspx'
}

def get_scraper():
    return BidsAspxBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()



