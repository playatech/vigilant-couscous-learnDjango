from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs): # *args, **kwargs
    print(args, kwargs)
    print(request.user)
    # return HttpResponse("<h1>Hello world</h1>") # string of HTML code
    return render(request, "home.html", {})

def contact_view(request, *args, **kwargs): # *args, **kwargs
    # return HttpResponse("<h1>Contact page</h1>") # string of HTML code
    return render(request, "contact.html", {})

def about_view(request, *args, **kwargs): # *args, **kwargs
    # return HttpResponse("<h1>About Us</h1>") # string of HTML code
    my_context = {
        "my_text": "This is about us",
        "my_number": 123,
        "my_list": [2345, 456, 7878]
    }
    return render(request, "about.html", my_context)

