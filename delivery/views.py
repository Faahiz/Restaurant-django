from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from delivery.models import Customer, Restaurant, MenuItem

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
        
def show_restaurant_page(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'delivery/show_restaurants.html', {"restaurants":restaurants})

def restaurant_menu(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, id = restaurant_id)

    if request.method == 'POST':
        # Handle adding new menu item
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        is_veg = request.POST.get('is_veg') == 'on'
        picture = request.POST.get('picture')

        MenuItem.objects.create(
            restaurant=restaurant,
            name=name,
            description=description,
            price=price,
            is_veg=is_veg,
            picture=picture
        )

        return redirect('restaurant_menu', restaurant_id=restaurant.id)
    
    # Fetch all menu item for this restaurant
    menu_items = restaurant.menu_items.all()

    return render(request, 'delivery/menu.html', {'restaurant':restaurant, 'menu_items': menu_items,})