from bidmap.bidscrapers.bidsaspx.bidsaspx import BidsAspxBidScraper

GOVINFO = {
    'name': 'City of Lindsay Oklahoma',
    'location': 'Lindsay, OK',

    'home_page_url': 'http://www.cityoflindsay.com',
    'bids_page_url': 'http://www.cityoflindsay.com/bids.aspx'
}

def get_scraper():
    return BidsAspxBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()


