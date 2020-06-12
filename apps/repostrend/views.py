from django.shortcuts import render

import requests
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view()
def index(request):
    url = 'https://api.github.com/search/repositories?q=created:>{}&sort={}&order={}&page={}&per_page={}'
    date = '2020-06-10'
    sort = 'stars'
    order = 'desc'
    page = '1'
    per_page = '100'
    r = requests.get(url.format(date, sort, order, page, per_page)).json()
    items = r['items']
    return Response(items)
