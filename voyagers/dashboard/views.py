from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import ExtendUserCreationForm, ProfileForm
from django.contrib.auth import authenticate, login

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = ExtendUserCreationForm(request.POST)
        profile_form = ProfileForm(request.POST)

        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)

            login(request, user)

            return redirect('dashboard')

    else:
        form = ExtendUserCreationForm()
        profile_form = ProfileForm()

    context = {'form' : form, 'profile_form' : profile_form}
    return render(request, 'dashboard/register.html', context)





@login_required
def dashboard(request):
    #fetch data from mongo and display
    if request.user.is_authenticated:
        username = request.user.username
        userid = request.user.id
        useremail = request.user.email
        profiles = Profile.objects.order_by('id')
        context = {'profiles': profiles, 'username' : username, 'userid': userid, 'useremail' : useremail}
    
    else:
        profiles = Profile.objects.order_by('id')
        context = {'profiles' : profiles}
    # Render the HTML template index.html
    return render(request, 'dashboard.html', context)

def editing(request):

    #update mongo user details with user's changes
    if request.method == 'POST':
        form = ProfileForm(request.POST)
    
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ProfileForm()
    context = {'form': form}
    
    return render(request, 'editing.html', context)


