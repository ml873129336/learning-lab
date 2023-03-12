from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

app_name = 'users'
LoginView.template_name = 'users/login.html'


urlpatterns = [
    #登录界面
    path('login/',LoginView.as_view(),name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('register/',views.register,name='register')

]