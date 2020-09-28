from django.shortcuts import render
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def encyclopedia(request, title):
    content = util.get_entry(title)
    if content == None:
        return render(request, 'encyclopedia/encyclopedia.html', {
            'title': 'Entry not found',
            'header': 'Entry not found',
            'content': 'Sorry, that entry does not exist yet'
        })
    return render(request, 'encyclopedia/encyclopedia.html', {
        'page_title': 'Wiki - ' + title.capitalize(),
        'content': content
    })