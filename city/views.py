from django.db.models import F, Count
from django.shortcuts import render
from .models import City, Person, Event
from django.views.generic import ListView
from django.core.paginator import Paginator


def pagination(request):
    event = Event.objects.all()
    paginator = Paginator(event, 2)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    return render(request, 'city/pagination.html', {'page_obj': page_obj})


class PersonInCityView(ListView):
    model = Person
    template_name = 'city/person_in_city.html'
    context_object_name = 'person'
    paginate_by = 3

    def get_queryset(self):
        return Person.objects.values('name', 'city__name')


class PersonPopularionCityView(ListView):
    model = City
    template_name = 'city/population.html'
    context_object_name = 'city'

    def get_queryset(self):
        return \
            City.objects.all().annotate(population=Count('person')).order_by('-population')[:5]


class PersonInMiami(ListView):
    Model = Person
    template_name = 'city/person_in_miami.html'
    context_object_name = 'person'

    def get_queryset(self):
        return Person.objects.filter(city__name='Miami')


class EventView(ListView):
    Model = Event
    template_name = 'city/event.html'
    context_object_name = 'event'
    paginate_by = 3

    def get_queryset(self):
        return Event.objects.all().order_by('start_date')
