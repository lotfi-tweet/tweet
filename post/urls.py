from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='post'),
    path('mobile/', views.mobile_part, name='mobile_part'),
    path('dash-bord/', views.dash_bord, name='dash-bord'),
    path('discount/', views.discount_mob, name='discount_mob'),
    path('offer/', views.offer_part, name='offer_part'),
    path('computer/', views.technology_part, name='computer_part'),
    path('mix/', views.mix_part, name='mix_part'),
    path('about/', views.about_as, name='about_as'),
    path('detaill/<int:id>', views.post_detaill, name='detail'),
    path('add-post/', views.add_post, name='add-post'),
    path('add-discount/', views.add_discount, name='add-discount'),
    path('signin/', views.signin, name='signin'),
    path('logout/', views.logout, name='logout'),
]
