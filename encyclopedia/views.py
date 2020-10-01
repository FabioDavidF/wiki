from django.shortcuts import render
from . import util
from random import randint


lista = util.list_entries()

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        'random_entry_ref': f'/entry/{lista[randint(0, len(lista) - 1)]}',
        
    })

def encyclopedia(request, title):
    content = util.get_entry(title)
    if content == None:
        return render(request, 'encyclopedia/encyclopedia.html', {
            'title': 'Entry not found',
            'header': 'Entry not found',
            'content': 'Sorry, that entry does not exist yet',
            'random_entry_ref': f'../{lista[randint(0, len(lista) - 1)]}'
        })
    return render(request, 'encyclopedia/encyclopedia.html', {
        'page_title': 'Wiki - ' + title.capitalize(),
        'content': content,
        'random_entry_ref': f'../{lista[randint(0, len(lista) - 1)]}'
    })