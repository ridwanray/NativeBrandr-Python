from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import UserProfile,Design,Category
from .forms import UserForm,NewDesign
from django.forms.models import inlineformset_factory
from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages
def get_user_profile(request, username):
			context_dict = {}
			user = User.objects.get(username=username)
			tests =Design.objects.filter(user=user)
			return render(request, "user/user_profile.html", {
				"user":user,
				"tests":tests,
			})
@login_required() # only logged in users should access this
def edit_user(request, username):
    # querying the User object with pk from url
    user = User.objects.get(username=username)
 
    # prepopulate UserProfileForm with retrieved user values from above.
    user_form = UserForm(instance=user)
 
    # The sorcery begins from here, see explanation below
    ProfileInlineFormset = inlineformset_factory(User, UserProfile, fields=('area', 'city', 'state', 'country', 'tagline', 'phoneNumber', 'category', 'profileImage', 'address', 'aboutMe', ))
    formset = ProfileInlineFormset(instance=user)
 
    if request.user.is_authenticated and request.user.id == user.id:
        if request.method == "POST":
            user_form = UserForm(request.POST, request.FILES, instance=user)
            formset = ProfileInlineFormset(request.POST, request.FILES, instance=user)
 
            if user_form.is_valid():
                created_user = user_form.save(commit=False)
                formset = ProfileInlineFormset(request.POST, request.FILES, instance=created_user)
 
                if formset.is_valid():
                    created_user.save()
                    formset.save()
					#messages.success(request, 'Your password was updated successfully!')
                    return HttpResponseRedirect('/dashboard/')
        return render(request, "account_update.html", {
            "noodle":username,
            "noodle_form": user_form,
            "formset": formset,
        })
    else:
        raise PermissionDenied
@login_required(login_url='/accounts/login/')	
def newdesign(request):
			if request.method == "POST":
				form = NewDesign(request.POST, request.FILES)
				if form.is_valid():
				 # SAVE TO DB
					instance = form.save(commit=False)
					instance.user= request.user
					instance.save()
					messages.success(request, 'Your password was updated successfully!', extra_tags='alert')
					return HttpResponseRedirect('/dashboard/')								
			else:
				form =NewDesign()
			return render(request, "newdesign.html", {
				"form":form,
			})



			
'''def testing(request):				query to be used in user dashboard to fetch individual uploaded  previous design designs
	user=request.user
	tests = NewDesign.objects.filter(user=user)
	return render(request, 'query.html', {"tests":tests})	'''	
		
		
		
'''def testing(request):				to be used for individual categories i.e .com/categories/  2.
	tests = Design.objects.filter(category__name="Customized Vest")
	return render(request, 'query.html', {"tests":tests})	
	
																'''	
	
	
	
'''def get_user_profile(request, username):   
			context_dict = {}
			user = User.objects.get(username=username)
			tests =Design.objects.filter(user=user)
			return render(request, "user/user_profile.html", {
				"user":user,
				"tests":tests,
			})				'''
	
	
	
	
	
	
	
	
	
	
'''       to do
		1. get user design when his url visited privately logged in  done
		2. get query result based of category filtered   done
		3. get user design profile when visited pyublicly.... done
		'''	
	
	
	


'''
test each design and getting info aboout each user
'''

