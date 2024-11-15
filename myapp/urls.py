from django.urls import path
from . import views
from myapp.views import AddPointsView

urlpatterns = [
    path('', views.home, name='home'),
    path('add_points/', AddPointsView.as_view(), name='add_points'),
]
