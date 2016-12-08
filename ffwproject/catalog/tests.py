from django.test import TestCase
from django.test import TestCase, Client
from django.core import urlresolvers
import httplib
from django.contrib.auth import SESSION_KEY
from catalog.models import Category, Product


# Create your tests here.

class NewUserTestCase(TestCase):
    fixtures = ['initial_data']

    def setUp(self):
        self.client = Client()

    def test_delete_product_all(self):
        for product in Product.objects.all():
            print "The product name is: ", product.name
            product.delete()

        # Check that all the products are deleted
        self.assertEquals(Product.objects.all().count(), 0)
        print "Deleted all products from fixtures"

    def test_products_exist(self):
        self.assertTrue(Product.objects.all().count() > 0)
        print "Fixtures contain products i.e. they exist"

    def test_view_catalog(self):
        print "We are viewing a 'catalog' stored in the database"

        # Lets fetch values from our model first that we wish to check
        category = Category.objects.all()[0]
        print "The category name I'm looking at is: ", category.name
        print "The category slug I'm looking at is: ", category.slug
        category_url = category.get_absolute_url()
        print "The category URL is: ", category_url

        # Lets test the loading of our category page
        response = self.client.get(category_url)

        # We need to check that we did get a response from our HTTP GET to the admin page.
        self.failUnless(response)

        # OK So far so good. Check the response matches an http 200 which is (httplib.OK = 200)
        self.assertEquals(response.status_code, httplib.OK)


