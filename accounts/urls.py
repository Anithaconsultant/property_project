from django.urls import path
from django.contrib.auth import views
from .views import SignUpView,property_view,search_view,download_file
from django.contrib.auth import views
from .forms import UserLoginForm
from django.contrib.auth import views as auth_views
urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path('property/', property_view, name='property_view'),
    path("search/", search_view, name="search_view"),
    #path('login/',views.LoginView.as_view(template_name="login.html",authentication_form=UserLoginForm),name='login'),
    path('login/',views.LoginView.as_view(),name='login'),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path('<str:file_name>/', download_file, name='download_file'),
    
]