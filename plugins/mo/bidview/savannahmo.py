from bidmap.bidscrapers.bidview.bidview import BidViewBidScraper

GOVINFO = {
    'name': 'Savannah Missouri',
    'location': 'Savannah, MO',

    'home_page_url': 'http://www.savannahmo.net',
    'bids_page_url': 'http://www.savannahmo.net/bids.aspx'
}

def get_scraper():
    return BidViewBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()
