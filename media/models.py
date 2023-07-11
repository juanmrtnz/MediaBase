from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField


class User(AbstractUser):
    pass


class Videogame(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='videogame_user', default=None)
    title = models.CharField(max_length=200)
    status = models.CharField(max_length=40, default='Finished')
    release_date = models.DateField(null=True)
    release_year_only = models.BooleanField(default=False)
    genre = models.CharField(max_length=40, null=True)
    subgenre = models.CharField(max_length=40, null=True)
    series = models.CharField(max_length=40, null=True)
    platform = ArrayField(models.CharField(max_length=40, null=True), null=True)
    finished_date = ArrayField(models.CharField(max_length=10, null=True), null=True)
    notes = models.CharField(max_length=600, null=True)


class Film(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='film_user', default=None)
    title = models.CharField(max_length=200)
    status = models.CharField(max_length=40, default='Finished')
    release_date = models.DateField(null=True)
    release_year_only = models.BooleanField(default=False)
    genre = models.CharField(max_length=40, null=True)
    genre_2 = models.CharField(max_length=40, null=True)
    finished_date = ArrayField(models.CharField(max_length=10, null=True), null=True)
    notes = models.CharField(max_length=600, null=True)


class Series(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='series_user', default=None)
    title = models.CharField(max_length=200)
    status = models.CharField(max_length=40, default='Finished')
    release_date = models.DateField(null=True)
    release_year_only = models.BooleanField(default=False)
    genre = models.CharField(max_length=40, null=True)
    genre_2 = models.CharField(max_length=40, null=True)
    finished_date = ArrayField(models.CharField(max_length=10, null=True), null=True)
    notes = models.CharField(max_length=600, null=True)

    class Meta:
        verbose_name_plural = "Series"


class Book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='book_user', default=None)
    title = models.CharField(max_length=200)
    status = models.CharField(max_length=40, default='Finished')
    release_date = models.DateField(null=True)
    release_year_only = models.BooleanField(default=False)
    genre = models.CharField(max_length=40, null=True)
    language = ArrayField(models.CharField(max_length=40, null=True), null=True)
    author = models.CharField(max_length=100, null=True)
    finished_date = ArrayField(models.CharField(max_length=10, null=True), null=True)
    notes = models.CharField(max_length=600, null=True)


class Collection(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='collection_user', default=None)
    title = models.CharField(max_length=200)
    status = models.CharField(max_length=40, default='Finished')
    platform = models.CharField(max_length=40, null=True)
    notes = models.CharField(max_length=600, null=True)


class Discography(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='discography_user', default=None)
    artist = models.CharField(max_length=200)



    # VIDEOGAME_GENRES = [
    #     ('-', '-'),
    #     ('Action', 'Action'),
    #     ('Action-Adventure', 'Action-Adventure'),
    #     ('Adventure', 'Adventure'),
    #     ('Horror', 'Horror'),
    #     ('Puzzle', 'Puzzle'),
    #     ('RPG', 'RPG'),
    #     ('Party', 'Party'),
    #     ('Simulation', 'Simulation'),
    #     ('Strategy', 'Strategy'),
    #     ('Sports', 'Sports'),
    #     ('Trivia', 'Trivia'),
    #     ('Other', 'Other'),
    # ]

    # VIDEOGAME_SUBGENRES = [
    #     ('-', '-'),
    #     ('1st-person Shooter', '1st-person Shooter'),
    #     ('3rd-person Shooter', '3rd-person Shooter'),
    #     ('Action RPG', 'Action RPG'),
    #     ('Arcade racing', 'Arcade racing'),
    #     ('Battle royale', 'Battle royale'),
    #     ("Beat 'em up", "Beat 'em up"),
    #     ('Clicker', 'Clicker'),
    #     ('CMS', 'CMS'),
    #     ('Fighting', 'Fighting'),
    #     ('Grand strategy', 'Grand srategy'),
    #     ('JRPG', 'JRPG'),
    #     ('Life simulation', 'Life simulation'),
    #     ('Light Gun Shooter', 'Light Gun Shooter'),
    #     ('Metroidvania', 'Metroidvania'),
    #     ('MMORPG', 'MMORPG'),
    #     ('MOBA', 'MOBA'),
    #     ('Open world', 'Open world'),
    #     ('Platform', 'Platform'),
    #     ('Rally racing', 'Rally racing'),
    #     ('Roguelike', 'Roguelike'),
    #     ('RTS', 'RTS'),
    #     ('Run and Gun', 'Run and Gun'),
    #     ('Rythm', 'Rythm'),
    #     ('Sandbox', 'Sandbox'),
    #     ("Shoot 'em up", "Shoot 'em up"),
    #     ('Sim racing', 'Sim racing'),
    #     ('Stealth', 'Stealth'),
    #     ('Survival', 'Survival'),
    #     ('Survival horror', 'Survival horror'),
    #     ('Tactical RPG', 'Tactical RPG'),
    #     ('Tower defense', 'Tower defense'),
    #     ('TBS', 'TBS'),
    #     ('Vehicle simulation', 'Vehicle simulation'),
    #     ('Visual novel', 'Visual novel'),
    #     ('Other', 'Other'),
    # ]
    
    # STATUS = [
    #     ('Finished', 'Finished'),
    #     ('Plan to finish', 'Plan to finish'),
    #     ('Ongoing', 'Ongoing'),
    #     ('Dropped', 'Dropped'),
    # ]


    # FILM_GENRES = [
    #     ('-', '-'),
    #     ('Action', 'Action'),
    #     ('Adventure', 'Adventure'),
    #     ('Animation', 'Animation'),
    #     ('Comedy', 'Comedy'),
    #     ('Crime', 'Crime'),
    #     ('Documentary', 'Documentary'),
    #     ('Drama', 'Drama'),
    #     ('Historical', 'Historical'),
    #     ('Horror', 'Horror'),
    #     ('Musical', 'Musical'),
    #     ('Romance', 'Romance'),
    #     ('Science fiction', 'Science fiction'),
    #     ('Sports', 'Sports'),
    #     ('Thriller', 'Thriller'),
    #     ('Western', 'Western'),
    #     ('Other', 'Other'),
    # ]

    # STATUS = [
    #     ('Finished', 'Finished'),
    #     ('Plan to finish', 'Plan to finish'),
    #     ('Dropped', 'Dropped'),
    # ]