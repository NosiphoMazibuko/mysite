from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import BandMember

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user after sign-up
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


def home(request):
    """
    Render the home page of the band website.
    
    Args:
        request (HttpRequest): The HTTP request object.
    
    Returns:
        HttpResponse: The rendered home page.
    """
    return render(request, 'home.html')


def about(request):
    """
    Render the about page, providing information about the band.
    
    Args:
        request (HttpRequest): The HTTP request object.
    
    Returns:
        HttpResponse: The rendered about page with band details.
    """
    return render(request, 'about.html')


@login_required(login_url='/login/')
def contact(request):
    """
    Render the contact page, allowing users to get in touch with the band.
    
    Args:
        request (HttpRequest): The HTTP request object.
    
    Returns:
        HttpResponse: The rendered contact page with a form for users to send messages.
    """
    return render(request, 'contact.html')


def band_members(request):
    members = BandMember.objects.all()
    return render(request, 'band_members.html', {'members': members})