from django.shortcuts import render, redirect

from .forms import BuyForm
from kratos_app.models import Component

def cart(request):
    context = []

    if 'cart' in request.session.keys():
        for item in request.session['cart']:
            item_id = item.get('id')
            component = Component.objects.get(id=item_id)
            context.append(component)
    else:
        return render(request, 'cart/empty-cart.html')

    if len(context) == 0:
        return render(request, 'cart/empty-cart.html')
    else:
        total_sum = get_total_price(request, context)
        return render(request, 'cart/cart.html', {"cart": context, "total_sum": total_sum})


def add(request, id):
    if request.method == 'POST':
        if not request.session.get('cart'):
            request.session['cart'] = []
        else:
            request.session['cart'] = list(request.session['cart'])

        added_data = {
            'type': request.POST.get('type'),
            'id': id,
        }

        request.session['cart'].append(added_data)
        request.session.modified = True

    return redirect("/")


def remove(request, id):
    if request.method == 'POST':
        for item in request.session['cart']:
            if item['id'] == id and item['type'] == request.POST.get('type'):
                item.clear()
                break

        clear_remains(request)

    return redirect("/cart/")


def remove_all(request):
    for item in request.session['cart']:
        item.clear()

    clear_remains(request)

    return redirect('/cart')

def clear_remains(request):
    while {} in request.session['cart']:
        request.session['cart'].remove({})

    if not request.session['cart']:
        del request.session['cart']

    request.session.modified = True


def get_total_price(request, context):
    total_sum = 0

    for item in context:
        total_sum += item.price

    return total_sum


def buy(request):
    if request.method == 'POST':
        form = BuyForm(request.POST)
        if form.is_valid():

            return redirect("thanks")
    else:
        form = BuyForm()

    return render(request, 'cart/buy.html', {"form": form})


def thanks(request):
    remove_all(request)
    return render(request, "cart/thanks.html")