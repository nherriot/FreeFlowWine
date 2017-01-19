from django.contrib import admin

# Register your models here.
from .models import UserProfile
# from django_markdown.admin import MarkdownModelAdmin

class UserProfilAdmin(admin.ModelAdmin):
	list_display = ('first_name', 'last_name')


admin.site.register(UserProfile, UserProfilAdmin)