from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('register', views.register_view, name='register'),
    path('login/', views.MyLoginView.as_view(next_page='home'), name='login' ),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout' ),
    path('profile/', views.profile_view, name='profile' )
]
