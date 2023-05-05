from django.urls import path
from django.contrib.auth import views as auth_views
from .import views

app_name='core'
from .forms import LoginForm
urlpatterns=[
    path('',views.index,name='index'),
    path('contact/',views.contact,name='contact'),
    path('signup/',views.signup,name='signup'),
    path('login/',auth_views.LoginView.as_view(template_name='core/login.html',authentication_form=LoginForm),name='login'),
    path('logout/',views.logout,name='logout'),
    path('management/',views.management,name='management'),
    path('bookings/',views.bookings,name='bookings'),
    path('book/<int:item_id>/', views.book_item, name='book_item'),
     path('cancel/<int:item_id>/', views.cancel_item, name='cancel_item'),
]