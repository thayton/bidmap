from bidmap.bidscrapers.bidview.bidview import BidViewBidScraper

GOVINFO = {
    'name': 'Mason City Iowa',
    'location': 'Mason City, IA',

    'home_page_url': 'http://masoncity.net',
    'bids_page_url': 'http://masoncity.net/bids.aspx'
}

def get_scraper():
    return BidViewBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()
