from bidmap.bidscrapers.bidview.bidview import BidViewBidScraper

GOVINFO = {
    'name': 'Rockingham County North Carolina',
    'location': 'Reidsville, NC',

    'home_page_url': 'http://co.rockingham.nc.us',
    'bids_page_url': 'http://co.rockingham.nc.us/bids.aspx'
}

def get_scraper():
    return BidViewBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()
