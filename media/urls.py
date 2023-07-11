from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<str:media>/<str:action>', views.post, name='post'),
    path('delete/<str:media>/<int:item_id>', views.delete_item, name='delete_item'),
    path('videogames', views.videogames_view, name='videogames_view'),
    path('films', views.films_view, name='films_view'),
    path('series', views.series_view, name='series_view'),
    path('books', views.books_view, name='books_view'),
    path('collection', views.collection_view, name='collection_view'),
    path('download/<str:media>', views.download, name='download'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('register', views.register, name='register'),
]
