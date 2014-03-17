from bidmap.bidscrapers.bidview.bidview import BidViewBidScraper

GOVINFO = {
    'name': 'Town Of Atoka Tennessee ',
    'location': 'Atoka, TN',

    'home_page_url': 'http://www.townofatoka.com',
    'bids_page_url': 'http://www.townofatoka.com/bids.aspx'
}

def get_scraper():
    return BidViewBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()
