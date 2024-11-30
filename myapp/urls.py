from django.urls import path
from . import views
from myapp.views import EcdhPublicView, EcdhSharedView

urlpatterns = [
    path('', views.home, name='home'),
    path('multiply_points/', views.multiply_points, name='multiply_points'),
    path('ecdh_shared/', EcdhSharedView.as_view(), name='ecdh_shared'),
    path('ecdh_public/', EcdhPublicView.as_view(), name='ecdh_public'),
]
