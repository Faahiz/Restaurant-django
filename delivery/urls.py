from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('signin/', views.signin),
    path('signup/', views.signup),
    path('login/', views.handle_login,name='handle_login'),
    path('sign_up/', views.handle_signup,name='handle_signup'),
    
    path('login/restaurant/', views.restaurant_page,name='restaurant_page'),
    path('login/restaurants/', views.add_restaurant,name='add_restaurant'),
    path('login/show_restaurant_page/', views.show_restaurant_page,name='show_restaurant_page'),
    path('restaurant/<int:restaurant_id>/menu', views.restaurant_menu, name='restaurant_menu'),
    path('restaurants/<int:restaurant_id>/update/', views.update_restaurant, name='update_restaurant'),
    path('restaurants/<int:restaurant_id>/update/page/', views.update_restaurant_page, name='update_restaurant_page'),
    path('restaurants/<int:restaurant_id>/delete/', views.delete_restaurant, name='delete_restaurant'),
    
    path('menu/<int:menuItem_id>/update/', views.update_menuItem, name='update_menuItem'),
    path('menu/<int:menuItem_id>/update/page/', views.update_menuItem_page, name='update_menuItem_page'),
    path('menu/<int:menuItem_id>/delete/', views.delete_menuItem, name='delete_menuItem'),

    path('restaurants/<int:restaurant_id>/menu/customer/', views.customer_menu, name='customer_menu')
]