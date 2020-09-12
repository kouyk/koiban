from django.urls import path, re_path

from . import views

app_name = 'movie'
urlpatterns = [
    # ex. /, /film
    path('', views.FilmListView.as_view(), name='index'),
    path('film/', views.FilmListView.as_view(), name='film_list'),

    # ex. /film/1000000
    path('film/<int:pk>/', views.FilmDetailView.as_view(), name='film_detail'),

    # ex. /actor/
    path('actor/', views.ActorListView.as_view(), name='actor_list'),

    # ex. /movie/actor/1000000
    path('actor/<int:pk>/', views.ActorDetailView.as_view(), name='actor_detail'),

    # ex. /search/film/doraemon
    # ex. /search/actor/doraemon
    # ex. /search/comment/good
    re_path(r'^search/(?P<category>film|actor|comment)/(?P<search_term>[^/]+)/', views.search, name='search')
]
