from bidmap.bidscrapers.bidsaspx.bidsaspx import BidsAspxBidScraper

GOVINFO = {
    'name': 'DiamondNet Oklahoma',
    'location': 'Sallisaw, OK',

    'home_page_url': 'http://www.diamondnetok.com',
    'bids_page_url': 'http://www.diamondnetok.com/bids.aspx'
}

def get_scraper():
    return BidsAspxBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()



