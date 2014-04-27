import os, sys, json

sys.path.append(os.path.realpath(os.path.join(os.path.dirname(__file__), '../bidmap_django/')))
sys.path.append(os.path.realpath(os.path.join(os.path.dirname(__file__), '../bidmap_django/bidmap_django/')))

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

from django.core import serializers
from bidmapdb.models import *

def serialize_org(o):
    org_fields = ('name', 'home_page_url', 'bids_page_url', 'location')
    bid_fields = ()
 
    d = serializers.serialize("json", [o], fields=org_fields, indent=2, use_natural_keys=True)
    j = json.loads(d)

    org = j[0]['fields']
    org['bids'] = []

    d = serializers.serialize("json", o.bid_set.all(), indent=2, use_natural_keys=True)
    j = json.loads(d)

    for b in j:
        bid = b['fields']
        org['bids'].append(bid)

    return org
    
if __name__ == '__main__':
    for o in Organization.objects.all():
        org = serialize_org(o)
        print json.dumps(org, indent=2)
