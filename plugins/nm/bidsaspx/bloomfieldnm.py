from bidmap.bidscrapers.bidsaspx.bidsaspx import BidsAspxBidScraper

GOVINFO = {
    'name': 'Bloomfield New Mexico',
    'location': 'Bloomfield, NM',

    'home_page_url': 'http://www.bloomfieldnm.com',
    'bids_page_url': 'http://www.bloomfieldnm.com/bids.aspx'
}

def get_scraper():
    return BidsAspxBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()



