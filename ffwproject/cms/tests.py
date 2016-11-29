from django.test import TestCase, Client
from django.core import urlresolvers
import httplib
from django.contrib.auth import SESSION_KEY
from catalog.models import Category

# Create your tests here.

# First functional test to ensure we have an HTTP 200 response from our main page

class HomePageTestCase(TestCase):

    def setUp(self):
        self.client = Client()

    def test_view_homepage(self):
        home_url = urlresolvers.reverse('cms:index')
        print "home url is:", home_url
        response = self.client.get(home_url)

        # We need to check that did get a response from our HTTP GET to the home page.
        self.failUnless(response)

        # OK So far so good. Check the response matches an http 200 which is (httplib.OK = 200)
        self.assertEquals(response.status_code, httplib.OK)



class DashboardTestCase(TestCase):

    def setUp(self):
        self.client = Client()

    def test_view_adminpage(self):
        home_url = urlresolvers.reverse('cms:admin_page')
        print "admin url is:", home_url
        response = self.client.get(home_url)

        # We need to check that we did get a response from our HTTP GET to the admin page.
        self.failUnless(response)

        # OK So far so good. Check the response matches an http 200 which is (httplib.OK = 200)
        self.assertEquals(response.status_code, httplib.OK)

# This checks that we can setup can self check the user is logged in before running any of the methods in this class
class NewUserTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        logged_in = self.client.session.has_key(SESSION_KEY)
        self.assertFalse(logged_in)

# This checks that we can setup a value called my_value in the setup method and use in methods for this class
class ExampleTestCase(TestCase):
    def setUp(self):
        self.my_value = 0
        print "Running setUp for ExampleTestCase. my_value is: ", self.my_value

    def test_setup_method(self):
        self.my_value = 0
        print "Running test_setup_method. my_value is: ", self.my_value

    def test_setup_method_2(self):
        print "Running test_setup_method_2"
        print "Check that my_value is: ", self.my_value
        self.assertEquals(self.my_value, 0)
        self.failIfEqual(self.my_value, 1)



class NewUserTestCase(TestCase):
    def setUp(self):
        self.client = Client()

        
    def test_view_catalog(self):
        print "We are viewing a 'catalog' stored in the database"

        # Lets fetch values from our model first that we wish to check
        category = Category.active.all()[0]
        category_url = category.get_absolute_url()

        # Lets test the loading of our category page
        response = self.client.get(category_url)

        # now test that we get a response for that url
        print "The category URL is:", category_url


        # We need to check that we did get a response from our HTTP GET to the admin page.
        self.failUnless(response)

        # OK So far so good. Check the response matches an http 200 which is (httplib.OK = 200)
        self.assertEquals(response.status_code, httplib.OK)













