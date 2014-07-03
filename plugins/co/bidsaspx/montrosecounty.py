from bidmap.bidscrapers.bidsaspx.bidsaspx import BidsAspxBidScraper

GOVINFO = {
    'name': 'Montrose County Colorado',
    'location': 'Montrose, CO',

    'home_page_url': 'http://www.montrosecounty.net',
    'bids_page_url': 'http://www.montrosecounty.net/Bids.aspx'
}

def get_scraper():
    return BidsAspxBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()



