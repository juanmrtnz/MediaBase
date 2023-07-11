from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.db.models import F
from .models import User, Videogame, Film, Series, Book, Collection, Discography


def index(request):
    return render(request, 'media/index.html')


@login_required
def videogames_view(request):
    items = Videogame.objects.filter(user=request.user).order_by('-status', 'platform', 'title')
    finished = 0
    for item in items:
        if item.status == 'Finished':
            finished += 1
    return render(request, 'media/videogames.html', {
        'items': items,
        'items_count': len(items),
        'finished': finished,
        'media': 'videogames' 
    })


@login_required
def films_view(request):
    items = Film.objects.filter(user=request.user).order_by('-status', 'title')
    finished = 0
    for item in items:
        if item.status == 'Finished':
            finished += 1
    return render(request, 'media/films.html', {
        'items': items,
        'items_count': len(items),
        'finished': finished
    })


@login_required
def series_view(request):
    items = Series.objects.filter(user=request.user).order_by('-status', 'title')
    return render(request, 'media/series.html', {
        'items': items,
        'items_count': len(items)
    })
    

@login_required
def books_view(request):
    items = Book.objects.filter(user=request.user).order_by('-status', F('finished_date').desc(nulls_last=True))
    return render(request, 'media/books.html', {
        'items': items,
        'items_count': len(items),
        'media': 'books'
    })


@login_required
def collection_view(request):
    items = Collection.objects.filter(user=request.user).order_by('-status', 'platform', 'title')
    finished = 0
    for item in items:
        if item.status == 'Finished':
            finished += 1
    return render(request, 'media/collection.html', {
        'items': items,
        'finished': finished,
        'items_count': len(items),
        'media': 'collection'
    })


@login_required
def discographies_view(request):
    items = Discography.objects.filter(user=request.user).order_by('title')
    return render(request, 'media/collection.html', {
        'items': items,
        'items_count': len(items),
        'media': 'discographies'
    })

        
