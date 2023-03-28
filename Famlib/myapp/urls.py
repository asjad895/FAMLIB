from django.contrib import admin
from django.urls import path
from myapp import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns=[
 path('',views.index,name='index'),
 path('api/signup/',views.signup,name='signup'),
 path('api/search/',views.search,name='search'),
 path('api/share/',views.share,name='share'),
 path('api/contactus/',views.contactus,name='contactus'),
 path('api/upload/',views.upload,name='upload'),
 path('api/login_user/',views.login_user,name='login_user'),
 path('api/home/',views.home,name='home'),
 path('api/create_library/', views.create_library, name='create_library'),
 path('api/userslevel/', views.userslevel, name='userslevel'),
 path('api/users/', views.users_detail, name='user-list'),
 path('api/users/<str:username>/',views.users_detail, name='user-detail'),
 path('api/users/<uuid:libraryid>/',views.users_detail, name='users-detail'),
 path('api/books/user/<str:user_pk>/', views.book_list),
 path('api/books/', views.book_list),
 path('api/books/library/<str:library_name>/', views.book_list),
 path('api/library/<str:name>/', views.library_detail, name='library_detail')

]