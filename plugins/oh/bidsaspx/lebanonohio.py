from bidmap.bidscrapers.bidsaspx.bidsaspx import BidsAspxBidScraper

GOVINFO = {
    'name': 'Lebanon Ohio',
    'location': 'Lebanon, OH',

    'home_page_url': 'https://www.lebanonohio.gov',
    'bids_page_url': 'https://www.lebanonohio.gov/Bids.aspx'
}

def get_scraper():
    return BidsAspxBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()



