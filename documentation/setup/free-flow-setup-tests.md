# Free Flow Wines Setup Testing and Running Testing

This document explains how to setup and run tests from python django management command interface.
First you need to setup your database to allow the test case framework to write/read from it. The framework
will read your actual database and copy the structure of this but append the word test_. e.g.

	my_database

becomes:

	test_mydatabase




## Functional Tests

Functional tests show that your application works as tested. As an example we will define a functional test
which shows that we correctly deliver the index.html page. It does not test that the page renders correctly just
that it does not fail to deliver a http 200 code.

from django.test import TestCase, Client
from django.core import urlresolvers

import httplib

class NewUserTestCase(TestCase):
	def test_view_homepage(self):
		client = Client()
		home_url = urlresolvers.reverse('home.index')
		response = client.get('home.index')
		# check that we did get a response
		self.failUnless(response)
		# check that status code of response was success
		# (httplib.UK = 200)
		self.asserEqual(response.status_code, httplib.OK)


## Unit Tests




## Running Tests For A Particular Application



## Running All Tests


