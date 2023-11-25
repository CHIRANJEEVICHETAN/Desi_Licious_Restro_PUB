from django.urls import path
from Restro_PUB import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('TermsOfServices', views.termsOfServices, name='TermsOfServices'),
    path('indexLogin', views.indexLogin, name='indexLogin'),
]
