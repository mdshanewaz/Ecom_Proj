from django.urls import path
from Login_App import views


app_name = 'Login_App'

urlpatterns = [
    path('signup/', views.signupView, name='signup'),
    path('login/', views.loginView, name='login'),
    path('logout/', views.logoutView, name='logout'),
    path('profile/', views.user_profileView, name='profile'),    
]