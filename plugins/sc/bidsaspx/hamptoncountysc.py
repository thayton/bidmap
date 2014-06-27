from bidmap.bidscrapers.bidsaspx.bidsaspx import BidsAspxBidScraper

GOVINFO = {
    'name': 'Hampton County South Carolina',
    'location': 'Hampton, SC',

    'home_page_url': 'http://www.hamptoncountysc.org',
    'bids_page_url': 'http://www.hamptoncountysc.org/bids.aspx'
}

def get_scraper():
    return BidsAspxBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()



