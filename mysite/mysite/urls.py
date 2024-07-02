from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from myapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path('delete/<int:id>/',views.delete_consume,name="delete"),
    path('signup/', views.signup_view, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='myapp/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]