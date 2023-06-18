from django.shortcuts import render, redirect
from .models import Component, Category
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.views.generic import FormView
from .forms import RegisterForm


# Create your views here.
def index(request):
    temps = Component.objects.order_by("category")
    components = {}
    for temp in temps:
        i = temp.category.id
        if i in components:
            if len(components[i]) < 4:
                components[i].append(temp)
        else:
            components[i] = [temp]

    temps = Category.objects.all()
    categories = {}
    for temp in temps:
        categories[temp.id] = temp.category
    return render(request, "index.html", {"components": components, "categories": categories})


def about(request):
    return render(request, 'about.html')


def component_details(request, id):
    component = Component.objects.get(id=id)
    return render(request, "component_details.html", {"component": component})


class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = '/accounts/login'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


@login_required
def profile(request):
    return render(request, "profile.html")