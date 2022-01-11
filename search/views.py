from django.shortcuts import render
from pymongo import MongoClient
import os

connect_string = os.environ.get('MONGODB_URI')
cluster = MongoClient(connect_string)
db = cluster["techonerd"]
collection = db["banklist"]

def index(request):
    return render(request, 'search/index.html')

def search(request):

    if request.method != 'POST':
        return render(request, 'search/search.html', {})
    q = request.POST['searched']
    results = collection.find({'ifsc':q.upper()})
    data={}
    result = list(results)
    if not result:
        data["oh-no!!"]="No results found"
    else:
        for k,v in result[0].items():
            if k in ['ifsc','branch','address','city','district','state','bank_name']:
                data[k.upper()]= v
    return render(request, 'search/search.html', {'query': data})