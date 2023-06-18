from django.shortcuts import render, redirect
from kratos_app.models import Component


def favorites(request):
    context = []

    if 'favorites' in request.session.keys():
        for item in request.session['favorites']:
            if item.get('type') == 'component':
                item_id = item.get('id')
                component = Component.objects.get(id=item_id)
                context.append(component)

    else:
        return render(request, 'favorites/empty-favorites.html')

    if len(context) == 0:
        return render(request, 'favorites/empty-favorites.html')
    else:
        return render(request, 'favorites/favorites.html', {"favorites": context})


def add(request, id):
    if request.method == 'POST':
        if not request.session.get('favorites'):
            request.session['favorites'] = []
        else:
            request.session['favorites'] = list(request.session['favorites'])

        added_data = {
            'type': request.POST.get('type'),
            'id': id,
        }

        if not is_exists(request, id):
            request.session['favorites'].append(added_data)
            request.session.modified = True

    return redirect("/")


def is_exists(request, id):
    for item in request.session['favorites']:
        if item['type'] == request.POST.get('type') and item['id'] == id:
            return True


def remove(request, id):
    if request.method == 'POST':
        for item in request.session['favorites']:
            if item['id'] == id and item['type'] == request.POST.get('type'):
                item.clear()

        clear_remains(request)

    return redirect("/favorites/")


def clear_remains(request):
    while {} in request.session['favorites']:
        request.session['favorites'].remove({})

    if not request.session['favorites']:
        del request.session['favorites']

    request.session.modified = True
