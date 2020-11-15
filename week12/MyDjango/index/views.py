from django.shortcuts import render
from django.http import HttpResponse
from .models import PhoneTop10
from .models import PhoneComments
from django.db.models import Avg, Sum, Max, Min, Count


def index(request):
    search_dict = dict()
    query = request.GET.get('q', '')
    if query:
        search_dict['title__contains'] = query
    query = request.GET.get('qt', '')
    if query:
        search_dict['hour__contains'] = query
    phones = PhoneTop10.objects.filter(**search_dict).annotate(avgmark=Avg("phonecomments__mark")).values(
        "avgmark", "title", "zhi", "buzhi", "star", "comment", "hour", "id")
    return render(request, 'index.html', locals())


def comments(request, phoneid, title):
    comments = PhoneComments.objects.filter(phoneid=phoneid)
    markavg = PhoneComments.objects.filter(
        phoneid=phoneid).aggregate(Avg('mark'))
    return render(request, 'comments.html', locals())
