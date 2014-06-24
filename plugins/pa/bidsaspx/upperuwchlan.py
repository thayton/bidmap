from bidmap.bidscrapers.bidsaspx.bidsaspx import BidsAspxBidScraper

GOVINFO = {
    'name': 'Upper Uwchlan Township',
    'location': 'Chester Springs, PA',

    'home_page_url': 'http://www.upperuwchlan-pa.gov',
    'bids_page_url': 'http://www.upperuwchlan-pa.gov/Bids.aspx'
}

def get_scraper():
    return BidsAspxBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()



