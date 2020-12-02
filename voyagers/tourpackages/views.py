from django.shortcuts import render, get_object_or_404
from .models import *
from django.views.generic import ListView
from django.db.models import Q


# Create your views here.
def tours(request):

    attractions = Attraction.objects.all()

    context = dict(attraction=attractions)
    print(context)
    # print(context)
    if(request.GET.get('q')):
        a = (request.GET.get('q'))
        attractionSearch = Attraction.objects.all().filter(
            city__icontains=a)
        context = dict(attraction=attractionSearch)

    # attractionSearch = Attraction.objects.all().filter(attractionName='Shanghai')
    return render(request, 'tours.html', context)


def detail(request, pk):
    
    attraction = get_object_or_404(Attraction, pk=pk)
    context = dict(attraction=attraction)

    return render(request, 'tourdetail.html', context)

# class attractionSearch(ListView):
    # paginate_by = 10

# def get_queryset(request,self):
#     attractionSearch = Attraction.objects.all().filter(attractionName='Shanghai')
#     contexts= dict(attraction=attractionSearch)

#     # result = super(ListView, self).get_queryset()

#     # query = self.request.GET.get('q')
#     # if query:
#     #     query_list = query.split()
#     #     result = result.filter(
#     #         reduce(operator.and_,
#     #                (Q(attractionName__icontains=q) for q in query_list))
#     #     )

#     return render(request, 'tours.html', contexts)
