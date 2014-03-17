from bidmap.bidscrapers.bidview.bidview import BidViewBidScraper

GOVINFO = {
    'name': 'City Of Claremont North Carolina ',
    'location': 'City Of Claremont, NC',

    'home_page_url': 'http://www.cityofclaremont.org',
    'bids_page_url': 'http://www.cityofclaremont.org/bids.aspx'
}

def get_scraper():
    return BidViewBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()
