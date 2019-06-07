from django.urls import path
from .views import Allbook, home, logoutView, detailbook


app_name = 'tubook'

urlpatterns = [
    path('', home, name='home'),
    path('Allbook/', Allbook, name='Allbook'),
    path('detailbook/<int:pk>/', detailbook, name='detailbook'),
    path('logout/', logoutView, name='logout'),
    

]