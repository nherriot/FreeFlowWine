from django.test import TestCase
from django.test import TestCase, Client
from django.core import urlresolvers
import httplib
from django.contrib.auth import SESSION_KEY
from catalog.models import Category


# Create your tests here.

class NewUserTestCase(TestCase):
    fixtures = ['initial_data']

    def setUp(self):
        self.client = Client()


    def test_view_catalog(self):
        print "We are viewing a 'catalog' stored in the database"

        # Lets fetch values from our model first that we wish to check
        category = Category.objects.all()[0]
        category_url = category.get_absolute_url()

        # Lets test the loading of our category page
        response = self.client.get(category_url)

        # now test that we get a response for that url
        print "The category URL is:", category_url


        # We need to check that we did get a response from our HTTP GET to the admin page.
        self.failUnless(response)

        # OK So far so good. Check the response matches an http 200 which is (httplib.OK = 200)
        self.assertEquals(response.status_code, httplib.OK)


