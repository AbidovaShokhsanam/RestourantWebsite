from django.urls import path
from apps.views import HomeView, IndexView, SendEmailView, MenuView, NewsView, NewsdetailView, register, \
    logout, Email, login_view

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about', HomeView.as_view(), name='about'),
    path('contact', SendEmailView.as_view(), name='contact'),
    path('reservation',Email.as_view(),name='reservation'),
    path('menu', MenuView.as_view(), name='menu'),
    path('news', NewsView.as_view(), name='news'),
    path('news_detail/<int:pk>', NewsdetailView.as_view(), name='news_detail'),
    path('register', register, name='register'),
    path('login_page',login_view, name = 'login_page'),
    path('logout',logout, name = 'logout')
    ]