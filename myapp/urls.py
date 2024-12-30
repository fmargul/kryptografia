from django.urls import path
from . import views
from myapp.views import EcdhPublicView, EcdhSharedView, RSAKeysView, RSAEncryptView, RSADecryptView, DiffieHellmanPublicView, DiffieHellmanSharedView, DssSignView, generate_valid_parameters

urlpatterns = [
    path('', views.home, name='home'),
    path('multiply_points/', views.multiply_points, name='multiply_points'),
    path('prime_algorithms_comparison/', views.prime_algorithms_comparison, name='prime_algorithms_comparison'),
    path('crt/', views.crt, name='crt'),
    path('exponentiation/', views.exponentiation, name='exponentiation'),
    path('ecdh_shared/', EcdhSharedView.as_view(), name='ecdh_shared'),
    path('ecdh_public/', EcdhPublicView.as_view(), name='ecdh_public'),
    path('rsa_keys/', RSAKeysView.as_view(), name='rsa_keys'),
    path('rsa_encrypt/', RSAEncryptView.as_view(), name='rsa_encrypt'),
    path('rsa_decrypt/', RSADecryptView.as_view(), name='rsa_decrypt'),
    path('diffie_hellman_public/', DiffieHellmanPublicView.as_view(), name='diffie_hellman_public'),
    path('diffie_hellman_shared/', DiffieHellmanSharedView.as_view(), name='diffie_hellman_shared'),
    path("dss-sign/", DssSignView.as_view(), name="dss_sign"),
    path("generate-valid-parameters/", generate_valid_parameters, name="generate_valid_parameters"),
]
