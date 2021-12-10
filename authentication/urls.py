from django.contrib import admin
from django.urls import path
from confirm.views import LoginView, RegisterView, HomeView, logoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('home/', HomeView.as_view(), name='home'),
    path('logout/', logoutView, name='logout'),
]
