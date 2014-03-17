from bidmap.bidscrapers.bidview.bidview import BidViewBidScraper

GOVINFO = {
    'name': 'Junction City Kansas',
    'location': 'Junction City, KS',

    'home_page_url': 'http://www.junctioncity-ks.gov',
    'bids_page_url': 'http://www.junctioncity-ks.gov/bids.aspx'
}

def get_scraper():
    return BidViewBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()
