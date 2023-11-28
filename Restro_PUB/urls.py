from django.urls import path
from Restro_PUB import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('TermsOfServices', views.termsOfServices, name='TermsOfServices'),
    path('indexLogin', views.indexLogin, name='indexLogin'),
    path('ourBranches', views.ourBranches, name='ourBranches'),
    path('about', views.about, name='about'),
    path('menu', views.menu, name='menu'),
    path('specials', views.specials, name='specials'),
    path('events', views.events, name='events'),
    path('chefs', views.chefs, name='chefs'),
    path('gallery', views.gallery, name='gallery'),
]