@login_required
def post(request, media, action):
    title = request.POST.get('title')
    multiple_titles = request.POST.get('multiple_titles')
    status = request.POST.get('status')
    series = request.POST.get('series')
    platform = request.POST.get('platform')
    author = request.POST.get('author')
    language = request.POST.get('language')
    genre = request.POST.get('genre')
    genre_2 = request.POST.get('genre2')
    subgenre = request.POST.get('subgenre')
    release_date = request.POST.get('release_date')
    release_year = request.POST.get('release_year')
    finished_date = request.POST.get('finished_date')
    notes = request.POST.get('notes')

    if title == "":
        title = multiple_titles
    titles = title.split('\r\n')
    if release_date == "":
        release_date = None
    if release_year:
        if len(release_year) == 1:
            release_year = f'000{release_year}'
        if len(release_year) == 2:
            release_year = f'00{release_year}'
        if len(release_year) == 3:
            release_year = f'0{release_year}'
    if (release_date is None and release_year == "") or (release_date != None and release_year == "") or (release_date != None and release_year != ""):
        release_year_only = False
    if release_date is None and release_year != "":
        release_date = f"{release_year}-01-01"
        release_year_only = True
    if genre == "-":
        genre = None
    if genre_2 == "-":
        genre_2 = None
    if subgenre == "-":
        subgenre = None
    if series == "":
        series = None
    if platform == "":
        platform = None
    if platform is not None:
        platforms = platform.split('\r\n')
        platform = []
        for item in platforms:
            if item != "":
                platform.append(item.strip())
    if author == "":
        author = None
    if language == "":
        language = None
    if language is not None:
        languages = language.split('\r\n')
        language = []
        for item in languages:
            if item != "":
                language.append(item.strip())
    if finished_date == "":
        finished_date = None
    if finished_date is not None:
        finished_dates = finished_date.split('\r\n')
        finished_date = []
        for item in finished_dates:
            if item != "":
                finished_date.append(item)
    if status == "Plan to finish":
        finished_date = None
    if notes == "":
        notes = None
    if notes is not None:
        notes = notes.replace('\r\n', ' ')
        notes = notes.strip()

    if media == "videogame":
        for name in titles:
            name = name.strip()
            if name != "" and len(name) <= 200:
                if action == "new":
                    new_item = Videogame(user=User.objects.get(username=request.user.username),
                                    title=name, status=status, release_date=release_date,
                                    release_year_only=release_year_only, genre=genre, subgenre=subgenre,
                                    series=series, platform=platform,
                                    finished_date=finished_date, notes=notes)
                    new_item.save()
                else:
                    edit_item = Videogame.objects.get(pk=action)
                    if edit_item.user == request.user:
                        edit_item.title = title
                        edit_item.status = status
                        edit_item.release_date = release_date
                        edit_item.release_year_only = release_year_only
                        edit_item.genre = genre
                        edit_item.subgenre = subgenre
                        edit_item.series = series
                        edit_item.platform = platform
                        edit_item.finished_date = finished_date
                        edit_item.notes = notes
                        edit_item.save()
                    else:
                        return HttpResponse("Sneaky sneaky...")

        return HttpResponseRedirect(reverse("videogames_view"))

    if media == "film" or media == "series":
        if media == "film":
            model = Film
        if media == "series":
            model = Series
        for name in titles:
            name = name.strip()
            if name != "" and len(name) <= 200:
                if action == "new":
                    new_item = model(user=User.objects.get(username=request.user.username),
                                    title=name, status=status, release_date=release_date,
                                    release_year_only=release_year_only,genre=genre,
                                    genre_2=genre_2, finished_date=finished_date,notes=notes)
                    new_item.save()
                else:
                    edit_item = model.objects.get(pk=action)
                    if edit_item.user == request.user:
                        edit_item.title = title
                        edit_item.status = status
                        edit_item.release_date = release_date
                        edit_item.release_year_only = release_year_only
                        edit_item.genre = genre
                        edit_item.genre_2 = genre_2
                        edit_item.finished_date = finished_date
                        edit_item.notes = notes
                        edit_item.save()
                    else:
                        return HttpResponse("Sneaky sneaky...")

        if media =="film":
            return HttpResponseRedirect(reverse("films_view"))
        if media=="series":
            return HttpResponseRedirect(reverse("series_view"))

    if media == "book":
        for name in titles:
            name = name.strip()
            if name != "" and len(name) <= 200:
                if action == "new":
                    new_item = Book(user=User.objects.get(username=request.user.username),
                                    title=name, status=status, release_date=release_date, 
                                    release_year_only=release_year_only, genre=genre, author=author,
                                    language=language, finished_date=finished_date, notes=notes)
                    new_item.save()
                else:
                    edit_item = Book.objects.get(pk=action)
                    if edit_item.user == request.user:
                        edit_item.title = title
                        edit_item.status = status
                        edit_item.release_date = release_date
                        edit_item.release_year_only = release_year_only
                        edit_item.genre = genre
                        edit_item.author = author
                        edit_item.language = language
                        edit_item.finished_date = finished_date
                        edit_item.notes = notes
                        edit_item.save()
                    else:
                        return HttpResponse("Sneaky sneaky...")

        return HttpResponseRedirect(reverse("books_view"))
    
    if media == "collection":
        for name in titles:
            name = name.strip()
            if name != "" and len(name) <= 200:
                if action == "new":
                    new_item = Collection(user=User.objects.get(username=request.user.username),
                                    title=name, status=status, platform=platform, notes=notes)
                    new_item.save()
                else:
                    edit_item = Collection.objects.get(pk=action)
                    if edit_item.user == request.user:
                        edit_item.title = title
                        edit_item.status = status
                        edit_item.platform = platform
                        edit_item.notes = notes
                        edit_item.save()
                    else:
                        return HttpResponse("Sneaky sneaky...")

        return HttpResponseRedirect(reverse("collection_view"))


