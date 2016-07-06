from django.shortcuts import render
from django.http import HttpResponse
from books.models import Publisher
# Create your views here.}
def search_form(request):
    return render(request, 'search_form.html')



def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        books = Publisher.objects.filter(name__icontains=q)
        return render(request, 'search_results.html',
            {'books': books, 'query': q})
    else:
        return HttpResponse('Please submit a search term.')

"""
def search(request):
    if 'q' in request.GET:
        message = 'You searched for: %s' % request.GET['q']
        message += "  " + str(len(request.GET['q']))
    else:
        message = 'You submitted an empty form.'
    return HttpResponse(message)
"""