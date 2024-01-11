from django.urls import path
from core.views import index, index_english, sitemap, robots


app_name = 'core'

urlpatterns = [
    path('', index, name='index'),
    path('en', index_english, name='index_english'),
    path('sitemap', sitemap, name='sitemap'),
    path('robots', robots, name='robots'),
]
