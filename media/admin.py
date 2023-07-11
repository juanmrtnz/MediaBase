from django.contrib import admin
from .models import User, Videogame, Film, Series, Book, Collection, Discography


admin.site.register(User)
admin.site.register(Videogame)
admin.site.register(Film)
admin.site.register(Series)
admin.site.register(Book)
admin.site.register(Collection)
admin.site.register(Discography)
