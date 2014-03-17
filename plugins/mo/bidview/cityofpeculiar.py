from bidmap.bidscrapers.bidview.bidview import BidViewBidScraper

GOVINFO = {
    'name': 'City Of Peculiar Missouri ',
    'location': 'City Of Peculiar, MO',

    'home_page_url': 'http://cityofpeculiar.com',
    'bids_page_url': 'http://cityofpeculiar.com/bids.aspx'
}

def get_scraper():
    return BidViewBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()
