from bidmap.bidscrapers.bidsaspx.bidsaspx import BidsAspxBidScraper

GOVINFO = {
    'name': 'Gardnerville Nevada',
    'location': 'Gardnerville, NV',

    'home_page_url': 'http://www.gardnerville-nv.gov',
    'bids_page_url': 'http://www.gardnerville-nv.gov/bids.aspx'
}

def get_scraper():
    return BidsAspxBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()



