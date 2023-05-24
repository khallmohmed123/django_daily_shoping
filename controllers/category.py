from django.shortcuts import render
from django.core.paginator import Paginator
from categories.models import Category
from products.models import *
from categories.models import Category
from products.models import *
import controllers.navigation_dynamic as navController

def search_category(request,id,page):
    if isinstance(page,type(None)):
        page=1
    else:
        page=int(page.replace("/",""))
    url_page="/category/{}/".format(id)
    categories=load_featured_products(id)
    productsss=Product.objects.filter(category_id__in=categories).distinct().order_by('id')
    paginator=Paginator(productsss, 25)
    page_obj = paginator.get_page(page)
    nav = navController.load_featured_products()
    context={"products":page_obj.object_list,"paginatios":page_obj,"url_page":url_page,"nav":nav}
    return render(request,"categories/search.html", context)
def load_featured_products(id):
    items_node_array=[]
    categories = Category.objects.filter(id=id)
    for i in categories:
        items_node_array.append(i.id)
        recurse(i.id,node_str=items_node_array)
    return items_node_array
def recurse(id,node_str):
    try:
        sub=Category.objects.filter(parent_id=id).all()
        if len(sub) == 0 :
            raise(Category.DoesNotExist)
        for i in sub:
            node_str.append(i.id)
            recurse(i.id,node_str)
    except Category.DoesNotExist:
        return ""
    except:
        return ""
    return node_str