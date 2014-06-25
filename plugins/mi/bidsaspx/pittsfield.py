from bidmap.bidscrapers.bidsaspx.bidsaspx import BidsAspxBidScraper

GOVINFO = {
    'name': 'Pittsfield Charter Township Michigan',
    'location': 'Pittsfield, MI',

    'home_page_url': 'http://pittsfield-mi.gov',
    'bids_page_url': 'http://pittsfield-mi.gov/Bids.aspx'
}

def get_scraper():
    return BidsAspxBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()



