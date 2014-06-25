from bidmap.bidscrapers.bidsaspx.bidsaspx import BidsAspxBidScraper

GOVINFO = {
    'name': 'Council Bluffs Iowa',
    'location': 'Council Bluffs, IA',

    'home_page_url': 'http://www.councilbluffs-ia.gov',
    'bids_page_url': 'http://www.councilbluffs-ia.gov/Bids.aspx'
}

def get_scraper():
    return BidsAspxBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()



