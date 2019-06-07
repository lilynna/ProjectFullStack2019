from django.urls import path
from .views import Allbook, home, logoutView


app_name = 'tubook'

urlpatterns = [
    path('', home, name='home'),
    path('Allbook/', Allbook, name='Allbook'),
    path('logout/', logoutView, name='logout'),
    

]