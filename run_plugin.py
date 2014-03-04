import os, sys, imp

##################################################################
# Purpose:
#    Run a plugin via 'python run_plugin.py <path-to-plugin>
#
# Example: 
#    $ python run_plugin.py plugins/va/bidsaspx/norfolk.py
#
##################################################################
if __name__ == '__main__':
    path = sys.argv[1]

    modname = os.path.splitext(os.path.basename(path))[0]
    plug = imp.load_source(modname, path)

    bid_scraper = plug.get_scraper()
    bid_scraper.scrape_bids()

