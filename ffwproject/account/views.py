import datetime
from django.contrib.auth.decorators import login_required
from django.contrib	import messages
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.shortcuts import render

# Create your views here.
from .models import UserProfile
from .forms import UserProfileForm



@login_required
def create_profile(request):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	form = UserProfileForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
		instace.save()
		messages.success(request, 'Your profile successfully created!')
		return HttpResponseRedirect('account:profile')
	else:
		messages.error(request, 'Profile not created!')
	context = {
		'form': form,
	}
	return render(request, 'create_profile.html', context)


@login_required
def view_profile(request):
	# if request.user.is_authenticated:
	query_set = UserProfile.objects.all()

	context = {
		'User': 'Dilshad',
		'objects': query_set,
		'Date': datetime.datetime.now().today(),
	}
	return render(request, 'profile.html', context)
	


# We only want a user who can login to be able to create posts
@login_required
def update_profile(request, slug=None):
    instance = get_object_or_404(UserProfile, slug=slug)

    form = UserProfileForm(request.POST or None,
                    		request.FILES or None, instance=instance)
    if form.is_valid():
        obj_form = form.save(commit=False)
        # print form.cleaned_date.get('title')
        obj_form.save()
        # message successfully updated
        messages.success(request, 'Successfully Updated ')
        return HttpResponseRedirect(obj_form.get_absolute_url())
    # To render the page title on the navbar     
    title_page = Page.objects.all().order_by('-title')

    context = {
        'title': instance.title,
        'instance': instance.content,
        'form': form,
        'image': instance.image,
        'slug': instance.slug,
        'query_page': title_page
    }
    return render(request, 'update_profile.html', context)

# We only want a user who can login to be able to create UserProfile
@login_required
def delete_profile(request, slug=None):
    instance = get_object_or_404(UserProfile, slug=slug)
    instance.delete()
    messages.success(request, 'Your profile has been deleted ')
    return redirect('cms:admin_page')
