from bidmap.bidscrapers.bidsaspx.bidsaspx import BidsAspxBidScraper

GOVINFO = {
    'name': 'Burlington North Carolina',
    'location': 'Burlington, NC',

    'home_page_url': 'http://www.burlingtonnc.gov',
    'bids_page_url': 'http://www.burlingtonnc.gov/Bids.aspx'
}

def get_scraper():
    return BidsAspxBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()



