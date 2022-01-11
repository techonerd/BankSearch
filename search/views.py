from django.shortcuts import render
# from .models import *
# Create your views here.
def index(request):
    return render(request, 'search/index.html')

def search(request):
    if request.method == 'POST':
        query = request.POST['searched']
        return render(request, 'search/search.html', {'query': query})
    else:
        return render(request, 'search/search.html', {})