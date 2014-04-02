import hashlib

from django.db import models
from django.utils.encoding import smart_str, smart_unicode
from django.template.defaultfilters import slugify

def remove_non_ascii(s): return "".join(filter(lambda x: ord(x)<128, s))

class LocationManager(models.Manager):
    def get_by_natural_key(self, city, state, country):
        return self.get(city=city, state=state, country=country)

class Location(models.Model):
    objects = LocationManager()
    slug    = models.SlugField(blank=True)

    city    = models.CharField(max_length=64)
    state   = models.CharField(max_length=2)
    country = models.CharField(max_length=2)

    lat     = models.FloatField(blank=True, null=True)
    lng     = models.FloatField(blank=True, null=True)

    class Meta:
        unique_together = ('city', 'state', 'country')

    def natural_key(self):
        return (self.city, self.state, self.country)

    def __unicode__(self):
        return '%s, %s, %s' % (self.city, self.state, self.country)

class OrganizationManager(models.Manager):
    def get_by_natural_key(self, home_page_url):
        return self.get(home_page_url=home_page_url)
    
class Organization(models.Model):
    objects       = OrganizationManager()

    name          = models.CharField(max_length=64)
    name_slug     = models.SlugField(blank=True, unique=True, max_length=64)

    home_page_url = models.CharField(max_length=255, unique=True)
    bids_page_url = models.CharField(max_length=512)

    location = models.ForeignKey(Location)

    def __unicode__(self):
        return self.name

    def natural_key(self):
        return (self.home_page_url,)

    def save(self, *args, **kwargs):
        if not self.id:
            self.name_slug = slugify(self.name)

        super(Organization, self).save(*args, **kwargs)

class Bid(models.Model):
    title       = models.CharField(max_length=256)
    org         = models.ForeignKey(Organization)

    url         = models.URLField(max_length=512)
    url_data    = models.TextField(blank=True)

    location    = models.ForeignKey(Location)
    description = models.TextField()

    due_date    = models.DateField(null=True, blank=True)
    email       = models.EmailField(max_length=256, blank=True)

    md5         = models.CharField(max_length=32, unique=True)

    def clean_title(self):
        ''' Remove cruft from titles '''
        self.title = remove_non_ascii(self.title.strip())[:256]
        self.title = self.title.replace('&nbsp;', '')

    def clean_description(self):
        ''' Chop spaces in description '''
        self.description = ' '.join(self.description.split())

    def hexdigest(self):
        ''' Unique MD5 for each bid '''
        self.clean_title()
        self.clean_description()

        m = hashlib.md5()
        m.update(self.org.home_page_url)
        m.update(self.title)
        m.update(self.url.encode('utf8'))
        m.update(self.url_data)
        m.update(smart_str(self.description))

        return m.hexdigest()

    def save(self, *args, **kwargs):
        self.md5 = self.hexdigest()
        super(Bid, self).save(*args, **kwargs)









