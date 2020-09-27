from django.shortcuts import render

# Create your views here.
from .models import Shawshank


def index(request):
    search_dict = dict()

    query = request.GET.get('q', '')

    if query:
        search_dict['content__contains'] = query
    else:
        search_dict['rating__gt'] = 3

    comments = Shawshank.objects.filter(**search_dict)
    return render(request, 'index.html', locals())
