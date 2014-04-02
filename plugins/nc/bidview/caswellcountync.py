from bidmap.bidscrapers.bidview.bidview import BidViewBidScraper

GOVINFO = {
    'name': 'Caswell County North Carolina',
    'location': 'Yanceyville, NC',

    'home_page_url': 'http://www.caswellcountync.gov',
    'bids_page_url': 'http://www.caswellcountync.gov/bids.aspx'
}

def get_scraper():
    return BidViewBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()
