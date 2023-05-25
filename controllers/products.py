from django.shortcuts import render
from categories.models import Category
from products.models import *
import controllers.navigation_dynamic as navController
from controllers.view_helper import *

def single_product(request,uid):
    productsss=Product.objects.filter(uniq_id=uid)
    categoris_list=make_sub_categories(get_parents_categories(productsss[0].category_id))
    related_ad=related_ads(productsss[0].category_id)
    nav = navController.load_featured_products()
    context={"nav":nav,"categoris_list":categoris_list,"productsss":productsss,"related_ads":related_ad}
    return render(request,"products/product.html", context)
def get_parents_categories(id):
    categories=list()
    category = Category.objects.filter(id=id).values()[0]
    categories.append(category)
    while(category["is_parent"]!=True):
        category=Category.objects.filter(id=category["parent_id"]).values()[0]
        categories.append(category)
    categories=list(reversed(categories))
    return categories
def make_sub_categories(categories):
    response=""
    for i in categories[:-1]:
        response+=items.open_li()+items.a(href="{}/category/{}".format("http://192.168.33.180",i["id"]),content=i["name"])+items.colse_li()
    last=categories[-1]
    response+=items.open_li(li_class="active")+items.a(href="{}/category/{}".format("http://192.168.33.180",last["id"]),content=last["name"])+items.colse_li()
    return response
def related_ads(id):
    products=Product.objects.filter(category_id=id)
    return products

