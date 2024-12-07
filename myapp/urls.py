from django.urls import path
from . import views
from myapp.views import EcdhPublicView, EcdhSharedView, RSAKeysView, RSAEncryptView, RSADecryptView

urlpatterns = [
    path('', views.home, name='home'),
    path('multiply_points/', views.multiply_points, name='multiply_points'),
    path('crt/', views.crt, name='crt'),
    path('ecdh_shared/', EcdhSharedView.as_view(), name='ecdh_shared'),
    path('ecdh_public/', EcdhPublicView.as_view(), name='ecdh_public'),
    path('rsa_keys/', RSAKeysView.as_view(), name='rsa_keys'),
    path('rsa_encrypt/', RSAEncryptView.as_view(), name='rsa_encrypt'),
    path('rsa_decrypt/', RSADecryptView.as_view(), name='rsa_decrypt'),
]
