from django.urls import include, path

from . import views


urlpatterns = [
    path('', views.scrape_home, name='home'),
    path('delete/', views.clear_links, name="clear_links")
]
