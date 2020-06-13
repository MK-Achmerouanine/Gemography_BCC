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
    languages = []
    counts = {}
    repos = {}
    for item in items:
        if item['language'] not in languages and item['language'] is not None:
            lang = item['language']
            languages.append(item['language'])
            counts[lang] = 1
            repos[lang] = [item]
        else:
            if item['language'] in languages and item['language'] is not None:
                lang = item['language']
                counts[lang] += 1
                repos[lang].append(item)
            else:
                if item['language'] == 'None':
                    if item['language'] not in languages:
                        languages.append(item['language'])

                    lang = item['language']
                    counts[lang] += 1
                    repos[lang].append(item)
    results = []
    for lang in languages:
        results.append(
            {'language': lang, 'count': counts[lang], 'repos': repos[lang]})
    return Response(results)
