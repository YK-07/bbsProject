from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.IndexView, name='index'),
    path('signup/', views.SignupView, name='signup'),
    path('login/', views.LoginView, name='login'),
    path('logout/', views.LogoutView, name='logout'),
    path('main/', views.MainView, name='main'),
    path('admin/', admin.site.urls),
    path('detail/<int:pk>/', views.DetailView, name='detail'),
    path('create/', views.CreateClass.as_view(), name='create'),
]