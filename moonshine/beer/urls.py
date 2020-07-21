from django.conf.urls import url
from beer.views import BeerView, BeerListView

urlpatterns = [
    url(r'^beer/$', BeerView.as_view(), name='beer-post'),
    url(r'^beer/(?P<pk>.*)/$', BeerView.as_view(), name='beer-get'),
    url(r'^beers/$', BeerListView.as_view(), name='beer-list'),
]

beer_api_urls = urlpatterns
