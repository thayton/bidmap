from bidmap.bidscrapers.bidsaspx.bidsaspx import BidsAspxBidScraper

GOVINFO = {
    'name': 'Yadkin County North Carolina',
    'location': 'Yadkinville, NC',

    'home_page_url': 'http://www.yadkincountync.gov',
    'bids_page_url': 'http://www.yadkincountync.gov/Bids.aspx'
}

def get_scraper():
    return BidsAspxBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()



