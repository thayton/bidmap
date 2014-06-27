from bidmap.bidscrapers.bidsaspx.bidsaspx import BidsAspxBidScraper

GOVINFO = {
    'name': 'Rivers Edge Convention Center',
    'location': 'St Cloud, MN',

    'home_page_url': 'http://www.stcloudriversedgeconventioncenter.com',
    'bids_page_url': 'http://www.stcloudriversedgeconventioncenter.com/bids.aspx'
}

def get_scraper():
    return BidsAspxBidScraper(GOVINFO)

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()



