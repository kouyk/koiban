from django.db import models


# Create your models here.
class Film(models.Model):
    short_title = models.CharField(max_length=50)
    full_title = models.CharField(max_length=100, db_index=True)
    alt_titles = models.CharField("alternative titles", max_length=350, db_index=True)
    rating = models.CharField(max_length=4, default='0.0')
    cover_url = models.URLField("cover image url")
    directors = models.CharField(max_length=150)
    screenwriters = models.CharField(max_length=200)
    genre = models.CharField(max_length=40)
    official_site = models.URLField()
    prod_region = models.CharField(max_length=40)
    language = models.CharField(max_length=50)
    premiere_dates = models.CharField(max_length=80)
    length = models.CharField(max_length=120)
    imdb = models.SlugField(max_length=10, db_index=False)
    year = models.CharField(max_length=6)
    synopsis = models.TextField()


class Actor(models.Model):
    name = models.CharField(max_length=70, db_index=True)
    fullname = models.CharField(max_length=40, db_index=True)
    douban_url = models.URLField()
    films = models.ManyToManyField(Film)
    screen_partners = models.ManyToManyField('self', symmetrical=False)
    sex = models.CharField(max_length=1)
    horoscope = models.CharField(max_length=3)
    birth_date = models.CharField(max_length=10)
    birth_place = models.CharField(max_length=38)
    careers = models.CharField(max_length=30)
    other_names = models.CharField(max_length=300)
    alt_zh_names = models.CharField(max_length=100)
    family = models.CharField(max_length=200)
    imdb = models.SlugField(max_length=10, db_index=False)
    introduction = models.TextField()
    photo_url = models.URLField()
    website_url = models.URLField()

    def __str__(self):
        return self.name


class Comment(models.Model):
    username = models.CharField(max_length=15)
    submit_time = models.CharField(max_length=10)
    text = models.TextField(db_index=True)
    film = models.ForeignKey(Film, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
