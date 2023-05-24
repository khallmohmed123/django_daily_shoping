from django.shortcuts import render
from products.models import *
from controllers.navigation_dynamic import *
def home(request):
    print("hello")
    title="shop seekers"
    nav = load_featured_products()
    return render(request,"index.html", locals())
def Not_found(request,exception):
    title="shop seekers"
    return render(request,"static/404.html", locals())