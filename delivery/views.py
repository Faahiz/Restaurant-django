from django.shortcuts import render
from django.http import HttpResponse
from delivery.models import Customer, Restaurant

# Create your views here.
def index(request):
    return render(request, 'delivery/index.html')

def signin(request):
    return render(request, 'delivery/signin.html')

def signup(request):
    return render(request, 'delivery/signup.html')

def handle_login(request):
    

    if request.method == 'POST':
        username = request.POST.get('name')
        password = request.POST.get('pass')
        
        try:
            cust = Customer.objects.get(username = username, password = password)
            return render(request, 'delivery/success.html')
        except:
            return render(request, 'delivery/failed.html')

    else:
        return HttpResponse("invalid")
    
def handle_signup(request):
    if request.method == 'POST':
        username = request.POST.get('name')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            cust = Customer.objects.get(username = username)
        except: 
            c = Customer(username = username, phone = phone, address = address, email = email, password = password)
            c.save()

        return render(request, 'delivery/signin.html')
    
    else:
        return HttpResponse("invalid")

def restaurant_page(request):
    return render(request, 'delivery/add_restaurant.html')

def add_restaurant(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        picture = request.POST.get('picture')
        cuisine = request.POST.get('cuisine')
        rating = request.POST.get('rating')

        rest = Restaurant(name=name, picture=picture, cuisine=cuisine, rating=rating)
        rest.save()

        restaurants = Restaurant.objects.all()

        return render(request, 'delivery/show_restaurants.html', {"restaurants":restaurants})

    else:
        return HttpResponse("Invalid request")
        