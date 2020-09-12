import time

from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.db.models import Q

from .models import Film, Actor, Comment


# Create your views here.
class FilmListView(generic.ListView):
    model = Film
    context_object_name = 'films'
    paginate_by = 20

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['total_count'] = Film.objects.count()
        return context

    def get_ordering(self):
        return ['-rating', '-premiere_dates']


class FilmDetailView(generic.DetailView):
    model = Film


class ActorListView(generic.ListView):
    model = Actor
    context_object_name = 'actors'
    paginate_by = 20

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['total_count'] = Actor.objects.count()
        return context

    def get_queryset(self):
        return Actor.objects.exclude(photo_url__exact='').order_by('name')


class ActorDetailView(generic.DetailView):
    model = Actor

    def get_screen_partners(self):
        actor = self.get_object()

        class Partner:
            def __init__(self, partner_id, name, photo_url, count):
                self.partner_id = partner_id
                self.name = name
                self.photo_url = photo_url
                self.count = count

            def __str__(self):
                return str(self.count)

        partners = []
        for partner in actor.screen_partners.all():
            collaborations = actor.films.intersection(partner.films.all())
            partners.append(Partner(partner.id, partner.name, partner.photo_url, collaborations.count()))

        partners.sort(key=lambda x: x.count, reverse=True)
        return partners[:10]


def search(request, category, search_term):
    if category == 'film':
        search_model = Film.objects.all().prefetch_related("actor_set")
        search_filter = Q(full_title__icontains=search_term) \
                        | Q(actor__name__icontains=search_term)\
                        | Q(actor__fullname__icontains=search_term)
    elif category == 'actor':
        search_model = Actor.objects.all().prefetch_related("films")
        search_filter = Q(name__icontains=search_term) \
                        | Q(fullname__icontains=search_term) \
                        | Q(films__full_title=search_term)
    elif category == 'comment':
        search_model = Comment.objects.all().prefetch_related("film")
        search_filter = Q(text__icontains=search_term)

    start_time = time.time()
    search_results = search_model.filter(search_filter).distinct()
    count = search_results.count()  # force retrieval
    time_taken = "{:.3f}".format(time.time() - start_time)
    total = search_model.count()

    paginator = Paginator(search_results, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'movie/{}_search_results.html'.format(category),
                  {'query': search_term,
                   'page_obj': page_obj,
                   'total_count': count,
                   'time_taken': time_taken,
                   'total': total,
                   'category': category})
