from __future__ import unicode_literals


from django.conf import settings
from django.db import models
from django.contrib.auth.models import (
				    BaseUserManager, 
				    AbstractBaseUser
				)
from django.core.urlresolvers import reverse
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.utils import timezone
## 
from django.contrib.auth.models import User


def upload_image_profile(instance, filename):
	return '%s/%s' %(instance.id, filename)

class UserProfile(models.Model):
	user 		= models.OneToOneField(settings.AUTH_USER_MODEL)
	first_name 	= models.CharField(max_length=124, null=True, blank=True)
	last_name	= models.CharField(max_length=124, null=True, blank=True)
	address		= models.CharField(max_length=255, null=True, blank=True)
	address_1	= models.CharField(max_length=255, null=True, blank=True)
	city 		= models.CharField(max_length=132, null=True, blank=True)
	post_code 	= models.CharField(max_length=124, null=True, blank=True)
	image 		= models.ImageField(upload_to=upload_image_profile, null=True, blank=True)
	bio			= models.TextField(max_length=300)
	updated		= models.DateTimeField(auto_now=True, auto_now_add=False) #auto_now saved to db everytime update
	timestamp	= models.DateTimeField(auto_now=False, auto_now_add=True) #auto_now_add saved as soon as



	def __unicode__(self):
		return str(self.user.username)


	def get_absolute_url(self):
		return reverse('account:create', kwargs={'slug': self.slug})


# class Company(models.Model):
# 	name 		= models.CharField()
# 	address 	= models.CharField()
# 	address_1 	= models.CharField()
# 	city	 	= models.CharField()
# 	postcode	= models.CharField()
# 	weblink		= models.URLField()

def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    query_set = UserProfile.objects.filter(slug=slug).order_by('-id')
    exists = query_set.exists()
    if exists:
        new_slug = '%s-%s' % (slug, query_set.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_profile_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(pre_save_profile_receiver, sender=UserProfile)