def delete_item(request, media, item_id):
    if media == "videogame":
        model = Videogame
    if media == "film":
        model = Film
    if media == "series":
        model = Series
    if media == "book":
        model = Book
    if media == "collection":
        model = Collection
    item = model.objects.get(pk=item_id)
    
    if item.user == request.user:
        item.delete()
        return HttpResponseRedirect(reverse('index'))
    else:
        return HttpResponse("Sneaky sneaky...")
    

@login_required
def download(request, media):
    response = HttpResponse(content_type='text/plain')
    response['Content-Disposition'] = f'attachment; filename={media}.txt'
    
    if media == "videogames":
        items = Videogame.objects.filter(user=request.user).order_by('title')
        platforms = ''
        finished_dates = ''
        for item in items:
            if item.release_year_only is False:
                release_date = item.release_date
            else:
                release_date = str(item.release_date)[0:4]

            if item.platform != None:
                for platform in item.platform:
                    if platform != item.platform[-1]:
                        platforms = platforms + platform + ', '
                    else:
                        platforms = platforms + platform

            if item.finished_date != None:
                for date in item.finished_date:
                    if date != item.finished_date[-1]:
                        finished_dates = finished_dates + date + ', '
                    else:
                        finished_dates = finished_dates + date

            list.append(f"{item.title} // {item.status} // {release_date} // {item.genre} // {item.subgenre} // {item.series} // {platforms} // {finished_dates} // {item.notes}\n")

        response.write("TITLE, STATUS, RELEASE DATE, GENRE, SUBGENRE, SERIES, PLATFORM, FINISHED DATE, NOTES\n\n")
        response.writelines(list)

    if media == "films" or media == "series":
        if media == "films":
            model = Film
        elif media == "series":
            model = Series

        items = model.objects.filter(user=request.user).order_by('title')
        finished_dates = ''
        for item in items:
            if item.release_year_only is False:
                release_date = item.release_date
            else:
                release_date = str(item.release_date)[0:4]

            if item.finished_date != None:
                for date in item.finished_date:
                    if date != item.finished_date[-1]:
                        finished_dates = finished_dates + date + ', '
                    else:
                        finished_dates = finished_dates + date

            list.append(f"{item.title} // {item.status} // {release_date} // {item.genre} // {item.genre_2} // {finished_dates} // {item.notes}\n")

        response.write("TITLE, STATUS, RELEASE DATE, GENRE_1, GENRE_2, FINISHED DATE, NOTES\n\n")
        response.writelines(list)

    if media == "books":
        items = Book.objects.filter(user=request.user).order_by('title')
        languages = ''
        finished_dates = ''
        for item in items:
            if item.release_year_only is False:
                release_date = item.release_date
            else:
                release_date = str(item.release_date)[0:4]
            for item in items:
                if item.release_year_only is False:
                    release_date = item.release_date
                else:
                    release_date = str(item.release_date)[0:4]

                if item.language != None:
                    for language in item.language:
                        if language != item.language[-1]:
                            languages = languages + language + ', '
                        else:
                            languages = languages + language

            if item.finished_date != None:
                for date in item.finished_date:
                    if date != item.finished_date[-1]:
                        finished_dates = finished_dates + date + ', '
                    else:
                        finished_dates = finished_dates + date
            list.append(f"{item.title} // {item.status} // {release_date} // {item.genre} // {item.author} // {languages} // {finished_dates} // {item.notes}\n")

        response.write("TITLE, STATUS, RELEASE DATE, GENRE, AUTHOR, LANGUAGE, FINISHED DATE, NOTES\n\n")
        response.writelines(list)

    if media == "collection":
        items = Collection.objects.filter(user=request.user).order_by('platform', 'title')
        for item in items:
            list.append(f"{item.title} // {item.status} // {item.platform} // {item.notes}\n")

        response.write("TITLE, STATUS, PLATFORM, NOTES\n\n")
        response.writelines(list)

    return response


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "media/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "media/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        if len(username) > 15:
            return render(request, "media/register.html", {
                "message": "Username cannot be longer than 15 characters."
            })
        email = request.POST["email"]
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "media/register.html", {
                "message": "Passwords must match."
            })
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "media/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "media/register.html")
