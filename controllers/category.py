from django.shortcuts import render
from django.core.paginator import Paginator
from categories.models import Category
from products.models import *
from categories.models import Category
from products.models import *

def search_category(request,id):
    categories=load_featured_products(id)
    productsss=Product.objects.filter(category_id__in=categories).distinct()
    paginator=Paginator(productsss, 25)
    page_obj = paginator.get_page(1)
    context={"products":page_obj.object_list,"paginatios":page_obj}
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