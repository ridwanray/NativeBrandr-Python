from django.shortcuts import render, HttpResponseRedirect
#from django.contrib.auth.decorators import login_required
#from django.contrib.auth.models import User
#from .models import UserProfile
#from .forms import UserForm
#from django.forms.models import inlineformset_factory
from user.models import Design
from random import shuffle
from user.models import UserProfile,Design,Category
from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.contrib.auth.models import User
from user.forms import UserForm,NewDesign
from django.core.exceptions import PermissionDenied
from django.forms.models import inlineformset_factory
from django.contrib.auth.decorators import login_required
def home(request):
    return render(request, 'index.html')

@login_required()
def dashboard(request):
    return render(request, 'dashboard.html')


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


	
def alldesign(request):
			#user = User.objects.get(username=username)
			tests =Design.objects.all().order_by('?')
			return render(request, "index2.html", {"tests":tests,})

'''login_required() # only logged in users should access this
def edit_user(request, pk):
    # querying the User object with pk from url
    user = User.objects.get(pk=pk)

    # prepopulate UserProfileForm with retrieved user values from above.
    user_form = UserForm(instance=user)

    # The sorcery begins from here, see explanation below
    ProfileInlineFormset = inlineformset_factory(User, UserProfile, fields=('user', 'city', 'area', 'tagline', 'phonenumber', 'companyname', 'userlogoimage', 'fullstoreaddress'))
    formset = ProfileInlineFormset(instance=user)

    if request.user.is_authenticated() and request.user.id == user.id:
        if request.method == "POST":
            user_form = UserForm(request.POST, request.FILES, instance=user)
            formset = ProfileInlineFormset(request.POST, request.FILES, instance=user)

            if user_form.is_valid():
                created_user = user_form.save(commit=False)
                formset = ProfileInlineFormset(request.POST, request.FILES, instance=created_user)

                if formset.is_valid():
                    created_user.save()
                    formset.save()
                    return HttpResponseRedirect('/dashboard/')

        return render(request, "account_update.html", {
            "noodle": pk,
            "noodle_form": user_form,
            "formset": formset,
        })
    else:
        raise PermissionDenied'''