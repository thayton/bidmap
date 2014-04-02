import re, urlparse

from bidmap.bidscrapers.bidscraper import BidScraper
from bidmap.htmlparse.soupify import soupify

from bidmapdb.models import *

GOVINFO = {
    'name': 'Augusta Geogia',
    'location': 'Augusta, GA',

    'home_page_url': 'http://appweb.augustaga.gov',
    'bids_page_url': 'http://appweb.augustaga.gov/arcbid/Default.aspx'
}

class AugustaGaBidScraper(BidScraper):
    def __init__(self):
        super(AugustaGaBidScraper, self).__init__(GOVINFO)

    def scrape_bid_links(self, url):
        bids = []

        self.br.open(url)
        self.br.select_form('form1')
        self.br.submit()

        self.br.select_form('form1')
        self.br.submit('ARCBidSearch1$ctl01$btnOpen')

        s = soupify(self.br.response().read())
        r = re.compile(r"__doPostBack\('([^']+)")

        for i in s.findAll('a', href=r):
            if not i['id'].endswith('LinkButton1'):
                continue

            m = re.search(r, i['href'])

            self.br.select_form('form1')
            self.br.form.set_all_readonly(False)
            self.br.form.new_control('hidden', 'ScriptManager1', {'value': 'Results$upResults|' + m.group(1)})
            self.br.form.new_control('hidden', '__AjaxControlToolkitCalendarCssLoaded',   {'value': ''})
            self.br.form.new_control('hidden', '__ASYNCPOST', {'value': 'true'})
            self.br.form.fixup()
            self.br.form['__EVENTTARGET'] = m.group(1)
            self.br.form['ARCBidSearch1$ctl03$ARCBidCustomSearch1$cpeField_ClientState'] = 'true'
            self.br.form['ARCBidSearch1$ctl03$CodeSearch1$cpeField_ClientState'] = 'true'
            self.br.form['ARCBidSearch1$ctl03$DateSearch1$cpeField_ClientState'] = 'true'
            self.br.form['ARCBidSearch1$ctl03$DateSearch2$cpeField_ClientState'] = 'true'
            self.br.form['ARCBidSearch1$ctl03$CodeSearch2$cpeField_ClientState'] = 'true'
            self.br.form['ARCBidSearch1$ctl03$DateSearch3$cpeField_ClientState'] = 'true'
            self.br.form['ScriptManager1_HiddenField'] = ';;AjaxControlToolkit, Version=1.0.11119.18552, Culture=neutral, PublicKeyToken=28f01b0e84b6d53e:en-US:1390ef9b-ff44-4cd4-9260-b2fef7ff31d6:e2e86ef9:9ea3f0e2:9e8e87e9:1df13a87:9758eba:80f47b59:c4c00916:4c9865be:ba594826:c76f1358:69ce9abf:a9a7729d:507fcf1b:c7a4182e;'

            for control in self.br.form.controls[:]:
                if control.type in ['submit', 'image', 'checkbox']:
                    self.br.form.controls.remove(control)

            self.br.submit()

            x = soupify(self.br.response().read())
            z = re.compile(r'_ITB')
            d = re.compile(r'DocumentView\.aspx\?DocID=\d+$')
            f = lambda y: y.name == 'a' and re.search(d, y.get('href', '')) and re.search(z, y.text) 
            a = x.find(f)

            bid = Bid(org=self.org)
            bid.title = i.text
            bid.url = urlparse.urljoin(self.br.geturl(), a['href'])
            bid.location = self.org.location
            bids.append(bid)

            self.br.back()

        return bids

    def scrape_bids(self):
        bid_list = self.scrape_bid_links(self.gov['bids_page_url'])
        for bid in bid_list:
            print bid

def get_scraper():
    return AugustaGaBidScraper()

if __name__ == '__main__':
    bid_scraper = get_scraper()
    bid_scraper.scrape_bids()
