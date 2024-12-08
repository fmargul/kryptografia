from django.urls import path
from . import views
from myapp.views import EcdhPublicView, EcdhSharedView, RSAKeysView, RSAEncryptView, RSADecryptView, DiffieHellmanPublicView, DiffieHellmanSharedView

urlpatterns = [
    path('', views.home, name='home'),
    path('multiply_points/', views.multiply_points, name='multiply_points'),
    path('crt/', views.crt, name='crt'),
    path('modular_exponentiation/', views.modular_exponentiation, name='modular_exponentiation'),
    path('ecdh_shared/', EcdhSharedView.as_view(), name='ecdh_shared'),
    path('ecdh_public/', EcdhPublicView.as_view(), name='ecdh_public'),
    path('rsa_keys/', RSAKeysView.as_view(), name='rsa_keys'),
    path('rsa_encrypt/', RSAEncryptView.as_view(), name='rsa_encrypt'),
    path('rsa_decrypt/', RSADecryptView.as_view(), name='rsa_decrypt'),
    path('diffie_hellman_public/', DiffieHellmanPublicView.as_view(), name='diffie_hellman_public'),
    path('diffie_hellman_shared/', DiffieHellmanSharedView.as_view(), name='diffie_hellman_shared'),
]
