from django.urls import path
from . import views

# localhost:8000/course1
urlpatterns = [
    
    path('', views.all_chai, name='all_chaihome'),
    path('<int:chai_id>/', views.chai_detail, name='chai_detail'),
    path('chai_stores/', views.chai_store_view, name='chai_store'),
    
]
