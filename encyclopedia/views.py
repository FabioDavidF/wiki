from django.shortcuts import render, redirect
from . import util
from random import randint
from django.http import HttpResponse
from pathlib import Path
from django.urls import reverse


lista = util.list_entries()

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        'random_entry_ref': f'/wiki/{lista[randint(0, len(lista) - 1)]}',
        
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
        'title': title,
        'content': content,
        'random_entry_ref': f'../{lista[randint(0, len(lista) - 1)]}'
    })

def search(request):
    info = request.POST.get('q')
    return redirect(f'wiki/{info}/')

def create(request):
    return render(request, "encyclopedia/create.html", {
        'random_entry_ref': f'../wiki/{lista[randint(0, len(lista) - 1)]}'
    })

def create_file(request):
    if request.method != "POST":
        raise Http404
    title = request.POST.get('title_input')
    content = request.POST.get('content_input')
    try:
        entry = open(f'{Path(".").parent}/entries/{title}.md', 'x')
        entry.write(f'# {title} \n')
        entry.write(f'{content}')
        entry.close()
        return redirect(f'wiki/{title}/')
    except:
        raise Http404

def edit(request, title):
    content = util.get_entry(title)
    return render(request, 'encyclopedia/edit.html', {
        'title': title,
        'content': content
        })

def edit_file(request, title):
    if request.method != 'POST':
        raise Http404
    new_content = request.POST.get('new_content')
    entry = open(f'{Path(".").parent}/entries/{title}.md', 'w')
    entry.write(new_content)
    entry.close()
    url = reverse('entry_title', kwargs={'title':title})
    return redirect(url)
