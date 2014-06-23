from bidmap.bidscrapers.bidsaspx.bidsaspx import BidsAspxBidScraper

GOVINFO = {
    'name': 'Story County Iowa',
    'location': 'Nevada, IA',

    'home_page_url': 'http://www.storycountyiowa.gov',
    'bids_page_url': 'http://www.storycountyiowa.gov/Bids.aspx'
}

def get_scraper():
    return BidsAspxBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()



