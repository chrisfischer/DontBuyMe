# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from .api import parse_get, parse_post

# Create your views here.

@csrf_exempt
def api(request):
    print (request.method)
    if request.method == 'GET':
        g = dict(request.GET)
        if g:
            results = parse_get(g)
    
    elif request.method == 'POST':
        p = dict(request.POST)
        if p:
            print(p)
            results = parse_post(p)

    if results:
        return JsonResponse(results, safe=False)
    else:
        print("Malformed")
        return None

