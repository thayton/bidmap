from bidmap.bidscrapers.bidsaspx.bidsaspx import BidsAspxBidScraper

GOVINFO = {
    'name': 'Muscatine Iowa',
    'location': 'Muscatine, IA',

    'home_page_url': 'http://www.muscatineiowa.gov',
    'bids_page_url': 'http://www.muscatineiowa.gov/bids.aspx'
}

def get_scraper():
    return BidsAspxBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()



