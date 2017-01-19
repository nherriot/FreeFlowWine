from django.core.urlresolvers import reverse
from django.test import TestCase
# To test the slug on the models need to importet and test i if the slug working
from django.utils.text import slugify

# Create your tests here. WE TESTING THE MODELS 
############################################################################
########################## WE TESTING MODELS NOW ###########################
############################################################################
from .models import Post

class PostModelTestCase(TestCase):
	# frst test
	# first we create a setup func to create the data to the test database
	def setUp(self):
		Post.objects.create(title='My new Book', slug='no-there-is-now-new-books-in-my-library')
	# To test we need to run this command depend of the apps name python manage.py test posts
	# after the the above command run and test it we try to test the all in general run the below command
	# python manage.py test
	def test_post_title(self):
		obj = Post.objects.get(slug='no-there-is-now-new-books-in-my-library')
		self.assertEqual(obj.title, 'My new Book')
		self.assertTrue(obj.content == '')

	# second test 
	def create_post(self, title='My dog name is Raffi'):
		return Post.objects.create(title=title)

	# to test the codes of the test working with the slug in the method in the models def create_slug()
	# python manage.py test if the both title not Equal or not the same
	# now we try to run another test if both slug are the same!!! to test run python manage.py test
	# in this case it faild because the two slugs are Equal which is not in the create_slug() in the models!!!!
	# to make this happen the title_one must be the same with title_two like that:
	# title_one = 'My male dog is Raffi'
	# title_two = 'My male dog is Raffi'
#TEST 1
	def test_post_slug(self):
		title_one = 'My male dog is Raffi'
		title_two = 'My male dog is Raffi 123'
		title_three = 'My male dog is Raffi'
		

		slug_one = slugify(title_one)
		slug_two = slugify(title_two)
		slug_three = slugify(title_three)

		obj_one = self.create_post(title=title_one)
		obj_two = self.create_post(title=title_two)
		obj_three = self.create_post(title=title_three)

		#now we test here
		# but to make the test run without error if both title the same we need to change
		# self.assertEqual(obj_two.slug, slug_two) to self.assertNotEqual(obj_two.slug, slug_two)
		# than run the test again python manage.py test
		self.assertEqual(obj_one.slug, slug_one)
		self.assertEqual(obj_two.slug, slug_two)
		self.assertNotEqual(obj_three.slug, slug_three)

		self.assertTrue(slug_one  == slug_three)
		self.assertTrue(slug_one  != slug_two)
		self.assertTrue(slug_two  != slug_three)
